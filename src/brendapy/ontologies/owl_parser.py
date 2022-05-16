"""Preparation of ontologies from OWL format to JSON.

Improved lookup and speed.
"""
import json
import logging
import warnings
from pathlib import Path
from typing import Any, Dict, Union

import pronto


RESOURCES_PATH = Path(__file__).parent.parent / "resources"
BTO_JSON = RESOURCES_PATH / "data" / "bto" / "bto.json"
CHEBI_JSON = RESOURCES_PATH / "data" / "chebi" / "chebi.json"


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

    def set_default(obj: Any) -> Any:
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=2, default=set_default)


if __name__ == "__main__":
    parse_owl_map(
        owl_path=RESOURCES_PATH / "data" / "bto" / "bto_lite.owl", json_path=BTO_JSON
    )
    parse_owl_map(
        owl_path=RESOURCES_PATH / "data" / "chebi" / "chebi_lite.owl",
        json_path=CHEBI_JSON,
    )
