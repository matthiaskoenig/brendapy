"""Working with ontologies to resolve information.

Ontologies have been downloaded from
    https://www.ebi.ac.uk/ols/ontologies/bto
    https://www.ebi.ac.uk/ols/ontologies/chebi


Using the following library for OWL parsing:
    owlready2 https://bitbucket.org/jibalamy/owlready2/src/default/
    https://pypi.org/project/Owlready2/
    https://owlready2.readthedocs.io/en/latest/

An ontology has the following attributes:
6
and the following methods:

 * .classes() : returns a generator for the Classes defined in the ontology (see :doc:`class`)
 * .individuals() : returns a generator for the individuals (or instances) defined in the ontology (see :doc:`class`)
 * .object_properties() : returns a generator for ObjectProperties defined in the ontology (see :doc:`properties`)
 * .data_properties() : returns a generator for DataProperties defined in the ontology (see :doc:`properties`)
 * .annotation_properties() : returns a generator for AnnotationProperties defined in the ontology (see :doc:`annotations`)
 * .properties() : returns a generator for all Properties (object-, data- and annotation-) defined in the ontology
 * .disjoint_classes() : returns a generator for AllDisjoint constructs for Classes defined in the ontology (see :doc:`disjoint`)
 * .disjoint_properties() : returns a generator for AllDisjoint constructs for Properties defined in the ontology (see :doc:`disjoint`)
 * .disjoints() : returns a generator for AllDisjoint constructs (for Classes and Properties) defined in the ontology
 * .different_individuals() : returns a generator for AllDifferent constructs for individuals defined in the ontology (see :doc:`disjoint`)
 * .get_namepace(base_iri) : returns a namespace for the ontology and the given base IRI (see namespaces below, in the next section)

"""
import json
from pathlib import Path
from typing import Any, Dict

from owlready2 import *
from owlready2.entity import ThingClass

from brendapy.log import get_logger


logger = get_logger(__name__)


RESOURCES_PATH = Path(__file__).parent / "resources"
BTO_OWL = RESOURCES_PATH / "data" / "bto" / "bto.owl"
BTO_JSON = RESOURCES_PATH / "data" / "bto" / "bto.json"
CHEBI_OWL = RESOURCES_PATH / "data" / "chebi" / "chebi.owl"
CHEBI_JSON = RESOURCES_PATH / "data" / "chebi" / "chebi.json"


def parse_bto_owl(
    owl_path: Path = BTO_OWL,
    json_path: Path = BTO_JSON,
    onto_repository_path: str = "/tmp/owl",
):
    """Parse BRENDA Tissue Ontology (BTO) OWL information.

    Stores processed information as JSON for fast lookup.
    """

    onto_path.append(onto_repository_path)
    onto = get_ontology(str(owl_path)).load()

    # accessing entities defined in the bto namespace
    # print(onto._namespaces)
    # for key, value in onto._namespaces.items():
    #     print(f"'{key}': '{value}'")

    d_key = {}
    d_label = {}

    for c in onto.classes():
        key = c.name
        # print(key)

        label = c.label[0]
        ancestors = {
            c.name for c in c.ancestors() if c.name not in ["owl.Thing", "Thing"]
        }
        _ = {c.name for c in c.descendants() if c.name not in ["owl.Thing", "Thing"]}
        synonyms = c.hasRelatedSynonym

        description = ThingClass.__getattr__(c, "IAO_0000115")
        if description and isinstance(description, (list, tuple)):
            _ = description[0]

        item = OrderedDict(
            [
                ("key", key),
                # ("iri", c.iri),
                ("label", label),
                ("ancestors", ancestors),
                # ("descendents", _descendants),
                # ("description", _description),
            ]
        )
        if len(synonyms) > 0:
            item["synonyms"] = synonyms

        d_key[key] = item
        d_label[label] = item

    # Add all the synonyms to the dictionary
    for bto_key, item in d_key.items():
        if "synonyms" in item:
            for name in item["synonyms"]:

                if name in d_label:
                    bto_key_duplicate = d_label[name]["key"]
                    if bto_key != bto_key_duplicate:
                        logger.error(
                            f"Duplicate synonym: '{name}', "
                            f"mismatch bto: '{bto_key}' vs "
                            f"'{bto_key_duplicate}'"
                        )
                else:
                    d_label[name] = d_key[bto_key]

    _serialize_to_json(data=d_label, json_path=json_path)

    return d_key, d_label


def parse_chebi_owl(
    owl_path: Path = CHEBI_OWL,
    json_path: Path = CHEBI_JSON,
    onto_repository_path="/tmp/owl",
):
    """Parse the ChEBI OWL information.

    Stores as JSON for fast lookup.
    """
    onto_path.append(onto_repository_path)
    onto = get_ontology(str(owl_path)).load()

    # accessing entities defined in the bto namespace
    chebi = get_namespace("http://purl.obolibrary.org/obo/")
    print("-" * 80)
    print(chebi.CHEBI_17634)
    print(chebi.CHEBI_17634.iri)
    print(chebi.CHEBI_17634.label)
    print("Descendents:", chebi.CHEBI_17634.descendants())
    print("Ancestors:", chebi.CHEBI_17634.ancestors())
    print("Class properties:", chebi.CHEBI_17634.get_class_properties())
    print("Synonyms:", chebi.CHEBI_17634.hasRelatedSynonym)
    print("-" * 80)

    # TODO: remove the deprecated entries (and filter by the 3* entries)
    d_key = {}
    d_label = {}

    for c in onto.classes():
        key = c.name
        label = c.label
        if len(label) > 0:
            label = label[0]
        else:
            label = None

        print(key)

        ancestors = {
            c.name for c in c.ancestors() if c.name not in ["owl.Thing", "Thing"]
        }
        _ = {c.name for c in c.descendants() if c.name not in ["owl.Thing", "Thing"]}
        description = ThingClass.__getattr__(c, "IAO_0000115")
        if description and isinstance(description, (list, tuple)):
            _ = description[0]
        synonyms = c.hasRelatedSynonym + c.hasExactSynonym

        item = OrderedDict(
            [
                ("key", key),
                # ("iri", c.iri),
                ("label", label),
                ("ancestors", ancestors),
                # ("descendents", descendants),
                # ("description", description),
            ]
        )
        if len(synonyms) > 0:
            item["synonyms"] = synonyms

        d_key[key] = item
        if label:
            d_label[label] = item

    # Add all the synonyms to the dictionary
    for chebi_key, item in d_key.items():
        if "synonyms" in item:
            for name in item["synonyms"]:
                if name in d_label:
                    chebi_key_duplicate = d_label[name]["key"]
                    if chebi_key != chebi_key_duplicate:
                        logger.error(
                            f"Duplicate synonym: '{name}', "
                            f"mismatch chebi: '{chebi_key}' "
                            f"vs '{chebi_key_duplicate}'"
                        )
                else:
                    d_label[name] = d_key[chebi_key]

    # additional substances have to be resolved
    # TODO: see https://github.com/matthiaskoenig/brendapy/issues/#17

    _serialize_to_json(data=d_label, json_path=json_path)

    return d_key, d_label


def _serialize_to_json(data: Dict[Any, Any], json_path: Path) -> None:
    """Serialize dictionary to JSON."""

    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=2, default=set_default)


if __name__ == "__main__":

    # parse_bto_owl(owl_path=BTO_OWL, json_path=BTO_JSON)
    parse_chebi_owl(owl_path=CHEBI_OWL, json_path=CHEBI_JSON)
