"""Preparation of ontologies from OWL format to JSON.

Improved lookup and speed.
"""
import logging
import json
import warnings
from pathlib import Path
from typing import Any, Dict, Union

import pronto


def parse_owl_map(owl_path: Path, json_path: Path) -> None:
    """Parse ontology label:id information in lookup dictionary.

    Stores processed information as JSON for fast lookup of ontology id.
    """

    # read ontology with pronto
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", pronto.utils.warnings.SyntaxWarning)
        warnings.simplefilter("ignore", pronto.utils.warnings.NotImplementedWarning)
        ontology: pronto.Ontology = pronto.Ontology(owl_path)

    term_map: Dict[str, str] = {}

    for term_id in ontology:
        term: pronto.Term = ontology[term_id]

        pronto_name: Union[str, None, Any] = term.name
        if not isinstance(pronto_name, str):
            logging.warning(f"Pronto name is none: `{term}`")
            continue

        term_map[term.name] = term.id

    _serialize_to_json(data=term_map, json_path=json_path)



# def parse_chebi_owl(
#     owl_path: Path = CHEBI_OWL,
#     json_path: Path = CHEBI_JSON,
#     onto_repository_path="/tmp/owl",
# ):
#     """Parse the ChEBI OWL information.
#
#     Stores as JSON for fast lookup.
#     """
#     onto_path.append(onto_repository_path)
#     onto = get_ontology(str(owl_path)).load()
#
#     # accessing entities defined in the bto namespace
#     chebi = get_namespace("http://purl.obolibrary.org/obo/")
#     print("-" * 80)
#     print(chebi.CHEBI_17634)
#     print(chebi.CHEBI_17634.iri)
#     print(chebi.CHEBI_17634.label)
#     print("Descendents:", chebi.CHEBI_17634.descendants())
#     print("Ancestors:", chebi.CHEBI_17634.ancestors())
#     print("Class properties:", chebi.CHEBI_17634.get_class_properties())
#     print("Synonyms:", chebi.CHEBI_17634.hasRelatedSynonym)
#     print("-" * 80)
#
#     # TODO: remove the deprecated entries (and filter by the 3* entries)
#     d_key = {}
#     d_label = {}
#
#     for c in onto.classes():
#         key = c.name
#         label = c.label
#         if len(label) > 0:
#             label = label[0]
#         else:
#             label = None
#
#         print(key)
#
#         ancestors = {
#             c.name for c in c.ancestors() if c.name not in ["owl.Thing", "Thing"]
#         }
#         _ = {c.name for c in c.descendants() if c.name not in ["owl.Thing", "Thing"]}
#         description = ThingClass.__getattr__(c, "IAO_0000115")
#         if description and isinstance(description, (list, tuple)):
#             _ = description[0]
#         synonyms = c.hasRelatedSynonym + c.hasExactSynonym
#
#         item = OrderedDict(
#             [
#                 ("key", key),
#                 # ("iri", c.iri),
#                 ("label", label),
#                 ("ancestors", ancestors),
#                 # ("descendents", descendants),
#                 # ("description", description),
#             ]
#         )
#         if len(synonyms) > 0:
#             item["synonyms"] = synonyms
#
#         d_key[key] = item
#         if label:
#             d_label[label] = item
#
#     # Add all the synonyms to the dictionary
#     for chebi_key, item in d_key.items():
#         if "synonyms" in item:
#             for name in item["synonyms"]:
#                 if name in d_label:
#                     chebi_key_duplicate = d_label[name]["key"]
#                     if chebi_key != chebi_key_duplicate:
#                         logger.error(
#                             f"Duplicate synonym: '{name}', "
#                             f"mismatch chebi: '{chebi_key}' "
#                             f"vs '{chebi_key_duplicate}'"
#                         )
#                 else:
#                     d_label[name] = d_key[chebi_key]
#
#     # additional substances have to be resolved
#     # TODO: see https://github.com/matthiaskoenig/brendapy/issues/#17
#
#     _serialize_to_json(data=d_label, json_path=json_path)
#
#     return d_key, d_label


def _serialize_to_json(data: Dict[Any, Any], json_path: Path) -> None:
    """Serialize dictionary to JSON."""

    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=2, default=set_default)


if __name__ == "__main__":
    RESOURCES_PATH = Path(__file__).parent.parent / "resources"
    # parse_owl_map(
    #     owl_url="https://www.ebi.ac.uk/ols/ontologies/bto/download",
    #     json_path=RESOURCES_PATH / "data" / "bto" / "bto.json"
    # )
    parse_owl_map(
        # owl_url="https://www.ebi.ac.uk/ols/ontologies/chebi/download",
        owl_path=RESOURCES_PATH / "data" / "chebi" / "chebi.obo",
        json_path=RESOURCES_PATH / "data" / "chebi" / "chebi.json"
    )

