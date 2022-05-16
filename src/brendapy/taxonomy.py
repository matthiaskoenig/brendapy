r"""
Module for working with taxonomy information and taxonomy tree.

Methods are provided to parse the taxonomy tree,
get the distance between species, and find things like the first common ancestor.

----------------------------------------------------------------
*.dmp files are bcp-like dump from GenBank taxonomy database.

General information.
Field terminator is "\t|\t"
Row terminator is "\t|\n"

nodes.dmp file consists of taxonomy nodes. The description for each node includes the
following

fields:
    tax_id					-- node id in GenBank taxonomy database
    parent tax_id			-- parent node id in GenBank taxonomy database
    rank					-- rank of this node (superkingdom, kingdom, ...)
    embl code				-- locus-name prefix; not unique
    division id				-- see division.dmp file
    inherited div flag  (1 or 0)		-- 1 if node inherits division from parent
    genetic code id				-- see gencode.dmp file
    inherited GC  flag  (1 or 0)		-- 1 if node inherits genetic code from parent
    mitochondrial genetic code id	-- see gencode.dmp file
    inherited MGC flag  (1 or 0)    -- 1 if node inherits mitochondrial gencode
    GenBank hidden flag (1 or 0)    -- 1 if name is suppressed in GenBank entry lineage
    hidden subtree root flag (1 or 0)     -- 1 if this subtree has no sequence data yet
    comments				-- free-text comments and citations

Taxonomy names file (names.dmp):
    tax_id					-- the id of node associated with this name
    name_txt				-- name itself
    unique name				-- the unique variant of this name if name not unique
    name class				-- (synonym, common name, ...)
----------------------------------------------------------------
"""

import io
import time
import zipfile
from typing import List, Optional

import ujson

from brendapy.console import console
from brendapy.log import get_logger
from brendapy.settings import TAXONOMY_JSON, TAXONOMY_ZIP


logger = get_logger(__name__)


def parse_taxonomy_data() -> None:
    """Parse the node and tree information for the taxonomy.

    Stores processed data as json dictionary.

    :param f_taxonomy: json file with stored processed taxonomy data.
    :return:
    """
    console.print("Parsing taxonomy information, ...")
    ts = time.time()

    tid_name_dict = {}
    name_tid_dict = {}
    node_parent_dict = {}

    # load from zip file
    with zipfile.ZipFile(TAXONOMY_ZIP) as z:

        # parse names information
        with io.TextIOWrapper(z.open("names.dmp", "r")) as f_names:
            for line in f_names:
                # every line is a single node which is converted to a dictionary entry
                items = [t.strip() for t in line.split("|")]
                tid = int(items[0])
                name = items[1]
                # store name
                name_tid_dict[name] = tid
                if items[3] == "scientific name":
                    tid_name_dict[tid] = name

        # parse tree information
        with io.TextIOWrapper(z.open("nodes.dmp")) as f_nodes:
            for line in f_nodes:
                items = [t.strip() for t in line.split("|")]
                node, parent = int(items[0]), int(items[1])
                node_parent_dict[node] = parent

    # store data
    data = {
        "tid_name_dict": tid_name_dict,
        "name_tid_dict": name_tid_dict,
        "node_parent_dict": node_parent_dict,
    }
    with open(TAXONOMY_JSON, "w") as f_out:
        ujson.dump(data, f_out)

    te = time.time()
    console.print(f"[success]Taxonomy parsed in {(te - ts):.3} seconds.")


if not TAXONOMY_JSON.exists():
    parse_taxonomy_data()


# ----------------------------------------------------
class Taxonomy(object):
    """Taxonomy class."""

    tid_name_dict = None  # { ncbi_id: ncbi_name }
    name_tid_dict = None  # { ncbi_scientific_name: ncbi_id }
    node_parent_dict = None  # storage of tree information

    def __init__(self, f_taxonomy=TAXONOMY_JSON):
        """Initialize taxonomy."""
        if Taxonomy.tid_name_dict is None:
            ts = time.time()
            with open(f_taxonomy, "r") as f_tax:
                data = ujson.load(f_tax)
                Taxonomy.tid_name_dict = {
                    int(k): v for k, v in data["tid_name_dict"].items()
                }
                Taxonomy.name_tid_dict = data["name_tid_dict"]
                Taxonomy.node_parent_dict = {
                    int(k): int(v) for k, v in data["node_parent_dict"].items()
                }
                del data
            te = time.time()
            console.print(f"[success]Taxonomy loaded in {(te - ts):.3} seconds.")

    @staticmethod
    def _tax_id_clean(tax_id):
        if isinstance(tax_id, str):
            if tax_id.startswith("TAX:"):
                tax_id = tax_id[4:]
            tax_id = int(tax_id)

        return tax_id

    def get_taxonomy_id(self, name):
        """Get NCBI taxonomy id.

        :param name: species name
        :return: NBCI taxonomy id or None if not existing in taxonomy
        """
        if name not in self.name_tid_dict:
            logger.warning(
                f"Taxonomy id could not be resolved for species/organism: {name}"
            )
        return self.name_tid_dict.get(name, None)

    def get_scientific_name(self, tax_id):
        """Get the NCBI scientific name for NCBI taxonomy id.

        :param tax_id:
        :return: NCBI scientific name, None if not existing in taxonomy
        """
        tax_id = Taxonomy._tax_id_clean(tax_id)
        return self.tid_name_dict.get(tax_id, None)

    def get_parent_nodes(self, tax_id):
        """Get list of parent nodes for given NCBI taxonomy identifier.

        First entry in list is tax_id, last entry is 1 ('all').
        If no valid tax_id given returns 'None'
        :return:
        """
        tax_id = Taxonomy._tax_id_clean(tax_id)
        nodes = [tax_id]
        # Find parent nodes in NCBI until 'all' node is reached
        parent_id = -1
        while parent_id != 1:
            tid = nodes[-1]
            try:
                parent_id = self.node_parent_dict[tid]
            except KeyError:
                logger.error(f"taxonomy id not found: {tax_id}")
                return None

            nodes.append(parent_id)
        return nodes

    def find_common_node_by_name(self, name: str, name_ref):
        """Find common node in ontology by name."""
        return self.find_common_node(
            tax_id=self.get_taxonomy_id(name), tax_id_ref=self.get_taxonomy_id(name_ref)
        )

    def find_common_node(self, tax_id, tax_id_ref) -> List:
        """Find the first ancestor node of the species with reference organism.

        :param tax_id:
        :param tax_id_ref:
        :return: Returns list of three items: [common node id,
                                               scientific name of common node id,
                                               distance in nodes reference]
        """
        nodes1 = self.get_parent_nodes(tax_id)
        nodes2 = self.get_parent_nodes(tax_id_ref)

        # Find common ancestor node
        for tid in nodes1:
            for i in range(len(nodes2)):
                if tid == nodes2[i]:
                    return [tid, self.get_scientific_name(tid), i]

        return [None, None, -1]


if __name__ == "__main__":
    tax = Taxonomy()
    print(tax.get_parent_nodes(tax_id=7227))
