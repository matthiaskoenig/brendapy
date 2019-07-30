[![PyPI version](https://badge.fury.io/py/brendapy.svg)](https://badge.fury.io/py/brendapy)
[![GitHub version](https://badge.fury.io/gh/matthiaskoenig%2Fbrendapy.svg)](https://badge.fury.io/gh/matthiaskoenig%2Fbrendapy)
[![Build Status](https://travis-ci.org/matthiaskoenig/brendapy.svg?branch=develop)](https://travis-ci.org/matthiaskoenig/brendapy)
[![License (LGPL version 3)](https://img.shields.io/badge/license-LGPLv3.0-blue.svg?style=flat-square)](http://opensource.org/licenses/LGPL-3.0)
[![DOI](https://zenodo.org/badge/199438774.svg)](https://zenodo.org/badge/latestdoi/199438774)

# brendapy - BRENDA in python
<b><a href="https://orcid.org/0000-0003-1725-179X" title="https://orcid.org/0000-0003-1725-179X"><img src="./docs/images/orcid.png" height="15" width="15"/></a> Matthias König</b>

The `brendapy` package provides a python parser for [BRENDA](https://www.brenda-enzymes.org/index.php) 
enzyme information. The parser extracts the protein information from the
 database flat file and makes it accessible in a simple manner. 
 
 This package was developed in the context of building kinetic pathway models.
 
 `brendapy` support has been tested on `py36` and `py37`.


**License**
* Source Code: [LGPLv3](http://opensource.org/licenses/LGPL-3.0)
* Documentation: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)

**Citation**  
If you use brendapy in your project cite  

<a href="https://www.brenda-enzymes.org"><img src="./docs/images/brenda.png" height="50"/></a>
> BRENDA in 2019: a European ELIXIR core data resource
> Jeske L., Placzek S., Schomburg I., Chang A., Schomburg D., Nucleic Acids Res., in print (2019)

and  
[![DOI](https://zenodo.org/badge/199438774.svg)](https://zenodo.org/badge/latestdoi/199438774)

**Funding**  
Matthias König is supported by the Federal Ministry of Education and Research (BMBF, Germany)
within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054).

## Installation
`brendapy` is available from [pypi](https://pypi.python.org/pypi/brendapy)
```
pip install brendapy
```

## Usage
Examples are provided in [./brendapy/examples.py](./brendapy/examples.py) or in the tests [./brendapy/tests/test_brenda.py](./brendapy/tests/test_brenda.py) 

```python
from brendapy import BrendaParser, BrendaProtein


def parse_proteins_for_ec():
    """Parse the protein entries for a given EC number in BRENDA.

    Prints overview of proteins, protein ids, and Human proteins.
    """
    brenda = BrendaParser()
    ec = "1.1.1.1"
    proteins = brenda.get_proteins(ec)

    print(f"{len(proteins)} proteins for EC {ec} in BRENDA")
    print(f"Protein identifier: {proteins.keys()}")
    print("-"*80)
    for p in proteins.values():
        if p.organism == "Homo sapiens":
            print(p)
            print("-" * 80)


if __name__ == "__main__":
    parse_proteins_for_ec()
```

```
167 proteins for EC 1.1.1.1 in BRENDA
Protein identifier: dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167])
--------------------------------------------------------------------------------
OrderedDict([('protein_id', 8),
             ('ec', '1.1.1.1'),
             ('organism', 'Homo sapiens'),
             ('AP', [{'data': 'medicine', 'refs': [8, 24]}]),
             ('CF',
              [{'data': 'NAD+',
                'refs': [1,
                         2,
                         3,
                         4,
                         5,
                         6,
                         7,
                         8,
                         9,
                         10,
                         11,
                         12,
                         13,
                         14,
                         15,
                         16,
                         17,
                         18,
                         19,
                         21,
                         22,
                         23,
                         24,
                         27,
                         28,
                         32,
                         33,
                         34,
                         36,
                         38,
                         39,
                         41,
                         42,
                         43,
                         44,
                         45,
                         46,
                         47,
                         48,
                         50,
                         51,
                         52,
                         53,
                         55,
                         59,
                         60,
                         61,
                         63,
                         64,
                         66,
                         67,
                         68,
                         69,
                         70,
                         71,
                         72,
                         73,
                         74,
                         75,
                         76,
                         77,
                         78,
                         79,
                         80,
                         81,
                         82,
                         83,
                         84,
                         85,
                         86,
                         87,
                         88,
                         90,
                         91,
                         92,
                         93,
                         94,
                         95,
                         96,
                         98,
                         105,
                         106,
                         107,
                         108,
                         109,
                         110,
                         111,
                         112,
                         113,
                         114,
                         115,
                         119,
                         122,
                         123,
                         124,
                         125,
                         126,
                         127,
                         128,
                         129,
                         130,
                         133,
                         137,
                         138,
                         139,
                         140,
                         142,
                         143,
                         150,
                         153,
                         161,
                         162,
                         163,
                         166]},
               {'data': 'NADH',
                'refs': [1,
                         2,
                         3,
                         4,
                         5,
                         6,
                         8,
                         9,
                         10,
                         11,
                         12,
                         13,
                         14,
                         15,
                         16,
                         17,
                         18,
                         19,
                         21,
                         22,
                         23,
                         24,
                         27,
                         28,
                         29,
                         32,
                         33,
                         36,
                         38,
                         39,
                         40,
                         41,
                         42,
                         43,
                         44,
                         45,
                         46,
                         47,
                         48,
                         52,
                         53,
                         54,
                         55,
                         59,
                         61,
                         63,
                         64,
                         67,
                         68,
                         69,
                         70,
                         72,
                         73,
                         74,
                         75,
                         76,
                         77,
                         78,
                         79,
                         80,
                         81,
                         82,
                         83,
                         84,
                         85,
                         88,
                         89,
                         90,
                         93,
                         115,
                         119,
                         122,
                         123,
                         124,
                         125,
                         126,
                         127,
                         128,
                         136,
                         137,
                         138,
                         141,
                         144,
                         147,
                         149,
                         153,
                         156,
                         157,
                         161,
                         162,
                         163,
                         164]}]),
             ('EN',
              [{'data': 'A93F', 'refs': [8]},
               {'data': 'S48T', 'refs': [8]},
               {'data': 'V141L', 'refs': [8]}]),
             ('IN',
              [{'data': '4-Methylpyrazole',
                'refs': [5,
                         7,
                         8,
                         27,
                         34,
                         36,
                         41,
                         43,
                         46,
                         66,
                         73,
                         79,
                         106,
                         109]},
               {'data': '1,10-phenanthroline',
                'refs': [5, 8, 12, 18, 26, 36, 42, 43, 68, 73, 79, 92, 101]},
               {'data': 'pyrazole',
                'refs': [5, 8, 9, 10, 12, 19, 43, 46, 69, 78, 79, 88]},
               {'data': 'NADP+', 'refs': [8]},
               {'data': '4-bromopyrazole', 'refs': [8]},
               {'data': '4-pentylpyrazole', 'refs': [8]},
               {'data': 'sulfonic acid', 'refs': [8]},
               {'data': '8-Amino-6-methoxyquinoline', 'refs': [8]},
               {'data': '4-cyanopyrazole', 'refs': [8]},
               {'data': '4-nitropyrazole', 'refs': [8]},
               {'data': '4-octylpyrazole', 'refs': [8]},
               {'data': '4-propylpyrazole', 'refs': [8]},
               {'data': 'all-trans-retinal', 'refs': [8]},
               {'data': '4-androsten-3,17-dione', 'refs': [8]},
               {'data': '3-butylthiolan 1-oxide', 'refs': [8]},
               {'data': '5alpha-androstan-17beta-ol-3-one', 'refs': [8]},
               {'data': 'N-cyclopentyl-N-cyclobutylformamide', 'refs': [8]},
               {'data': 'N-benzylformamide', 'refs': [8]},
               {'data': 'N-heptylformamide', 'refs': [8]},
               {'data': 'N-1-methylheptylformamide', 'refs': [8]},
               {'data': 'all-trans-retinoic acid', 'refs': [8]},
               {'data': 'cimetidine', 'refs': [8]},
               {'data': 'acetaminophen', 'refs': [8]},
               {'data': 'Acetylsalicylate', 'refs': [8]},
               {'data': 'salicylate', 'refs': [8]},
               {'data': 'trifluoroethanol', 'refs': [8, 10]},
               {'data': 'dipicolinic acid', 'refs': [8, 10, 79]},
               {'data': 'EDTA',
                'refs': [8, 18, 26, 43, 46, 48, 55, 57, 58, 61, 79, 112, 124]},
               {'data': 'Isobutyramide', 'refs': [8, 41]},
               {'data': "2,2'-bipyridine", 'refs': [8, 43]},
               {'data': '4-iodopyrazole', 'refs': [8, 46]},
               {'data': '8-hydroxyquinoline 5-sulfonic acid', 'refs': [8, 79]},
               {'data': '4-methoxypyrazole', 'refs': [8, 9, 10, 12, 36]},
               {'data': 'Tween 80', 'refs': [8, 99, 112]}]),
             ('KI',
              [{'data': '0.014 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.028 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.0047 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.0047 {4-androsten-3,17-dione}', 'refs': [8]},
               {'data': '0.014 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.028 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.0047 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.0047 {4-androsten-3,17-dione}', 'refs': [8]},
               {'data': '0.014 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.028 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.0047 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.0047 {4-androsten-3,17-dione}', 'refs': [8]}]),
             ('KM',
              [{'data': '10.6 {ethanol}', 'refs': [7, 8]},
               {'data': '0.06 {16-hydroxyhexadecanoate}', 'refs': [8]},
               {'data': '0.55 {1-Octanol}', 'refs': [8]},
               {'data': '0.004 {4-hydroxy-retinol}', 'refs': [8]},
               {'data': '0.012 {all-trans-retinal}', 'refs': [8]},
               {'data': '0.012 {retinol}', 'refs': [8]},
               {'data': '0.008 {Cyclohexanol}', 'refs': [8]},
               {'data': '0.013 {NAD+}', 'refs': [8]},
               {'data': '0.049 {ethanol}', 'refs': [8]},
               {'data': '0.015 {4-hydroxy-retinol}', 'refs': [8]},
               {'data': '0.018 {11-cis-retinol}', 'refs': [8]},
               {'data': '0.022 {NAD+}', 'refs': [8]},
               {'data': '0.027 {5beta-Pregnan-3beta-ol-20-one}', 'refs': [8]},
               {'data': '0.027 {4-oxo-retinal}', 'refs': [8]},
               {'data': '0.032 {3-Phenyl-1-propanol}', 'refs': [8]},
               {'data': '0.09 {Pentanol}', 'refs': [8]},
               {'data': '0.025 {NAD+}', 'refs': [8]},
               {'data': '0.025 {4-oxo-retinal}', 'refs': [8]},
               {'data': '0.025 {3,4-dihydro-retinal}', 'refs': [8]},
               {'data': '0.2 {tryptophol}', 'refs': [8]},
               {'data': '1 {ethanol}', 'refs': [8]},
               {'data': '0.009 {all-trans-retinol}', 'refs': [8]},
               {'data': '0.009 {Octanol}', 'refs': [8]},
               {'data': '0.023 {all-trans-retinol}', 'refs': [8]},
               {'data': '0.023 {9-cis-retinol}', 'refs': [8]},
               {'data': '0.25 {5beta-cholanic acid-3-one}', 'refs': [8]},
               {'data': '0.28 {Pentanol}', 'refs': [8]},
               {'data': '0.0025 {NADH}', 'refs': [8]},
               {'data': '0.8 {Octanol}', 'refs': [8]},
               {'data': '2.4 {octanal}', 'refs': [8]},
               {'data': '1.8 {ethanol}', 'refs': [8]},
               {'data': '0.23 {12-hydroxydodecanoate}', 'refs': [8]},
               {'data': '0.028 {3,4-dihydro-retinol}', 'refs': [8]},
               {'data': '0.15 {benzyl alcohol}', 'refs': [8]},
               {'data': '0.0036 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [8]},
               {'data': '0.0036 {5beta-pregnan-3,20-dione}', 'refs': [8]},
               {'data': '0.011 {NADH}', 'refs': [8]},
               {'data': '0.011 {all-trans-retinal}', 'refs': [8]},
               {'data': '0.011 {retinol}', 'refs': [8]},
               {'data': '0.011 {9-cis-retinol}', 'refs': [8]},
               {'data': '0.011 {4-hydroxy-retinol}', 'refs': [8]},
               {'data': '1.2 {Octanol}', 'refs': [8]},
               {'data': '4.3 {acetaldehyde}', 'refs': [8]},
               {'data': '0.007 {NADH}', 'refs': [8]},
               {'data': '0.007 {benzyl alcohol}', 'refs': [8]},
               {'data': '0.007 {Octanol}', 'refs': [8]},
               {'data': '0.033 {all-trans-retinol}', 'refs': [8]},
               {'data': '0.034 {all-trans-retinal}', 'refs': [8]},
               {'data': '0.034 {Vanillyl alcohol}', 'refs': [8]},
               {'data': '0.08 {Octanol}', 'refs': [8]},
               {'data': '0.085 {acetaldehyde}', 'refs': [8]},
               {'data': '0.84 {ethanol}', 'refs': [8]},
               {'data': '0.017 {4-oxo-retinal}', 'refs': [8]},
               {'data': '0.046 {5beta-androstan-17beta-ol-3-one}', 'refs': [8]},
               {'data': '0.33 {acetaldehyde}', 'refs': [8]},
               {'data': '0.13 {Hexanol}', 'refs': [8]},
               {'data': '0.34 {NAD+}', 'refs': [8]},
               {'data': '0.024 {3,4-dihydro-retinol}', 'refs': [8]},
               {'data': '0.035 {11-cis-retinol}', 'refs': [8]},
               {'data': '0.048 {12-hydroxydodecanoate}', 'refs': [8]},
               {'data': '9 {ethanol}', 'refs': [8]},
               {'data': '17 {Hexanol}', 'refs': [8]},
               {'data': '0.026 {3,4-dihydro-retinal}', 'refs': [8]},
               {'data': '0.63 {ethanol}', 'refs': [8]},
               {'data': '11 {Vanillyl alcohol}', 'refs': [8]},
               {'data': '1.6 {ethanol}', 'refs': [8]},
               {'data': '4.2 {ethanol}', 'refs': [8]},
               {'data': '0.016 {Octanol}', 'refs': [8]},
               {'data': '0.056 {12-Hydroxydodecanoic acid}', 'refs': [8]},
               {'data': '0.91 {Propanol}', 'refs': [8]},
               {'data': '50 {ethylene glycol}', 'refs': [8]},
               {'data': '260 {NADH}', 'refs': [8]},
               {'data': '0.047 {12-hydroxydodecanoate}', 'refs': [8]},
               {'data': '150 {methanol}', 'refs': [8]},
               {'data': '0.24 {acetaldehyde}', 'refs': [8]},
               {'data': '0.24 {butanol}', 'refs': [8]},
               {'data': '0.94 {ethanol}', 'refs': [8]},
               {'data': '10.4 {methanol}', 'refs': [8]},
               {'data': '3.4 {acetaldehyde}', 'refs': [8]},
               {'data': '6.4 {NADH}', 'refs': [8]},
               {'data': '0.044 {Pentanol}', 'refs': [8]},
               {'data': '0.058 {5beta-androstan-3beta-ol-17-one}', 'refs': [8]},
               {'data': '0.0064 {NADH}', 'refs': [8]},
               {'data': '36 {ethanol}', 'refs': [8]},
               {'data': '120 {ethanol}', 'refs': [8]},
               {'data': '120 {', 'refs': [8]},
               {'data': '7.4 {NAD+}', 'refs': [8]},
               {'data': '18 {ethanol}', 'refs': [8]},
               {'data': '23 {Cyclohexanol}', 'refs': [8]},
               {'data': '3.2 {ethanol}', 'refs': [8]},
               {'data': '27 {1-Pentanol}', 'refs': [8]},
               {'data': '210 {Cyclohexanol}', 'refs': [8]},
               {'data': '290 {ethylene glycol}', 'refs': [8]},
               {'data': '0.0074 {NAD+}', 'refs': [8]},
               {'data': '0.0087 {NAD+}', 'refs': [8]},
               {'data': '0.79 {butanol}', 'refs': [8]},
               {'data': '180 {NAD+}', 'refs': [8]},
               {'data': '310 {2-deoxy-D-ribose}', 'refs': [8]},
               {'data': '1.39 {Propanol}', 'refs': [8]},
               {'data': '0.0079 {NAD+}', 'refs': [8]},
               {'data': '105 {NADH}', 'refs': [8]},
               {'data': '560 {2-propanol}', 'refs': [8]},
               {'data': '710 {NAD+}', 'refs': [8]},
               {'data': '1.5 {ethanol}', 'refs': [8, 119]},
               {'data': '0.45 {ethanol}', 'refs': [8, 12, 127]},
               {'data': '0.18 {NAD+}', 'refs': [8, 124]},
               {'data': '0.105 {NADH}', 'refs': [8, 150]},
               {'data': '1.7 {ethanol}', 'refs': [8, 16]},
               {'data': '0.063 {NAD+}', 'refs': [8, 23]},
               {'data': '0.022 {ethanol}', 'refs': [8, 31]},
               {'data': '0.03 {all-trans-retinol}', 'refs': [8, 36]},
               {'data': '28 {ethanol}', 'refs': [8, 36]},
               {'data': '0.074 {NAD+}', 'refs': [8, 55]},
               {'data': '0.1 {12-hydroxydodecanoate}', 'refs': [8, 9]}]),
             ('LO',
              [{'data': 'cytosol',
                'refs': [7, 8, 24, 27, 34, 50, 61, 66, 106, 109]}]),
             ('ME',
              [{'data': 'Zn2+',
                'refs': [5,
                         6,
                         8,
                         10,
                         13,
                         26,
                         27,
                         41,
                         44,
                         46,
                         61,
                         87,
                         94,
                         110,
                         111,
                         122,
                         149,
                         161]},
               {'data': 'Zinc',
                'refs': [5,
                         8,
                         9,
                         12,
                         14,
                         18,
                         36,
                         41,
                         42,
                         43,
                         46,
                         55,
                         68,
                         79,
                         103,
                         104,
                         105]}]),
             ('MW',
              [{'data': '40000',
                'refs': [1,
                         8,
                         9,
                         10,
                         36,
                         42,
                         53,
                         79,
                         80,
                         92,
                         106,
                         109,
                         112,
                         131,
                         132,
                         153]},
               {'data': '78000', 'refs': [8]},
               {'data': '78000-85000', 'refs': [8]},
               {'data': '79000-84000', 'refs': [8]},
               {'data': '82700', 'refs': [8]},
               {'data': '42000', 'refs': [8, 23, 61, 68, 69, 70]},
               {'data': '41000', 'refs': [8, 36]}]),
             ('NSP',
              [{'data': 'all-trans-retinol + NAD+ = all-trans-retinal + NADH',
                'refs': [5, 8]},
               {'data': 'all-trans-retinol + NAD+ = all-trans-retinal + NADH',
                'refs': [5, 8]},
               {'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [5, 8, 10, 31, 41]},
               {'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [5, 8, 10, 31, 41]},
               {'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [5, 8, 10, 31, 41]},
               {'data': 'isobutyramide + NAD+ = ? {r}', 'refs': [8]},
               {'data': '1-butanol + NAD+ = butanal + NADH + H+', 'refs': [8]},
               {'data': '1-butanol + NAD+ = butanal + NADH + H+ {r}',
                'refs': [8]}]),
             ('PHO',
              [{'data': '7.5', 'refs': [3, 5, 8, 10, 46, 55, 75]},
               {'data': '8.5', 'refs': [3, 8, 18, 46, 61, 90, 128]},
               {'data': '8',
                'refs': [4,
                         8,
                         18,
                         25,
                         41,
                         48,
                         72,
                         114,
                         115,
                         119,
                         132,
                         136,
                         151]},
               {'data': '10.5', 'refs': [5, 8, 9, 20, 73, 122, 132]},
               {'data': '7.4', 'refs': [8]},
               {'data': '7-7.5', 'refs': [8]},
               {'data': '7.6', 'refs': [8]},
               {'data': '8.5-8.8', 'refs': [8]},
               {'data': '10-10.5', 'refs': [8]},
               {'data': '7',
                'refs': [8, 10, 52, 89, 122, 137, 138, 139, 163, 164]},
               {'data': '10.8', 'refs': [8, 12]},
               {'data': '10', 'refs': [8, 18, 42, 88, 124, 129, 133, 161]},
               {'data': '5.9', 'refs': [8, 29]},
               {'data': '7.3', 'refs': [8, 41]},
               {'data': '10.4', 'refs': [8, 47]}]),
             ('PHR',
              [{'data': '8-10.5', 'refs': [8]},
               {'data': '8-12', 'refs': [8, 31, 47]}]),
             ('PHS', [{'data': '7-10.6', 'refs': [8]}]),
             ('SA',
              [{'data': '3.3', 'refs': [8]},
               {'data': '0.6', 'refs': [8]},
               {'data': '0.65', 'refs': [8]},
               {'data': '1.47', 'refs': [8]},
               {'data': '1.3', 'refs': [8, 9]}]),
             ('SP',
              [{'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [4,
                         5,
                         7,
                         8,
                         9,
                         10,
                         12,
                         13,
                         14,
                         18,
                         19,
                         21,
                         24,
                         27,
                         28,
                         31,
                         32,
                         34,
                         36,
                         41,
                         42,
                         43,
                         45,
                         47,
                         50,
                         52,
                         53,
                         55,
                         58,
                         61,
                         66,
                         67,
                         68,
                         69,
                         70,
                         71,
                         72,
                         73,
                         75,
                         79,
                         80,
                         81,
                         82,
                         83,
                         88,
                         90,
                         98]},
               {'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [4,
                         5,
                         7,
                         8,
                         9,
                         10,
                         12,
                         13,
                         14,
                         18,
                         19,
                         21,
                         24,
                         27,
                         28,
                         31,
                         32,
                         34,
                         36,
                         41,
                         42,
                         43,
                         45,
                         47,
                         50,
                         52,
                         53,
                         55,
                         58,
                         61,
                         66,
                         67,
                         68,
                         69,
                         70,
                         71,
                         72,
                         73,
                         75,
                         79,
                         80,
                         81,
                         82,
                         83,
                         88,
                         90,
                         98]},
               {'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [4,
                         5,
                         7,
                         8,
                         9,
                         10,
                         12,
                         13,
                         14,
                         18,
                         19,
                         21,
                         24,
                         27,
                         28,
                         31,
                         32,
                         34,
                         36,
                         41,
                         42,
                         43,
                         45,
                         47,
                         50,
                         52,
                         53,
                         55,
                         58,
                         61,
                         66,
                         67,
                         68,
                         69,
                         70,
                         71,
                         72,
                         73,
                         75,
                         79,
                         80,
                         81,
                         82,
                         83,
                         88,
                         90,
                         98]},
               {'data': 'propan-2-ol + NAD+ = acetone + NADH',
                'refs': [4,
                         8,
                         10,
                         12,
                         14,
                         18,
                         38,
                         41,
                         42,
                         46,
                         55,
                         70,
                         72,
                         75,
                         78]},
               {'data': 'propan-2-ol + NAD+ = acetone + NADH',
                'refs': [4,
                         8,
                         10,
                         12,
                         14,
                         18,
                         38,
                         41,
                         42,
                         46,
                         55,
                         70,
                         72,
                         75,
                         78]},
               {'data': 'propanol + NADH = propionaldehyde + NADH',
                'refs': [4,
                         8,
                         10,
                         12,
                         18,
                         19,
                         38,
                         42,
                         46,
                         53,
                         55,
                         67,
                         70,
                         78,
                         81,
                         82]},
               {'data': 'propanol + NADH = propionaldehyde + NADH {}',
                'refs': [4,
                         8,
                         10,
                         12,
                         18,
                         19,
                         38,
                         42,
                         46,
                         53,
                         55,
                         67,
                         70,
                         78,
                         81,
                         82]},
               {'data': 'butan-2-ol + NAD+ = butan-2-one + NADH',
                'refs': [4, 8, 18, 36, 38, 41, 46, 53, 70, 72, 75, 78, 82]},
               {'data': 'butan-2-ol + NAD+ = butan-2-one + NADH',
                'refs': [4, 8, 18, 36, 38, 41, 46, 53, 70, 72, 75, 78, 82]},
               {'data': 'butanol + NAD+ = butyraldehyde + NADH',
                'refs': [4,
                         8,
                         9,
                         10,
                         12,
                         18,
                         36,
                         38,
                         41,
                         42,
                         46,
                         53,
                         67,
                         69,
                         72,
                         75,
                         78,
                         81,
                         82,
                         83]},
               {'data': 'butanol + NAD+ = butyraldehyde + NADH',
                'refs': [4,
                         8,
                         9,
                         10,
                         12,
                         18,
                         36,
                         38,
                         41,
                         42,
                         46,
                         53,
                         67,
                         69,
                         72,
                         75,
                         78,
                         81,
                         82,
                         83]},
               {'data': '7-cis-retinol + NAD+ = 7-cis-retinal + NADH',
                'refs': [5, 8]},
               {'data': 'octanol + NAD+ = octanal + NADH', 'refs': [5, 8]},
               {'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [5,
                         8,
                         10,
                         20,
                         31,
                         41,
                         42,
                         46,
                         48,
                         51,
                         57,
                         71,
                         86,
                         91,
                         92,
                         94,
                         95,
                         99,
                         100,
                         102,
                         105,
                         106,
                         107,
                         108,
                         109,
                         110,
                         111,
                         112,
                         119,
                         125,
                         126,
                         127,
                         132,
                         133,
                         136,
                         137,
                         138,
                         139,
                         155,
                         161,
                         163]},
               {'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [5,
                         8,
                         10,
                         20,
                         31,
                         41,
                         42,
                         46,
                         48,
                         51,
                         57,
                         71,
                         86,
                         91,
                         92,
                         94,
                         95,
                         99,
                         100,
                         102,
                         105,
                         106,
                         107,
                         108,
                         109,
                         110,
                         111,
                         112,
                         119,
                         125,
                         126,
                         127,
                         132,
                         133,
                         136,
                         137,
                         138,
                         139,
                         155,
                         161,
                         163]},
               {'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [5,
                         8,
                         10,
                         20,
                         31,
                         41,
                         42,
                         46,
                         48,
                         51,
                         57,
                         71,
                         86,
                         91,
                         92,
                         94,
                         95,
                         99,
                         100,
                         102,
                         105,
                         106,
                         107,
                         108,
                         109,
                         110,
                         111,
                         112,
                         119,
                         125,
                         126,
                         127,
                         132,
                         133,
                         136,
                         137,
                         138,
                         139,
                         155,
                         161,
                         163]},
               {'data': 'all-trans-retinol + NAD+ = all-trans-retinal + NADH',
                'refs': [5, 8, 36, 41]},
               {'data': 'all-trans-retinol + NAD+ = all-trans-retinal + NADH',
                'refs': [5, 8, 36, 41]},
               {'data': 'hexanol + NAD+ = n-hexanal + NADH',
                'refs': [5, 8, 36, 41, 42, 70, 83]},
               {'data': 'hexanol + NAD+ = n-hexanal + NADH',
                'refs': [5, 8, 36, 41, 42, 70, 83]},
               {'data': 'ethylene glycol + NAD+ = ? + NADH',
                'refs': [5, 8, 38, 69]},
               {'data': 'ethylene glycol + NAD+ = ? + NADH',
                'refs': [5, 8, 38, 69]},
               {'data': '9-cis-retinol + NAD+ = 9-cis-retinal + NADH',
                'refs': [5, 8, 41]},
               {'data': '11-cis-retinol + NAD+ = 11-cis-retinal + NADH',
                'refs': [5, 8, 41]},
               {'data': '13-cis-retinol + NAD+ = 13-cis-retinal + NADH',
                'refs': [5, 8, 41]},
               {'data': 'pentanal + NAD+ = pentanone + NADH',
                'refs': [5, 8, 41, 43, 70, 79]},
               {'data': 'methanol + NAD+ = formaldehyde + NADH + H+',
                'refs': [5,
                         8,
                         9,
                         12,
                         18,
                         38,
                         42,
                         43,
                         52,
                         53,
                         57,
                         58,
                         69,
                         70,
                         79,
                         83,
                         88,
                         99,
                         100,
                         111]},
               {'data': 'methanol + NAD+ = formaldehyde + NADH + H+',
                'refs': [5,
                         8,
                         9,
                         12,
                         18,
                         38,
                         42,
                         43,
                         52,
                         53,
                         57,
                         58,
                         69,
                         70,
                         79,
                         83,
                         88,
                         99,
                         100,
                         111]},
               {'data': 'methanol + NAD+ = formaldehyde + NADH + H+',
                'refs': [5,
                         8,
                         9,
                         12,
                         18,
                         38,
                         42,
                         43,
                         52,
                         53,
                         57,
                         58,
                         69,
                         70,
                         79,
                         83,
                         88,
                         99,
                         100,
                         111]},
               {'data': 'methanol + NAD+ = formaldehyde + NADH + H+',
                'refs': [5,
                         8,
                         9,
                         12,
                         18,
                         38,
                         42,
                         43,
                         52,
                         53,
                         57,
                         58,
                         69,
                         70,
                         79,
                         83,
                         88,
                         99,
                         100,
                         111]},
               {'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH',
                'refs': [5, 8, 9, 18, 36, 41, 46, 58, 69]},
               {'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH',
                'refs': [5, 8, 9, 18, 36, 41, 46, 58, 69]},
               {'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH',
                'refs': [5, 8, 9, 18, 36, 41, 46, 58, 69]},
               {'data': 'cyclohexanol + NAD+ = cyclohexanone + NADH',
                'refs': [5, 8, 9, 18, 36, 43, 67, 69, 78, 81, 83]},
               {'data': 'cyclohexanol + NAD+ = cyclohexanone + NADH',
                'refs': [5, 8, 9, 18, 36, 43, 67, 69, 78, 81, 83]},
               {'data': 'octan-1-ol + NAD+ = n-octanal + NADH',
                'refs': [5, 8, 9, 18, 38, 42, 43, 69, 70, 83]},
               {'data': '3-phenyl-1-propanol + NAD+ = 3-phenyl-1-propanone + '
                        'NADH {}',
                'refs': [8]},
               {'data': '3-phenyl-1-propanol + NAD+ = 3-phenyl-1-propanone + '
                        'NADH',
                'refs': [8]},
               {'data': 'isobutyl alcohol + NAD+ = ? + NADH', 'refs': [8]},
               {'data': 'isopentenyl alcohol + NAD+ = isopentanone + NADH',
                'refs': [8]},
               {'data': '16-hydroxyhexadecanoate + NAD+ = 16-oxohexadecanoic '
                        'acid + NADH',
                'refs': [8]},
               {'data': 'vanillyl alcohol + NAD+ = vanillin + NADH',
                'refs': [8]},
               {'data': 'tryptophol + NAD+ = ? + NADH', 'refs': [8]},
               {'data': '2-deoxy-D-ribose + NAD+ = ? + NADH', 'refs': [8]},
               {'data': '17beta-hydroxyetiocholan-3-one + NAD+ = '
                        'ethiocholan-3,17-dione + NADH',
                'refs': [8]},
               {'data': 'phenylalaninol + NAD+ = ? + NADH', 'refs': [8]},
               {'data': 'digitose + NAD+ = ? + NADH', 'refs': [8]},
               {'data': '3-pyridylcarbinol + NAD+ = pyridine-3-carbaldehyde + '
                        'NADH',
                'refs': [8]},
               {'data': 'trans-4-', 'refs': [8]},
               {'data': 'retinol + NAD+ = retinal + NADH', 'refs': [8]},
               {'data': '5alpha-pregnan-3beta-ol-20-one + NAD+ = '
                        '5alpha-pregnan-3,20-dione + NADH',
                'refs': [8]},
               {'data': 'isobutyramide + NAD+ = ? {r}', 'refs': [8]},
               {'data': '3,4-dihydro-retinol + NAD+ = 3,4-dihydro-retinal {r}',
                'refs': [8]},
               {'data': '4-hydroxy-retinol + NAD+ = 4-oxo-retinal + NADH {r}',
                'refs': [8]},
               {'data': '5beta-cholanic acid-3-one + NADH = 5beta-cholanic '
                        'acid-3-ol + NAD+',
                'refs': [8]},
               {'data': '5beta-pregnan-3,20-dione + NADH = ?', 'refs': [8]},
               {'data': '5beta-pregnan-3beta-ol-20-one + NAD+ = '
                        '5beta-pregnan-3,20-dione + NADH',
                'refs': [8]},
               {'data': 'hexanol + NAD+ = hexanal + NADH', 'refs': [8]},
               {'data': '4-methoxy-1-naphthaldehyde + NAD+ = '
                        '4-methoxy-1-naphthyl alcohol + NADH + H+',
                'refs': [8]},
               {'data': '4-methoxy-1-naphthaldehyde + NADH + H+ = '
                        '4-methoxynaphthalene-1-carbaldehyde + NAD+',
                'refs': [8]},
               {'data': '6-methoxy-2-naphthaldehyde + NADH + H+ = '
                        '6-methoxy-2-naphthyl alcohol + NAD+',
                'refs': [8]},
               {'data': '6-methoxy-2-naphthaldehyde + NADH + H+ =',
                'refs': [8]},
               {'data': 'm-nitrobenzaldehyde + NAD+ = m-nitrobenzyl alcohol + '
                        'NADH + H+',
                'refs': [8]},
               {'data': 'n-butanol + NAD+ = butylaldehyde + NADH + H+',
                'refs': [8]},
               {'data': 'n-butanol + NAD+ = butylaldehyde + NADH + H+ {r}',
                'refs': [8]},
               {'data': 'p-nitrobenzaldehyde + NADH + H+ = p-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [8]},
               {'data': 'retinal + NADH + H+ = retinol + NAD+', 'refs': [8]},
               {'data': '4-methoxy-1-naphthaldehyde + NAD+ = '
                        '4-methoxy-1-naphthol + NADH + H+',
                'refs': [8]},
               {'data': '4-nitrosodimethylaniline + NAD+ = ? + NADH + H+',
                'refs': [8]},
               {'data': '6-methoxy-2-naphthaldehyde + NADH + H+ = '
                        '6-methoxy-2-naphtol + NAD+',
                'refs': [8]},
               {'data': 'n-butanol + NAD+ = n-butanal + NADH', 'refs': [8, 10]},
               {'data': 'n-butanol + NAD+ = n-butanal + NADH {r}',
                'refs': [8, 10]},
               {'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH + H+',
                'refs': [8,
                         10,
                         41,
                         46,
                         47,
                         57,
                         71,
                         95,
                         96,
                         105,
                         112,
                         113,
                         119,
                         132,
                         142]},
               {'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH + H+',
                'refs': [8,
                         10,
                         41,
                         46,
                         47,
                         57,
                         71,
                         95,
                         96,
                         105,
                         112,
                         113,
                         119,
                         132,
                         142]},
               {'data': 'cyclohexanone + NADH + H+ = cyclohexanol + NAD+',
                'refs': [8, 124, 143]},
               {'data': 'cyclohexanone + NADH + H+ = cyclohexanol + NAD+',
                'refs': [8, 124, 143]},
               {'data': '3-nitrobenzaldehyde + NADH + H+ = 3-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [8, 128]},
               {'data': '3-nitrobenzaldehyde + NADH + H+ = 3-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [8, 128]},
               {'data': '1-butanol + NAD+ = butanal + NADH + H+',
                'refs': [8,
                         31,
                         48,
                         57,
                         92,
                         96,
                         98,
                         105,
                         110,
                         111,
                         112,
                         127,
                         132,
                         161]},
               {'data': '1-butanol + NAD+ = butanal + NADH + H+',
                'refs': [8,
                         31,
                         48,
                         57,
                         92,
                         96,
                         98,
                         105,
                         110,
                         111,
                         112,
                         127,
                         132,
                         161]},
               {'data': '5beta-androstan-3beta-ol-17-one + NAD+ = '
                        '5beta-androstan-3,17-dione + NADH',
                'refs': [8, 41]},
               {'data': '5beta-androstan-17beta-ol-3-one + NAD+ = '
                        '5beta-androstan-3,17-dione + NADH',
                'refs': [8, 41]},
               {'data': 'octan-2-ol + NAD+ = octan-2-one + NADH',
                'refs': [8, 41, 70, 78]},
               {'data': 'furfuryl alcohol + NAD+ = furfural + NADH',
                'refs': [8, 42]},
               {'data': 'furfuryl alcohol + NAD+ = furfural + NADH',
                'refs': [8, 42]},
               {'data': '5alpha-androstan-17beta-ol-3-one + NADH + H+ = '
                        '3beta,17beta-dihydroxy-5alpha-androstan + NAD+ {}',
                'refs': [8, 9]},
               {'data': '5alpha-androstan-17beta-ol-3-one + NADH + H+ = '
                        '3beta,17beta-dihydroxy-5alpha-androstan + NAD+',
                'refs': [8, 9]},
               {'data': 'm-nitrobenzaldehyde + NADH + H+ = m-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [8, 9]},
               {'data': 'm-nitrobenzaldehyde + NADH + H+ = m-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [8, 9]},
               {'data': 'pentanol + NAD+ = n-pentanal + NADH',
                'refs': [8, 9, 12, 18, 19, 38, 42, 67, 68, 69, 78, 81]},
               {'data': '12-hydroxydodecanoate + NAD+ = 12-oxododecanoic acid '
                        '+ NADH',
                'refs': [8, 9, 36, 69]},
               {'data': '12-hydroxydodecanoate + NAD+ = 12-oxododecanoic acid '
                        '+ NADH',
                'refs': [8, 9, 36, 69]},
               {'data': 'octanal + NADH + H+ = octanol + NAD+',
                'refs': [8, 9, 69]}]),
             ('ST',
              [{'data': 'liver',
                'refs': [1,
                         2,
                         5,
                         8,
                         9,
                         12,
                         36,
                         41,
                         43,
                         53,
                         59,
                         69,
                         73,
                         79,
                         80,
                         83,
                         106,
                         130,
                         131]},
               {'data': 'hepatocyte', 'refs': [5, 8]},
               {'data': 'retina', 'refs': [5, 8]},
               {'data': 'stomach', 'refs': [5, 8, 9, 84]},
               {'data': 'skin', 'refs': [8]},
               {'data': 'hepatoma cell', 'refs': [8]},
               {'data': 'serum', 'refs': [8]},
               {'data': 'adenocarcinoma cell', 'refs': [8]},
               {'data': 'aorta', 'refs': [8]},
               {'data': 'esophagus', 'refs': [8]},
               {'data': 'blood serum', 'refs': [8]},
               {'data': 'colorectum', 'refs': [8]},
               {'data': 'cervical cancer cell', 'refs': [8]},
               {'data': 'pancreas', 'refs': [8, 9]},
               {'data': 'uterus', 'refs': [8, 9]},
               {'data': 'kidney', 'refs': [8, 9]},
               {'data': 'lung', 'refs': [8, 9]},
               {'data': 'cornea', 'refs': [8, 9]},
               {'data': 'testis', 'refs': [8, 9, 36]}]),
             ('SU',
              [{'data': '?',
                'refs': [1,
                         8,
                         14,
                         15,
                         24,
                         25,
                         31,
                         73,
                         80,
                         85,
                         98,
                         103,
                         104,
                         126,
                         131,
                         149,
                         151,
                         153,
                         158]},
               {'data': 'dimer',
                'refs': [3,
                         4,
                         5,
                         8,
                         9,
                         10,
                         12,
                         16,
                         18,
                         19,
                         20,
                         21,
                         26,
                         36,
                         41,
                         42,
                         44,
                         45,
                         46,
                         53,
                         61,
                         67,
                         68,
                         69,
                         72,
                         75,
                         78,
                         79,
                         81,
                         88,
                         100,
                         149,
                         161]},
               {'data': 'More', 'refs': [8, 27, 48, 124]}]),
             ('SY',
              [{'data': 'alcohol dehydrogenase 1', 'refs': [5, 8, 10]},
               {'data': 'ADH',
                'refs': [5,
                         8,
                         10,
                         13,
                         27,
                         37,
                         41,
                         46,
                         61,
                         71,
                         87,
                         88,
                         91,
                         95,
                         105,
                         108,
                         111,
                         112,
                         125,
                         126,
                         166]},
               {'data': 'ALDH', 'refs': [8]},
               {'data': 'ADH1C*1', 'refs': [8]},
               {'data': 'ADH1C*2', 'refs': [8]},
               {'data': 'aldehyde dehydrogenase', 'refs': [8]},
               {'data': 'class III ADH', 'refs': [8]},
               {'data': 'class I ADH', 'refs': [8]},
               {'data': 'class II ADH', 'refs': [8]},
               {'data': 'class IV ADH', 'refs': [8]},
               {'data': 'ADH1B', 'refs': [8]},
               {'data': 'ADH1', 'refs': [8, 10, 96, 98, 113, 114, 136, 162]},
               {'data': 'ADH4', 'refs': [8, 102, 104, 109, 139]}]),
             ('TN',
              [{'data': '0.55 {all-trans-retinal}', 'refs': [8]},
               {'data': '0.4 {all-trans-retinol}', 'refs': [8]},
               {'data': '8 {Pentanol}', 'refs': [8]},
               {'data': '0.7 {ethanol}', 'refs': [8]},
               {'data': '0.7 {butanol}', 'refs': [8]},
               {'data': '0.9 {all-trans-retinol}', 'refs': [8]},
               {'data': '0.04 {Octanol}', 'refs': [8]},
               {'data': '16 {Pentanol}', 'refs': [8]},
               {'data': '2.5 {ethanol}', 'refs': [8]},
               {'data': '2.5 {3,4-dihydro-retinol}', 'refs': [8]},
               {'data': '6.17 {16-hydroxyhexadecanoate}', 'refs': [8]},
               {'data': '20 {4-oxo-retinal}', 'refs': [8]},
               {'data': '4 {ethanol}', 'refs': [8]},
               {'data': '4 {12-hydroxydodecanoate}', 'refs': [8]},
               {'data': '0.11 {retinol}', 'refs': [8]},
               {'data': '3.83 {ethanol}', 'refs': [8]},
               {'data': '4.33 {Octanol}', 'refs': [8]},
               {'data': '0.167 {ethanol}', 'refs': [8]},
               {'data': '0.167 {4-oxo-retinal}', 'refs': [8]},
               {'data': '0.183 {1-Pentanol}', 'refs': [8]},
               {'data': '0.583 {Cyclohexanol}', 'refs': [8]},
               {'data': '0.75 {2-propanol}', 'refs': [8]},
               {'data': '0.75 {ethylene glycol}', 'refs': [8]},
               {'data': '2.83 {1-Octanol}', 'refs': [8]},
               {'data': '2.83 {2-deoxy-D-ribose}', 'refs': [8]},
               {'data': '2.83 {4-hydroxy-retinol}', 'refs': [8]},
               {'data': '7.5 {3-Phenyl-1-propanol}', 'refs': [8]},
               {'data': '3.33 {octanal}', 'refs': [8]},
               {'data': '7.33 {Octanol}', 'refs': [8]},
               {'data': '0.333 {12-Hydroxydodecanoic acid}', 'refs': [8]},
               {'data': '2.17 {', 'refs': [8]},
               {'data': '0.018 {all-trans-retinal}', 'refs': [8]},
               {'data': '0.092 {4-hydroxy-retinol}', 'refs': [8]},
               {'data': '0.25 {all-trans-retinol}', 'refs': [8]},
               {'data': '0.667 {Pentanol}', 'refs': [8]},
               {'data': '0.038 {Octanol}', 'refs': [8]},
               {'data': '2.95 {12-hydroxydodecanoate}', 'refs': [8]},
               {'data': '8.33 {Octanol}', 'refs': [8]},
               {'data': '9.17 {benzyl alcohol}', 'refs': [8]},
               {'data': '0.22 {3,4-dihydro-retinal}', 'refs': [8]},
               {'data': '4.67 {benzyl alcohol}', 'refs': [8]},
               {'data': '17.2 {Propanol}', 'refs': [8]},
               {'data': '0.245 {Pentanol}', 'refs': [8]},
               {'data': '0.717 {NAD+}', 'refs': [8]},
               {'data': '1.83 {all-trans-retinal}', 'refs': [8]},
               {'data': '1.83 {tryptophol}', 'refs': [8]},
               {'data': '0.102 {methanol}', 'refs': [8]},
               {'data': '0.467 {Vanillyl alcohol}', 'refs': [8]},
               {'data': '0.683 {3-Pyridylcarbinol}', 'refs': [8]},
               {'data': '1.22 {3,4-dihydro-retinal}', 'refs': [8]},
               {'data': '3.03 {12-hydroxydodecanoate}', 'refs': [8]},
               {'data': '7.83 {ethanol}', 'refs': [8]},
               {'data': '7.83 {4-oxo-retinal}', 'refs': [8]},
               {'data': '8.67 {Vanillyl alcohol}', 'refs': [8]},
               {'data': '10.2 {ethanol}', 'refs': [8]},
               {'data': '19.5 {Hexanol}', 'refs': [8]},
               {'data': '30.7 {ethanol}', 'refs': [8]},
               {'data': '34.8 {butanol}', 'refs': [8]},
               {'data': '0.175 {ethanol}', 'refs': [8]},
               {'data': '0.028 {all-trans-retinol}', 'refs': [8]},
               {'data': '0.087 {retinol}', 'refs': [8]},
               {'data': '34.2 {4-hydroxy-retinol}', 'refs': [8]},
               {'data': '0.088 {3,4-dihydro-retinol}', 'refs': [8]}]),
             ('TO',
              [{'data': '25', 'refs': [5, 8, 10, 25, 40, 61]},
               {'data': '30-37', 'refs': [8, 41]}]),
             ('TS', [{'data': '23', 'refs': [8]}]),
             ('references',
              {1: {'info': 'Talbot, B.G.; Qureshi, A.A.; Cohen, R.; Thirion, '
                           'J.P.: Purification and properties of two distinct '
                           'groups of ADH isozymes from Chinese hamster liver. '
                           'Biochem. Genet. (1981) 19, 813-829.',
                   'pubmed': '6794566'},
               2: {'info': 'Fong, W.P.: Isolation and characterization of '
                           'grass carp (Ctenopharyngodon idellus) liver '
                           'alcohol dehydrogenase. Comp. Biochem. Physiol. B '
                           '(1991) 98, 297-302.',
                   'pubmed': ''},
               3: {'info': 'Pessione, E.; Pergola, L.; Cavaletto, M.; Giunta, '
                           'C.; Trotta, A.; Vanni, A.: Extraction, '
                           'purification and characterization of ADH1 from the '
                           'budding yeast Kluyveromyces marxianus. Ital. J. '
                           'Biochem. (1990) 39, 71-82.',
                   'pubmed': '2193901'},
               4: {'info': 'Leblova, S.; El Ahmad, M.: Characterization of '
                           'alcohol dehydrogenase isolated from germinating '
                           'bean (Vicia faba) seeds. Collect. Czech. Chem. '
                           'Commun. (1989) 54, 2519-2527.',
                   'pubmed': ''},
               5: {'info': 'Keung, W.M.; Ho, Y.W.; Fong, W.P.; Lee, C.Y.: '
                           'Isolation and characterization of shrew (Suncus '
                           'murinus) liver alcohol dehydrogenase. Comp. '
                           'Biochem. Physiol. B (1989) 93, 169-173.',
                   'pubmed': '2666017'},
               6: {'info': 'Tong, W.F.; Lin, S.W.: Purification and '
                           'biochemical properties of rice alcohol '
                           'dehydrogenase. Bot. Bull. Acad. Sin. (1988) 29, '
                           '245-253.',
                   'pubmed': ''},
               7: {'info': 'Van Geyt, J.; Jacobs, M.; Triest, L.: '
                           'Characterization of alcohol dehydrogenase in Najas '
                           'marina L. Aquat. Bot. (1987) 28, 129-141.',
                   'pubmed': ''},
               8: {'info': 'Vilageliu, L.; Juan, E.; Gonzalez-Duarte, R.: '
                           'Determination of some biochemical features of '
                           'alcohol dehydrogenase from Drosophila '
                           'melanogaster, Drosophila simulans, Drosophila '
                           'virilis, Drosophila funebris, Drosophila imigrans '
                           'and drosophila lebanonensis. Comparison of their '
                           'properties and estimation of the homology of the '
                           'ADH enzyme of different species. Adv. Genet. , '
                           'Dev. , Evol. Drosophila, [Proc. Eur. Drosophila '
                           'Res. Conf. ] (Lakovaara, S. , ed. ) Plenum N. Y. '
                           '(1982) 7, 237-250.',
                   'pubmed': ''},
               9: {'info': 'Edenberg, H.J.; Brown, C.J.; Carr, L.G.; Ho, W.H.; '
                           'Hu, M.W.: Alcohol dehydrogenase gene expression '
                           'and cloning of the mouse chi-like ADH. Adv. Exp. '
                           'Med. Biol. (1991) 284, 253-262.',
                   'pubmed': '2053480'},
               10: {'info': 'Herrera, E.; Zorzano, A.; Fresneda, V.: '
                            'Comparative kinetics of human and rat liver '
                            'alcohol dehydrogenase. Biochem. Soc. Trans. '
                            '(1983) 11, 729-730.',
                    'pubmed': ''},
               11: {'info': 'Dafeldecker, W.P.; Vallee, B.L.: Organ-specific '
                            'human alcohol dehydrogenase: isolation and '
                            'characterization of isozymes from testis. '
                            'Biochem. Biophys. Res. Commun. (1986) 134, '
                            '1056-1063.',
                    'pubmed': '2936344'},
               12: {'info': 'Woronick, C.L.: Alcohol dehydrogenase from human '
                            'liver. Methods Enzymol. (1975) 41B, 369-374.',
                    'pubmed': '236461'},
               13: {'info': 'Wagner, F.W.; Burger, A.R.; Vallee, B.L.: Kinetic '
                            'properties of human liver alcohol dehydrogenase: '
                            'oxidation of alcohols by class I isoenzymes. '
                            'Biochemistry (1983) 22, 1857-1863.',
                    'pubmed': '6342669'},
               14: {'info': 'Ditlow, C.C.; Holmquist, B.; Morelock, M.M.; '
                            'Vallee, B.L.: Physical and enzymatic properties '
                            'of a class II alcohol dehydrogenase isozyme of '
                            'human liver: pi-ADH. Biochemistry (1984) 23, '
                            '6363-6368.',
                    'pubmed': '6397223'},
               15: {'info': 'Yin, S.J.; Bosron, W.F.; Magnes, L.J.; Li, T.K.: '
                            'Human liver alcohol dehydrogenase: purification '
                            'and kinetic characterization of the beta 2 beta '
                            '2, beta 2 beta 1, alpha beta 2, and beta 2 gamma '
                            '1 Oriental isoenzymes. Biochemistry (1984) 23, '
                            '5847-5853.',
                    'pubmed': '6395883'},
               16: {'info': 'Wagner, F.W.; Pares, X.; Holmquist, B.; Vallee, '
                            'B.L.: Physical and enzymatic properties of a '
                            'class III isozyme of human liver alcohol '
                            'dehydrogenase: chi-ADH. Biochemistry (1984) 23, '
                            '2193-2199.',
                    'pubmed': '6375718'},
               17: {'info': 'Bosron, W.F.; Magnes, L.J.; Li, T.K.: Kinetic and '
                            'electrophoretic properties of native and '
                            'recombined isoenzymes of human liver alcohol '
                            'dehydrogenase. Biochemistry (1983) 22, 1852-1857.',
                    'pubmed': '6342668'},
               18: {'info': 'Bosron, W.F.; Li, T.K.: Isolation and '
                            'characterization of an anodic form of human liver '
                            'alcohol dehydrogenase. Biochem. Biophys. Res. '
                            'Commun. (1977) 74, 85-91.',
                    'pubmed': '836289'},
               19: {'info': 'Schneider-Bernloehr, H.; Formicka-Kozlowska, G.; '
                            'Buehler, R.; Wartburg, J.P.; Zeppezauer, M.: '
                            'Active-site-specific zinc-depleted and '
                            'reconstituted cobalt(II) human-liver alcohol '
                            'dehydrogenase. Preparation, characterization and '
                            'complexation with NADH and '
                            'trans-4-(N,N-dimethylamino)-cinnamaldehyde. Eur. '
                            'J. Biochem. (1988) 173, 275-280.',
                    'pubmed': '3360008'},
               20: {'info': 'Burnell, J.C.; Li, T.K.; Bosron, W.F.: '
                            'Purification and steady-state kinetic '
                            'characterization of human liver beta 3 beta 3 '
                            'alcohol dehydrogenase. Biochemistry (1989) 28, '
                            '6810-6815.',
                    'pubmed': '2819035'},
               21: {'info': 'Pares, X.; Vallee, B.L.: New human liver alcohol '
                            'dehydrogenase forms with unique kinetic '
                            'characteristics. Biochem. Biophys. Res. Commun. '
                            '(1981) 98, 122-130.',
                    'pubmed': '7011320'},
               22: {'info': 'Bosron, W.F.; Li, T.K.; Vallee, B.L.: New '
                            'molecular forms of human liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'ADHIndianapolis. Proc. Natl. Acad. Sci. USA '
                            '(1980) 77, 5784-5788.',
                    'pubmed': '7003596'},
               23: {'info': 'Bosron, W.F.; Li, T.K.; Dafeldecker, W.P.; '
                            'Vallee, B.L.: Human liver pig-alcohol '
                            'dehydrogenase: kinetic and molecular properties. '
                            'Biochemistry (1979) 18, 1101-1105.',
                    'pubmed': '427099'},
               24: {'info': 'Dafeldecker, W.P.; Pares, X.; Vallee, B.L.; '
                            'Bosron, W.F.; Li, T.K.: Simian liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'isoenzymes from Saimiri sciureus. Biochemistry '
                            '(1981) 20, 856-861.',
                    'pubmed': '7011375'},
               25: {'info': 'Dafeldecker, W.P.; Meadow, P.E.; Pares, X.; '
                            'Vallee, B.L.: Simian liver alcohol dehydrogenase: '
                            'isolation and characterization of isoenzymes from '
                            'Macaca mulatta. Biochemistry (1981) 20, '
                            '6729-6734.',
                    'pubmed': '7030395'},
               26: {'info': 'Kvassman, J.; Pettersson, G.: Kinetics of '
                            'coenzyme binding to liver alcohol dehydrogenase '
                            'in the pH range 10-12. Eur. J. Biochem. (1987) '
                            '166, 167-172.',
                    'pubmed': '3595610'},
               27: {'info': 'Andersson, L.; Mosbach, K.: Alcohol dehydrogenase '
                            'from horse liver by affinity chromatography. '
                            'Methods Enzymol. (1982) 89, 435-445.',
                    'pubmed': '6755178'},
               28: {'info': 'Pietruszko, R.: Alcohol dehydrogenase from horse '
                            'liver, steroid-active SS isoenzyme. Methods '
                            'Enzymol. (1982) 89, 429-435.',
                    'pubmed': ''},
               29: {'info': 'Dahl, K.H.; Eklund, H.; McKinley-McKee, J.S.: '
                            'Enantioselective affinity labelling of horse '
                            'liver alcohol dehydrogenase. Correlation of '
                            'inactivation kinetics with the three-dimensional '
                            'structure of the enzyme. Biochem. J. (1983) 211, '
                            '391-396.',
                    'pubmed': '6347187'},
               31: {'info': 'Adolph, H.W.; Maurer, P.; Schneider-Bernloehr, '
                            'H.; Sartorius, C.; Zeppezauer, M.: Substrate '
                            'specificity and stereoselectivity of horse liver '
                            'alcohol dehydrogenase. Kinetic evaluation of '
                            'binding and activation parameters controlling the '
                            'catalytic cycles of unbranched, acyclic secondary '
                            'alcohols and ketones as substrates of the native '
                            'and active-site-specific Co(II)-substituted '
                            'enzyme. Eur. J. Biochem. (1991) 201, 615-625.',
                    'pubmed': '1935957'},
               32: {'info': 'Freudenreich, C.; Samama, J.P.; Biellmann, J.F.: '
                            'Design of inhibitors from the three-dimensional '
                            'structure of alcohol dehydrogenase. Chemical '
                            'synthesis and enzymatic properties. J. Am. Chem. '
                            'Soc. (1984) 106, 3344-3353.',
                    'pubmed': ''},
               33: {'info': 'Samama, J.P.; Hirsch, D.; Goulas, P.; Biellmann, '
                            'J.F.: Dependence of the substrate specificity and '
                            'kinetic mechanism of horse-liver alcohol '
                            'dehydrogenase on the size of the C-3 pyridinium '
                            'substituent. 3-Benzoylpyridine-adenine '
                            'dinucleotide. Eur. J. Biochem. (1986) 159, '
                            '375-380.',
                    'pubmed': '3758068'},
               34: {'info': 'Eklund, H.: Coenzyme binding in alcohol '
                            'dehydrogenase. Biochem. Soc. Trans. (1989) 17, '
                            '293-296.',
                    'pubmed': '2753206'},
               36: {'info': 'Maret, W.; Andersson, I.; Dietrich, H.; '
                            'Schneider-Bernloehr, H.; Einarsson, R.; '
                            'Zeppezauer, M.: Site-specific substituted '
                            'cobalt(II) horse liver alcohol dehydrogenases. '
                            'Preparation and characterization in solution, '
                            'crystalline and immobilized state. Eur. J. '
                            'Biochem. (1979) 98, 501-512.',
                    'pubmed': '488110'},
               37: {'info': 'Skerker, P.S.; Clark, D.S.: Thermostability of '
                            'alcohol dehydrogenase: evidence for distinct '
                            'subunits with different deactivation properties. '
                            'Biotechnol. Bioeng. (1989) 33, 62-71.',
                    'pubmed': '18587844'},
               38: {'info': 'Benach, J.; Atrian, S.; Gonzalez-Duarte, R.; '
                            'Ladenstein, R.: The catalytic reaction and '
                            'inhibition mechanism of Drosophila alcohol '
                            'dehydrogenase: observation of an enzyme-bound '
                            'NAD-ketone adduct at 1.4 A resolution by X-ray '
                            'crystallography. J. Mol. Biol. (1999) 289, '
                            '335-355.',
                    'pubmed': '10366509'},
               39: {'info': 'Tsai, C.S.: Multifunctionality of liver alcohol '
                            'dehydrogenase: kinetic and mechanistic studies of '
                            'esterase reaction. Arch. Biochem. Biophys. (1982) '
                            '213, 635-642.',
                    'pubmed': '7041828'},
               40: {'info': 'Favilla, R.; Cavatorta, P.; Mazzini, A.; Fava, '
                            'A.: The peroxidatic reaction catalyzed by horse '
                            'liver alcohol dehydrogenase. 2. Steady-state '
                            'kinetics and inactivation. Eur. J. Biochem. '
                            '(1980) 104, 223-227.',
                    'pubmed': '6989598'},
               41: {'info': 'Ryzewski, C.N.; Pietruszko, R.: Kinetic mechanism '
                            'of horse liver alcohol dehydrogenase SS. '
                            'Biochemistry (1980) 19, 4843-4848.',
                    'pubmed': '7000185'},
               42: {'info': 'Ryzewski, C.N.; Pietruszko, R.: Horse liver '
                            'alcohol dehydrogenase SS: purification and '
                            'characterization of the homogenous isoenzyme. '
                            'Arch. Biochem. Biophys. (1977) 183, 73-82.',
                    'pubmed': '20851'},
               43: {'info': 'Winberg, J.O.; McKinley-McKee, J.S.: Drosophila '
                            'melanogaster alcohol dehydrogenase: '
                            'product-inhibition studies. Biochem. J. (1994) '
                            '301, 901-909.',
                    'pubmed': '8053914'},
               44: {'info': 'von Bahr-Lindstroem, H.; Andersson, L.; Mosbach, '
                            'K.; Joernvall, H.: Purification and '
                            'characterization of chicken liver alcohol '
                            'dehydrogenase. FEBS Lett. (1978) 89, 293-297.',
                    'pubmed': '658420'},
               45: {'info': 'Hoshino, T.; Ishigura, I.; Ohta, Y.: Rabbit liver '
                            'alcohol dehydrogenase: purification and '
                            'properties. J. Biochem. (1985) 97, 1163-1172.',
                    'pubmed': '3161873'},
               46: {'info': 'Keung, W.M.; Yip, P.K.: Rabbit liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'class I isozymes. Biochem. Biophys. Res. Commun. '
                            '(1989) 158, 445-453.',
                    'pubmed': '2916992'},
               47: {'info': 'Keung, W.M.: A genuine organ specific alcohol '
                            'dehydrogenase from hamster testes: isolation, '
                            'characterization and developmental changes. '
                            'Biochem. Biophys. Res. Commun. (1988) 156, 38-45.',
                    'pubmed': '3178842'},
               48: {'info': 'Algar, E.M.; Seeley, T.L.; Holmes, R.S.: '
                            'Purification and molecular properties of mouse '
                            'alcohol dehydrogenase isozymes. Eur. J. Biochem. '
                            '(1983) 137, 139-147.',
                    'pubmed': '6360682'},
               50: {'info': 'Pares, X.; Moreno, A.; Cederlund, E.; Hoeoeg, '
                            'J.O.; Joernvall, H.: Class IV mammalian alcohol '
                            'dehydrogenase. Structural data of the rat stomach '
                            'enzyme reveal a new class well separated from '
                            'those already characterized. FEBS Lett. (1990) '
                            '277, 115-118.',
                    'pubmed': '2269340'},
               51: {'info': 'Mezey, E.; Potter, J.J.: Separation and partial '
                            'characterization of multiple forms of rat liver '
                            'alcohol dehydrogenase. Arch. Biochem. Biophys. '
                            '(1983) 225, 787-794.',
                    'pubmed': '6354095'},
               52: {'info': 'Hjelmqvist, L.; Shafqqat, J.; Siddiqi, A.R.; '
                            'Joernvall, H.: Linking of isoenzyme and class '
                            'variability patterns in the emergence of novel '
                            'alcohol dehydrogenase functions. Characterization '
                            'of isozymes in Uromastix hardwickii. Eur. J. '
                            'Biochem. (1996) 236, 563-570.',
                    'pubmed': '8612630'},
               53: {'info': 'Kedishvili, N.Y.; Bosron, W.F.; Stone, C.L.; '
                            'Hurley, T.D.; Peggs, C.F.; Thomasson, H.R.; '
                            'Popov, K.M.; Carr, L.G.; Edenberg, H.J.; Li, '
                            'T.K.: Expression and kinetic characterization of '
                            'recombinant human stomach alcohol dehydrogenase. '
                            'Active-site amino acid sequence explains '
                            'substrate specificity copared with liver '
                            'isozymes. J. Biol. Chem. (1995) 270, 3625-3630.',
                    'pubmed': '7876099'},
               54: {'info': 'Plapp, B.V.; Sogin, D.C.; Dworschack, R.T.; '
                            'Bohlken, D.P.; Woenckhaus, C.: Kinetics of native '
                            'and modified liver alcohol dehydrogenase with '
                            'coenzyme analogues: isomerization of '
                            'enzyme-nicotinamide adenine dinucleotide complex. '
                            'Biochemistry (1986) 25, 5396-5402.',
                    'pubmed': '3778867'},
               55: {'info': 'Li, H.; Hallows, W.H.; Punzi, J.S.; Marquez, '
                            'V.E.; Carrell, H.L.; Pankiewicz, K.W.; Watanabe, '
                            'K.A.; Goldstein, B.M.: Crystallographic studies '
                            'of two alcohol dehydrogenase-bound analogues of '
                            'thiazole-4-carboxamide adenine dinucleotide '
                            '(TAD), the active anabolite of the antitumor '
                            'agent tiazofurin. Biochemistry (1994) 33, 23-32.',
                    'pubmed': '8286346'},
               57: {'info': 'Shafqat, J.; Hjelmqvist, L.; Joernvall, H.: Liver '
                            'class-I alcohol dehydrogenase isozyme '
                            'relationships and constant patterns in a variable '
                            'basic structure. Distinctions from '
                            'characterization of an ethanol dehydrogenase in '
                            'cobra, Naja naja. Eur. J. Biochem. (1996) 236, '
                            '571-578.',
                    'pubmed': '8612631'},
               58: {'info': 'Retzios, A.; Thatcher, D.R.: Characterization of '
                            'the Adhf and Adhus alleloenzymes of Drosophila '
                            'melanogaster (fruitfly) alcohol dehydrogenase. '
                            'Biochem. Soc. Trans. (1981) 9, 298-299.',
                    'pubmed': ''},
               59: {'info': 'Bauermeister, A.; Sargent, J.: Purification and '
                            'properties of an alcohol dehydrogenase from the '
                            'liver and intestinal caecum of rainbow trout '
                            '(Salmo gairdnerii). Biochem. Soc. Trans. (1978) '
                            '6, 222-224.',
                    'pubmed': '640168'},
               60: {'info': 'Nussrallah, B.A.; Dam, R.; Wagner, F.W.: '
                            'Characterization of Coturnix quail liver alcohol '
                            'dehydrogenase enzymes. Biochemistry (1989) 28, '
                            '6245-6251.',
                    'pubmed': '2789998'},
               61: {'info': 'Winberg, J.O.; Hovik, R.; McKinley-McKee, J.S.; '
                            'Juan, E.; Gonzalez-Duarte, R.: Biochemical '
                            'properties of alcohol dehydrogenase from '
                            'Drosophila lebanonensis. Biochem. J. (1986) 235, '
                            '481-490.',
                    'pubmed': '2943270'},
               63: {'info': 'Heinstra, P.W.H.; Thoerig, G.E.W.; Scharloo, W.; '
                            'Drenth, W.; Nolte, R.J.M.: Kinetics and '
                            'thermodynamics of ethanol oxidation catalyzed by '
                            'genetic variants of the alcohol dehydrogenase '
                            'from Drosophila melanogaster and D. simulans. '
                            'Biochim. Biophys. Acta (1988) 967, 224-233.',
                    'pubmed': '3142528'},
               64: {'info': 'Juan, E.; Gonzalez-Duarte, R.: Determination of '
                            'some biochemical and structural features of '
                            'alcohol dehydrogenases from Drosophila simulans '
                            'and Drosophila virilis. Comparison of their '
                            'properties with the Drosophila melanogaster Adhs '
                            'enzyme. Biochem. J. (1981) 195, 61-69.',
                    'pubmed': '6796069'},
               66: {'info': 'Rella, R.; Raia, C.A.; Pensa, M.; Pisani, F.M.; '
                            'Gambacorta, A.; de Rosa, M.; Rossi, M.: A novel '
                            'archaebacterial NAD+-dependent alcohol '
                            'dehydrogenase. Purification and properties. Eur. '
                            'J. Biochem. (1987) 167, 475-479.',
                    'pubmed': '3115775'},
               67: {'info': 'Wills, C.; Kratofil, P.; Londo, D.; Martin, T.: '
                            'Characterization of the two alcohol '
                            'dehydrogenases of Zymomonas mobilis. Arch. '
                            'Biochem. Biophys. (1981) 210, 775-785.',
                    'pubmed': '7030207'},
               68: {'info': 'Kinoshita, S.; Kakizono, T.; Kadota, K.; Das, K.; '
                            'Taguchi, H.: Purification of two alcohol '
                            'dehydrogenases from Zymomonas mobilis and their '
                            'properties. Appl. Microbiol. Biotechnol. (1985) '
                            '22, 249-254.',
                    'pubmed': ''},
               69: {'info': 'Grondal, E.J.M.; Betz, A.; Kreuzberg, K.: Partial '
                            'purification and properties of alcohol '
                            'dehydrogenase from unicellular green alga '
                            'Chlamydomonas moewusii. Phytochemistry (1983) 22, '
                            '1695-1699.',
                    'pubmed': ''},
               70: {'info': 'Ammendola, S.; Raia, C.A.; Caruso, C.; '
                            "Camardella, L.; D'Auria, S.; De Rosa, M.; Rossi, "
                            'M.: Thermostable NAD(+)-dependent alcohol '
                            'dehydrogenase from Sulfolobus solfataricus: gene '
                            'and protein sequence determination and '
                            'relationship to other alcohol dehydrogenases. '
                            'Biochemistry (1992) 31, 12514-12523.',
                    'pubmed': '1463738'},
               71: {'info': 'Tihanyi, K.; Talbot, B.; Brzezinski, R.; Thirion, '
                            'J.P.: Purification and characterization of '
                            'alcohol dehydrogenase from soybean. '
                            'Phytochemistry (1989) 28, 1335-1338.',
                    'pubmed': ''},
               72: {'info': 'Liang, Z.Q.; Hayase, F.; Nishimura, T.; Kato, H.: '
                            'Purification and characterization of '
                            'NAD-dependent alcohol dehydrogenase and '
                            'NADH-dependent 2-oxoaldehyde reductase from '
                            'parsley. Agric. Biol. Chem. (1990) 54, 1717-1719.',
                    'pubmed': ''},
               73: {'info': 'Hatanaka, A.; Harada, T.: Purification and '
                            'properties of alcohol dehydrogenase from tea '
                            'seeds. Agric. Biol. Chem. (1972) 36, 2033-2035.',
                    'pubmed': ''},
               74: {'info': 'Stiborova, M.; Leblova, S.: Kinetics of the '
                            'reaction catalysed by rape alcohol dehydrogenase. '
                            'Phytochemistry (1979) 18, 23-24.',
                    'pubmed': ''},
               75: {'info': 'Lai, Y.K.; Chandlee, J.M.; Scandalios, J.G.: '
                            'Purification and characterization of three '
                            'non-allelic alcohol dehydrogenase isoenzymes in '
                            'maize. Biochim. Biophys. Acta (1982) 706, 9-18.',
                    'pubmed': ''},
               76: {'info': 'Leblova, S.; Ehlichova, D.: Purification and some '
                            'properties of alcohol dehydrogenase from maize. '
                            'Phytochemistry (1972) 11, 1345-1346.',
                    'pubmed': ''},
               77: {'info': 'Langston, P.J.; Pace, C.N.; Hart, G.E.: Wheat '
                            'alcohol dehydrogenase iszymes. Purification, '
                            'characterization, and gene expression. Plant '
                            'Physiol. (1980) 65, 518-522.',
                    'pubmed': '16661226'},
               78: {'info': 'Langston, P.J.; Hart, G.E.; Pace, C.N.: '
                            'Purification and partial characterization of '
                            'alcohol dehydrogenase from wheat. Arch. Biochem. '
                            'Biophys. (1979) 196, 611-618.',
                    'pubmed': '485168'},
               79: {'info': 'Mayne, M.G.; Lea, P.J.: Properties of three sets '
                            'of isoenzymes of alcohol dehydrogenase isolated '
                            'from barley (Hordeum vulgare). Phytochemistry '
                            '(1985) 24, 1433-1438.',
                    'pubmed': ''},
               80: {'info': 'Shimomura, S.; Beevers, H.: Alcohol dehydrogenase '
                            'inactivator from rice seedlings. Properties and '
                            'intracellular location. Plant Physiol. (1983) 71, '
                            '742-746.',
                    'pubmed': '16662899'},
               81: {'info': 'Creaser, E.H.; Porter, R.L.; Britt, K.A.; '
                            'Pateman, J.A.; Doy, C.H.: Purification and '
                            'preliminary characterization of alcohol '
                            'dehydrogenase from Aspergillus nidulans. Biochem. '
                            'J. (1985) 225, 449-454.',
                    'pubmed': '3156582'},
               82: {'info': 'Yabe, M.; Shitara, K.; Kawashima, J.; Shinoyama, '
                            'H.; Ando, A.; Fujii, T.: Purification and '
                            'properties of an alcohol dehydrogenase isozyme '
                            'from a methanol-using yeast, Candida sp. N-16. '
                            'Biosci. Biotechnol. Biochem. (1992) 56, 338-339.',
                    'pubmed': ''},
               83: {'info': 'Morosoli, R.; Begin-Heick, N.: The partial '
                            'purification and characterization of cytosol '
                            'alcohol dehydrogenase from Astasia. Biochem. J. '
                            '(1974) 141, 469-475.',
                    'pubmed': '4455216'},
               84: {'info': 'Rudge, J.; Bickerstaff, G.F.: Purification and '
                            'properties of an alcohol dehydrogenase from '
                            'Sporotrichum pulverulentum. Enzyme Microb. '
                            'Technol. (1986) 8, 120-124.',
                    'pubmed': ''},
               85: {'info': 'Indrati, R.; Ohita, Y.: Purification and '
                            'properties of alcohol dehydrogenase from a mutant '
                            'strain of Candida guilliermondii. Can. J. '
                            'Microbiol. (1992) 38, 953-957.',
                    'pubmed': ''},
               86: {'info': 'Tkachenko, A.G.; Winston, G.W.: Interaction of '
                            'alcohol dehydrogenase with '
                            'tert-butylhydroperoxide: stimulation of the horse '
                            'liver and inhibition of the yeast enzyme. Arch. '
                            'Biochem. Biophys. (2000) 380, 165-173.',
                    'pubmed': '10900146'},
               87: {'info': 'Drewke, C.; Ciriacy, M.: Overexpression, '
                            'purification and properties of alcohol '
                            'dehydrogenase IV from Saccharomyces cerevisiae. '
                            'Biochim. Biophys. Acta (1988) 950, 54-60.',
                    'pubmed': '3282541'},
               88: {'info': 'Yamazaki, Y.; Maeda, H.; Satoh, A.; Hiromi, K.: A '
                            'kinetic study on the binding of monomeric and '
                            'polymeric derivatives of NAD+ to yeast alcohol '
                            'dehydrogenase. J. Biochem. (1984) 95, 109-115.',
                    'pubmed': '6368531'},
               89: {'info': 'Mazid, M.A.; Laidler, K.J.: pH Dependence of free '
                            'and immobilized yeast alcohol dehydrogenase '
                            'kinetics. Can. J. Microbiol. (1982) 60, 100-107.',
                    'pubmed': '7044497'},
               90: {'info': 'Dickinson, F.M.; Monger, G.P.: A study of the '
                            'kinetics and mechanism of yeast alcohol '
                            'dehydrogenase with a variety of substrates. '
                            'Biochem. J. (1973) 131, 261-270.',
                    'pubmed': '4352908'},
               91: {'info': 'Ganzhorn, A.J.; Green, D.W.; Hershey, A.D.; '
                            'Gould, R.M.; Plapp, B.V.: Kinetic '
                            'characterization of yeast alcohol dehydrogenases. '
                            'Amino acid residue 294 and substrate specificity. '
                            'J. Biol. Chem. (1987) 262, 3754-3761.',
                    'pubmed': '3546317'},
               92: {'info': 'Weinhold, E.G.; Benner, S.A.: Engineering yeast '
                            'alcohol dehydrogenase. Replacing Trp54 by Leu '
                            'broadens substrate specificity. Protein Eng. '
                            '(1995) 8, 457-461.',
                    'pubmed': '8532667'},
               93: {'info': 'Pocker, Y.; Li, H.: Mechanistic enzymology of '
                            'liver alcohol dehydrogenase. Kinetic and '
                            'stereochemical characterization of retinal '
                            'oxidation and reduction. Adv. Exp.Med. Biol. '
                            '(1996) 6, 331-338.',
                    'pubmed': '9059637'},
               94: {'info': 'Leskovac, V.; Trivic, S.; Anderson, B.M.: Use of '
                            'competitive dead-end inhibitors to determine the '
                            'chemical mechanism of action of yeast alcohol '
                            'dehydrogenase. Mol. Cell. Biochem. (1998) 178, '
                            '219-227.',
                    'pubmed': '9546603'},
               95: {'info': 'Keung, W.M.: Isolation and characterization of '
                            'three alcohol dehydrogenase isozymes from Syrian '
                            'golden hamster. Alcohol. Clin. Exp. Res. (1996) '
                            '20, 213-220.',
                    'pubmed': '8730210'},
               96: {'info': 'Yin, S.J.; Wang, M.F.; Liao, C.S.; Chen, C.M.; '
                            'Wu, C.W.: Identification of a human stomach '
                            'alcohol dehydrogenase with distinctive kinetic '
                            'properties. Biochem. Int. (1990) 22, 829-835.',
                    'pubmed': '2099148'},
               98: {'info': 'Langeland, B.T.; Morris, D.L.; McKinley-McKee, '
                            'J.S.: Metal binding properties of thiols: '
                            'complexes with horse liver alcohol dehydrogenase. '
                            'Comp. Biochem. Physiol. B (1999) 123, 155-162.',
                    'pubmed': '10425719'},
               99: {'info': 'Hensgens, C.M.H.; Vonck, J.; van Beeumen, J.; '
                            'Bruggen, E.F.J.; Hansen, T.A.: Purification and '
                            'characterization of an oxygen-labile, '
                            'NAD-dependent alcohol dehydrogenase from '
                            'Desulfovibrio gigas. J. Bacteriol. (1993) 175, '
                            '2859-2863.',
                    'pubmed': '8491707'},
               100: {'info': 'Flores, B.M.; Stanley, S.L.; Yong, T.S.; Ali, '
                             'M.; Yang, W.; Diedrich, D.L.; Torian, B.E.: '
                             'Surface localization, regulation, and biologic '
                             'properties of the 96-kDA alcohol/aldehyde '
                             'dehydrogenase (EhADH2) of pathogenic Entamoeba '
                             'histolytica. J. Infect. Dis. (1996) 173, '
                             '226-231.',
                     'pubmed': '8537663'},
               101: {'info': 'Persson, B.; Bergman, T.; Keung, W.M.; '
                             'Waldenstroem, U.; Holmquist, B.; Vallee, B.L.; '
                             'Joernvall, H.: Basic features of class-I alcohol '
                             'dehydrogenase variable and constant segments '
                             'coordinated by inter-class and intra-class '
                             'variabvility. Conclusions from characterization '
                             'of the alligator enzyme. Eur. J. Biochem. (1993) '
                             '216, 49-56.',
                     'pubmed': '8365416'},
               102: {'info': 'Gergel, D.; Cederbaum, A.I.: Inhibition of the '
                             'catalytic activity of alcohol dehydrogenase by '
                             'nitric oxide is associated with S nitrosylation '
                             'and the release of zinc. Biochemistry (1996) 35, '
                             '16186-16194.',
                     'pubmed': '8973191'},
               103: {'info': 'Lamed, R.; Zeikus, J.G.: Ethanol production by '
                             'thermophilic bacteria: relationship between '
                             'fermentation product yields of and catabolic '
                             'enzyme activities in Clostridium thermocellum '
                             'and Thermoanaerobium brockii. J. Bacteriol. '
                             '(1980) 144, 569-578.',
                     'pubmed': '7430065'},
               104: {'info': 'Kim, K.J.; Howard, A.J.: Crystallization and '
                             'preliminary X-ray diffraction analysis of the '
                             'trigonal crystal form of Saccharomyces '
                             'cerevisiae alcohol dehydrogenase I: evidence for '
                             'the existence of Zn ions in the crystal. Acta '
                             'Crystallogr. Sect. D (2002) 58, 1332-1334.',
                     'pubmed': '12136146'},
               105: {'info': 'Hadizadeh, M.; Keyhani, E.: Detection and '
                             'kinetic properties of alcohol dehydrogenase in '
                             'dormant corm of Crocus sativus L. Acta Hortic. '
                             '(2004) 650, 127-139.',
                     'pubmed': ''},
               106: {'info': 'Hildebrandt, P.; Musidlowska, A.; Bornscheuer, '
                             'U.T.; Altenbuchner, J.: Cloning, functional '
                             'expression and biochemical characterization of a '
                             'stereoselective alcohol dehydrogenase from '
                             'Pseudomonas fluorescens DSM50106. Appl. '
                             'Microbiol. Biotechnol. (2002) 59, 483-487.',
                     'pubmed': '12172614'},
               107: {'info': 'Martras, S.; Alvarez, R.; Gallego, O.; '
                             'Dominguez, M.; de Lera, A.R.; Farres, J.; Pares, '
                             'X.: Kinetics of human alcohol dehydrogenase with '
                             'ring-oxidized retinoids: effect of Tween 80. '
                             'Arch. Biochem. Biophys. (2004) 430, 210-217.',
                     'pubmed': '15369820'},
               108: {'info': 'Esposito, L.; Bruno, I.; Sica, F.; Raia, C.A.; '
                             'Giordano, A.; Rossi, M.; Mazzarella, L.; Zagari, '
                             'A.: Crystal structure of a ternary complex of '
                             'the alcohol dehydrogenase from Sulfolobus '
                             'solfataricus. Biochemistry (2003) 42, '
                             '14397-14407.',
                     'pubmed': '14661950'},
               109: {'info': 'Gibbons, B.J.; Hurley, T.D.: Structure of three '
                             'class I human alcohol dehydrogenases complexed '
                             'with isoenzyme specific formamide inhibitors. '
                             'Biochemistry (2004) 43, 12555-12562.',
                     'pubmed': '15449945'},
               110: {'info': 'Stroemberg, P.; Svensson, S.; Berst, K.B.; '
                             'Plapp, B.V.; Höög, J.O.: Enzymatic mechanism of '
                             'low-activity mouse alcohol dehydrogenase 2. '
                             'Biochemistry (2004) 43, 1323-1328.',
                     'pubmed': '14756569'},
               111: {'info': 'LeBrun, L.A.; Park, D.H.; Ramaswamy, S.; Plapp, '
                             'B.V.: Participation of histidine-51 in catalysis '
                             'by horse liver alcohol dehydrogenase. '
                             'Biochemistry (2004) 43, 3014-3026.',
                     'pubmed': '15023053'},
               112: {'info': 'Ceccarelli, C.; Liang, Z.X.; Strickler, M.; '
                             'Prehna, G.; Goldstein, B.M.; Klinman, J.P.; '
                             'Bahnson, B.J.: Crystal structure and amide H/D '
                             'exchange of binary complexes of alcohol '
                             'dehydrogenase from Bacillus stearothermophilus: '
                             'insight into thermostability and cofactor '
                             'binding. Biochemistry (2004) 43, 5266-5277.',
                     'pubmed': '15122892'},
               113: {'info': 'Chinnawirotpisan, P.; Matsushita, K.; Toyama, '
                             'H.; Adachi, O.; Limtong, S.; Theeragool, G.: '
                             'Purification and characterization of two '
                             'NAD-dependent alcohol dehydrogenases (ADHs) '
                             'induced in the quinoprotein ADH-deficient mutant '
                             'of Acetobacter pasteurianus SKU1108. Biosci. '
                             'Biotechnol. Biochem. (2003) 67, 958-965.',
                     'pubmed': '12834271'},
               114: {'info': 'Kosjek, B.; Stampfer, W.; Pogorevc, M.; '
                             'Goessler, W.; Faber, K.; Kroutil, W.: '
                             'Purification and characterization of a '
                             'chemotolerant alcohol dehydrogenase applicable '
                             'to coupled redox reactions. Biotechnol. Bioeng. '
                             '(2004) 86, 55-62.',
                     'pubmed': '15007841'},
               115: {'info': 'Stroemberg, P.; Svensson, S.; Hedberg, J.J.; '
                             'Nordling, E.; Hoog, J.O.: Identification and '
                             'characterisation of two allelic forms of human '
                             'alcohol dehydrogenase 2. Cell. Mol. Life Sci. '
                             '(2002) 59, 552-559.',
                     'pubmed': '11964133'},
               119: {'info': 'Martras, S.; Alvarez, R.; Martinez, S.E.; '
                             'Torres, D.; Gallego, O.; Duester, G.; Farres, '
                             'J.; de Lera, A.R.; Pares, X.: The specificity of '
                             'alcohol dehydrogenase with cis-retinoids. '
                             'Activity with 11-cis-retinol and localization in '
                             'retina. Eur. J. Biochem. (2004) 271, 1660-1670.',
                     'pubmed': '15096205'},
               122: {'info': 'Vanni, A.; Anfossi, L.; Pessione, E.; '
                             'Giovannoli, C.: Catalytic and spectroscopic '
                             'characterisation of a copper-substituted alcohol '
                             'dehydrogenase from yeast. Int. J. Biol. '
                             'Macromol. (2002) 30, 41-45.',
                     'pubmed': '11893392'},
               123: {'info': 'Espinosa, A.; Clark, D.; Stanley, S.L., Jr.: '
                             'Entamoeba histolytica alcohol dehydrogenase 2 '
                             '(EhADH2) as a target for anti-amoebic agents. J. '
                             'Antimicrob. Chemother. (2004) 54, 56-59.',
                     'pubmed': '15150165'},
               124: {'info': 'Chou, C.F.; Lai, C.L.; Chang, Y.C.; Duester, G.; '
                             'Yin, S.J.: Kinetic mechanism of human class IV '
                             'alcohol dehydrogenase functioning as retinol '
                             'dehydrogenase. J. Biol. Chem. (2002) 277, '
                             '25209-25216.',
                     'pubmed': '11997393'},
               125: {'info': 'Rosell, A.; Valencia, E.; Ochoa, W.F.; Fita, I.; '
                             'Pares, X.; Farres, J.: Complete reversal of '
                             'coenzyme specificity by concerted mutation of '
                             'three consecutive residues in alcohol '
                             'dehydrogenase. J. Biol. Chem. (2003) 278, '
                             '40573-40580.',
                     'pubmed': '12902331'},
               126: {'info': 'Shim, E.J.; Jeon, S.H.; Kong, K.H.: '
                             'Overexpression, purification, and biochemical '
                             'characterization of the thermostable '
                             'NAD-dependent alcohol dehydrogenase from '
                             'Bacillus stearothermophilus. J. Microbiol. '
                             'Biotechnol. (2003) 13, 738-744.',
                     'pubmed': ''},
               127: {'info': 'Guy, J.E.; Isupov, M.N.; Littlechild, J.A.: The '
                             'structure of an alcohol dehydrogenase from the '
                             'hyperthermophilic archaeon Aeropyrum pernix. J. '
                             'Mol. Biol. (2003) 331, 1041-1051.',
                     'pubmed': '12927540'},
               128: {'info': 'Avila, E.E.; Martinez-Alcaraz, E.R.; '
                             'Barbosa-Sabanero, G.; Rivera-Baron, E.I.; '
                             'Arias-Negrete, S.; Zazueta-Sandoval, R.: '
                             'Subcellular localization of the NAD+-dependent '
                             'alcohol dehydrogenase in Entamoeba histolytica '
                             'trophozoites. J. Parasitol. (2002) 88, 217-222.',
                     'pubmed': '12058720'},
               129: {'info': 'Levin, I.; Meiri, G.; Peretz, M.; Burstein, Y.; '
                             'Frolow, F.: The ternary complex of Pseudomonas '
                             'aeruginosa alcohol dehydrogenase with NADH and '
                             'ethylene glycol. Protein Sci. (2004) 13, '
                             '1547-1556.',
                     'pubmed': '15152088'},
               130: {'info': 'Koumanov, A.; Benach, J.; Atrian, S.; '
                             'Gonzalez-Duarte, R.; Karshikoff, A.; Ladenstein, '
                             'R.: The catalytic mechanism of Drosophila '
                             'alcohol dehydrogenase: evidence for a proton '
                             'relay modulated by the coupled ionization of the '
                             'active site lysine/tyrosine pair and a NAD+ '
                             'ribose OH switch. Proteins (2003) 51, 289-298.',
                     'pubmed': '12660997'},
               131: {'info': 'Kragl, U.; Kruse, W.; Hummel, W.; Wandrey, C.: '
                             'Enzyme engineering aspects of biocatalysis: '
                             'Cofactor regeneration as example. Biotechnol. '
                             'Bioeng. (1996) 52, 309-319.',
                     'pubmed': '18629898'},
               132: {'info': 'Vicenzi, J.T.; Zmijewski, M.J.; Reinhard, M.R.; '
                             'Landen, B.E.; Muth, W.L.; Marler, P.G.: '
                             'Large-scale stereoselective enzymatic ketone '
                             'reduction with in-situ product removal via '
                             'polymeric adsorbent resins. Enzyme Microb. '
                             'Technol. (1997) 20, 494-499.',
                     'pubmed': ''},
               133: {'info': 'Sit, S.Y.; Parker, R.A.; Motoc, I.; Han, W.; '
                             'Balasubramanian, N.: Synthesis, biological '
                             'profile, and quantitative structure-activity '
                             'relationship of a series of novel '
                             '3-hydroxy-3-methylglutaryl coenzyme A reductase '
                             'inhibitors. J. Med. Chem. (1990) 33, 2982-2999.',
                     'pubmed': '2231596'},
               136: {'info': 'Duron-Castellanos, A.; Zazueta-Novoa, V.; '
                             'Silva-Jimenez, H.; Alvarado-Caudillo, Y.; Pena '
                             'Cabrera, E.; Zazueta-Sandoval, R.: Detection of '
                             'NAD+dependent alcohol dehydrogenase activities '
                             'in YR-1 strain of Mucor circinelloides, a '
                             'potential bioremediator of petroleum '
                             'contaminated soils. Appl. Biochem. Biotechnol. '
                             '(2005) 121-124, 279-288.',
                     'pubmed': '15917606'},
               137: {'info': 'Inoue, K.; Makino, Y.; Itoh, N.: Purification '
                             'and characterization of a novel alcohol '
                             'dehydrogenase from Leifsonia sp. strain S749: a '
                             'promising biocatalyst for an asymmetric hydrogen '
                             'transfer bioreduction. Appl. Environ. Microbiol. '
                             '(2005) 71, 3633-3641.',
                     'pubmed': '16000771'},
               138: {'info': 'Machielsen, R.; Uria, A.R.; Kengen, S.W.; van '
                             'der Oost, J.: Production and characterization of '
                             'a thermostable alcohol dehydrogenase that '
                             'belongs to the aldo-keto reductase uperfamily. '
                             'Appl. Environ. Microbiol. (2006) 72, 233-238.',
                     'pubmed': '16391048'},
               139: {'info': 'Park, H.; Kidman, G.; Northrop, D.B.: Effects of '
                             'pressure on deuterium isotope effects of yeast '
                             'alcohol dehydrogenase using alternative '
                             'substrates. Arch. Biochem. Biophys. (2005) 433, '
                             '335-340.',
                     'pubmed': '15581588'},
               140: {'info': 'Kalnenieks, U.; Galinina, N.; Toma, M.M.: '
                             'Physiological regulation of the properties of '
                             'alcohol dehydrogenase II (ADH II) of Zymomonas '
                             'mobilis: NADH renders ADH II resistant to '
                             'cyanide and aeration. Arch. Microbiol. (2005) '
                             '183, 450-455.',
                     'pubmed': '16027951'},
               141: {'info': 'Haseba, T.; Duester, G.; Shimizu, A.; Yamamoto, '
                             'I.; Kameyama, K.; Ohno, Y.: In vivo contribution '
                             'of class III alcohol dehydrogenase (ADH3) to '
                             'alcohol metabolism through activation by '
                             'cytoplasmic solution hydrophobicity. Biochim. '
                             'Biophys. Acta (2006) 1762, 276-283.',
                     'pubmed': '16431092'},
               142: {'info': 'Westerlund, M.; Galter, D.; Carmine, A.; Olson, '
                             'L.: Tissue- and species-specific expression '
                             'patterns of class I, III, and IV Adh and Aldh 1 '
                             'mRNAs in rodent embryos. Cell Tissue Res. (2005) '
                             '322, 227-236.',
                     'pubmed': '16047160'},
               143: {'info': 'Negoro, M.; Wakabayashi, I.: Enhancement of '
                             'alcohol dehydrogenase activity in vitro by '
                             'acetylsalicylic acid. Eur. J. Pharmacol. (2005) '
                             '523, 25-28.',
                     'pubmed': '16226743'},
               144: {'info': 'Kazuoka, T.; Oikawa, T.; Muraoka, I.; Kuroda, '
                             'S.; Soda, K.: A cold-active and thermostable '
                             'alcohol dehydrogenase of a psychrotorelant from '
                             'Antarctic seawater, Flavobacterium frigidimaris '
                             'KUC-1. Extremophiles (2007) 11, 257-267.',
                     'pubmed': '17072683'},
               147: {'info': 'Koutsompogeras, P.; Kyriacou, A.; Zabetakis, I.: '
                             'Characterizing NAD-dependent alcohol '
                             'dehydrogenase enzymes of Methylobacterium '
                             'extorquens and strawberry (Fragaria x ananassa '
                             'cv. Elsanta). J. Agric. Food Chem. (2006) 54, '
                             '235-242.',
                     'pubmed': '16390205'},
               149: {'info': 'Hirano, J.; Miyamoto, K.; Ohta, H.: Purification '
                             'and characterization of the alcohol '
                             'dehydrogenase with a broad substrate specificity '
                             'originated from 2-phenylethanol-assimilating '
                             'Brevibacterium sp. KU 1309. J. Biosci. Bioeng. '
                             '(2005) 100, 318-322.',
                     'pubmed': '16243283'},
               150: {'info': 'Jelski, W.; Chrostek, L.; Markiewicz, W.; '
                             'Szmitkowski, M.: Activity of alcohol '
                             'dehydrogenase (ADH) isoenzymes and aldehyde '
                             'dehydrogenase (ALDH) in the sera of patients '
                             'with breast cancer. J. Clin. Lab. Anal. (2006) '
                             '20, 105-108.',
                     'pubmed': '16721836'},
               151: {'info': 'Manriquez, D.; El-Sharkawy, I.; Flores, F.B.; '
                             'El-Yahyaoui, F.; Regad, F.; Bouzayen, M.; '
                             'Latche, A.; Pech, J.C.: Two highly divergent '
                             'alcohol dehydrogenases of melon exhibit fruit '
                             'ripening-specific expression and distinct '
                             'biochemical characteristics. Plant Mol. Biol. '
                             '(2006) 61, 675-685.',
                     'pubmed': '16897483'},
               153: {'info': 'Raia, C.A.; Caruso, C.; Marino, M.; Vespa, N.; '
                             'Rossi, M.: Activation of Sulfolobus solfataricus '
                             'alcohol dehydrogenase by modification of '
                             'cysteine residue 38 with iodoacetic acid. '
                             'Biochemistry (1996) 35, 638-647.',
                     'pubmed': '8555238'},
               155: {'info': "Trincone, A.; Lama, L.; Rella, R.; D'Auria, S.; "
                             'Raia, C.A.; Nicolaus, B.: Determination of '
                             'hydride transfer stereospecificity of '
                             'NADH-dependent alcohol-aldehyde/ketone '
                             'oxidoreductase from Sulfolobus solfataricus. '
                             'Biochim. Biophys. Acta (1990) 1041, 94-96.',
                     'pubmed': '2121281'},
               156: {'info': 'Tasaki, Y.; Yoshikawa, H.; Tamura, H.: Isolation '
                             'and characterization of an alcohol dehydrogenase '
                             'gene from the octylphenol polyethoxylate '
                             'degrader Pseudomonas putida S-5. Biosci. '
                             'Biotechnol. Biochem. (2006) 70, 1855-1863.',
                     'pubmed': '16926497'},
               157: {'info': 'Esposito, L.; Bruno, I.; Sica, F.; Raia, C.A.; '
                             'Giordano, A.; Rossi, M.; Mazzarella, L.; Zagari, '
                             'A.: Structural study of a single-point mutant of '
                             'Sulfolobus solfataricus alcohol dehydrogenase '
                             'with enhanced activity.. FEBS Lett. (2003) 539, '
                             '14-18.',
                     'pubmed': '12650918'},
               158: {'info': 'Cannio, R.; Fiorentino, G.; Rossi, M.; '
                             'Bartolucci, S.: The alcohol dehydrogenase gene: '
                             'distribution among Sulfolobales and regulation '
                             'in Sulfolobus solfataricus. FEMS Microbiol. '
                             'Lett. (1999) 170, 31-39.',
                     'pubmed': '9919650'},
               161: {'info': 'Esposito, L.; Sica, F.; Raia, C.A.; Giordano, '
                             'A.; Rossi, M.; Mazzarella, L.; Zagari, A.: '
                             'Crystal structure of the alcohol dehydrogenase '
                             'from the hyperthermophilic archaeon Sulfolobus '
                             'solfataricus at 1.85 A resolution. J. Mol. Biol. '
                             '(2002) 318, 463-477.',
                     'pubmed': '12051852'},
               162: {'info': 'Chong, P.K.; Burja, A.M.; Radianingtyas, H.; '
                             'Fazeli, A.; Wright, P.C.: Proteome and '
                             'transcriptional analysis of ethanol-grown '
                             'Sulfolobus solfataricus P2 reveals ADH2, a '
                             'potential alcohol dehydrogenase. J. Proteome '
                             'Res. (2007) 6, 3985-3994.',
                     'pubmed': '17824633'},
               163: {'info': 'Raia, C.A.; Giordano, A.; Rossi, M.: Alcohol '
                             'dehydrogenase from Sulfolobus solfataricus. '
                             'Methods Enzymol. (2001) 331, 176-195.',
                     'pubmed': '11265460'},
               164: {'info': 'Casadio, R.; Martelli, P.L.; Giordano, A.; '
                             'Rossi, M.; Raia, C.A.: A low-resolution 3D model '
                             'of the tetrameric alcohol dehydrogenase from '
                             'Sulfolobus solfataricus. Protein Eng. (2002) 15, '
                             '215-223.',
                     'pubmed': '11932492'},
               166: {'info': 'Hoellrigl, V.; Otto, K.; Schmid, A.: '
                             'Electroenzymatic asymmetric reduction of '
                             'rac-3-methylcyclohexanone to '
                             '(1S,3S)-3-methylcyclohexanol in organic/aqueous '
                             'media catalyzed by a thermophilic alcohol '
                             'dehydrogenase. Adv. Synth. Catal. (2007) 349, '
                             '1337-1340.',
                     'pubmed': ''}})])
--------------------------------------------------------------------------------
```
## Release notes
### 0.2.0
* unittests and continuous integration
* complete refactoring of parser
* supporting full set of information

### 0.1.0
* initial release of updated parser
---
&copy; 2019 Matthias König (https://livermetabolism.com)