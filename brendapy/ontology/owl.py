"""
Working with ontologies to resolve information

Ontologies have been downloaded from
    https://www.ebi.ac.uk/ols/ontologies/bto


Using the following library for OWL parsing:
    owlready2 https://bitbucket.org/jibalamy/owlready2/src/default/
    https://pypi.org/project/Owlready2/

An ontology has the following attributes:

 * .base_iri : base IRI for the ontology
 * .imported_ontologies : the list of imported ontologies (see below)

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
import os
import json
from collections import OrderedDict
from owlready2 import *
from owlready2.entity import ThingClass


def parse_bto_owl(bto_owl_path="bto.owl", onto_repository_path="/home/mkoenig/tmp/owl"):
    """ Parse the OWL information."""

    onto_path.append(onto_repository_path)
    onto = get_ontology(bto_owl_path).load()

    # accessing entities defined in the bto namespace
    print(onto._namespaces)
    for key, value in onto._namespaces.items():
        print(f"'{key}': '{value}'")

    # testing
    # bto = get_namespace("http://purl.obolibrary.org/obo/")
    # print('-' * 80)
    # print(bto.BTO_0000759)
    # print(bto.BTO_0000759.iri)
    # print(bto.BTO_0000759.label)
    # print('Descendents:',  bto.BTO_0000759.descendants())
    # print('Ancestors:',  bto.BTO_0000759.ancestors())
    # print('Class properties:', bto.BTO_0000759.get_class_properties())
    # print(type(bto.BTO_0000759))
    # print(ThingClass.__getattr__((bto.BTO_0000759), "IAO_0000115"))
    # print('-' * 80)


    d_key = {}
    d_label = {}

    for c in onto.classes():
        key = c.name
        print(key)

        label = c.label[0]
        ancestors = {c.name for c in c.ancestors() if c.name not in ["owl.Thing", "Thing"]}
        descendants = {c.name for c in c.descendants() if c.name not in ["owl.Thing", "Thing"]}

        description = ThingClass.__getattr__(c, "IAO_0000115")
        if description and isinstance(description, (list, tuple)):
            description = description[0]

        item = OrderedDict([
            ("key", key),
            ("iri", c.iri),
            ("label", label),
            ("ancestors", ancestors),
            ("descendents", descendants),
            ("description", description),
        ])
        d_key[key] = item
        d_label[label] = item

    # FIXME: parse the synonyms
    # oboInOwl:hasRelatedSynonym

    # Manual fixes (use all the synonmys for fixing):
    fixes = {
        "sperm": "BTO_0001277",  # spermatozoon
        "sperm cell": "BTO_0001277",  # spermatozoon

        "prostate": "BTO_0001129",  # prostate gland
        "prostate cancer cell": "BTO_0001130",  # prostate gland cancer cell
        "prostate carcinoma cell": "BTO_0001130",  # prostate gland cancer cell
        "prostate tumor cell": "BTO_0001130",  # prostate gland cancer cell

        "liver parenchymal cell": "BTO_0000575",  # hepatocyte
        "hepatocellular carcinoma cell": "BTO_0000594",  # liver cancer cell
        "hepatic carcinoma cell": "BTO_0000594",  # liver cancer cell
        "hepatocarcinoma cell": "BTO_0000594",  # liver cancer cell

        "cardiomyocyte": "BTO_0002320",  # cardiac muscle fiber
        "cardiac myocyte": "BTO_0002320",  # cardiac muscle fiber

        "neuronal cell": "BTO_0000938",   # neuron
        "adipose": "BTO_0001487",  # adipose tissue
        "plasma": "BTO_0000131",  # blood plasma

        "pituitary gland": "BTO_0001073",  # hypophysis (131)
        "brain cortex": "BTO_0000233",  # cerebral cortex (110)
        "Huh-7 cell": "BTO_0001950",  # HuH-7 cell (81)
        "platelet": "BTO_0000132",  # blood platelet" (75)
        "T-cell": "BTO_0000782",  # T-cell (69)
    }
    for key, bto in fixes.items():
        d_label[key] = d_key[bto]

    outpath = os.path.join("..", "resources", "bto", "bto.json")
    _serialize_to_json(data=d_label, outpath=outpath)

    return d_key, d_label


def parse_chebi_owl(bto_owl_path="chebi.owl", onto_repository_path="/home/mkoenig/tmp/owl"):
    """ Parse the OWL information."""
    onto_path.append(onto_repository_path)
    onto = get_ontology(bto_owl_path).load()

    # accessing entities defined in the bto namespace
    print(onto._namespaces)
    for key, value in onto._namespaces.items():
        print(f"'{key}': '{value}'")

    d_key = {}
    d_label = {}

    for c in onto.classes():
        key = c.name
        print(key)
        print('Class properties:', c.get_class_properties())

        label = c.label
        ancestors = {c.name for c in c.ancestors() if c.name not in ["owl.Thing", "Thing"]}
        descendants = {c.name for c in c.descendants() if c.name not in ["owl.Thing", "Thing"]}
        IAO_0000231 = ThingClass.__getattr__(c, "IAO_0000231")
        IAO_0100001 = ThingClass.__getattr__(c, "IAO_0100001")

        # description = ThingClass.__getattr__(c, "IAO_0000115")
        # if description and isinstance(description, (list, tuple)):
        #    description = description[0]

        item = OrderedDict([
            ("key", key),
            ("iri", c.iri),
            ("label", label),
            ("ancestors", ancestors),
            ("descendents", descendants),
            # ("description", description),
            ("IAO_0000231",  IAO_0000231),
            ("IAO_0100001", IAO_0100001),
        ])
        d_key[key] = item
        d_label[label] = item

    outpath = os.path.join("..", "resources", "chebi", "chebi.json")
    _serialize_to_json(data=d_label, outpath=outpath)

    return d_key, d_label


def _serialize_to_json(data, outpath):
    # serialize to json
    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    with open(outpath, 'w') as fp:
        json.dump(data, fp, indent=2, default=set_default)


if __name__ == "__main__":

    # parse_chebi_owl()

    if 1:
        d_key, d_label = parse_bto_owl()
        from pprint import pprint
        print("-" * 80)
        pprint(d_label["liver"])




