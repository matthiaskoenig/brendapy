import json
from copy import deepcopy
from sbmlutils.units import *
from sbmlutils.factory import *
from sbmlutils.modelcreator import templates
from sbmlutils.annotation.miriam import *
from sbmlutils.annotation.sbo import *

import os
RESULTS_PATH = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "resources", "misc")
)
PARAMETER_JSON = os.path.join(RESULTS_PATH, "parameters.json")  # created via parameters.py
# ---------------------------------------------------------------------------------------------------------------------
mid = 'brenda_parameters'
version = 1
notes = Notes([
    """
    <h1>BRENDA kinetic parameters</h1>
    <h2>Description</h2>
    
    <p>This file contains the parsed and annotated kinetic parameters of the
    <a href="https://www.brenda-enzymes.org">BRENDA enzyme database</a>.
    </p>
    
    <p>
    <b>BRENDA in 2019: a European ELIXIR core data resource</b><br />
    Jeske L., Placzek S., Schomburg I., Chang A., Schomburg D., Nucleic Acids Res., in print (2019)
    </p>
    
    <p>
    The information was processed using 
    <a href="https://github.com/matthiaskoenig/brendapy">brendapy</a>
    (<a href="https://doi.org/10.5281/zenodo.3355000">https://doi.org/10.5281/zenodo.3355000</a>).<br />
    The SBML was created using
    <a href="https://github.com/matthiaskoenig/sbmlutils">sbmlutils</a>
    (<a href="https://doi.org/10.5281/zenodo.597149">https://doi.org/10.5281/zenodo.597149</a>).
    </p>
    """,
    templates.terms_of_use
])
creators = [
    Creator(familyName='Koenig',
            givenName='Matthias',
            email='koenigmx@hu-berlin.de',
            organization='Humboldt-University Berlin, Institute for Theoretical Biology',
            site="https://livermetabolism.com")
]

# ---------------------------------------------------------------------------------------------------------------------
# Units
# ---------------------------------------------------------------------------------------------------------------------
model_units = ModelUnits(time=UNIT_s, extent=UNIT_mmole, substance=UNIT_mmole,
                         length=UNIT_m, area=UNIT_m2, volume=UNIT_KIND_LITRE)
units = [
    UNIT_s,
    UNIT_mmole,
    UNIT_m,
    UNIT_m2,
    Unit('mM', [(UNIT_KIND_MOLE, 1, -3, 1.0), (UNIT_KIND_LITRE, -1.0)]),
    Unit('per_s', [(UNIT_KIND_SECOND, -1.0, 0, 1)]),
    Unit('per_mM_s', [(UNIT_KIND_MOLE, 1, -3, -1.0), (UNIT_KIND_LITRE, 1.0), (UNIT_KIND_SECOND, -1.0, 0, 1)]),
    Unit('mumol_per_min_mg', [(UNIT_KIND_MOLE, 1, -6, 1.0), (UNIT_KIND_GRAM, -1.0, -3, 1.0), (UNIT_KIND_SECOND, -1.0, 0, 60)]),
]

# ---------------------------------------------------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------------------------------------------------
parameters = []

unit_map = {
    "mM": 'mM',
    "1/s": "per_s",
    "1/mM/s": "per_mM_s",
    "µmol/min/mg": "mumol_per_min_mg",
}

# KKM - Kcat/Km does not exist in SBO)
sbo_map = {
    "KM": "SBO:0000027",  # Michaelis constant
    "KI": "SBO:0000261",  # Inhibitory constant
    "TN": "SBO:0000025",  # catalytic rate constant
    "SA": "SBO:0000558",  # specific activity
}

with open(PARAMETER_JSON, "r") as fpars:
    pdata = json.load(fpars)

    counter = 1
    for key, pentry in pdata.items():

        # protein annotations
        p_annotations = [
            (BQB.IS, f"brenda/{pentry['ec']}"),
            (BQB.IS, f"ec-code/{pentry['ec']}"),
            (BQB.IS, f"taxonomy/{pentry['taxonomy']}"),
        ]
        for tissue in pentry['tissues']:
            bto_id = tissue.replace("_", ":")
            p_annotations.append((BQB.IS, f"bto/{bto_id}"))

        for kin_key in ['KM', 'KI', 'TN', 'KKM', 'SA']:
            sbo = sbo_map.get(kin_key, None)

            if kin_key in pentry["data"]:
                for item in pentry["data"][kin_key]:

                    # get attributes
                    sid = "PB{0:06d}".format(counter)
                    if "substrate" in item:
                        name = f"{kin_key} {key} {pentry['organism']} ({item['substrate']})"
                    else:
                        name = f"{kin_key} {key} {pentry['organism']})"

                    value = item["value"]
                    units_str = unit_map[item["units"]]

                    # annotations
                    annotations = deepcopy(p_annotations)
                    if sbo:
                        annotations.append((BQB.IS, f"sbo/{sbo}"))

                    if "chebi" in item:
                        # FIXME: additional annotations (infered from chebi via pubchem)
                        chebi_id = item["chebi"].replace("_", ":")
                        annotations.append((BQB.IS, f"chebi/{chebi_id}"))

                    for pubmed in item["pubmeds"]:
                        annotations.append((BQB.IS_DESCRIBED_BY, f"pubmed/{pubmed}"))

                    # create parameter
                    p = Parameter(sid=sid, value=value, name=name, unit=units_str,
                                  sboTerm=sbo, annotations=annotations)
                    parameters.append(p)
                    counter += 1
        # break

if __name__ == "__main__":
    from sbmlutils.modelcreator.creator import create_model
    create_model(modules=['parameters_sbml'],
                 target_dir=RESULTS_PATH,
                 create_report=False,
                 validate=False)
