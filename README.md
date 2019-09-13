[![PyPI version](https://badge.fury.io/py/brendapy.svg)](https://badge.fury.io/py/brendapy)
[![GitHub version](https://badge.fury.io/gh/matthiaskoenig%2Fbrendapy.svg)](https://badge.fury.io/gh/matthiaskoenig%2Fbrendapy)
[![Build Status](https://travis-ci.org/matthiaskoenig/brendapy.svg?branch=develop)](https://travis-ci.org/matthiaskoenig/brendapy)
[![License (LGPL version 3)](https://img.shields.io/badge/license-LGPLv3.0-blue.svg?style=flat-square)](http://opensource.org/licenses/LGPL-3.0)
[![DOI](https://zenodo.org/badge/199438774.svg)](https://zenodo.org/badge/latestdoi/199438774)

# brendapy - BRENDA in python
<b><a href="https://orcid.org/0000-0003-1725-179X" title="https://orcid.org/0000-0003-1725-179X"><img src="./docs/images/orcid.png" height="15" width="15"/></a> Matthias König</b>

The `brendapy` package provides a python parser and utility functions 
for enzyme information from [BRENDA](https://www.brenda-enzymes.org/index.php). 
The parser extracts the all information split up by individual protein entries from the
 database flat file and makes it accessible in a simple manner.
 
 This package was developed in the context of building kinetic pathway models with 
 focus on extracting parameters like `Km` or `Ki` from BRENDA.
 
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

## Release notes
### 0.4.1
* downloading online resources instead of pypi packaging

### 0.4.0
* resolving uniprot and swissprot information
* removing redundant information
* fixing references in entries
* mapping to BRENDA tissue ontology (BTO)
* mapping to chebi ontology
* bugfixes (encoding issues, organism parsing, taxonomy, ...)
* removing git-lfs dependencies

### 0.3.0
* taxonomy information added
* parsing of all BRENDA fields
* extracting values and substrates for kinetic parameters
* multitude of bug-fixes (e.g., correct references, species, ...)
* testing of all examples

### 0.2.0
* unittests and continuous integration
* complete refactoring of parser
* supporting full set of information

### 0.1.0
* initial release of updated parser

## Usage
Examples are provided in [./brendapy/examples.py](./brendapy/examples.py) or in the tests [./brendapy/tests/test_brenda.py](./brendapy/tests/test_brenda.py) 

```python
from brendapy import BrendaParser


def parse_human_proteins_for_ec(ec="1.1.1.1"):
    """Parse the protein entries for a given EC number in BRENDA.

    Prints overview of proteins, protein ids, and Human proteins.
    """
    brenda = BrendaParser()
    proteins = brenda.get_proteins(ec)

    print(f"{len(proteins)} proteins for EC {ec} in BRENDA")
    print(f"Protein identifier: {proteins.keys()}")
    print("-" * 80)
    for p in proteins.values():
        if p.organism == "Homo sapiens":
            print(p)
            print("-" * 80)


if __name__ == "__main__":
    parse_human_proteins_for_ec(ec="1.1.1.1")
```

```
OrderedDict([('protein_id', 106),
             ('ec', '1.1.1.1'),
             ('organism', 'Homo sapiens'),
             ('taxonomy', 9606),
             ('uniprot', 'P00326'),
             ('CF',
              [{'comment': '#13,24,44,61,110,112,166# dependent on '
                           '<113,114,126,128,197,210,292>; #162# specific for '
                           '<287>; #46,95# dependent <153,154,159>; #163# '
                           'preferred cofactor <288>; #41# kinetics of '
                           'coenzyme binding in the pH-range 10-12 <26>; #4# '
                           'NAD+-plus-acetone-induced conversion <62>; #41# '
                           'NAD+ acts as an activator which induces an active '
                           'form of the enzyme <34>; #41# preferred substrate '
                           '<42>; #84# activity with mutants G223D/T224I and '
                           'G223D/T224I/H225N <125>; #10# cofactor binding '
                           'mode <120>; #13# dependent on, cofactor binding '
                           'mechanism and conformation from crystal structure '
                           'analysis <112>; #87# the monomer consists of a '
                           'catalytic and a cofactor-binding domain, the '
                           'cofactor is bound between 2 domains in a cleft '
                           '<127>; #7,27,34,50,66# strongly preferred as '
                           'cofactor <135>; #92# specific for NAD+, no '
                           'activity with NADP+, pro-R stereospecificity for '
                           'hydrogen transfer <144>; #98# ADH1 preferrs NAD+ '
                           '205fold better than NADP+ as cofactor <172>; #15# '
                           'ADH3 does not react with NADP+ <172>; #143# '
                           'preferred over NADP+ <138>; #6# strict requirement '
                           'for NAD(H) as the coenzyme. Critical role of the '
                           'D37 residue in discriminating NAD(H) from NADP(H) '
                           '<169>; #111# shows NAD+ as the preferred co-factor '
                           'over NADP+ <213>; #41# the binding of NAD+ is '
                           'kinetically limited by a unimolecular '
                           'isomerization (corresponding to the conformational '
                           'change) that is controlled by deprotonation of the '
                           'catalytic zinc-water to produce a '
                           'negatively-charged zinc-hydroxide, which can '
                           'attract the positively-charged nicotinamide ring '
                           '<198>; #114# NAD+ is prefered over NADP+ <215>; '
                           '#115# NADP+ is prefered over NAD+ <215>; #124# '
                           'strict requirement for NAD(H) as the coenzyme, no '
                           'activity with NADP+. The specificity constant '
                           'value is 6fold higher for NADH than NAD+ <218>; '
                           '#123# the enzyme transfers the deuteride to the '
                           'Si-face of NAD+ <219>; #48# Adh3 is strictly '
                           'dependent on NAD+/NADH, and shows no activity with '
                           'NADP+/NADPH as cofactor <223>; #133# exclusively '
                           'NAD+ dependent <237>; #51# 57fold preferred over '
                           'NADP+ <279>; #23# H255R single mutant exhibits an '
                           'increased binding affinity toward NADP+ and a '
                           'concomitant reduction in affinity for NAD+ <290>; '
                           '#23# insertion of an RTX domain from the adenylate '
                           'cyclase of Bordetella pertussis into a loop near '
                           'the catalytic active site of the thermostable '
                           'alcohol dehydrogenase D from Pyrococcus furiosus. '
                           'The resultant chimera, beta-AdhD, gains the '
                           'calcium-binding ability of the beta-roll, retains '
                           'the thermostable activity of AdhD, and exhibits '
                           'reduced overall alcohol dehydrogenase activity. '
                           'The addition of calcium to beta-AdhD '
                           'preferentially inhibits NAD+-dependent activity in '
                           'comparison to NADP+-dependent activity. Calcium is '
                           'a competitive inhibitor of AdhD, and the addition '
                           'of the RTX domain introduces calcium-dependent '
                           'noncompetitive inhibition to beta-AdhD affecting '
                           'NAD+-dependent activity <289>',
                'data': 'NAD+',
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
                         20,
                         21,
                         22,
                         23,
                         24,
                         25,
                         26,
                         27,
                         28,
                         29,
                         30,
                         31,
                         32,
                         33,
                         34,
                         35,
                         36,
                         37,
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
                         49,
                         50,
                         51,
                         52,
                         53,
                         54,
                         55,
                         56,
                         57,
                         58,
                         59,
                         60,
                         61,
                         62,
                         63,
                         64,
                         65,
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
                         89,
                         90,
                         91,
                         92,
                         93,
                         94,
                         95,
                         96,
                         97,
                         98,
                         99,
                         100,
                         101,
                         102,
                         103,
                         105,
                         110,
                         111,
                         112,
                         113,
                         114,
                         115,
                         116,
                         118,
                         120,
                         121,
                         124,
                         125,
                         126,
                         127,
                         128,
                         129,
                         130,
                         135,
                         136,
                         137,
                         138,
                         139,
                         141,
                         143,
                         144,
                         146,
                         148,
                         149,
                         152,
                         153,
                         154,
                         156,
                         157,
                         158,
                         159,
                         161,
                         162,
                         163,
                         164,
                         165,
                         169,
                         172,
                         180,
                         194,
                         195,
                         196,
                         197,
                         198,
                         200,
                         201,
                         202,
                         203,
                         204,
                         205,
                         206,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         215,
                         217,
                         218,
                         219,
                         220,
                         221,
                         222,
                         223,
                         225,
                         226,
                         227,
                         229,
                         230,
                         231,
                         232,
                         233,
                         234,
                         237,
                         243,
                         252,
                         254,
                         256,
                         257,
                         260,
                         269,
                         272,
                         279,
                         286,
                         287,
                         288,
                         289,
                         290,
                         292,
                         293]}]),
             ('ID', '1.1.1.1'),
             ('IN',
              [{'comment': '#46# competitive inhibitor <163>; #8# 1 mM, 31% '
                           'inhibition <23>; #8# class III enzyme is '
                           'completely insensitive to inhibition <11,16>; #8# '
                           'poor inhibitor, class II isoenzyme <14>; #8# no '
                           'inhibition by 12 mM <21>; #8# competitive against '
                           'ethanol <96>; #36# isoenzyme AA-ADH, BB-ADH and '
                           'TT-ADH <95>; #5# inhibits cell protein '
                           'carbonylation following exposure to crotyl alcohol '
                           '<117>',
                'data': '4-Methylpyrazole',
                'refs': [2,
                         11,
                         14,
                         16,
                         21,
                         23,
                         24,
                         25,
                         95,
                         96,
                         117,
                         135,
                         163,
                         214]},
               {'comment': '#90# substrate inhibition above 0.5 M <105>; #99# '
                           '50% (v/v), 59% loss of activity <173>; #106# '
                           'ethanol competitively inhibits the oxidation of '
                           '1-hydroxymethylpyrene by ADH1C and ADH3 <214>; '
                           '#109# ethanol competitively inhibits the oxidation '
                           'of 1-hydroxymethylpyrene by ADH4 <214>',
                'data': 'ethanol',
                'refs': [105, 173, 214]},
               {'comment': '#99# 50% (v/v), 29% loss of activity <173>; #106# '
                           'DMSO inhibits isozyme ADH2-catalysed oxidation in '
                           'an uncompetitive mode and reduction in a mixed '
                           'mode <214>; #106# DMSO inhibits isozymes '
                           'ADH1C-catalysed oxidation in an uncompetitive mode '
                           'and reduction in a mixed mode, no inhibition is '
                           'detected with isozyme ADH3 <214>; #109# DMSO '
                           'inhibits isozymes ADH4-catalysed oxidation in an '
                           'uncompetitive mode and reduction in a mixed mode '
                           '<214>',
                'data': 'DMSO',
                'refs': [173, 214]}]),
             ('KI',
              [{'chebi': 'CHEBI_16236',
                'comment': '#106# isozyme ADH1C, using 1-hydroxymethylpyrene '
                           'as substrate <214>',
                'data': '1.7 {ethanol}',
                'refs': [214],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 1.7},
               {'chebi': 'CHEBI_16236',
                'comment': '#106# isozyme ADH3, using 1-hydroxymethylpyrene as '
                           'substrate <214>',
                'data': '1470 {ethanol}',
                'refs': [214],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 1470.0}]),
             ('KM',
              [{'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.00024 {1-formyl-8-methylpyrene}',
                'refs': [214],
                'substrate': '1-formyl-8-methylpyrene',
                'units': 'mM',
                'value': 0.00024},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.00031 {1-hydroxymethyl-8-methylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethyl-8-methylpyrene',
                'units': 'mM',
                'value': 0.00031},
               {'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.00032 {1-formyl-6-methylpyrene}',
                'refs': [214],
                'substrate': '1-formyl-6-methylpyrene',
                'units': 'mM',
                'value': 0.00032},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.00037 {4-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '4-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.00037},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.00048 {2-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '2-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.00048},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.0005 {1-formylpyrene}',
                'refs': [214],
                'substrate': '1-formylpyrene',
                'units': 'mM',
                'value': 0.0005},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.00055 {1-formylpyrene}',
                'refs': [214],
                'substrate': '1-formylpyrene',
                'units': 'mM',
                'value': 0.00055},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.00057 {1-hydroxymethyl-6-methylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethyl-6-methylpyrene',
                'units': 'mM',
                'value': 0.00057},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.00059 {1-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.00059},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.00075 {1-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.00075},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.0009 {1-formyl-6-methylpyrene}',
                'refs': [214],
                'substrate': '1-formyl-6-methylpyrene',
                'units': 'mM',
                'value': 0.0009},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.001 {4-formylpyrene}',
                'refs': [214],
                'substrate': '4-formylpyrene',
                'units': 'mM',
                'value': 0.001},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.001 {4-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '4-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.001},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.00115 {1-hydroxymethyl-6-methylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethyl-6-methylpyrene',
                'units': 'mM',
                'value': 0.00115},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.00131 {1-formyl-8-methylpyrene}',
                'refs': [214],
                'substrate': '1-formyl-8-methylpyrene',
                'units': 'mM',
                'value': 0.00131},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.00149 {1-formyl-8-methylpyrene}',
                'refs': [214],
                'substrate': '1-formyl-8-methylpyrene',
                'units': 'mM',
                'value': 0.00149},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.0021 {2-formylpyrene}',
                'refs': [214],
                'substrate': '2-formylpyrene',
                'units': 'mM',
                'value': 0.0021},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.0021 {4-formylpyrene}',
                'refs': [214],
                'substrate': '4-formylpyrene',
                'units': 'mM',
                'value': 0.0021},
               {'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.0029 {2-formylpyrene}',
                'refs': [214],
                'substrate': '2-formylpyrene',
                'units': 'mM',
                'value': 0.0029},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.0038 {1-formyl-6-methylpyrene}',
                'refs': [214],
                'substrate': '1-formyl-6-methylpyrene',
                'units': 'mM',
                'value': 0.0038},
               {'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.0038 {4-formylpyrene}',
                'refs': [214],
                'substrate': '4-formylpyrene',
                'units': 'mM',
                'value': 0.0038},
               {'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.0044 {2-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '2-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.0044},
               {'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.0064 {1-hydroxymethyl-6-methylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethyl-6-methylpyrene',
                'units': 'mM',
                'value': 0.0064},
               {'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.0064 {1-hydroxymethyl-8-methylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethyl-8-methylpyrene',
                'units': 'mM',
                'value': 0.0064},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.009 {2-formylpyrene}',
                'refs': [214],
                'substrate': '2-formylpyrene',
                'units': 'mM',
                'value': 0.009},
               {'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.012 {1-formylpyrene}',
                'refs': [214],
                'substrate': '1-formylpyrene',
                'units': 'mM',
                'value': 0.012},
               {'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.04 {4-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '4-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.04},
               {'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.059 {1-hydroxymethyl-8-methylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethyl-8-methylpyrene',
                'units': 'mM',
                'value': 0.059},
               {'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '0.076 {1-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.076},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.106 {2-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '2-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.106},
               {'chebi': 'CHEBI_15343',
                'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.34 {acetaldehyde}',
                'refs': [214],
                'substrate': 'acetaldehyde',
                'units': 'mM',
                'value': 0.34},
               {'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '0.39 {1-Octanol}',
                'refs': [214],
                'substrate': '1-Octanol',
                'units': 'mM',
                'value': 0.39},
               {'chebi': 'CHEBI_16236',
                'comment': '#106# isozyme ADH1C, at 21-23°C <214>',
                'data': '0.77 {ethanol}',
                'refs': [214],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 0.77},
               {'chebi': 'CHEBI_15343',
                'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '26 {acetaldehyde}',
                'refs': [214],
                'substrate': 'acetaldehyde',
                'units': 'mM',
                'value': 26.0},
               {'chebi': 'CHEBI_16236',
                'comment': '#106# isozyme ADH2, at 21-23°C <214>',
                'data': '33 {ethanol}',
                'refs': [214],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 33.0},
               {'chebi': 'CHEBI_17935',
                'comment': '#106# isozyme ADH3, at 21-23°C <214>',
                'data': '9.6 {octanal}',
                'refs': [214],
                'substrate': 'octanal',
                'units': 'mM',
                'value': 9.6}]),
             ('LO',
              [{'comment': '#61# 2 isozymes <113>; #24# enzyme polymer forms '
                           'rod-like helical particles <128>',
                'data': 'cytosol',
                'refs': [113, 128, 135, 194, 214]}]),
             ('MW',
              [{'comment': '#112# SDS-PAGE <197>; #106# isozyme ADH2, apparent '
                           'molecular weight deduced from electrophoretic '
                           'mobility <214>; #109# isozyme ADH4, calculated '
                           'from amino acid sequence <214>; #92,132# 4 * '
                           '40000, SDS-PAGE <144,239>; #8,10,36,53,79# 2 * '
                           '40000, SDS-PAGE <16,23,24,59,87,95>; #1,8,80,131# '
                           'x * 40000, SDS-PAGE <11,44,52,227>; #9# 2 * 40000, '
                           'ADH-3, SDS-PAGE <49>; #42# 2 * 40000, enzyme form '
                           'ADHI <68>',
                'data': '40000',
                'refs': [11,
                         16,
                         23,
                         24,
                         44,
                         49,
                         52,
                         59,
                         68,
                         87,
                         95,
                         144,
                         197,
                         214,
                         227,
                         239,
                         272]},
               {'comment': '#106# isozyme ADH3, apparent molecular weight '
                           'deduced from electrophoretic mobility <214>',
                'data': '39500',
                'refs': [214]},
               {'comment': '#106# isozyme ADH3, calculated from amino acid '
                           'sequence <214>',
                'data': '39720',
                'refs': [214]},
               {'comment': '#106# isozyme ADH1C, calculated from amino acid '
                           'sequence <214>',
                'data': '39870',
                'refs': [214]},
               {'comment': '#106# isozyme ADH2, calculated from amino acid '
                           'sequence <214>',
                'data': '40220',
                'refs': [214]},
               {'comment': '#106# isozyme ADH1C, apparent molecular weight '
                           'deduced from electrophoretic mobility <214>; #109# '
                           'isozyme ADH4, apparent molecular weight deduced '
                           'from electrophoretic mobility <214>',
                'data': '40500',
                'refs': [214]}]),
             ('OSS',
              [{'comment': '#106,109# DMSO is not an ideal '
                           'substrate-delivering solvent for ADH-catalysed '
                           'reactions <214>; #151# 20% v/v, 24 h, 87% residual '
                           'activity <244>; #56# 20% v/v, 70% residual '
                           'activity <255>',
                'data': 'DMSO',
                'refs': [214, 244, 255]}]),
             ('RE',
              {'a primary alcohol + NAD+ = an aldehyde + NADH + H+ (#4,41# '
               'ordered bi-bi mechanism <31,43>; #4,75# rapid equilibrium '
               'random mechanism <63>; #8# ordered bi bi mechanism with '
               'cofactor adding first to form a binary enzyme complex <23>; '
               '#41# isoenzyme EE and SS: ordered bi bi mechanism <35>; '
               '#10,33# mechanism is predominantly ordered with ethanol, but '
               'partially random with butanol <91>; #41# kinetic mechanism is '
               'random for ethanol oxidation and compulsory ordered for '
               'acetaldehyde reduction <41>; #38# oxidizes ethanol in an '
               'ordered bi-bi mechanism with NAD+ as the first substrate fixed '
               '<85>; #10# compulsory-order mechanism with the rate-limiting '
               'step being the dissociation of the product enzyme-NAD+ complex '
               '<90>; #28,68,78# Theorell-Chance mechanism <38,69,74>; #44# '
               'sequential reaction mechanism <114>; #87# active site '
               'structure <127>; #78# catalytic mechanism involves a proton '
               'relay modulated by the coupled ionization of the active site '
               'Lys155/Tyr151 pair, and a NAD+ ribose 2-OH switch, other '
               'active site residues are Ser138 and Trp144, ionization '
               'properties, substrate binding, overview <130>; #8# class IV '
               'alcohol dehydrogenase also functions as retinol dehydrogenase, '
               'reaction and kinetic mechanism: asymmetric rapid equilibrium '
               'random mechanism with 2 dead-end ternary complexes fro retinol '
               'oxidation and a rapid equilibrium ordered mechanism with one '
               'dead-end ternary complex for retinal reduction, a unique '
               'mechanistic form fro zinc-containing ADH in the medium chain '
               'dehydrogenase/reductase superfamily of enzymes <124>; #10# '
               'detailed determination of the reaction and kinetic mechanisms, '
               'active site structure and determination of amino acid residues '
               'involved in catalysis, 3 isozymes <120>; #5# ordered bibi '
               'mechanism, structural and functional implications of amino '
               'acid residue 47 <110>; #41# ordered sequential bibi reaction '
               'mechanism, modeling of oxidation kinetic mechanism <117>; #41# '
               'reaction mechanism, His51 is involved, but not essential, in '
               'catalysis facilitating the deprotonation of the hydroxyl group '
               'of water or alcohol ligated to the catalytic zinc <111>; #8# '
               'Ser48 is involved in catalysis, isozyme gamma(2)gamma(2) '
               '<109>; #27# the catalytic triad consists of Cys44, His67, and '
               'Cys154, active site structure <129>)',
               'a secondary alcohol + NAD+ = a ketone + NADH + H+'}),
             ('RN', {'alcohol dehydrogenase'}),
             ('RT', {'reduction', 'redox reaction', 'oxidation'}),
             ('SN', {'alcohol:NAD+ oxidoreductase'}),
             ('SP',
              [{'data': '1-hydroxymethyl-6-methylpyrene + NAD+ = '
                        '1-formyl-6-methylpyrene + NADH + H+ {r}',
                'refs': [214]},
               {'data': '1-hydroxymethyl-8-methylpyrene + NAD+ = '
                        '1-formyl-8-methylpyrene + NADH + H+ {r}',
                'refs': [214]},
               {'data': '1-hydroxymethylpyrene + NAD+ = 1-formylpyrene + NADH '
                        '+ H+ {r}',
                'refs': [214]},
               {'data': '2-hydroxymethylpyrene + NAD+ = 2-formylpyrene + NADH '
                        '+ H+ {r}',
                'refs': [214]},
               {'data': '4-hydroxymethylpyrene + NAD+ = 4-formylpyrene + NADH '
                        '+ H+ {r}',
                'refs': [214]},
               {'comment': '#48# best substrate <223>; #111# 100% activity '
                           '<213>; #100# no activity with NADP+, in reverse '
                           'reaction no activity with NADPH <171>; #31# the '
                           'enzyme is highly specific for ethanol with NAD+ as '
                           'the coenzyme <181>; #112# 88% activity compared to '
                           'cyclohexanol <197>; #106# substrate for isozyme '
                           'ADH1C, extremely poor substrate for isozyme ADH3 '
                           '<214>; #106# substrate for isozyme ADH2 <214>; '
                           '#109# substrate for isozyme ADH4 <214>; #133# the '
                           'enzyme shows a preference for short-chain alcohols '
                           'ethanol and 1-propanol <237>; #155# 12% of the '
                           'activity with butan-1-ol <271>; #161# 33% of the '
                           'activity with 1,4-butanediol <286>) |#119# 83% of '
                           'the activity with butan-2-ol <256>',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [66,
                         103,
                         136,
                         139,
                         140,
                         143,
                         144,
                         147,
                         148,
                         153,
                         159,
                         161,
                         162,
                         163,
                         171,
                         173,
                         174,
                         181,
                         194,
                         195,
                         196,
                         197,
                         203,
                         205,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         222,
                         223,
                         231,
                         233,
                         237,
                         239,
                         246,
                         252,
                         256,
                         271,
                         277,
                         279,
                         284,
                         286,
                         288]},
               {'comment': '#48# best substrate <223>; #111# 100% activity '
                           '<213>; #100# no activity with NADP+, in reverse '
                           'reaction no activity with NADPH <171>; #31# the '
                           'enzyme is highly specific for ethanol with NAD+ as '
                           'the coenzyme <181>; #112# 88% activity compared to '
                           'cyclohexanol <197>; #106# substrate for isozyme '
                           'ADH1C, extremely poor substrate for isozyme ADH3 '
                           '<214>; #106# substrate for isozyme ADH2 <214>; '
                           '#109# substrate for isozyme ADH4 <214>; #133# the '
                           'enzyme shows a preference for short-chain alcohols '
                           'ethanol and 1-propanol <237>; #155# 12% of the '
                           'activity with butan-1-ol <271>; #161# 33% of the '
                           'activity with 1,4-butanediol <286>) |#119# 83% of '
                           'the activity with butan-2-ol <256>| {r',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [66,
                         103,
                         136,
                         139,
                         140,
                         143,
                         144,
                         147,
                         148,
                         153,
                         159,
                         161,
                         162,
                         163,
                         171,
                         173,
                         174,
                         181,
                         194,
                         195,
                         196,
                         197,
                         203,
                         205,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         222,
                         223,
                         231,
                         233,
                         237,
                         239,
                         246,
                         252,
                         256,
                         271,
                         277,
                         279,
                         284,
                         286,
                         288]},
               {'comment': '#48# best substrate <223>; #111# 100% activity '
                           '<213>; #100# no activity with NADP+, in reverse '
                           'reaction no activity with NADPH <171>; #31# the '
                           'enzyme is highly specific for ethanol with NAD+ as '
                           'the coenzyme <181>; #112# 88% activity compared to '
                           'cyclohexanol <197>; #106# substrate for isozyme '
                           'ADH1C, extremely poor substrate for isozyme ADH3 '
                           '<214>; #106# substrate for isozyme ADH2 <214>; '
                           '#109# substrate for isozyme ADH4 <214>; #133# the '
                           'enzyme shows a preference for short-chain alcohols '
                           'ethanol and 1-propanol <237>; #155# 12% of the '
                           'activity with butan-1-ol <271>; #161# 33% of the '
                           'activity with 1,4-butanediol <286>) |#119# 83% of '
                           'the activity with butan-2-ol <256>| {',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [66,
                         103,
                         136,
                         139,
                         140,
                         143,
                         144,
                         147,
                         148,
                         153,
                         159,
                         161,
                         162,
                         163,
                         171,
                         173,
                         174,
                         181,
                         194,
                         195,
                         196,
                         197,
                         203,
                         205,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         222,
                         223,
                         231,
                         233,
                         237,
                         239,
                         246,
                         252,
                         256,
                         271,
                         277,
                         279,
                         284,
                         286,
                         288]},
               {'comment': '#13# broad substrate specificity <126>; #10# '
                           'constitutive enzyme <94>; #42# key enzyme in '
                           'ethanol production <68>; #52# one constitutive '
                           'enzyme, ADH-MI and one inducible enzyme, ADH-MII '
                           '<82>; #53# enzyme may be involved in the '
                           'metabolism of dietary wax esters in salmonid fish '
                           '<59>; #78# the enzyme oxidizes alcohols to '
                           'aldehydes or ketones both for detoxification and '
                           'metabolic purposes <38>; #36# involvement in the '
                           'development of male hamster reproductive system '
                           '<47>; #88# enzyme shows high substrate specificity '
                           'towards primary aliphatic alcohols, no activity '
                           'with 2-butanol, tert-butanol, isoamyl alcohol, '
                           'isobutyl alcohol, 1,6-hexadiol, and mono-, di-, '
                           'and triethanolamine <118>; #90# no activity with '
                           'methanol, 2-propanol, and isoamyl alcohol <105>; '
                           '#10# substrate specificity and stereospecificity, '
                           'substrate binding pocket structure of the 3 '
                           'isozymes, involving Met294, Trp57, and Trp93 '
                           '<120>; #61# substrate specificity of the 2 '
                           'isozmyes with various substrates, overview, '
                           'isozymes are highly specific for the '
                           '(R)-stereoisomers and enantioselctive for the '
                           'R(-)isomers <113>; #46# the enzyme undergoes a '
                           'substantial conformational change in the apo-holo '
                           'transition, accompanied by loop movements at the '
                           'domain interface <108>; #60# alcohol dehydrogenase '
                           'activity may not limit alcohol supply for ester '
                           'production during ripening <146>; #54# Cm-ADH2 '
                           'cannot reduce branched aldehydes <151>; #10# '
                           'effects of pressure on deuterium isotope effects '
                           'of yeast alcohol dehydrogenase using alternative '
                           'substrates <139>; #92# no activity with methanol '
                           '<144>; #93# the enzyme does not act on short-chain '
                           'normal alkyl alcohols, including methanol and '
                           'ethanol <137>; #96# no activity towards methanol, '
                           'ethanol, 1-propanol, triethylene glycol, '
                           'polyethylene glycol 400, polyethylene glycol 1000, '
                           'D-sorbitol, D-sorbose, formaldehyde, acetaldehyde, '
                           'propionaldehyde, butyraldehyde, and valeraldehyde '
                           '<156>; #98# ADH1 preferrs primary alcohols '
                           'containing C3-C8 carbons to secondary alcohols '
                           'such as 2-propanol and 2-butanol. ADH1 possesses '
                           'specific carboxylate ester-forming activity <172>; '
                           '#101# no activity detected with: '
                           'N-benzyl-2-pyrrolidinone, 2-pyrrolidinone, '
                           '3-hexanone, 4-hydroxy-2-butanone, '
                           '(R)-N-benzyl-3-pyrrolidinol, ethanol, '
                           '1,3-propanediol, 1-butanol, 1,4-butanediol, '
                           '1,2,3-butanetriol, 1,2,4-butanetriol, acetol, '
                           '2-phenyl-1-propanol, 3-phenyl-1-propanol, benzyl '
                           'alcohol and glycerol. No activity with NADP+ or '
                           'NADPH <185>; #6# preference for reduction of '
                           'aromatic ketones and alpha-keto esters, and poor '
                           'activity on aromatic alcohols and aldehydes <169>; '
                           '#26# when NADH is replaced with NADPH, the '
                           'reaction rate is reduced by 0.6% <188>; #41# '
                           'activity is severely reduced towards aliphatic '
                           'alcohols of more than 8 carbon atoms for the free '
                           'enzyme, but not so with immobilized HLAD, '
                           'exhibiting an activity towards C22 and C24 '
                           'aliphatic alcohols higher than 50% of the highest '
                           'value, obtained with C8 <204>; #8# differences in '
                           'the activities of total ADH and class I ADH '
                           'isoenzyme between cancer liver tissues and healthy '
                           'hepatocytes may be a factor in ethanol metabolism '
                           'disorders, which can intensify carcinogenesis '
                           '<180>; #112# TADH is a NAD(H)-dependent enzyme and '
                           'shows a very broad substrate spectrum producing '
                           'exclusively the (S)-enantiomer in high '
                           'enantiomeric excess (more than 99%) during '
                           'asymmetric reduction of ketones <197>; #106# '
                           '1-octanal is no substrate for isozyme ADH1C <214>; '
                           '#106# 1-octanal is no substrate for isozyme ADH2 '
                           '<214>; #109# 1-octanal is no substrate for isozyme '
                           'ADH4 <214>; #112# ADH exhibits a clear preference '
                           'for primary alcohols and corresponding aldehydes '
                           'for aliphatic substrates, in the oxidative '
                           'direction activity steeply increases with chain '
                           'length until 1-propanol and then decreases '
                           'slightly again with growing chain length, '
                           'alpha,beta-unsaturated ketones like 3-penten-2-one '
                           'and cyclohexenone are not converted by ADH, almost '
                           'no conversion of methanol (0.2%) and (+)-carvone '
                           '(0.4%) is detected <197>; #110# no activity '
                           'towards methanol <210>; #114# substrates are a '
                           'broad range of alkyl alcohols from ethanol to '
                           '1-triacontanol <215>; #123# the physiological '
                           'direction of the catalytic reaction is reduction '
                           'rather than oxidation <219>; #124# the enzyme '
                           'displays a preference for the reduction of '
                           'alicyclic, bicyclic and aromatic ketones and '
                           'alpha-ketoesters, but is poorly active on '
                           'aliphatic, cyclic and aromatic alcohols, showing '
                           'no activity on aldehydes <218>; #123# the enzyme '
                           'shows no activity on aliphatic linear and branched '
                           'alcohols, except for a poor activity on '
                           '2-propyn-1-ol, 3-methyl-1-butanol and 2-pentanol; '
                           'however, it shows a discrete activity on aliphatic '
                           'cyclic and bicyclic alcohols. Benzyl alcohol and '
                           '4-bromobenzyl alcohol are not found to be '
                           'substrates. The S and R enantiomers of '
                           'a-(trifluoromethyl)benzyl alcohol and methyl and '
                           'ethyl mandelates show no apparent activity with '
                           'SaADH. The enzyme shows poor activity on '
                           '(+/-)-1-phenyl-1-propanol, 1-(1-naphthyl)ethanol '
                           'and the two enantiomers of 1-(2-naphthyl)ethanol. '
                           'The enzyme is not active on aliphatic and aromatic '
                           'aldehydes, and on aliphatic linear, branched and '
                           'cyclic ketones except for 3-methylcyclohexanone. '
                           'Catalytic inactivity is observed with acetophenone '
                           'and (S)-a-(trifluoromethyl)benzyl <219>; #127# '
                           'methanol, formaldehyde, and acetone are no '
                           'substrates for HpADH3 <222>; #48# no activity with '
                           'methanol, 1-butanol, glycerol or 2-propanol <223>; '
                           '#128# substrate specificity and '
                           'enantiospecificity, overview. The (R)-specific '
                           'alcohol dehydrogenase requires NADH and reduces '
                           'various kinds of carbonyl compounds, including '
                           'ketones and aldehydes. AFPDH reduces '
                           'acetylpyridine derivatives, beta-keto esters, and '
                           'some ketones compounds with high '
                           'enantiospecificity, overview. No activity with '
                           '2-chlorobenzaldehyde and 2-tetralone, poor '
                           'activity with 1-tetralone, pyruvate, '
                           '2-oxobutyrate, oxalacetate, cyclopentanone, '
                           'cyclohexanone, cycloheptanone, and dipropylketone. '
                           'No activity with 1,2-propanediol, '
                           '3-chloro-1,2-propanediol, 3-bromo-1,2-propanediol, '
                           'glycerol, 1-pentanol, poor activity with '
                           '1-butanol, 1-propanol, ethanol, and methanol '
                           '<225>; #85# the enzyme exhibits broad substrate '
                           'specificity towards aliphatic ketones, '
                           'cycloalkanones, aromatic ketones, and ketoesters '
                           '<226>; #132# the enzyme shows broad substrate '
                           'specificity and prefers aliphatic alcohols and '
                           'ketones. There are no large differences in the '
                           'reactivities between primary and secondary '
                           'alcohols. The enzyme produces (S)-alcohols from '
                           'the corresponding ketones. The values of the '
                           'enantiomeric excess increase with the increase of '
                           'chain length except for the reduction of '
                           '2-hexanone. The highest enantioselectivity is '
                           'shown with the reduction of 2-nonanone <239>; '
                           '#133# the NAD+-dependent HvADH1 shows a preference '
                           'for short-chain alcohols, no activity with '
                           'methanol <237>; #143# broad substrate specificity '
                           'with a preference for the reduction of ketones and '
                           'the oxidation of secondary alcohols <138>; #124# '
                           'enzyme displays a preference for the reduction of '
                           'alicyclic, bicyclic and aromatic ketones and '
                           'alpha-keto esters, but is poorly active on '
                           'aliphatic, cyclic and aromatic alcohols, and shows '
                           'no activity on aldehydes <219>; #150# enzyme '
                           'reduces aldehydes to (R)-alcohols with more than '
                           '99.8% enantiomeric excess <243>; #151# enzyme '
                           'selectively reduces the C=O bond of allylic '
                           'aldehydes/ketones to the corresponding '
                           'alpha,beta-unsaturated alcohols and also has the '
                           'capacity of stereoselectively reducing aromatic '
                           'ketones to (S)-enantioselective alcohols. The '
                           'enzyme preferentially catalyzes oxidation of '
                           'allylic/benzyl aldehydes <244>; #71# ethanol '
                           'dehydrogenase activity of Thermoanaerobium brockii '
                           'is both NAD and NADP linked, reversible, and not '
                           'inhibited by low levels of reaction products '
                           '<103>; #119,142# mutation at the substrate-binding '
                           'site, or at a dimer interface, alters kinetic '
                           'properties and protein oligomeric structure, '
                           'active site flexibility is correlated with subunit '
                           'interactions 20 A away <260>; #6# the enzyme '
                           'transfers the pro-S hydrogen of [4R-(2)H]NADH and '
                           'exhibits Prelog specificity <269>; #41# acycloNAD+ '
                           'i.e. NAD+-analogue, where the nicotinamide ribosyl '
                           'moiety has been replaced by the nicotinamide '
                           '(2-hydroxyethoxy)methyl moiety. There is no '
                           'detectable reduction of acycloNAD+ by secondary '
                           'alcohols although these alcohols serve as '
                           'competitive inhibitors. AcycloNAD+ converts horse '
                           'liver ADH from a broad spectrum alcohol '
                           'dehydrogenase, capable of utilizing either primary '
                           'or secondary alcohols, into an exclusively primary '
                           'alcohol dehydrogenase <275>; #51# bifunctional '
                           'enzyme consisting of an N-terminal acetaldehyde '
                           'dehydrogenase (ALDH) and a C-terminal alcohol '
                           'dehydrogenase (ADH). The specificity constant '
                           '(kcat/Km) is 47fold higher for acetaldehyde '
                           'reductase than that for ethanol dehydrogenase '
                           '<279>; #153# enzyme is an alcohol dehydrogenase '
                           'with additional activity for all-trans-retinol, '
                           'reaction of EC 1.1.1.184 <272>; #155# enzyme shows '
                           'activity as a reductase specific for (S)-acetoin, '
                           'EC 1.1.1.76, and both diacetyl reductase (EC '
                           '1.1.1.304) and NAD+-dependent alcohol '
                           'dehydrogenase (EC 1.1.1.1) activities <271>; #160# '
                           'the enzyme additionally catalyzes selective '
                           'reduction of 3-quinuclidinone to '
                           '(R)-3-quinuclidinol, with 84% ee and 62% '
                           'conversion after 22 h <274>; #162# Candida '
                           'albicans ADH1 is a bifunctional enzyme that '
                           'catalyzes methylglyoxal oxidation and reduction, '
                           'cf. EC 1.2.1.23 <287>; #161# the enzyme catalyzes '
                           'NAD(H)-dependent oxidation of various alcohols and '
                           'reduction of aldehydes, with a marked preference '
                           'for substrates with functional group at the '
                           'terminal carbon atom <286>; #166# almost no '
                           'activity with D-arabinonate, D-lyxonate, '
                           'D-galactonate, glycerol, meso-erythritol, '
                           'D-ribitol, D-arabitol, D-xylitol, and D-mannitol. '
                           'No activity with propanal, butanal, hexanal, and '
                           '4-oxobutanoic acid <292>; #165# the enzyme '
                           'catalyzes the reduction of acetophenone '
                           'derivatives to the corresponding (S)-chiral '
                           'alcohols in an enantiomerically pure form. The '
                           'substituents on the benzene ring of the aryl '
                           'ketones exert some effect on the enzyme activity, '
                           'although the influence is not dramatic. The '
                           'enantioselectivity of the reduction is not '
                           'affected by the substituents and pattern of the '
                           'substitution. The alpha-chlorinated acetophenone '
                           'shows a much higher activity than the '
                           'unsubstituted one (more than 10 times) <294>) {',
                'data': 'more = ?',
                'refs': [38,
                         47,
                         59,
                         68,
                         82,
                         94,
                         103,
                         105,
                         108,
                         113,
                         118,
                         120,
                         126,
                         137,
                         138,
                         139,
                         144,
                         146,
                         151,
                         156,
                         169,
                         172,
                         180,
                         185,
                         188,
                         197,
                         204,
                         210,
                         211,
                         214,
                         215,
                         218,
                         219,
                         222,
                         223,
                         225,
                         226,
                         237,
                         239,
                         243,
                         244,
                         260,
                         269,
                         271,
                         272,
                         274,
                         275,
                         279,
                         286,
                         287,
                         292,
                         294]},
               {'comment': '#93# 33% of the activity with 2-propanol, in the '
                           'reverse reaction 435% of the activity with phenyl '
                           'trifluoromethyl ketone <137>; #96# 11% activity '
                           'compared to benzyl alcohol <156>; #98# about 85% '
                           'of activity with ethanol, ADH1 <172>; #112# 57% '
                           'activity compared to cyclohexanol <197>; #106# '
                           'substrate for isozyme ADH3 <214>',
                'data': '1-octanol + NAD+ = octanal + NADH + H+',
                'refs': [137, 144, 156, 172, 197, 210, 214, 222, 286]},
               {'comment': '#93# 33% of the activity with 2-propanol, in the '
                           'reverse reaction 435% of the activity with phenyl '
                           'trifluoromethyl ketone <137>; #96# 11% activity '
                           'compared to benzyl alcohol <156>; #98# about 85% '
                           'of activity with ethanol, ADH1 <172>; #112# 57% '
                           'activity compared to cyclohexanol <197>; #106# '
                           'substrate for isozyme ADH3 <214>) {r',
                'data': '1-octanol + NAD+ = octanal + NADH + H+',
                'refs': [137, 144, 156, 172, 197, 210, 214, 222, 286]}]),
             ('ST',
              [{'bto': 'BTO_0000759',
                'comment': '#5# isoenzyme A2 and B2 <48>; #36# isoenzyme '
                           'AA-ADH and BB-ADH most abundant in <95>; #8# '
                           'isozyme ADH1C*2 <116>; #9# females show 70% higher '
                           'hepatic alcohol dehydrogenase activity and display '
                           '60% lower voluntary ethanol intake than males. '
                           'Following ethanol administration (1 g/kg ip), '
                           'females generate a transient blood acetaldehyde '
                           'increase with levels that are 2.5fold greater than '
                           'in males. Castration of males leads to an increase '
                           'alcohol dehydrogenase activity the appearance of '
                           'an acetaldehyde burst a reduction of voluntary '
                           'ethanol intake comparable with that of females '
                           '<167>; #8# the activities of total alcohol '
                           'dehydrogenase, aldehyde dehydrogenase and class I '
                           'alcohol dehydrogenase isoenzyme between cancer '
                           'liver tissues and healthy hepatocytes might be a '
                           'factor in ethanol metabolism disorders which can '
                           'intensify carcinogenesis <186>; #106# isozymes '
                           'ADH1C and ADH3 <214>; #8# most abundant in the '
                           'liver <180>; #8# the total alcohol dehydrogenase '
                           'activity is significantly higher in cancer tissues '
                           'than in healthy liver <194>; #131# class III ADH '
                           '<227>',
                'data': 'liver',
                'refs': [1,
                         2,
                         5,
                         10,
                         12,
                         13,
                         14,
                         15,
                         16,
                         17,
                         18,
                         19,
                         20,
                         21,
                         22,
                         23,
                         24,
                         25,
                         26,
                         27,
                         28,
                         29,
                         30,
                         31,
                         32,
                         33,
                         34,
                         35,
                         36,
                         37,
                         39,
                         40,
                         41,
                         42,
                         44,
                         45,
                         46,
                         48,
                         49,
                         51,
                         52,
                         54,
                         55,
                         59,
                         60,
                         86,
                         92,
                         93,
                         95,
                         98,
                         101,
                         111,
                         116,
                         117,
                         143,
                         167,
                         175,
                         178,
                         180,
                         186,
                         194,
                         198,
                         200,
                         201,
                         204,
                         205,
                         212,
                         214,
                         224,
                         227,
                         275]},
               {'bto': 'BTO_0003833',
                'comment': '#106,109# isozyme ADH4 <214>',
                'data': 'buccal mucosa',
                'refs': [214]}]),
             ('SY',
              [{'comment': '#106# isozyme <214>',
                'data': 'ADH1C',
                'refs': [214]},
               {'comment': '#10,106# isozyme <202,214>',
                'data': 'ADH2',
                'refs': [110,
                         123,
                         128,
                         162,
                         170,
                         202,
                         214,
                         215,
                         233,
                         240,
                         252]},
               {'comment': '#106# isozyme <214>',
                'data': 'ADH3',
                'refs': [141, 172, 177, 200, 214, 252, 263]}]),
             ('references',
              {1: {'info': 'Talbot, B.G.; Qureshi, A.A.; Cohen, R.; Thirion, '
                           'J.P.: Purification and properties of two distinct '
                           'groups of ADH isozymes from Chinese hamster liver. '
                           'Biochem. Genet. (1981) 19, 813-829.',
                   'pubmed': 6794566},
               2: {'info': 'Fong, W.P.: Isolation and characterization of '
                           'grass carp (Ctenopharyngodon idellus) liver '
                           'alcohol dehydrogenase. Comp. Biochem. Physiol. B '
                           '(1991) 98, 297-302.'},
               3: {'info': 'Pessione, E.; Pergola, L.; Cavaletto, M.; Giunta, '
                           'C.; Trotta, A.; Vanni, A.: Extraction, '
                           'purification and characterization of ADH1 from the '
                           'budding yeast Kluyveromyces marxianus. Ital. J. '
                           'Biochem. (1990) 39, 71-82.',
                   'pubmed': 2193901},
               4: {'info': 'Leblova, S.; El Ahmad, M.: Characterization of '
                           'alcohol dehydrogenase isolated from germinating '
                           'bean (Vicia faba) seeds. Collect. Czech. Chem. '
                           'Commun. (1989) 54, 2519-2527.'},
               5: {'info': 'Keung, W.M.; Ho, Y.W.; Fong, W.P.; Lee, C.Y.: '
                           'Isolation and characterization of shrew (Suncus '
                           'murinus) liver alcohol dehydrogenase. Comp. '
                           'Biochem. Physiol. B (1989) 93, 169-173.',
                   'pubmed': 2666017},
               6: {'info': 'Tong, W.F.; Lin, S.W.: Purification and '
                           'biochemical properties of rice alcohol '
                           'dehydrogenase. Bot. Bull. Acad. Sin. (1988) 29, '
                           '245-253.'},
               7: {'info': 'Van Geyt, J.; Jacobs, M.; Triest, L.: '
                           'Characterization of alcohol dehydrogenase in Najas '
                           'marina L. Aquat. Bot. (1987) 28, 129-141.'},
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
                           '(1982) 7, 237-250.'},
               9: {'info': 'Edenberg, H.J.; Brown, C.J.; Carr, L.G.; Ho, W.H.; '
                           'Hu, M.W.: Alcohol dehydrogenase gene expression '
                           'and cloning of the mouse chi-like ADH. Adv. Exp. '
                           'Med. Biol. (1991) 284, 253-262.',
                   'pubmed': 2053480},
               10: {'info': 'Herrera, E.; Zorzano, A.; Fresneda, V.: '
                            'Comparative kinetics of human and rat liver '
                            'alcohol dehydrogenase. Biochem. Soc. Trans. '
                            '(1983) 11, 729-730.'},
               11: {'info': 'Dafeldecker, W.P.; Vallee, B.L.: Organ-specific '
                            'human alcohol dehydrogenase: isolation and '
                            'characterization of isozymes from testis. '
                            'Biochem. Biophys. Res. Commun. (1986) 134, '
                            '1056-1063.',
                    'pubmed': 2936344},
               12: {'info': 'Woronick, C.L.: Alcohol dehydrogenase from human '
                            'liver. Methods Enzymol. (1975) 41B, 369-374.',
                    'pubmed': 236461},
               13: {'info': 'Wagner, F.W.; Burger, A.R.; Vallee, B.L.: Kinetic '
                            'properties of human liver alcohol dehydrogenase: '
                            'oxidation of alcohols by class I isoenzymes. '
                            'Biochemistry (1983) 22, 1857-1863.',
                    'pubmed': 6342669},
               14: {'info': 'Ditlow, C.C.; Holmquist, B.; Morelock, M.M.; '
                            'Vallee, B.L.: Physical and enzymatic properties '
                            'of a class II alcohol dehydrogenase isozyme of '
                            'human liver: pi-ADH. Biochemistry (1984) 23, '
                            '6363-6368.',
                    'pubmed': 6397223},
               15: {'info': 'Yin, S.J.; Bosron, W.F.; Magnes, L.J.; Li, T.K.: '
                            'Human liver alcohol dehydrogenase: purification '
                            'and kinetic characterization of the beta 2 beta '
                            '2, beta 2 beta 1, alpha beta 2, and beta 2 gamma '
                            '1 Oriental isoenzymes. Biochemistry (1984) 23, '
                            '5847-5853.',
                    'pubmed': 6395883},
               16: {'info': 'Wagner, F.W.; Pares, X.; Holmquist, B.; Vallee, '
                            'B.L.: Physical and enzymatic properties of a '
                            'class III isozyme of human liver alcohol '
                            'dehydrogenase: chi-ADH. Biochemistry (1984) 23, '
                            '2193-2199.',
                    'pubmed': 6375718},
               17: {'info': 'Bosron, W.F.; Magnes, L.J.; Li, T.K.: Kinetic and '
                            'electrophoretic properties of native and '
                            'recombined isoenzymes of human liver alcohol '
                            'dehydrogenase. Biochemistry (1983) 22, 1852-1857.',
                    'pubmed': 6342668},
               18: {'info': 'Bosron, W.F.; Li, T.K.: Isolation and '
                            'characterization of an anodic form of human liver '
                            'alcohol dehydrogenase. Biochem. Biophys. Res. '
                            'Commun. (1977) 74, 85-91.',
                    'pubmed': 836289},
               19: {'info': 'Schneider-Bernloehr, H.; Formicka-Kozlowska, G.; '
                            'Buehler, R.; Wartburg, J.P.; Zeppezauer, M.: '
                            'Active-site-specific zinc-depleted and '
                            'reconstituted cobalt(II) human-liver alcohol '
                            'dehydrogenase. Preparation, characterization and '
                            'complexation with NADH and '
                            'trans-4-(N,N-dimethylamino)-cinnamaldehyde. Eur. '
                            'J. Biochem. (1988) 173, 275-280.',
                    'pubmed': 3360008},
               20: {'info': 'Burnell, J.C.; Li, T.K.; Bosron, W.F.: '
                            'Purification and steady-state kinetic '
                            'characterization of human liver beta 3 beta 3 '
                            'alcohol dehydrogenase. Biochemistry (1989) 28, '
                            '6810-6815.',
                    'pubmed': 2819035},
               21: {'info': 'Pares, X.; Vallee, B.L.: New human liver alcohol '
                            'dehydrogenase forms with unique kinetic '
                            'characteristics. Biochem. Biophys. Res. Commun. '
                            '(1981) 98, 122-130.',
                    'pubmed': 7011320},
               22: {'info': 'Bosron, W.F.; Li, T.K.; Vallee, B.L.: New '
                            'molecular forms of human liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'ADHIndianapolis. Proc. Natl. Acad. Sci. USA '
                            '(1980) 77, 5784-5788.',
                    'pubmed': 7003596},
               23: {'info': 'Bosron, W.F.; Li, T.K.; Dafeldecker, W.P.; '
                            'Vallee, B.L.: Human liver pig-alcohol '
                            'dehydrogenase: kinetic and molecular properties. '
                            'Biochemistry (1979) 18, 1101-1105.',
                    'pubmed': 427099},
               24: {'info': 'Dafeldecker, W.P.; Pares, X.; Vallee, B.L.; '
                            'Bosron, W.F.; Li, T.K.: Simian liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'isoenzymes from Saimiri sciureus. Biochemistry '
                            '(1981) 20, 856-861.',
                    'pubmed': 7011375},
               25: {'info': 'Dafeldecker, W.P.; Meadow, P.E.; Pares, X.; '
                            'Vallee, B.L.: Simian liver alcohol dehydrogenase: '
                            'isolation and characterization of isoenzymes from '
                            'Macaca mulatta. Biochemistry (1981) 20, '
                            '6729-6734.',
                    'pubmed': 7030395},
               26: {'info': 'Kvassman, J.; Pettersson, G.: Kinetics of '
                            'coenzyme binding to liver alcohol dehydrogenase '
                            'in the pH range 10-12. Eur. J. Biochem. (1987) '
                            '166, 167-172.',
                    'pubmed': 3595610},
               27: {'info': 'Andersson, L.; Mosbach, K.: Alcohol dehydrogenase '
                            'from horse liver by affinity chromatography. '
                            'Methods Enzymol. (1982) 89, 435-445.',
                    'pubmed': 6755178},
               28: {'info': 'Pietruszko, R.: Alcohol dehydrogenase from horse '
                            'liver, steroid-active SS isoenzyme. Methods '
                            'Enzymol. (1982) 89, 429-435.'},
               29: {'info': 'Dahl, K.H.; Eklund, H.; McKinley-McKee, J.S.: '
                            'Enantioselective affinity labelling of horse '
                            'liver alcohol dehydrogenase. Correlation of '
                            'inactivation kinetics with the three-dimensional '
                            'structure of the enzyme. Biochem. J. (1983) 211, '
                            '391-396.',
                    'pubmed': 6347187},
               30: {'info': 'Ramaswamy, S.: Dynamics in alcohol dehydrogenase '
                            'elucidated from crystallographic investigations. '
                            'Adv. Exp. Med. Biol. (1999) 7, 275-284.',
                    'pubmed': 10352696},
               31: {'info': 'Adolph, H.W.; Maurer, P.; Schneider-Bernloehr, '
                            'H.; Sartorius, C.; Zeppezauer, M.: Substrate '
                            'specificity and stereoselectivity of horse liver '
                            'alcohol dehydrogenase. Kinetic evaluation of '
                            'binding and activation parameters controlling the '
                            'catalytic cycles of unbranched, acyclic secondary '
                            'alcohols and ketones as substrates of the native '
                            'and active-site-specific Co(II)-substituted '
                            'enzyme. Eur. J. Biochem. (1991) 201, 615-625.',
                    'pubmed': 1935957},
               32: {'info': 'Freudenreich, C.; Samama, J.P.; Biellmann, J.F.: '
                            'Design of inhibitors from the three-dimensional '
                            'structure of alcohol dehydrogenase. Chemical '
                            'synthesis and enzymatic properties. J. Am. Chem. '
                            'Soc. (1984) 106, 3344-3353.'},
               33: {'info': 'Samama, J.P.; Hirsch, D.; Goulas, P.; Biellmann, '
                            'J.F.: Dependence of the substrate specificity and '
                            'kinetic mechanism of horse-liver alcohol '
                            'dehydrogenase on the size of the C-3 pyridinium '
                            'substituent. 3-Benzoylpyridine-adenine '
                            'dinucleotide. Eur. J. Biochem. (1986) 159, '
                            '375-380.',
                    'pubmed': 3758068},
               34: {'info': 'Eklund, H.: Coenzyme binding in alcohol '
                            'dehydrogenase. Biochem. Soc. Trans. (1989) 17, '
                            '293-296.',
                    'pubmed': 2753206},
               35: {'info': 'Dworschack, R.T.; Plapp, B.V.: Kinetics of native '
                            'and activated isozymes of horse liver alcohol '
                            'dehydrogenase. Biochemistry (1977) 16, 111-116.',
                    'pubmed': 831772},
               36: {'info': 'Maret, W.; Andersson, I.; Dietrich, H.; '
                            'Schneider-Bernloehr, H.; Einarsson, R.; '
                            'Zeppezauer, M.: Site-specific substituted '
                            'cobalt(II) horse liver alcohol dehydrogenases. '
                            'Preparation and characterization in solution, '
                            'crystalline and immobilized state. Eur. J. '
                            'Biochem. (1979) 98, 501-512.',
                    'pubmed': 488110},
               37: {'info': 'Skerker, P.S.; Clark, D.S.: Thermostability of '
                            'alcohol dehydrogenase: evidence for distinct '
                            'subunits with different deactivation properties. '
                            'Biotechnol. Bioeng. (1989) 33, 62-71.',
                    'pubmed': 18587844},
               38: {'info': 'Benach, J.; Atrian, S.; Gonzalez-Duarte, R.; '
                            'Ladenstein, R.: The catalytic reaction and '
                            'inhibition mechanism of Drosophila alcohol '
                            'dehydrogenase: observation of an enzyme-bound '
                            'NAD-ketone adduct at 1.4 A resolution by X-ray '
                            'crystallography. J. Mol. Biol. (1999) 289, '
                            '335-355.',
                    'pubmed': 10366509},
               39: {'info': 'Tsai, C.S.: Multifunctionality of liver alcohol '
                            'dehydrogenase: kinetic and mechanistic studies of '
                            'esterase reaction. Arch. Biochem. Biophys. (1982) '
                            '213, 635-642.',
                    'pubmed': 7041828},
               40: {'info': 'Favilla, R.; Cavatorta, P.; Mazzini, A.; Fava, '
                            'A.: The peroxidatic reaction catalyzed by horse '
                            'liver alcohol dehydrogenase. 2. Steady-state '
                            'kinetics and inactivation. Eur. J. Biochem. '
                            '(1980) 104, 223-227.',
                    'pubmed': 6989598},
               41: {'info': 'Ryzewski, C.N.; Pietruszko, R.: Kinetic mechanism '
                            'of horse liver alcohol dehydrogenase SS. '
                            'Biochemistry (1980) 19, 4843-4848.',
                    'pubmed': 7000185},
               42: {'info': 'Ryzewski, C.N.; Pietruszko, R.: Horse liver '
                            'alcohol dehydrogenase SS: purification and '
                            'characterization of the homogenous isoenzyme. '
                            'Arch. Biochem. Biophys. (1977) 183, 73-82.',
                    'pubmed': 20851},
               43: {'info': 'Winberg, J.O.; McKinley-McKee, J.S.: Drosophila '
                            'melanogaster alcohol dehydrogenase: '
                            'product-inhibition studies. Biochem. J. (1994) '
                            '301, 901-909.',
                    'pubmed': 8053914},
               44: {'info': 'von Bahr-Lindstroem, H.; Andersson, L.; Mosbach, '
                            'K.; Joernvall, H.: Purification and '
                            'characterization of chicken liver alcohol '
                            'dehydrogenase. FEBS Lett. (1978) 89, 293-297.',
                    'pubmed': 658420},
               45: {'info': 'Hoshino, T.; Ishigura, I.; Ohta, Y.: Rabbit liver '
                            'alcohol dehydrogenase: purification and '
                            'properties. J. Biochem. (1985) 97, 1163-1172.',
                    'pubmed': 3161873},
               46: {'info': 'Keung, W.M.; Yip, P.K.: Rabbit liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'class I isozymes. Biochem. Biophys. Res. Commun. '
                            '(1989) 158, 445-453.',
                    'pubmed': 2916992},
               47: {'info': 'Keung, W.M.: A genuine organ specific alcohol '
                            'dehydrogenase from hamster testes: isolation, '
                            'characterization and developmental changes. '
                            'Biochem. Biophys. Res. Commun. (1988) 156, 38-45.',
                    'pubmed': 3178842},
               48: {'info': 'Algar, E.M.; Seeley, T.L.; Holmes, R.S.: '
                            'Purification and molecular properties of mouse '
                            'alcohol dehydrogenase isozymes. Eur. J. Biochem. '
                            '(1983) 137, 139-147.',
                    'pubmed': 6360682},
               49: {'info': 'Julia, P.; Farres, J.; Pares, X.: '
                            'Characterization of three isoenzymes of rat '
                            'alcohol dehydrogenase. Tissue distribution and '
                            'physical and enzymatic properties. Eur. J. '
                            'Biochem. (1987) 162, 179-189.',
                    'pubmed': 3816781},
               50: {'info': 'Pares, X.; Moreno, A.; Cederlund, E.; Hoeoeg, '
                            'J.O.; Joernvall, H.: Class IV mammalian alcohol '
                            'dehydrogenase. Structural data of the rat stomach '
                            'enzyme reveal a new class well separated from '
                            'those already characterized. FEBS Lett. (1990) '
                            '277, 115-118.',
                    'pubmed': 2269340},
               51: {'info': 'Mezey, E.; Potter, J.J.: Separation and partial '
                            'characterization of multiple forms of rat liver '
                            'alcohol dehydrogenase. Arch. Biochem. Biophys. '
                            '(1983) 225, 787-794.',
                    'pubmed': 6354095},
               52: {'info': 'Hjelmqvist, L.; Shafqqat, J.; Siddiqi, A.R.; '
                            'Joernvall, H.: Linking of isoenzyme and class '
                            'variability patterns in the emergence of novel '
                            'alcohol dehydrogenase functions. Characterization '
                            'of isozymes in Uromastix hardwickii. Eur. J. '
                            'Biochem. (1996) 236, 563-570.',
                    'pubmed': 8612630},
               53: {'info': 'Kedishvili, N.Y.; Bosron, W.F.; Stone, C.L.; '
                            'Hurley, T.D.; Peggs, C.F.; Thomasson, H.R.; '
                            'Popov, K.M.; Carr, L.G.; Edenberg, H.J.; Li, '
                            'T.K.: Expression and kinetic characterization of '
                            'recombinant human stomach alcohol dehydrogenase. '
                            'Active-site amino acid sequence explains '
                            'substrate specificity copared with liver '
                            'isozymes. J. Biol. Chem. (1995) 270, 3625-3630.',
                    'pubmed': 7876099},
               54: {'info': 'Plapp, B.V.; Sogin, D.C.; Dworschack, R.T.; '
                            'Bohlken, D.P.; Woenckhaus, C.: Kinetics of native '
                            'and modified liver alcohol dehydrogenase with '
                            'coenzyme analogues: isomerization of '
                            'enzyme-nicotinamide adenine dinucleotide complex. '
                            'Biochemistry (1986) 25, 5396-5402.',
                    'pubmed': 3778867},
               55: {'info': 'Li, H.; Hallows, W.H.; Punzi, J.S.; Marquez, '
                            'V.E.; Carrell, H.L.; Pankiewicz, K.W.; Watanabe, '
                            'K.A.; Goldstein, B.M.: Crystallographic studies '
                            'of two alcohol dehydrogenase-bound analogues of '
                            'thiazole-4-carboxamide adenine dinucleotide '
                            '(TAD), the active anabolite of the antitumor '
                            'agent tiazofurin. Biochemistry (1994) 33, 23-32.',
                    'pubmed': 8286346},
               56: {'info': 'Pearl, L.H.; Demasi, D.; Hemmings, A.M.; Sica, '
                            "F.; Mazzarella, L.; Raia, C.A.; D'Auria, S.; "
                            'Rossi, M.: Crystallization and preliminary X-ray '
                            'analysis of an NAD(+)-dependent alcohol '
                            'dehydrogenase fromthe extreme thermophilic '
                            'archaebacterium Sulfolobus solfataricus. J. Mol. '
                            'Biol. (1993) 229, 782-784.',
                    'pubmed': 8433371},
               57: {'info': 'Shafqat, J.; Hjelmqvist, L.; Joernvall, H.: Liver '
                            'class-I alcohol dehydrogenase isozyme '
                            'relationships and constant patterns in a variable '
                            'basic structure. Distinctions from '
                            'characterization of an ethanol dehydrogenase in '
                            'cobra, Naja naja. Eur. J. Biochem. (1996) 236, '
                            '571-578.',
                    'pubmed': 8612631},
               58: {'info': 'Retzios, A.; Thatcher, D.R.: Characterization of '
                            'the Adhf and Adhus alleloenzymes of Drosophila '
                            'melanogaster (fruitfly) alcohol dehydrogenase. '
                            'Biochem. Soc. Trans. (1981) 9, 298-299.'},
               59: {'info': 'Bauermeister, A.; Sargent, J.: Purification and '
                            'properties of an alcohol dehydrogenase from the '
                            'liver and intestinal caecum of rainbow trout '
                            '(Salmo gairdnerii). Biochem. Soc. Trans. (1978) '
                            '6, 222-224.',
                    'pubmed': 640168},
               60: {'info': 'Nussrallah, B.A.; Dam, R.; Wagner, F.W.: '
                            'Characterization of Coturnix quail liver alcohol '
                            'dehydrogenase enzymes. Biochemistry (1989) 28, '
                            '6245-6251.',
                    'pubmed': 2789998},
               61: {'info': 'Winberg, J.O.; Hovik, R.; McKinley-McKee, J.S.; '
                            'Juan, E.; Gonzalez-Duarte, R.: Biochemical '
                            'properties of alcohol dehydrogenase from '
                            'Drosophila lebanonensis. Biochem. J. (1986) 235, '
                            '481-490.',
                    'pubmed': 2943270},
               62: {'info': 'Winberg, J.O.; McKinley-McKee, J.S.: Drosophila '
                            'melanogaster alcohol dehydrogenase. Biochemical '
                            'properties of the NAD+-plus-acetone-induced '
                            'isoenzyme conversion. Biochem. J. (1988) 251, '
                            '223-227.',
                    'pubmed': 3134011},
               63: {'info': 'Heinstra, P.W.H.; Thoerig, G.E.W.; Scharloo, W.; '
                            'Drenth, W.; Nolte, R.J.M.: Kinetics and '
                            'thermodynamics of ethanol oxidation catalyzed by '
                            'genetic variants of the alcohol dehydrogenase '
                            'from Drosophila melanogaster and D. simulans. '
                            'Biochim. Biophys. Acta (1988) 967, 224-233.',
                    'pubmed': 3142528},
               64: {'info': 'Juan, E.; Gonzalez-Duarte, R.: Determination of '
                            'some biochemical and structural features of '
                            'alcohol dehydrogenases from Drosophila simulans '
                            'and Drosophila virilis. Comparison of their '
                            'properties with the Drosophila melanogaster Adhs '
                            'enzyme. Biochem. J. (1981) 195, 61-69.',
                    'pubmed': 6796069},
               65: {'info': 'Lee, C.Y.: Alcohol dehydrogenase from Drosophila '
                            'melanogaster. Methods Enzymol. (1982) 89, '
                            '445-450.'},
               66: {'info': 'Rella, R.; Raia, C.A.; Pensa, M.; Pisani, F.M.; '
                            'Gambacorta, A.; de Rosa, M.; Rossi, M.: A novel '
                            'archaebacterial NAD+-dependent alcohol '
                            'dehydrogenase. Purification and properties. Eur. '
                            'J. Biochem. (1987) 167, 475-479.',
                    'pubmed': 3115775},
               67: {'info': 'Wills, C.; Kratofil, P.; Londo, D.; Martin, T.: '
                            'Characterization of the two alcohol '
                            'dehydrogenases of Zymomonas mobilis. Arch. '
                            'Biochem. Biophys. (1981) 210, 775-785.',
                    'pubmed': 7030207},
               68: {'info': 'Kinoshita, S.; Kakizono, T.; Kadota, K.; Das, K.; '
                            'Taguchi, H.: Purification of two alcohol '
                            'dehydrogenases from Zymomonas mobilis and their '
                            'properties. Appl. Microbiol. Biotechnol. (1985) '
                            '22, 249-254.'},
               69: {'info': 'Grondal, E.J.M.; Betz, A.; Kreuzberg, K.: Partial '
                            'purification and properties of alcohol '
                            'dehydrogenase from unicellular green alga '
                            'Chlamydomonas moewusii. Phytochemistry (1983) 22, '
                            '1695-1699.'},
               70: {'info': 'Ammendola, S.; Raia, C.A.; Caruso, C.; '
                            "Camardella, L.; D'Auria, S.; De Rosa, M.; Rossi, "
                            'M.: Thermostable NAD(+)-dependent alcohol '
                            'dehydrogenase from Sulfolobus solfataricus: gene '
                            'and protein sequence determination and '
                            'relationship to other alcohol dehydrogenases. '
                            'Biochemistry (1992) 31, 12514-12523.',
                    'pubmed': 1463738},
               71: {'info': 'Tihanyi, K.; Talbot, B.; Brzezinski, R.; Thirion, '
                            'J.P.: Purification and characterization of '
                            'alcohol dehydrogenase from soybean. '
                            'Phytochemistry (1989) 28, 1335-1338.'},
               72: {'info': 'Liang, Z.Q.; Hayase, F.; Nishimura, T.; Kato, H.: '
                            'Purification and characterization of '
                            'NAD-dependent alcohol dehydrogenase and '
                            'NADH-dependent 2-oxoaldehyde reductase from '
                            'parsley. Agric. Biol. Chem. (1990) 54, '
                            '1717-1719.'},
               73: {'info': 'Hatanaka, A.; Harada, T.: Purification and '
                            'properties of alcohol dehydrogenase from tea '
                            'seeds. Agric. Biol. Chem. (1972) 36, 2033-2035.'},
               74: {'info': 'Stiborova, M.; Leblova, S.: Kinetics of the '
                            'reaction catalysed by rape alcohol dehydrogenase. '
                            'Phytochemistry (1979) 18, 23-24.'},
               75: {'info': 'Lai, Y.K.; Chandlee, J.M.; Scandalios, J.G.: '
                            'Purification and characterization of three '
                            'non-allelic alcohol dehydrogenase isoenzymes in '
                            'maize. Biochim. Biophys. Acta (1982) 706, 9-18.'},
               76: {'info': 'Leblova, S.; Ehlichova, D.: Purification and some '
                            'properties of alcohol dehydrogenase from maize. '
                            'Phytochemistry (1972) 11, 1345-1346.'},
               77: {'info': 'Langston, P.J.; Pace, C.N.; Hart, G.E.: Wheat '
                            'alcohol dehydrogenase iszymes. Purification, '
                            'characterization, and gene expression. Plant '
                            'Physiol. (1980) 65, 518-522.',
                    'pubmed': 16661226},
               78: {'info': 'Langston, P.J.; Hart, G.E.; Pace, C.N.: '
                            'Purification and partial characterization of '
                            'alcohol dehydrogenase from wheat. Arch. Biochem. '
                            'Biophys. (1979) 196, 611-618.',
                    'pubmed': 485168},
               79: {'info': 'Mayne, M.G.; Lea, P.J.: Properties of three sets '
                            'of isoenzymes of alcohol dehydrogenase isolated '
                            'from barley (Hordeum vulgare). Phytochemistry '
                            '(1985) 24, 1433-1438.'},
               80: {'info': 'Shimomura, S.; Beevers, H.: Alcohol dehydrogenase '
                            'inactivator from rice seedlings. Properties and '
                            'intracellular location. Plant Physiol. (1983) 71, '
                            '742-746.',
                    'pubmed': 16662899},
               81: {'info': 'Creaser, E.H.; Porter, R.L.; Britt, K.A.; '
                            'Pateman, J.A.; Doy, C.H.: Purification and '
                            'preliminary characterization of alcohol '
                            'dehydrogenase from Aspergillus nidulans. Biochem. '
                            'J. (1985) 225, 449-454.',
                    'pubmed': 3156582},
               82: {'info': 'Yabe, M.; Shitara, K.; Kawashima, J.; Shinoyama, '
                            'H.; Ando, A.; Fujii, T.: Purification and '
                            'properties of an alcohol dehydrogenase isozyme '
                            'from a methanol-using yeast, Candida sp. N-16. '
                            'Biosci. Biotechnol. Biochem. (1992) 56, 338-339.'},
               83: {'info': 'Morosoli, R.; Begin-Heick, N.: The partial '
                            'purification and characterization of cytosol '
                            'alcohol dehydrogenase from Astasia. Biochem. J. '
                            '(1974) 141, 469-475.',
                    'pubmed': 4455216},
               84: {'info': 'Rudge, J.; Bickerstaff, G.F.: Purification and '
                            'properties of an alcohol dehydrogenase from '
                            'Sporotrichum pulverulentum. Enzyme Microb. '
                            'Technol. (1986) 8, 120-124.'},
               85: {'info': 'Indrati, R.; Ohita, Y.: Purification and '
                            'properties of alcohol dehydrogenase from a mutant '
                            'strain of Candida guilliermondii. Can. J. '
                            'Microbiol. (1992) 38, 953-957.'},
               86: {'info': 'Tkachenko, A.G.; Winston, G.W.: Interaction of '
                            'alcohol dehydrogenase with '
                            'tert-butylhydroperoxide: stimulation of the horse '
                            'liver and inhibition of the yeast enzyme. Arch. '
                            'Biochem. Biophys. (2000) 380, 165-173.',
                    'pubmed': 10900146},
               87: {'info': 'Drewke, C.; Ciriacy, M.: Overexpression, '
                            'purification and properties of alcohol '
                            'dehydrogenase IV from Saccharomyces cerevisiae. '
                            'Biochim. Biophys. Acta (1988) 950, 54-60.',
                    'pubmed': 3282541},
               88: {'info': 'Yamazaki, Y.; Maeda, H.; Satoh, A.; Hiromi, K.: A '
                            'kinetic study on the binding of monomeric and '
                            'polymeric derivatives of NAD+ to yeast alcohol '
                            'dehydrogenase. J. Biochem. (1984) 95, 109-115.',
                    'pubmed': 6368531},
               89: {'info': 'Mazid, M.A.; Laidler, K.J.: pH Dependence of free '
                            'and immobilized yeast alcohol dehydrogenase '
                            'kinetics. Can. J. Microbiol. (1982) 60, 100-107.',
                    'pubmed': 7044497},
               90: {'info': 'Dickinson, F.M.; Monger, G.P.: A study of the '
                            'kinetics and mechanism of yeast alcohol '
                            'dehydrogenase with a variety of substrates. '
                            'Biochem. J. (1973) 131, 261-270.',
                    'pubmed': 4352908},
               91: {'info': 'Ganzhorn, A.J.; Green, D.W.; Hershey, A.D.; '
                            'Gould, R.M.; Plapp, B.V.: Kinetic '
                            'characterization of yeast alcohol dehydrogenases. '
                            'Amino acid residue 294 and substrate specificity. '
                            'J. Biol. Chem. (1987) 262, 3754-3761.',
                    'pubmed': 3546317},
               92: {'info': 'Weinhold, E.G.; Benner, S.A.: Engineering yeast '
                            'alcohol dehydrogenase. Replacing Trp54 by Leu '
                            'broadens substrate specificity. Protein Eng. '
                            '(1995) 8, 457-461.',
                    'pubmed': 8532667},
               93: {'info': 'Pocker, Y.; Li, H.: Mechanistic enzymology of '
                            'liver alcohol dehydrogenase. Kinetic and '
                            'stereochemical characterization of retinal '
                            'oxidation and reduction. Adv. Exp.Med. Biol. '
                            '(1996) 6, 331-338.',
                    'pubmed': 9059637},
               94: {'info': 'Leskovac, V.; Trivic, S.; Anderson, B.M.: Use of '
                            'competitive dead-end inhibitors to determine the '
                            'chemical mechanism of action of yeast alcohol '
                            'dehydrogenase. Mol. Cell. Biochem. (1998) 178, '
                            '219-227.',
                    'pubmed': 9546603},
               95: {'info': 'Keung, W.M.: Isolation and characterization of '
                            'three alcohol dehydrogenase isozymes from Syrian '
                            'golden hamster. Alcohol. Clin. Exp. Res. (1996) '
                            '20, 213-220.',
                    'pubmed': 8730210},
               96: {'info': 'Yin, S.J.; Wang, M.F.; Liao, C.S.; Chen, C.M.; '
                            'Wu, C.W.: Identification of a human stomach '
                            'alcohol dehydrogenase with distinctive kinetic '
                            'properties. Biochem. Int. (1990) 22, 829-835.',
                    'pubmed': 2099148},
               97: {'info': 'Osterman, J.C.; Chiang, Y.; Markwell, J.: '
                            'Characterization of mutation-induced changes in '
                            'the maize (Zea mays L.) ADH1-1S1108 alcohol '
                            'dehydrogenase. Biochem. Genet. (1993) 31, '
                            '497-506.',
                    'pubmed': 8166623},
               98: {'info': 'Langeland, B.T.; Morris, D.L.; McKinley-McKee, '
                            'J.S.: Metal binding properties of thiols: '
                            'complexes with horse liver alcohol dehydrogenase. '
                            'Comp. Biochem. Physiol. B (1999) 123, 155-162.',
                    'pubmed': 10425719},
               99: {'info': 'Hensgens, C.M.H.; Vonck, J.; van Beeumen, J.; '
                            'Bruggen, E.F.J.; Hansen, T.A.: Purification and '
                            'characterization of an oxygen-labile, '
                            'NAD-dependent alcohol dehydrogenase from '
                            'Desulfovibrio gigas. J. Bacteriol. (1993) 175, '
                            '2859-2863.',
                    'pubmed': 8491707},
               100: {'info': 'Flores, B.M.; Stanley, S.L.; Yong, T.S.; Ali, '
                             'M.; Yang, W.; Diedrich, D.L.; Torian, B.E.: '
                             'Surface localization, regulation, and biologic '
                             'properties of the 96-kDA alcohol/aldehyde '
                             'dehydrogenase (EhADH2) of pathogenic Entamoeba '
                             'histolytica. J. Infect. Dis. (1996) 173, '
                             '226-231.',
                     'pubmed': 8537663},
               101: {'info': 'Persson, B.; Bergman, T.; Keung, W.M.; '
                             'Waldenstroem, U.; Holmquist, B.; Vallee, B.L.; '
                             'Joernvall, H.: Basic features of class-I alcohol '
                             'dehydrogenase variable and constant segments '
                             'coordinated by inter-class and intra-class '
                             'variabvility. Conclusions from characterization '
                             'of the alligator enzyme. Eur. J. Biochem. (1993) '
                             '216, 49-56.',
                     'pubmed': 8365416},
               102: {'info': 'Gergel, D.; Cederbaum, A.I.: Inhibition of the '
                             'catalytic activity of alcohol dehydrogenase by '
                             'nitric oxide is associated with S nitrosylation '
                             'and the release of zinc. Biochemistry (1996) 35, '
                             '16186-16194.',
                     'pubmed': 8973191},
               103: {'info': 'Lamed, R.; Zeikus, J.G.: Ethanol production by '
                             'thermophilic bacteria: relationship between '
                             'fermentation product yields of and catabolic '
                             'enzyme activities in Clostridium thermocellum '
                             'and Thermoanaerobium brockii. J. Bacteriol. '
                             '(1980) 144, 569-578.',
                     'pubmed': 7430065},
               105: {'info': 'Hadizadeh, M.; Keyhani, E.: Detection and '
                             'kinetic properties of alcohol dehydrogenase in '
                             'dormant corm of Crocus sativus L. Acta Hortic. '
                             '(2004) 650, 127-139.'},
               108: {'info': 'Esposito, L.; Bruno, I.; Sica, F.; Raia, C.A.; '
                             'Giordano, A.; Rossi, M.; Mazzarella, L.; Zagari, '
                             'A.: Crystal structure of a ternary complex of '
                             'the alcohol dehydrogenase from Sulfolobus '
                             'solfataricus. Biochemistry (2003) 42, '
                             '14397-14407.',
                     'pubmed': 14661950},
               110: {'info': 'Stroemberg, P.; Svensson, S.; Berst, K.B.; '
                             'Plapp, B.V.; Höög, J.O.: Enzymatic mechanism of '
                             'low-activity mouse alcohol dehydrogenase 2. '
                             'Biochemistry (2004) 43, 1323-1328.',
                     'pubmed': 14756569},
               111: {'info': 'LeBrun, L.A.; Park, D.H.; Ramaswamy, S.; Plapp, '
                             'B.V.: Participation of histidine-51 in catalysis '
                             'by horse liver alcohol dehydrogenase. '
                             'Biochemistry (2004) 43, 3014-3026.',
                     'pubmed': 15023053},
               112: {'info': 'Ceccarelli, C.; Liang, Z.X.; Strickler, M.; '
                             'Prehna, G.; Goldstein, B.M.; Klinman, J.P.; '
                             'Bahnson, B.J.: Crystal structure and amide H/D '
                             'exchange of binary complexes of alcohol '
                             'dehydrogenase from Bacillus stearothermophilus: '
                             'insight into thermostability and cofactor '
                             'binding. Biochemistry (2004) 43, 5266-5277.',
                     'pubmed': 15122892},
               113: {'info': 'Chinnawirotpisan, P.; Matsushita, K.; Toyama, '
                             'H.; Adachi, O.; Limtong, S.; Theeragool, G.: '
                             'Purification and characterization of two '
                             'NAD-dependent alcohol dehydrogenases (ADHs) '
                             'induced in the quinoprotein ADH-deficient mutant '
                             'of Acetobacter pasteurianus SKU1108. Biosci. '
                             'Biotechnol. Biochem. (2003) 67, 958-965.',
                     'pubmed': 12834271},
               114: {'info': 'Kosjek, B.; Stampfer, W.; Pogorevc, M.; '
                             'Goessler, W.; Faber, K.; Kroutil, W.: '
                             'Purification and characterization of a '
                             'chemotolerant alcohol dehydrogenase applicable '
                             'to coupled redox reactions. Biotechnol. Bioeng. '
                             '(2004) 86, 55-62.',
                     'pubmed': 15007841},
               115: {'info': 'Stroemberg, P.; Svensson, S.; Hedberg, J.J.; '
                             'Nordling, E.; Hoog, J.O.: Identification and '
                             'characterisation of two allelic forms of human '
                             'alcohol dehydrogenase 2. Cell. Mol. Life Sci. '
                             '(2002) 59, 552-559.',
                     'pubmed': 11964133},
               116: {'info': 'Plapp, B.V.; Berst, K.B.: Specificity of human '
                             'alcohol dehydrogenase 1C*2 (gamma2gamma2) for '
                             'steroids and simulation of the uncompetitive '
                             'inhibition of ethanol metabolism. Chem. Biol. '
                             'Interact. (2003) 143-144, 183-193.',
                     'pubmed': 12604203},
               117: {'info': 'Fontaine, F.R.; Dunlop, R.A.; Petersen, D.R.; '
                             'Burcham, P.C.: Oxidative bioactivation of crotyl '
                             'alcohol to the toxic endogenous aldehyde '
                             'crotonaldehyde: association of protein '
                             'carbonylation with toxicity in mouse '
                             'hepatocytes. Chem. Res. Toxicol. (2002) 15, '
                             '1051-1058.',
                     'pubmed': 12184789},
               118: {'info': 'Yoon, S.Y.; Noh, H.S.; Kim, E.H.; Kong, K.H.: '
                             'The highly stable alcohol dehydrogenase of '
                             'Thermomicrobium roseum: purification and '
                             'molecular characterization. Comp. Biochem. '
                             'Physiol. B (2002) 132, 415-422.',
                     'pubmed': 12031468},
               120: {'info': 'Leskovac, V.; Trivic, S.; Pericin, D.: The three '
                             'zinc-containing alcohol dehydrogenases from '
                             "bakers' yeast, Saccharomyces cerevisiae. FEMS "
                             'Yeast Res. (2002) 2, 481-494.',
                     'pubmed': 12702265},
               121: {'info': 'Miroliaei, M.; Nemat-Gorgani, M.: Effect of '
                             'organic solvents on stability and activity of '
                             'two related alcohol dehydrogenases: a '
                             'comparative study. Int. J. Biochem. Cell Biol. '
                             '(2002) 34, 169-175.',
                     'pubmed': 11809419},
               123: {'info': 'Espinosa, A.; Clark, D.; Stanley, S.L., Jr.: '
                             'Entamoeba histolytica alcohol dehydrogenase 2 '
                             '(EhADH2) as a target for anti-amoebic agents. J. '
                             'Antimicrob. Chemother. (2004) 54, 56-59.',
                     'pubmed': 15150165},
               124: {'info': 'Chou, C.F.; Lai, C.L.; Chang, Y.C.; Duester, G.; '
                             'Yin, S.J.: Kinetic mechanism of human class IV '
                             'alcohol dehydrogenase functioning as retinol '
                             'dehydrogenase. J. Biol. Chem. (2002) 277, '
                             '25209-25216.',
                     'pubmed': 11997393},
               125: {'info': 'Rosell, A.; Valencia, E.; Ochoa, W.F.; Fita, I.; '
                             'Pares, X.; Farres, J.: Complete reversal of '
                             'coenzyme specificity by concerted mutation of '
                             'three consecutive residues in alcohol '
                             'dehydrogenase. J. Biol. Chem. (2003) 278, '
                             '40573-40580.',
                     'pubmed': 12902331},
               126: {'info': 'Shim, E.J.; Jeon, S.H.; Kong, K.H.: '
                             'Overexpression, purification, and biochemical '
                             'characterization of the thermostable '
                             'NAD-dependent alcohol dehydrogenase from '
                             'Bacillus stearothermophilus. J. Microbiol. '
                             'Biotechnol. (2003) 13, 738-744.'},
               127: {'info': 'Guy, J.E.; Isupov, M.N.; Littlechild, J.A.: The '
                             'structure of an alcohol dehydrogenase from the '
                             'hyperthermophilic archaeon Aeropyrum pernix. J. '
                             'Mol. Biol. (2003) 331, 1041-1051.',
                     'pubmed': 12927540},
               128: {'info': 'Avila, E.E.; Martinez-Alcaraz, E.R.; '
                             'Barbosa-Sabanero, G.; Rivera-Baron, E.I.; '
                             'Arias-Negrete, S.; Zazueta-Sandoval, R.: '
                             'Subcellular localization of the NAD+-dependent '
                             'alcohol dehydrogenase in Entamoeba histolytica '
                             'trophozoites. J. Parasitol. (2002) 88, 217-222.',
                     'pubmed': 12058720},
               129: {'info': 'Levin, I.; Meiri, G.; Peretz, M.; Burstein, Y.; '
                             'Frolow, F.: The ternary complex of Pseudomonas '
                             'aeruginosa alcohol dehydrogenase with NADH and '
                             'ethylene glycol. Protein Sci. (2004) 13, '
                             '1547-1556.',
                     'pubmed': 15152088},
               130: {'info': 'Koumanov, A.; Benach, J.; Atrian, S.; '
                             'Gonzalez-Duarte, R.; Karshikoff, A.; Ladenstein, '
                             'R.: The catalytic mechanism of Drosophila '
                             'alcohol dehydrogenase: evidence for a proton '
                             'relay modulated by the coupled ionization of the '
                             'active site lysine/tyrosine pair and a NAD+ '
                             'ribose OH switch. Proteins (2003) 51, 289-298.',
                     'pubmed': 12660997},
               135: {'info': 'Nosova, T.; Jousimies-Somer, H.; Kaihovaara, P.; '
                             'Jokelainen, K.; Heine, R.; Salaspuro, M.: '
                             'Characteristics of alcohol dehydrogenases of '
                             'certain aerobic bacteria representing human '
                             'colonic flora. Alcohol. Clin. Exp. Res. (1997) '
                             '21, 489-494.',
                     'pubmed': 9161610},
               136: {'info': 'Duron-Castellanos, A.; Zazueta-Novoa, V.; '
                             'Silva-Jimenez, H.; Alvarado-Caudillo, Y.; Pena '
                             'Cabrera, E.; Zazueta-Sandoval, R.: Detection of '
                             'NAD+dependent alcohol dehydrogenase activities '
                             'in YR-1 strain of Mucor circinelloides, a '
                             'potential bioremediator of petroleum '
                             'contaminated soils. Appl. Biochem. Biotechnol. '
                             '(2005) 121-124, 279-288.',
                     'pubmed': 15917606},
               137: {'info': 'Inoue, K.; Makino, Y.; Itoh, N.: Purification '
                             'and characterization of a novel alcohol '
                             'dehydrogenase from Leifsonia sp. strain S749: a '
                             'promising biocatalyst for an asymmetric hydrogen '
                             'transfer bioreduction. Appl. Environ. Microbiol. '
                             '(2005) 71, 3633-3641.',
                     'pubmed': 16000771},
               138: {'info': 'Machielsen, R.; Uria, A.R.; Kengen, S.W.; van '
                             'der Oost, J.: Production and characterization of '
                             'a thermostable alcohol dehydrogenase that '
                             'belongs to the aldo-keto reductase uperfamily. '
                             'Appl. Environ. Microbiol. (2006) 72, 233-238.',
                     'pubmed': 16391048},
               139: {'info': 'Park, H.; Kidman, G.; Northrop, D.B.: Effects of '
                             'pressure on deuterium isotope effects of yeast '
                             'alcohol dehydrogenase using alternative '
                             'substrates. Arch. Biochem. Biophys. (2005) 433, '
                             '335-340.',
                     'pubmed': 15581588},
               140: {'info': 'Kalnenieks, U.; Galinina, N.; Toma, M.M.: '
                             'Physiological regulation of the properties of '
                             'alcohol dehydrogenase II (ADH II) of Zymomonas '
                             'mobilis: NADH renders ADH II resistant to '
                             'cyanide and aeration. Arch. Microbiol. (2005) '
                             '183, 450-455.',
                     'pubmed': 16027951},
               141: {'info': 'Haseba, T.; Duester, G.; Shimizu, A.; Yamamoto, '
                             'I.; Kameyama, K.; Ohno, Y.: In vivo contribution '
                             'of class III alcohol dehydrogenase (ADH3) to '
                             'alcohol metabolism through activation by '
                             'cytoplasmic solution hydrophobicity. Biochim. '
                             'Biophys. Acta (2006) 1762, 276-283.',
                     'pubmed': 16431092},
               143: {'info': 'Negoro, M.; Wakabayashi, I.: Enhancement of '
                             'alcohol dehydrogenase activity in vitro by '
                             'acetylsalicylic acid. Eur. J. Pharmacol. (2005) '
                             '523, 25-28.',
                     'pubmed': 16226743},
               144: {'info': 'Kazuoka, T.; Oikawa, T.; Muraoka, I.; Kuroda, '
                             'S.; Soda, K.: A cold-active and thermostable '
                             'alcohol dehydrogenase of a psychrotorelant from '
                             'Antarctic seawater, Flavobacterium frigidimaris '
                             'KUC-1. Extremophiles (2007) 11, 257-267.',
                     'pubmed': 17072683},
               146: {'info': 'Defilippi, B.G.; Dandekar, A.M.; Kader, A.A.: '
                             'Relationship of ethylene biosynthesis to '
                             'volatile production, related enzymes, and '
                             'precursor availability in apple peel and flesh '
                             'tissues. J. Agric. Food Chem. (2005) 53, '
                             '3133-3141.',
                     'pubmed': 15826070},
               147: {'info': 'Koutsompogeras, P.; Kyriacou, A.; Zabetakis, I.: '
                             'Characterizing NAD-dependent alcohol '
                             'dehydrogenase enzymes of Methylobacterium '
                             'extorquens and strawberry (Fragaria x ananassa '
                             'cv. Elsanta). J. Agric. Food Chem. (2006) 54, '
                             '235-242.',
                     'pubmed': 16390205},
               148: {'info': 'Ikegaya, K.: Kinetic analysis about the effects '
                             'of neutral salts on the thermal stability of '
                             'yeast alcohol dehydrogenase. J. Biochem. (2005) '
                             '137, 349-354.',
                     'pubmed': 15809336},
               149: {'info': 'Hirano, J.; Miyamoto, K.; Ohta, H.: Purification '
                             'and characterization of the alcohol '
                             'dehydrogenase with a broad substrate specificity '
                             'originated from 2-phenylethanol-assimilating '
                             'Brevibacterium sp. KU 1309. J. Biosci. Bioeng. '
                             '(2005) 100, 318-322.',
                     'pubmed': 16243283},
               151: {'info': 'Manriquez, D.; El-Sharkawy, I.; Flores, F.B.; '
                             'El-Yahyaoui, F.; Regad, F.; Bouzayen, M.; '
                             'Latche, A.; Pech, J.C.: Two highly divergent '
                             'alcohol dehydrogenases of melon exhibit fruit '
                             'ripening-specific expression and distinct '
                             'biochemical characteristics. Plant Mol. Biol. '
                             '(2006) 61, 675-685.',
                     'pubmed': 16897483},
               152: {'info': 'Sica, F.; Demasi, D.; Mazzarella, D.L.; Zagari, '
                             "A.; Capasso, S.; Pearl, L.H.; D'Auria, S.; Raia, "
                             'C.A.; Rossi, M.: Elimination of twinning in '
                             'crystals of Sulfolobus sofataricus alcohol '
                             'dehydrogenase holo-enzyme by growth in agarose '
                             'gels. Acta Crystallogr. Sect. D (1994) 50, '
                             '508-511.',
                     'pubmed': 15299411},
               153: {'info': 'Raia, C.A.; Caruso, C.; Marino, M.; Vespa, N.; '
                             'Rossi, M.: Activation of Sulfolobus solfataricus '
                             'alcohol dehydrogenase by modification of '
                             'cysteine residue 38 with iodoacetic acid. '
                             'Biochemistry (1996) 35, 638-647.',
                     'pubmed': 8555238},
               154: {'info': 'Giordano, A.; Cannio, R.; La Cara, F.; '
                             'Bartolucci, S.; Rossi, M.; Raia, C.A.: Asn249Tyr '
                             'substitution at the coenzyme binding domain '
                             'activates Sulfolobus solfataricus alcohol '
                             'dehydrogenase and increases its thermal '
                             'stability.. Biochemistry (1999) 38, 3043-3054.',
                     'pubmed': 10074357},
               156: {'info': 'Tasaki, Y.; Yoshikawa, H.; Tamura, H.: Isolation '
                             'and characterization of an alcohol dehydrogenase '
                             'gene from the octylphenol polyethoxylate '
                             'degrader Pseudomonas putida S-5. Biosci. '
                             'Biotechnol. Biochem. (2006) 70, 1855-1863.',
                     'pubmed': 16926497},
               157: {'info': 'Esposito, L.; Bruno, I.; Sica, F.; Raia, C.A.; '
                             'Giordano, A.; Rossi, M.; Mazzarella, L.; Zagari, '
                             'A.: Structural study of a single-point mutant of '
                             'Sulfolobus solfataricus alcohol dehydrogenase '
                             'with enhanced activity.. FEBS Lett. (2003) 539, '
                             '14-18.',
                     'pubmed': 12650918},
               158: {'info': 'Cannio, R.; Fiorentino, G.; Rossi, M.; '
                             'Bartolucci, S.: The alcohol dehydrogenase gene: '
                             'distribution among Sulfolobales and regulation '
                             'in Sulfolobus solfataricus. FEMS Microbiol. '
                             'Lett. (1999) 170, 31-39.',
                     'pubmed': 9919650},
               159: {'info': 'Cannio, R.; Fiorentino, G.; Carpinelli, P.; '
                             'Rossi, M.; Bartolucci, S.: Cloning and '
                             'overexpression in Escherichia coli of the genes '
                             'encoding NAD-dependent alcohol dehydrogenase '
                             'from two Sulfolobus species. J. Bacteriol. '
                             '(1996) 178, 301-305.',
                     'pubmed': 8550434},
               161: {'info': 'Esposito, L.; Sica, F.; Raia, C.A.; Giordano, '
                             'A.; Rossi, M.; Mazzarella, L.; Zagari, A.: '
                             'Crystal structure of the alcohol dehydrogenase '
                             'from the hyperthermophilic archaeon Sulfolobus '
                             'solfataricus at 1.85 A resolution. J. Mol. Biol. '
                             '(2002) 318, 463-477.',
                     'pubmed': 12051852},
               162: {'info': 'Chong, P.K.; Burja, A.M.; Radianingtyas, H.; '
                             'Fazeli, A.; Wright, P.C.: Proteome and '
                             'transcriptional analysis of ethanol-grown '
                             'Sulfolobus solfataricus P2 reveals ADH2, a '
                             'potential alcohol dehydrogenase. J. Proteome '
                             'Res. (2007) 6, 3985-3994.',
                     'pubmed': 17824633},
               163: {'info': 'Raia, C.A.; Giordano, A.; Rossi, M.: Alcohol '
                             'dehydrogenase from Sulfolobus solfataricus. '
                             'Methods Enzymol. (2001) 331, 176-195.',
                     'pubmed': 11265460},
               164: {'info': 'Casadio, R.; Martelli, P.L.; Giordano, A.; '
                             'Rossi, M.; Raia, C.A.: A low-resolution 3D model '
                             'of the tetrameric alcohol dehydrogenase from '
                             'Sulfolobus solfataricus. Protein Eng. (2002) 15, '
                             '215-223.',
                     'pubmed': 11932492},
               165: {'info': 'Ammendola, S.; Raucci, G.; Incani, O.; Mele, A.; '
                             'Tramontano, A.; Wallace, A.: Replacing the '
                             'glutamate ligand in the structural zinc site of '
                             'Sulfolobus solfataricus alcohol dehydrogenase '
                             'with a cysteine decreases thermostability.. '
                             'Protein Eng. (1995) 8, 31-37.',
                     'pubmed': 7770449},
               167: {'info': 'Quintanilla, M.E.; Tampier, L.; Sapag, A.; '
                             'Gerdtzen, Z.; Israel, Y.: Sex differences, '
                             'alcohol dehydrogenase, acetaldehyde burst, and '
                             'aversion to ethanol in the rat: a systems '
                             'perspective. Am. J. Physiol. Endocrinol. Metab. '
                             '(2007) 293, E531-E537.',
                     'pubmed': 17488809},
               169: {'info': 'Pennacchio, A.; Pucci, B.; Secundo, F.; La Cara, '
                             'F.; Rossi, M.; Raia, C.A.: Purification and '
                             'characterization of a novel recombinant highly '
                             'enantioselective short-chain NAD(H)-dependent '
                             'alcohol dehydrogenase from Thermus thermophilus. '
                             'Appl. Environ. Microbiol. (2008) 74, 3949-3958.',
                     'pubmed': 18456852},
               170: {'info': 'Maestre, O.; Garcia-Martinez, T.; Peinado, R.A.; '
                             'Mauricio, J.C.: Effects of ADH2 overexpression '
                             'in Saccharomyces bayanus during alcoholic '
                             'fermentation. Appl. Environ. Microbiol. (2008) '
                             '74, 702-707.',
                     'pubmed': 18065623},
               171: {'info': 'Kotrbova-Kozak, A.; Kotrba, P.; Inui, M.; '
                             'Sajdok, J.; Yukawa, H.: Transcriptionally '
                             'regulated adhA gene encodes alcohol '
                             'dehydrogenase required for ethanol and '
                             'n-propanol utilization in Corynebacterium '
                             'glutamicum R. Appl. Microbiol. Biotechnol. '
                             '(2007) 76, 1347-1356.',
                     'pubmed': 17646983},
               172: {'info': 'Park, Y.C.; San, K.Y.; Bennett, G.N.: '
                             'Characterization of alcohol dehydrogenase 1 and '
                             '3 from Neurospora crassa FGSC2489. Appl. '
                             'Microbiol. Biotechnol. (2007) 76, 349-356.',
                     'pubmed': 17516063},
               173: {'info': 'Hess, M.; Antranikian, G.: Archaeal alcohol '
                             'dehydrogenase active at increased temperatures '
                             'and in the presence of organic solvents. Appl. '
                             'Microbiol. Biotechnol. (2008) 77, 1003-1013.',
                     'pubmed': 17989975},
               174: {'info': 'Crichton, P.G.; Affourtit, C.; Moore, A.L.: '
                             'Identification of a mitochondrial alcohol '
                             'dehydrogenase in Schizosaccharomyces pombe: new '
                             'insights into energy metabolism. Biochem. J. '
                             '(2007) 401, 459-464.',
                     'pubmed': 16999687},
               175: {'info': 'Meijers, R.; Adolph, H.W.; Dauter, Z.; Wilson, '
                             'K.S.; Lamzin, V.S.; Cedergren-Zeppezauer, E.S.: '
                             'Structural evidence for a ligand coordination '
                             'switch in liver alcohol dehydrogenase. '
                             'Biochemistry (2007) 46, 5446-5454.',
                     'pubmed': 17429946},
               177: {'info': 'Lertwattanasakul, N.; Sootsuwan, K.; Limtong, '
                             'S.; Thanonkeo, P.; Yamada, M.: Comparison of the '
                             'gene expression patterns of alcohol '
                             'dehydrogenase isozymes in the thermotolerant '
                             'yeast Kluyveromyces marxianus and their '
                             'physiological functions. Biosci. Biotechnol. '
                             'Biochem. (2007) 71, 1170-1182.',
                     'pubmed': 17485854},
               178: {'info': 'Barzegar, A.; Moosavi-Movahedi, A.A.; '
                             'Rezaei-Zarchi, S.; Saboury, A.A.; Ganjali, M.R.; '
                             'Norouzi, P.; Hakimelahi, G.H.; Tsai, F.Y.: The '
                             'mechanisms underlying the effect of '
                             'alpha-cyclodextrin on the aggregation and '
                             'stability of alcohol dehydrogenase. Biotechnol. '
                             'Appl. Biochem. (2008) 49, 203-211.',
                     'pubmed': 17685894},
               180: {'info': 'Jelski, W.; Zalewski, B.; Szmitkowski, M.: The '
                             'activity of class I, II, III, and IV alcohol '
                             'dehydrogenase (ADH) isoenzymes and aldehyde '
                             'dehydrogenase (ALDH) in liver cancer. Digest. '
                             'Dis. Sci. (2008) 53, 2550-2555.',
                     'pubmed': 18224440},
               181: {'info': 'Cao, Y.; Liao, L.; Xu, X.W.; Oren, A.; Wang, C.; '
                             'Zhu, X.F.; Wu, M.: Characterization of alcohol '
                             'dehydrogenase from the haloalkaliphilic archaeon '
                             'Natronomonas pharaonis. Extremophiles (2008) 12, '
                             '471-476.',
                     'pubmed': 18189118},
               185: {'info': 'Yamada-Onodera, K.; Fukui, M.; Tani, Y.: '
                             'Purification and characterization of alcohol '
                             'dehydrogenase reducing N-benzyl-3-pyrrolidinone '
                             'from Geotrichum capitatum. J. Biosci. Bioeng. '
                             '(2007) 103, 174-178.',
                     'pubmed': 17368401},
               186: {'info': 'Jelski, W.; Zalewski, B.; Szmitkowski, M.: '
                             'Alcohol dehydrogenase (ADH) isoenzymes and '
                             'aldehyde dehydrogenase (ALDH) activity in the '
                             'sera of patients with liver cancer. J. Clin. '
                             'Lab. Anal. (2008) 22, 204-209.',
                     'pubmed': 18484658},
               188: {'info': 'Kizaki, N.; Yasohara, Y.; Nagashima, N.; '
                             'Hasegawa, J.: Characterization of novel alcohol '
                             'dehydrogenase of Devosia riboflavina involved in '
                             'stereoselective reduction of 3-pyrrolidinone '
                             'derivatives. J. Mol. Catal. B (2008) 51, 73-80.'},
               194: {'info': 'Jelski, W.; Szmitkowski, M.: Alcohol '
                             'dehydrogenase (ADH) and aldehyde dehydrogenase '
                             '(ALDH) in the cancer diseases. Clin. Chim. Acta '
                             '(2008) 395, 1-5.',
                     'pubmed': 18505683},
               195: {'info': 'Peng, H.; Wu, G.; Shao, W.: The aldehyde/alcohol '
                             'dehydrogenase (AdhE) in relation to the ethanol '
                             'formation in Thermoanaerobacter ethanolicus '
                             'JW200. Anaerobe (2008) 14, 125-127.',
                     'pubmed': 17981479},
               196: {'info': 'Zhao, Q.; Hou, Y.; Gong, G.H.; Yu, M.A.; Jiang, '
                             'L.; Liao, F.: Characterization of alcohol '
                             'dehydrogenase from permeabilized brewers yeast '
                             'cells immobilized on the derived attapulgite '
                             'nanofibers. Appl. Biochem. Biotechnol. (2009) '
                             '160, 2287-2299.',
                     'pubmed': 19578994},
               197: {'info': 'Hoellrigl, V.; Hollmann, F.; Kleeb, A.C.; '
                             'Buehler, K.; Schmid, A.: TADH, the thermostable '
                             'alcohol dehydrogenase from Thermus sp. ATN1: a '
                             'versatile new biocatalyst for organic synthesis. '
                             'Appl. Microbiol. Biotechnol. (2008) 81, 263-273.',
                     'pubmed': 18704396},
               198: {'info': 'Plapp, B.V.: Conformational changes and '
                             'catalysis by alcohol dehydrogenase. Arch. '
                             'Biochem. Biophys. (2010) 493, 3-12.',
                     'pubmed': 19583966},
               200: {'info': 'Staab, C.A.; Hellgren, M.; Hoeoeg, J.O.: Medium- '
                             'and short-chain dehydrogenase/reductase gene and '
                             'protein families: Dual functions of alcohol '
                             'dehydrogenase 3: implications with focus on '
                             'formaldehyde dehydrogenase and '
                             'S-nitrosoglutathione reductase activities. Cell. '
                             'Mol. Life Sci. (2008) 65, 3950-3960.',
                     'pubmed': 19011746},
               201: {'info': 'Bergman, T.; Zhang, K.; Palmberg, C.; Joernvall, '
                             'H.; Auld, D.S.: Zinc binding to peptide analogs '
                             'of the structural zinc site in alcohol '
                             'dehydrogenase: implications for an entatic '
                             'state. Cell. Mol. Life Sci. (2008) 65, '
                             '4019-4027.',
                     'pubmed': 18850316},
               202: {'info': 'Pal, S.; Park, D.H.; Plapp, B.V.: Activity of '
                             'yeast alcohol dehydrogenases on benzyl alcohols '
                             'and benzaldehydes: characterization of ADH1 from '
                             'Saccharomyces carlsbergensis and transition '
                             'state analysis. Chem. Biol. Interact. (2009) '
                             '178, 16-23.',
                     'pubmed': 19022233},
               203: {'info': 'Miyawaki, O.; Ma, G.; Horie, T.; Hibi, A.; '
                             'Ishikawa, T.; Kimura, S.: Thermodynamic, '
                             'kinetic, and operational stabilities of yeast '
                             'alcohol dehydrogenase in sugar and compatible '
                             'osmolyte solutions. Enzyme Microb. Technol. '
                             '(2008) 43, 495-499.'},
               204: {'info': 'Cea, G.; Wilson, L.; Bolivar, J.; Markovits, A.; '
                             'Illanes, A.: Effect of chain length on the '
                             'activity of free and immobilized alcohol '
                             'dehydrogenase towards aliphatic alcohols. Enzyme '
                             'Microb. Technol. (2009) 44, 135-138.'},
               205: {'info': 'Barzegar, A.; Moosavi-Movahedi, A.; Pedersen, '
                             'J.; Miroliaei, M.: Comparative thermostability '
                             'of mesophilic and thermophilic alcohol '
                             'dehydrogenases: Stability-determining roles of '
                             'proline residues and loop conformations. Enzyme '
                             'Microb. Technol. (2009) 45, 73-79.'},
               206: {'info': 'Jelski, W.; Orywal, K.; Panek, B.; Gacko, M.; '
                             'Mroczko, B.; Szmitkowski, M.: The activity of '
                             'class I, II, III and IV of alcohol dehydrogenase '
                             '(ADH) isoenzymes and aldehyde dehydrogenase '
                             '(ALDH) in the wall of abdominal aortic '
                             'aneurysms. Exp. Mol. Pathol. (2009) 87, 59-62.',
                     'pubmed': 19332052},
               207: {'info': 'Pennacchio, A.; Esposito, L.; Zagari, A.; Rossi, '
                             'M.; Raia, C.A.: Role of Tryptophan 95 in '
                             'substrate specificity and structural stability '
                             'of Sulfolobus solfataricus alcohol '
                             'dehydrogenase. Extremophiles (2009) 13, 751-761.',
                     'pubmed': 19588068},
               208: {'info': 'Carvalho, E.; Solferini, V.; Matioli, S.: '
                             'Alcohol dehydrogenase activities and ethanol '
                             'tolerance in Anastrepha (Diptera, Tephritidae) '
                             'fruit-fly species and their hybrids. Genet. Mol. '
                             'Biol. (2009) 32, 177-185.',
                     'pubmed': 21637665},
               209: {'info': 'Devi, P.G.; Chakraborty, P.K.; Dasgupta, D.: '
                             'Inhibition of a Zn(II)-containing enzyme, '
                             'alcohol dehydrogenase, by anticancer '
                             'antibiotics, mithramycin and chromomycin A3. J. '
                             'Biol. Inorg. Chem. (2009) 14, 347-359.',
                     'pubmed': 19034537},
               210: {'info': 'Jeon, Y.J.; Fong, J.C.; Riyanti, E.I.; Neilan, '
                             'B.A.; Rogers, P.L.; Svenson, C.J.: Heterologous '
                             'expression of the alcohol dehydrogenase (adhI) '
                             'gene from Geobacillus thermoglucosidasius strain '
                             'M10EXG. J. Biotechnol. (2008) 135, 127-133.',
                     'pubmed': 18436321},
               211: {'info': 'Palma-Gutierrez, H.; Rodriguez-Zavala, J.; '
                             'Jasso-Chavez, R.; Moreno-Sanchez, R.; Saavedra, '
                             'E.: Gene cloning and biochemical '
                             'characterization of an alcohol dehydrogenase '
                             'from Euglena gracilis. J. Eukaryot. Microbiol. '
                             '(2008) 55, 554-561.',
                     'pubmed': 19120802},
               212: {'info': 'Haseba, T.; Sugimoto, J.; Sato, S.; Abe, Y.; '
                             'Ohno, Y.: Phytophenols in whisky lower blood '
                             'acetaldehyde level by depressing alcohol '
                             'metabolism through inhibition of alcohol '
                             'dehydrogenase 1 (class I) in mice. Metab. Clin. '
                             'Exp. (2008) 57, 1753-1759.',
                     'pubmed': 19013301},
               213: {'info': 'Marino-Marmolejo, E.N.; De Leon-Rodriguez, A.; '
                             'de la Rosa, A.P.; Santos, L.: Heterologous '
                             'expression and characterization of an alcohol '
                             'dehydrogenase from the archeon Thermoplasma '
                             'acidophilum. Mol. Biotechnol. (2009) 42, 61-67.',
                     'pubmed': 19058034},
               214: {'info': 'Kollock, R.; Frank, H.; Seidel, A.; Meinl, W.; '
                             'Glatt, H.: Oxidation of alcohols and reduction '
                             'of aldehydes derived from methyl- and '
                             'dimethylpyrenes by cDNA-expressed human alcohol '
                             'dehydrogenases. Toxicology (2008) 245, 65-75.',
                     'pubmed': 18242813},
               215: {'info': 'Liu, X.; Dong, Y.; Zhang, J.; Zhang, A.; Wang, '
                             'L.; Feng, L.: Two novel metal-independent '
                             'long-chain alkyl alcohol dehydrogenases from '
                             'Geobacillus thermodenitrificans NG80-2. '
                             'Microbiology (2009) 155, 2078-2085.',
                     'pubmed': 19383697},
               217: {'info': 'Yanai, H.; Doi, K.; Ohshima, T.: Sulfolobus '
                             'tokodaii ST0053 produces a novel thermostable, '
                             'NAD-dependent medium-chain alcohol '
                             'dehydrogenase. Appl. Environ. Microbiol. (2009) '
                             '75, 1758-1763.',
                     'pubmed': 19139244},
               218: {'info': 'Pennacchio, A.; Sannino, V.; Sorrentino, G.; '
                             'Rossi, M.; Raia, C.A.; Esposito, L.: Biochemical '
                             'and structural characterization of recombinant '
                             'short-chain NAD(H)-dependent '
                             'dehydrogenase/reductase from Sulfolobus '
                             'acidocaldarius highly enantioselective on diaryl '
                             'diketone benzil. Appl. Microbiol. Biotechnol. '
                             '(2013) 97, 3949-3964.',
                     'pubmed': 22805786},
               219: {'info': 'Pennacchio, A.; Giordano, A.; Pucci, B.; Rossi, '
                             'M.; Raia, C.A.: Biochemical characterization of '
                             'a recombinant short-chain NAD(H)-dependent '
                             'dehydrogenase/reductase from Sulfolobus '
                             'acidocaldarius. Extremophiles (2010) 14, '
                             '193-204.',
                     'pubmed': 20049620},
               220: {'info': 'Giordano, A.; Raia, C.A.: Steady-state '
                             'fluorescence properties of S. solfataricus '
                             'alcohol dehydrogenase and its selenomethionyl '
                             'derivative. J. Fluoresc. (2003) 13, 17-24.'},
               221: {'info': 'Giordano, A.; Russo, C.; Raia, C.A.; Kuznetsova, '
                             'I.M.; Stepanenko, O.V.; Turoverov, K.K.: Highly '
                             'UV-absorbing complex in '
                             'selenomethionine-substituted alcohol '
                             'dehydrogenase from Sulfolobus solfataricus. J. '
                             'Proteome Res. (2004) 3, 613-620.',
                     'pubmed': 15253444},
               222: {'info': 'Suwannarangsee, S.; Kim, S.; Kim, O.C.; Oh, '
                             'D.B.; Seo, J.W.; Kim, C.H.; Rhee, S.K.; Kang, '
                             'H.A.; Chulalaksananukul, W.; Kwon, O.: '
                             'Characterization of alcohol dehydrogenase 3 of '
                             'the thermotolerant methylotrophic yeast '
                             'Hansenula polymorpha. Appl. Microbiol. '
                             'Biotechnol. (2012) 96, 697-709.',
                     'pubmed': 22249723},
               223: {'info': 'Elleuche, S.; Fodor, K.; Klippel, B.; von der '
                             'Heyde, A.; Wilmanns, M.; Antranikian, G.: '
                             'Structural and biochemical characterisation of a '
                             'NAD+-dependent alcohol dehydrogenase from '
                             'Oenococcus oeni as a new model molecule for '
                             'industrial biotechnology applications. Appl. '
                             'Microbiol. Biotechnol. (2013) 97, 8963-8975.',
                     'pubmed': 23385476},
               224: {'info': 'Muralidharan, F.N.; Muralidharan, V.B.: '
                             'Characterization of phytol-phytanate conversion '
                             'activity in rat liver. Biochim. Biophys. Acta '
                             '(1986) 883, 54-62.',
                     'pubmed': 3730426},
               225: {'info': 'Kawano, S.; Yano, M.; Hasegawa, J.; Yasohara, '
                             'Y.: Purification and characterization of an '
                             'NADH-dependent alcohol dehydrogenase from '
                             'Candida maris for the synthesis of optically '
                             'active 1-(pyridyl)ethanol derivatives. Biosci. '
                             'Biotechnol. Biochem. (2011) 75, 1055-1060.',
                     'pubmed': 21670533},
               226: {'info': 'Zhou, S.; Zhang, S.C.; Lai, D.Y.; Zhang, S.L.; '
                             'Chen, Z.M.: Biocatalytic characterization of a '
                             'short-chain alcohol dehydrogenase with broad '
                             'substrate specificity from thermophilic '
                             'Carboxydothermus hydrogenoformans. Biotechnol. '
                             'Lett. (2013) 35, 359-365.',
                     'pubmed': 23160740},
               227: {'info': 'Cederlund, E.; Hedlund, J.; Hjelmqvist, L.; '
                             'Jonsson, A.; Shafqat, J.; Norin, A.; Keung, '
                             'W.M.; Persson, B.; Joernvall, H.: '
                             'Characterization of new medium-chain alcohol '
                             'dehydrogenases adds resolution to duplications '
                             'of the class I/III and the sub-class I genes. '
                             'Chem. Biol. Interact. (2011) 191, 8-13.',
                     'pubmed': 21329683},
               229: {'info': 'Orywal, K.; Jelski, W.; Zdrodowski, M.; '
                             'Szmitkowski, M.: The activity of class I, II, '
                             'III and IV alcohol dehydrogenase isoenzymes and '
                             'aldehyde dehydrogenase in cervical cancer. Clin. '
                             'Biochem. (2011) 44, 1231-1234.',
                     'pubmed': 21784063},
               230: {'info': 'Kube, J.; Brokamp, C.; Machielsen, R.; van der '
                             'Oost, J.; Maerkl, H.: Influence of temperature '
                             'on the production of an archaeal thermoactive '
                             'alcohol dehydrogenase from Pyrococcus furiosus '
                             'with recombinant Escherichia coli. Extremophiles '
                             '(2006) 10, 221-227.',
                     'pubmed': 16463078},
               231: {'info': 'Wang, N.; Shi, H.; Yao, Q.; Zhou, Y.; Kang, L.; '
                             'Chen, H.; Chen, K.: Cloning, expression and '
                             'characterization of alcohol dehydrogenases in '
                             'the silkworm Bombyx mori. Genet. Mol. Biol. '
                             '(2011) 34, 240-243.',
                     'pubmed': 21734824},
               232: {'info': 'Giersberg, M.; Degelmann, A.; Bode, R.; Piontek, '
                             'M.; Kunze, G.: Production of a thermostable '
                             'alcohol dehydrogenase from Rhodococcus ruber in '
                             'three different yeast species using the '
                             'Xplor\x022 transformation/expression platform. '
                             'J. Ind. Microbiol. Biotechnol. (2012) 39, '
                             '1385-1396.',
                     'pubmed': 22584819},
               233: {'info': 'Komatsu, S.; Deschamps, T.; Thibaut, D.; Hiraga, '
                             'S.; Kato, M.; Chiba, M.; Hashiguchi, A.; Tougou, '
                             'M.; Shimamura, S.; Yasue, H.: Characterization '
                             'of a novel flooding stress-responsive alcohol '
                             'dehydrogenase expressed in soybean roots. Plant '
                             'Mol. Biol. (2011) 77, 309-322.',
                     'pubmed': 21811849},
               234: {'info': 'Pennacchio, A.; Rossi, M.; Raia, C.A.: Synthesis '
                             'of cinnamyl alcohol from cinnamaldehyde with '
                             'Bacillus stearothermophilus alcohol '
                             'dehydrogenase as the isolated enzyme and in '
                             'recombinant E. coli cells. Appl. Biochem. '
                             'Biotechnol. (2013) 170, 1482-1490.',
                     'pubmed': 23686507},
               237: {'info': 'Timpson, L.M.; Liliensiek, A.K.; Alsafadi, D.; '
                             'Cassidy, J.; Sharkeym M.A.; Liddell, S.; Allers, '
                             'T.; Paradisi, F.: A comparison of two novel '
                             'alcohol dehydrogenase enzymes (ADH1 and ADH2) '
                             'from the extreme halophile Haloferax volcanii. '
                             'Appl. Microbiol. Biotechnol. (2012) 97, 195-203.',
                     'pubmed': 22526808},
               239: {'info': 'Hirakawa, H.; Kamiya, N.; Kawarabayashi, Y.; '
                             'Nagamune, T.: Properties of an alcohol '
                             'dehydrogenase from the hyperthermophilic '
                             'archaeon Aeropyrum pernix K1. J. Biosci. Bioeng. '
                             '(2004) 97, 202-206.',
                     'pubmed': 16233615},
               240: {'info': 'Alsafadi, D.; Paradisi, F.: Covalent '
                             'immobilization of alcohol dehydrogenase (ADH2) '
                             'from Haloferax volcanii: how to maximize '
                             'activity and optimize performance of halophilic '
                             'enzymes. Mol. Biotechnol. (2014) 56, 240-247.',
                     'pubmed': 24062264},
               243: {'info': 'Wu, X.; Zhang, C.; Orita, I.; Imanaka, T.; '
                             'Fukui, T.; Xing, X.H.: Thermostable alcohol '
                             'dehydrogenase from Thermococcus kodakarensis '
                             'KOD1 for enantioselective bioconversion of '
                             'aromatic secondary alcohols. Appl. Environ. '
                             'Microbiol. (2013) 79, 2209-2217.',
                     'pubmed': 23354700},
               244: {'info': 'Ying, X.; Wang, Y.; Xiong, B.; Wu, T.; Xie, L.; '
                             'Yu, M.; Wang, Z.: Characterization of an '
                             'allylic/benzyl alcohol dehydrogenase from '
                             'Yokenella sp. strain WZY002, an organism '
                             'potentially useful for the synthesis of '
                             'alpha,beta-unsaturated alcohols from allylic '
                             'aldehydes and ketones. Appl. Environ. Microbiol. '
                             '(2014) 80, 2399-2409.',
                     'pubmed': 24509923},
               246: {'info': 'Kirmair, L.; Seiler, D.L.; Skerra, A.: Stability '
                             'engineering of the Geobacillus '
                             'stearothermophilus alcohol dehydrogenase and '
                             'application for the synthesis of a polyamide 12 '
                             'precursor. Appl. Microbiol. Biotechnol. (2015) '
                             '99, 10501-10513.',
                     'pubmed': 26329849},
               252: {'info': 'Liang, J.J.; Zhang, M.L.; Ding, M.; Mai, Z.M.; '
                             'Wu, S.X.; Du, Y.; Feng, J.X.: Alcohol '
                             'dehydrogenases from Kluyveromyces marxianus: '
                             'heterologous expression in Escherichia coli and '
                             'biochemical characterization. BMC Biotechnol. '
                             '(2014) 14, 45.',
                     'pubmed': 24885162},
               254: {'info': 'Kontani, A.; Masuda, M.; Matsumura, H.; '
                             'Nakamura, N.; Yohda, M.; Ohno, H.: A bioanode '
                             'using thermostable alcohol dehydrogenase for an '
                             'ethanol biofuel cell operating at high '
                             'temperatures. Electroanalysis (2014) 26, '
                             '682-686.'},
               255: {'info': 'Willies, S.; Isupov, M.; Littlechild, J.: '
                             'Thermophilic enzymes and their applications in '
                             'biocatalysis: a robust aldo-keto reductase. '
                             'Environ. Technol. (2010) 31, 1159-1167.',
                     'pubmed': 20718298},
               256: {'info': 'Guagliardi, A.; Martino, M.; Iaccarino, I.; De '
                             'Rosa, M.; Rossi, M.; Bartolucci, S.: '
                             'Purification and characterization of the alcohol '
                             'dehydrogenase from a novel strain of Bacillus '
                             'stearothermophilus growing at 70°C. Int. J. '
                             'Biochem. Cell Biol. (1996) 28, 239-246.',
                     'pubmed': 8729010},
               257: {'info': 'Meadows, C.W.; Tsang, J.E.; Klinman, J.P.: '
                             'Picosecond-resolved fluorescence studies of '
                             'substrate and cofactor-binding domain mutants in '
                             'a thermophilic alcohol dehydrogenase uncover an '
                             'extended network of communication. J. Am. Chem. '
                             'Soc. (2014) 136, 14821-14833.',
                     'pubmed': 25314615},
               260: {'info': 'Nagel, Z.D.; Cun, S.; Klinman, J.P.: '
                             'Identification of a long-range protein network '
                             'that modulates active site dynamics in '
                             'extremophilic alcohol dehydrogenases. J. Biol. '
                             'Chem. (2013) 288, 14087-14097.',
                     'pubmed': 23525111},
               263: {'info': 'Xiao, S.; Xu, J.; Chen, X.; Li, X.; Zhang, Y.; '
                             'Yuan, Z.: 3-Methyl-1-butanol biosynthesis in an '
                             'engineered Corynebacterium glutamicum. Mol. '
                             'Biotechnol. (2016) 58, 311-318.',
                     'pubmed': 26961908},
               269: {'info': 'Pennacchio, A.; Giordano, A.; Esposito, L.; '
                             'Langella, E.; Rossi, M.; Raia, C.A.: Insight '
                             'into the stereospecificity of short-chain '
                             'thermus thermophilus alcohol dehydrogenase '
                             'showing pro-S hydride transfer and prelog '
                             'enantioselectivity. Protein Pept. Lett. (2010) '
                             '17, 437-443.',
                     'pubmed': 19807673},
               271: {'info': 'Takeda, M.; Anamizu, S.; Motomatsu, S.; Chen, '
                             'X.; Thapa Chhetri, R.: Identification and '
                             'characterization of a mycobacterial '
                             'NAD+-dependent alcohol dehydrogenase with '
                             'superior reduction of diacetyl to (S)-acetoin. '
                             'Biosci. Biotechnol. Biochem. (2014) 78, '
                             '1879-1886.',
                     'pubmed': 25082080},
               272: {'info': 'Hong, S.H.; Ngo, H.P.; Kang, L.W.; Oh, D.K.: '
                             'Characterization of alcohol dehydrogenase from '
                             'Kangiella koreensis and its application to '
                             'production of all-trans-retinol. Biotechnol. '
                             'Lett. (2015) 37, 849-856.',
                     'pubmed': 25481533},
               274: {'info': 'Spickermann, D.; Hausmann, S.; Degering, C.; '
                             'Schwaneberg, U.; Leggewie, C.: Engineering of '
                             'highly selective variants of Parvibaculum '
                             'lavamentivorans alcohol dehydrogenase. '
                             'ChemBioChem (2014) 15, 2050-2052.',
                     'pubmed': 25169816},
               275: {'info': 'Malver, O.; Sebastian, M.J.; Oppenheimer, N.J.: '
                             'Alteration in substrate specificity of horse '
                             'liver alcohol dehydrogenase by an acyclic '
                             'nicotinamide analog of NAD(+). DNA Repair (2014) '
                             '23, 95-100.',
                     'pubmed': 25280628},
               277: {'info': 'Moosavi-Movahedi, F.; Saboury, A.A.; Alijanvand, '
                             'H.H.; Bohlooli, M.; Salami, M.; '
                             'Moosavi-Movahedi, A.A.: Thermal inactivation and '
                             'conformational lock studies on horse liver '
                             'alcohol dehydrogenase: structural mechanism. '
                             'Int. J. Biol. Macromol. (2013) 58, 66-72.',
                     'pubmed': 23548863},
               279: {'info': 'Tsuji, K.; Yoon, K.S.; Ogo, S.: Biochemical '
                             'characterization of a bifunctional '
                             'acetaldehyde-alcohol dehydrogenase purified from '
                             'a facultative anaerobic bacterium Citrobacter '
                             'sp. S-77. J. Biosci. Bioeng. (2016) 121, '
                             '253-258.',
                     'pubmed': 26216639},
               284: {'info': 'Cheng, F.; Hu, T.; An, Y.; Huang, J.; Xu, Y.: '
                             'Purification and enzymatic characterization of '
                             'alcohol dehydrogenase from Arabidopsis thaliana. '
                             'Protein Expr. Purif. (2013) 90, 74-77.',
                     'pubmed': 23707506},
               286: {'info': 'Ashraf, R.; Rashid, N.; Kanai, T.; Imanaka, T.; '
                             'Akhtar, M.:  Pcal_1311, an alcohol dehydrogenase '
                             'homologue from Pyrobaculum calidifontis, '
                             'displays NADH-dependent high aldehyde reductase '
                             'activity. Extremophiles (2017)  FEHLT,  0000 .',
                     'pubmed': 29022135},
               287: {'info': 'Kwak, M.K.; Ku, M.; Kang, S.O.:  NAD+-linked '
                             'alcohol dehydrogenase 1 regulates methylglyoxal '
                             'concentration in Candida albicans. FEBS Lett. '
                             '(2014)  588,  1144-1153 .',
                     'pubmed': 24607541},
               288: {'info': 'Tsuji, K.; Yoon, K.S.; Ogo, S.:  Biochemical '
                             'characterization of a bifunctional '
                             'acetaldehyde-alcohol dehydrogenase purified from '
                             'a facultative anaerobic bacterium Citrobacter '
                             'sp. S-77. J. Biosci. Bioeng. (2016)  121,  '
                             '253-258 .',
                     'pubmed': 26216639},
               289: {'info': 'Abdallah, W.; Solanki, K.; Banta, S.:  Insertion '
                             'of a calcium-responsive beta-roll domain into a '
                             'thermostable alcohol dehydrogenase enables '
                             'tunable control over cofactor selectivity. ACS '
                             'Catal. (2018)  8,  1602-1613 .'},
               290: {'info': 'Campbell, E.; Wheeldon, I.; Banta, S.:  '
                             'Broadening the cofactor specificity of a '
                             'thermostable alcohol dehydrogenase using '
                             'rational protein design introduces novel kinetic '
                             'transient behavior. Biotechnol. Bioeng. (2010)  '
                             '107,  763-774 .',
                     'pubmed': 20632378},
               292: {'info': 'Beer, B.; Pick, A.; Doering, M.; Lommes, P.; '
                             'Sieber, V.:  Substrate scope of a dehydrogenase '
                             'from Sphingomonas species A1 and its potential '
                             'application in the synthesis of rare sugars and '
                             'sugar derivatives. Microb. Biotechnol. (2018)  '
                             '11,  747-758 .',
                     'pubmed': 29697194},
               293: {'info': 'Solanki, K.; Abdallah, W.; Banta, S.:  '
                             'Engineering the cofactor specificity of an '
                             'alcohol dehydrogenase via single mutations or '
                             "insertions distal to the 2'-phosphate group of "
                             'NADP(H). Protein Eng. Des. Sel. (2017)  30,  '
                             '373-380 .',
                     'pubmed': 28201792},
               294: {'info': 'Zhu, D.; Malik, H.; Hua, L.:  Asymmetric ketone '
                             'reduction by a hyperthermophilic alcohol '
                             'dehydrogenase. The substrate specificity, '
                             'enantioselectivity and tolerance of organic '
                             'solvents. Tetrahedron Asymmetry (2006)  17,  '
                             '3010-3014 .'}}),
             ('tissues', {'BTO_0000759', 'BTO_0003833'})])
--------------------------------------------------------------------------------
OrderedDict([('protein_id', 109),
             ('ec', '1.1.1.1'),
             ('organism', 'Homo sapiens'),
             ('taxonomy', 9606),
             ('uniprot', 'P08319'),
             ('CF',
              [{'comment': '#13,24,44,61,110,112,166# dependent on '
                           '<113,114,126,128,197,210,292>; #162# specific for '
                           '<287>; #46,95# dependent <153,154,159>; #163# '
                           'preferred cofactor <288>; #41# kinetics of '
                           'coenzyme binding in the pH-range 10-12 <26>; #4# '
                           'NAD+-plus-acetone-induced conversion <62>; #41# '
                           'NAD+ acts as an activator which induces an active '
                           'form of the enzyme <34>; #41# preferred substrate '
                           '<42>; #84# activity with mutants G223D/T224I and '
                           'G223D/T224I/H225N <125>; #10# cofactor binding '
                           'mode <120>; #13# dependent on, cofactor binding '
                           'mechanism and conformation from crystal structure '
                           'analysis <112>; #87# the monomer consists of a '
                           'catalytic and a cofactor-binding domain, the '
                           'cofactor is bound between 2 domains in a cleft '
                           '<127>; #7,27,34,50,66# strongly preferred as '
                           'cofactor <135>; #92# specific for NAD+, no '
                           'activity with NADP+, pro-R stereospecificity for '
                           'hydrogen transfer <144>; #98# ADH1 preferrs NAD+ '
                           '205fold better than NADP+ as cofactor <172>; #15# '
                           'ADH3 does not react with NADP+ <172>; #143# '
                           'preferred over NADP+ <138>; #6# strict requirement '
                           'for NAD(H) as the coenzyme. Critical role of the '
                           'D37 residue in discriminating NAD(H) from NADP(H) '
                           '<169>; #111# shows NAD+ as the preferred co-factor '
                           'over NADP+ <213>; #41# the binding of NAD+ is '
                           'kinetically limited by a unimolecular '
                           'isomerization (corresponding to the conformational '
                           'change) that is controlled by deprotonation of the '
                           'catalytic zinc-water to produce a '
                           'negatively-charged zinc-hydroxide, which can '
                           'attract the positively-charged nicotinamide ring '
                           '<198>; #114# NAD+ is prefered over NADP+ <215>; '
                           '#115# NADP+ is prefered over NAD+ <215>; #124# '
                           'strict requirement for NAD(H) as the coenzyme, no '
                           'activity with NADP+. The specificity constant '
                           'value is 6fold higher for NADH than NAD+ <218>; '
                           '#123# the enzyme transfers the deuteride to the '
                           'Si-face of NAD+ <219>; #48# Adh3 is strictly '
                           'dependent on NAD+/NADH, and shows no activity with '
                           'NADP+/NADPH as cofactor <223>; #133# exclusively '
                           'NAD+ dependent <237>; #51# 57fold preferred over '
                           'NADP+ <279>; #23# H255R single mutant exhibits an '
                           'increased binding affinity toward NADP+ and a '
                           'concomitant reduction in affinity for NAD+ <290>; '
                           '#23# insertion of an RTX domain from the adenylate '
                           'cyclase of Bordetella pertussis into a loop near '
                           'the catalytic active site of the thermostable '
                           'alcohol dehydrogenase D from Pyrococcus furiosus. '
                           'The resultant chimera, beta-AdhD, gains the '
                           'calcium-binding ability of the beta-roll, retains '
                           'the thermostable activity of AdhD, and exhibits '
                           'reduced overall alcohol dehydrogenase activity. '
                           'The addition of calcium to beta-AdhD '
                           'preferentially inhibits NAD+-dependent activity in '
                           'comparison to NADP+-dependent activity. Calcium is '
                           'a competitive inhibitor of AdhD, and the addition '
                           'of the RTX domain introduces calcium-dependent '
                           'noncompetitive inhibition to beta-AdhD affecting '
                           'NAD+-dependent activity <289>',
                'data': 'NAD+',
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
                         20,
                         21,
                         22,
                         23,
                         24,
                         25,
                         26,
                         27,
                         28,
                         29,
                         30,
                         31,
                         32,
                         33,
                         34,
                         35,
                         36,
                         37,
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
                         49,
                         50,
                         51,
                         52,
                         53,
                         54,
                         55,
                         56,
                         57,
                         58,
                         59,
                         60,
                         61,
                         62,
                         63,
                         64,
                         65,
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
                         89,
                         90,
                         91,
                         92,
                         93,
                         94,
                         95,
                         96,
                         97,
                         98,
                         99,
                         100,
                         101,
                         102,
                         103,
                         105,
                         110,
                         111,
                         112,
                         113,
                         114,
                         115,
                         116,
                         118,
                         120,
                         121,
                         124,
                         125,
                         126,
                         127,
                         128,
                         129,
                         130,
                         135,
                         136,
                         137,
                         138,
                         139,
                         141,
                         143,
                         144,
                         146,
                         148,
                         149,
                         152,
                         153,
                         154,
                         156,
                         157,
                         158,
                         159,
                         161,
                         162,
                         163,
                         164,
                         165,
                         169,
                         172,
                         180,
                         194,
                         195,
                         196,
                         197,
                         198,
                         200,
                         201,
                         202,
                         203,
                         204,
                         205,
                         206,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         215,
                         217,
                         218,
                         219,
                         220,
                         221,
                         222,
                         223,
                         225,
                         226,
                         227,
                         229,
                         230,
                         231,
                         232,
                         233,
                         234,
                         237,
                         243,
                         252,
                         254,
                         256,
                         257,
                         260,
                         269,
                         272,
                         279,
                         286,
                         287,
                         288,
                         289,
                         290,
                         292,
                         293]}]),
             ('ID', '1.1.1.1'),
             ('IN',
              [{'comment': '#46# competitive inhibitor <163>; #8# 1 mM, 31% '
                           'inhibition <23>; #8# class III enzyme is '
                           'completely insensitive to inhibition <11,16>; #8# '
                           'poor inhibitor, class II isoenzyme <14>; #8# no '
                           'inhibition by 12 mM <21>; #8# competitive against '
                           'ethanol <96>; #36# isoenzyme AA-ADH, BB-ADH and '
                           'TT-ADH <95>; #5# inhibits cell protein '
                           'carbonylation following exposure to crotyl alcohol '
                           '<117>',
                'data': '4-Methylpyrazole',
                'refs': [2,
                         11,
                         14,
                         16,
                         21,
                         23,
                         24,
                         25,
                         95,
                         96,
                         117,
                         135,
                         163,
                         214]},
               {'comment': '#90# substrate inhibition above 0.5 M <105>; #99# '
                           '50% (v/v), 59% loss of activity <173>; #106# '
                           'ethanol competitively inhibits the oxidation of '
                           '1-hydroxymethylpyrene by ADH1C and ADH3 <214>; '
                           '#109# ethanol competitively inhibits the oxidation '
                           'of 1-hydroxymethylpyrene by ADH4 <214>',
                'data': 'ethanol',
                'refs': [105, 173, 214]},
               {'comment': '#99# 50% (v/v), 29% loss of activity <173>; #106# '
                           'DMSO inhibits isozyme ADH2-catalysed oxidation in '
                           'an uncompetitive mode and reduction in a mixed '
                           'mode <214>; #106# DMSO inhibits isozymes '
                           'ADH1C-catalysed oxidation in an uncompetitive mode '
                           'and reduction in a mixed mode, no inhibition is '
                           'detected with isozyme ADH3 <214>; #109# DMSO '
                           'inhibits isozymes ADH4-catalysed oxidation in an '
                           'uncompetitive mode and reduction in a mixed mode '
                           '<214>',
                'data': 'DMSO',
                'refs': [173, 214]}]),
             ('KI',
              [{'chebi': 'CHEBI_16236',
                'comment': '#109# isozyme ADH4, using 1-hydroxymethylpyrene as '
                           'substrate <214>',
                'data': '3.3 {ethanol}',
                'refs': [214],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 3.3}]),
             ('KM',
              [{'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.000035 {1-formyl-8-methylpyrene}',
                'refs': [214],
                'substrate': '1-formyl-8-methylpyrene',
                'units': 'mM',
                'value': 3.5e-05},
               {'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.000036 {1-formyl-6-methylpyrene}',
                'refs': [214],
                'substrate': '1-formyl-6-methylpyrene',
                'units': 'mM',
                'value': 3.6e-05},
               {'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.00028 {1-hydroxymethyl-6-methylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethyl-6-methylpyrene',
                'units': 'mM',
                'value': 0.00028},
               {'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.00048 {4-formylpyrene}',
                'refs': [214],
                'substrate': '4-formylpyrene',
                'units': 'mM',
                'value': 0.00048},
               {'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.00092 {1-formylpyrene}',
                'refs': [214],
                'substrate': '1-formylpyrene',
                'units': 'mM',
                'value': 0.00092},
               {'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.0016 {1-hydroxymethyl-8-methylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethyl-8-methylpyrene',
                'units': 'mM',
                'value': 0.0016},
               {'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.0029 {4-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '4-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.0029},
               {'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.0069 {2-formylpyrene}',
                'refs': [214],
                'substrate': '2-formylpyrene',
                'units': 'mM',
                'value': 0.0069},
               {'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.0283 {1-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '1-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.0283},
               {'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '0.033 {2-hydroxymethylpyrene}',
                'refs': [214],
                'substrate': '2-hydroxymethylpyrene',
                'units': 'mM',
                'value': 0.033},
               {'chebi': 'CHEBI_15343',
                'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '12.7 {acetaldehyde}',
                'refs': [214],
                'substrate': 'acetaldehyde',
                'units': 'mM',
                'value': 12.7},
               {'chebi': 'CHEBI_16236',
                'comment': '#109# isozyme ADH4, at 21-23°C <214>',
                'data': '3.6 {ethanol}',
                'refs': [214],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 3.6}]),
             ('LO',
              [{'comment': '#61# 2 isozymes <113>; #24# enzyme polymer forms '
                           'rod-like helical particles <128>',
                'data': 'cytosol',
                'refs': [113, 128, 135, 194, 214]}]),
             ('MW',
              [{'comment': '#112# SDS-PAGE <197>; #106# isozyme ADH2, apparent '
                           'molecular weight deduced from electrophoretic '
                           'mobility <214>; #109# isozyme ADH4, calculated '
                           'from amino acid sequence <214>; #92,132# 4 * '
                           '40000, SDS-PAGE <144,239>; #8,10,36,53,79# 2 * '
                           '40000, SDS-PAGE <16,23,24,59,87,95>; #1,8,80,131# '
                           'x * 40000, SDS-PAGE <11,44,52,227>; #9# 2 * 40000, '
                           'ADH-3, SDS-PAGE <49>; #42# 2 * 40000, enzyme form '
                           'ADHI <68>',
                'data': '40000',
                'refs': [11,
                         16,
                         23,
                         24,
                         44,
                         49,
                         52,
                         59,
                         68,
                         87,
                         95,
                         144,
                         197,
                         214,
                         227,
                         239,
                         272]},
               {'comment': '#106# isozyme ADH1C, apparent molecular weight '
                           'deduced from electrophoretic mobility <214>; #109# '
                           'isozyme ADH4, apparent molecular weight deduced '
                           'from electrophoretic mobility <214>',
                'data': '40500',
                'refs': [214]}]),
             ('OSS',
              [{'comment': '#106,109# DMSO is not an ideal '
                           'substrate-delivering solvent for ADH-catalysed '
                           'reactions <214>; #151# 20% v/v, 24 h, 87% residual '
                           'activity <244>; #56# 20% v/v, 70% residual '
                           'activity <255>',
                'data': 'DMSO',
                'refs': [214, 244, 255]}]),
             ('RE',
              {'a primary alcohol + NAD+ = an aldehyde + NADH + H+ (#4,41# '
               'ordered bi-bi mechanism <31,43>; #4,75# rapid equilibrium '
               'random mechanism <63>; #8# ordered bi bi mechanism with '
               'cofactor adding first to form a binary enzyme complex <23>; '
               '#41# isoenzyme EE and SS: ordered bi bi mechanism <35>; '
               '#10,33# mechanism is predominantly ordered with ethanol, but '
               'partially random with butanol <91>; #41# kinetic mechanism is '
               'random for ethanol oxidation and compulsory ordered for '
               'acetaldehyde reduction <41>; #38# oxidizes ethanol in an '
               'ordered bi-bi mechanism with NAD+ as the first substrate fixed '
               '<85>; #10# compulsory-order mechanism with the rate-limiting '
               'step being the dissociation of the product enzyme-NAD+ complex '
               '<90>; #28,68,78# Theorell-Chance mechanism <38,69,74>; #44# '
               'sequential reaction mechanism <114>; #87# active site '
               'structure <127>; #78# catalytic mechanism involves a proton '
               'relay modulated by the coupled ionization of the active site '
               'Lys155/Tyr151 pair, and a NAD+ ribose 2-OH switch, other '
               'active site residues are Ser138 and Trp144, ionization '
               'properties, substrate binding, overview <130>; #8# class IV '
               'alcohol dehydrogenase also functions as retinol dehydrogenase, '
               'reaction and kinetic mechanism: asymmetric rapid equilibrium '
               'random mechanism with 2 dead-end ternary complexes fro retinol '
               'oxidation and a rapid equilibrium ordered mechanism with one '
               'dead-end ternary complex for retinal reduction, a unique '
               'mechanistic form fro zinc-containing ADH in the medium chain '
               'dehydrogenase/reductase superfamily of enzymes <124>; #10# '
               'detailed determination of the reaction and kinetic mechanisms, '
               'active site structure and determination of amino acid residues '
               'involved in catalysis, 3 isozymes <120>; #5# ordered bibi '
               'mechanism, structural and functional implications of amino '
               'acid residue 47 <110>; #41# ordered sequential bibi reaction '
               'mechanism, modeling of oxidation kinetic mechanism <117>; #41# '
               'reaction mechanism, His51 is involved, but not essential, in '
               'catalysis facilitating the deprotonation of the hydroxyl group '
               'of water or alcohol ligated to the catalytic zinc <111>; #8# '
               'Ser48 is involved in catalysis, isozyme gamma(2)gamma(2) '
               '<109>; #27# the catalytic triad consists of Cys44, His67, and '
               'Cys154, active site structure <129>)',
               'a secondary alcohol + NAD+ = a ketone + NADH + H+'}),
             ('RN', {'alcohol dehydrogenase'}),
             ('RT', {'reduction', 'redox reaction', 'oxidation'}),
             ('SN', {'alcohol:NAD+ oxidoreductase'}),
             ('SP',
              [{'data': '1-hydroxymethyl-6-methylpyrene + NAD+ = '
                        '1-formyl-6-methylpyrene + NADH + H+ {r}',
                'refs': [214]},
               {'data': '1-hydroxymethyl-8-methylpyrene + NAD+ = '
                        '1-formyl-8-methylpyrene + NADH + H+ {r}',
                'refs': [214]},
               {'data': '1-hydroxymethylpyrene + NAD+ = 1-formylpyrene + NADH '
                        '+ H+ {r}',
                'refs': [214]},
               {'data': '2-hydroxymethylpyrene + NAD+ = 2-formylpyrene + NADH '
                        '+ H+ {r}',
                'refs': [214]},
               {'data': '4-hydroxymethylpyrene + NAD+ = 4-formylpyrene + NADH '
                        '+ H+ {r}',
                'refs': [214]},
               {'comment': '#48# best substrate <223>; #111# 100% activity '
                           '<213>; #100# no activity with NADP+, in reverse '
                           'reaction no activity with NADPH <171>; #31# the '
                           'enzyme is highly specific for ethanol with NAD+ as '
                           'the coenzyme <181>; #112# 88% activity compared to '
                           'cyclohexanol <197>; #106# substrate for isozyme '
                           'ADH1C, extremely poor substrate for isozyme ADH3 '
                           '<214>; #106# substrate for isozyme ADH2 <214>; '
                           '#109# substrate for isozyme ADH4 <214>; #133# the '
                           'enzyme shows a preference for short-chain alcohols '
                           'ethanol and 1-propanol <237>; #155# 12% of the '
                           'activity with butan-1-ol <271>; #161# 33% of the '
                           'activity with 1,4-butanediol <286>) |#119# 83% of '
                           'the activity with butan-2-ol <256>',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [66,
                         103,
                         136,
                         139,
                         140,
                         143,
                         144,
                         147,
                         148,
                         153,
                         159,
                         161,
                         162,
                         163,
                         171,
                         173,
                         174,
                         181,
                         194,
                         195,
                         196,
                         197,
                         203,
                         205,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         222,
                         223,
                         231,
                         233,
                         237,
                         239,
                         246,
                         252,
                         256,
                         271,
                         277,
                         279,
                         284,
                         286,
                         288]},
               {'comment': '#48# best substrate <223>; #111# 100% activity '
                           '<213>; #100# no activity with NADP+, in reverse '
                           'reaction no activity with NADPH <171>; #31# the '
                           'enzyme is highly specific for ethanol with NAD+ as '
                           'the coenzyme <181>; #112# 88% activity compared to '
                           'cyclohexanol <197>; #106# substrate for isozyme '
                           'ADH1C, extremely poor substrate for isozyme ADH3 '
                           '<214>; #106# substrate for isozyme ADH2 <214>; '
                           '#109# substrate for isozyme ADH4 <214>; #133# the '
                           'enzyme shows a preference for short-chain alcohols '
                           'ethanol and 1-propanol <237>; #155# 12% of the '
                           'activity with butan-1-ol <271>; #161# 33% of the '
                           'activity with 1,4-butanediol <286>) |#119# 83% of '
                           'the activity with butan-2-ol <256>| {r',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [66,
                         103,
                         136,
                         139,
                         140,
                         143,
                         144,
                         147,
                         148,
                         153,
                         159,
                         161,
                         162,
                         163,
                         171,
                         173,
                         174,
                         181,
                         194,
                         195,
                         196,
                         197,
                         203,
                         205,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         222,
                         223,
                         231,
                         233,
                         237,
                         239,
                         246,
                         252,
                         256,
                         271,
                         277,
                         279,
                         284,
                         286,
                         288]},
               {'comment': '#48# best substrate <223>; #111# 100% activity '
                           '<213>; #100# no activity with NADP+, in reverse '
                           'reaction no activity with NADPH <171>; #31# the '
                           'enzyme is highly specific for ethanol with NAD+ as '
                           'the coenzyme <181>; #112# 88% activity compared to '
                           'cyclohexanol <197>; #106# substrate for isozyme '
                           'ADH1C, extremely poor substrate for isozyme ADH3 '
                           '<214>; #106# substrate for isozyme ADH2 <214>; '
                           '#109# substrate for isozyme ADH4 <214>; #133# the '
                           'enzyme shows a preference for short-chain alcohols '
                           'ethanol and 1-propanol <237>; #155# 12% of the '
                           'activity with butan-1-ol <271>; #161# 33% of the '
                           'activity with 1,4-butanediol <286>) |#119# 83% of '
                           'the activity with butan-2-ol <256>| {',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [66,
                         103,
                         136,
                         139,
                         140,
                         143,
                         144,
                         147,
                         148,
                         153,
                         159,
                         161,
                         162,
                         163,
                         171,
                         173,
                         174,
                         181,
                         194,
                         195,
                         196,
                         197,
                         203,
                         205,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         222,
                         223,
                         231,
                         233,
                         237,
                         239,
                         246,
                         252,
                         256,
                         271,
                         277,
                         279,
                         284,
                         286,
                         288]},
               {'comment': '#13# broad substrate specificity <126>; #10# '
                           'constitutive enzyme <94>; #42# key enzyme in '
                           'ethanol production <68>; #52# one constitutive '
                           'enzyme, ADH-MI and one inducible enzyme, ADH-MII '
                           '<82>; #53# enzyme may be involved in the '
                           'metabolism of dietary wax esters in salmonid fish '
                           '<59>; #78# the enzyme oxidizes alcohols to '
                           'aldehydes or ketones both for detoxification and '
                           'metabolic purposes <38>; #36# involvement in the '
                           'development of male hamster reproductive system '
                           '<47>; #88# enzyme shows high substrate specificity '
                           'towards primary aliphatic alcohols, no activity '
                           'with 2-butanol, tert-butanol, isoamyl alcohol, '
                           'isobutyl alcohol, 1,6-hexadiol, and mono-, di-, '
                           'and triethanolamine <118>; #90# no activity with '
                           'methanol, 2-propanol, and isoamyl alcohol <105>; '
                           '#10# substrate specificity and stereospecificity, '
                           'substrate binding pocket structure of the 3 '
                           'isozymes, involving Met294, Trp57, and Trp93 '
                           '<120>; #61# substrate specificity of the 2 '
                           'isozmyes with various substrates, overview, '
                           'isozymes are highly specific for the '
                           '(R)-stereoisomers and enantioselctive for the '
                           'R(-)isomers <113>; #46# the enzyme undergoes a '
                           'substantial conformational change in the apo-holo '
                           'transition, accompanied by loop movements at the '
                           'domain interface <108>; #60# alcohol dehydrogenase '
                           'activity may not limit alcohol supply for ester '
                           'production during ripening <146>; #54# Cm-ADH2 '
                           'cannot reduce branched aldehydes <151>; #10# '
                           'effects of pressure on deuterium isotope effects '
                           'of yeast alcohol dehydrogenase using alternative '
                           'substrates <139>; #92# no activity with methanol '
                           '<144>; #93# the enzyme does not act on short-chain '
                           'normal alkyl alcohols, including methanol and '
                           'ethanol <137>; #96# no activity towards methanol, '
                           'ethanol, 1-propanol, triethylene glycol, '
                           'polyethylene glycol 400, polyethylene glycol 1000, '
                           'D-sorbitol, D-sorbose, formaldehyde, acetaldehyde, '
                           'propionaldehyde, butyraldehyde, and valeraldehyde '
                           '<156>; #98# ADH1 preferrs primary alcohols '
                           'containing C3-C8 carbons to secondary alcohols '
                           'such as 2-propanol and 2-butanol. ADH1 possesses '
                           'specific carboxylate ester-forming activity <172>; '
                           '#101# no activity detected with: '
                           'N-benzyl-2-pyrrolidinone, 2-pyrrolidinone, '
                           '3-hexanone, 4-hydroxy-2-butanone, '
                           '(R)-N-benzyl-3-pyrrolidinol, ethanol, '
                           '1,3-propanediol, 1-butanol, 1,4-butanediol, '
                           '1,2,3-butanetriol, 1,2,4-butanetriol, acetol, '
                           '2-phenyl-1-propanol, 3-phenyl-1-propanol, benzyl '
                           'alcohol and glycerol. No activity with NADP+ or '
                           'NADPH <185>; #6# preference for reduction of '
                           'aromatic ketones and alpha-keto esters, and poor '
                           'activity on aromatic alcohols and aldehydes <169>; '
                           '#26# when NADH is replaced with NADPH, the '
                           'reaction rate is reduced by 0.6% <188>; #41# '
                           'activity is severely reduced towards aliphatic '
                           'alcohols of more than 8 carbon atoms for the free '
                           'enzyme, but not so with immobilized HLAD, '
                           'exhibiting an activity towards C22 and C24 '
                           'aliphatic alcohols higher than 50% of the highest '
                           'value, obtained with C8 <204>; #8# differences in '
                           'the activities of total ADH and class I ADH '
                           'isoenzyme between cancer liver tissues and healthy '
                           'hepatocytes may be a factor in ethanol metabolism '
                           'disorders, which can intensify carcinogenesis '
                           '<180>; #112# TADH is a NAD(H)-dependent enzyme and '
                           'shows a very broad substrate spectrum producing '
                           'exclusively the (S)-enantiomer in high '
                           'enantiomeric excess (more than 99%) during '
                           'asymmetric reduction of ketones <197>; #106# '
                           '1-octanal is no substrate for isozyme ADH1C <214>; '
                           '#106# 1-octanal is no substrate for isozyme ADH2 '
                           '<214>; #109# 1-octanal is no substrate for isozyme '
                           'ADH4 <214>; #112# ADH exhibits a clear preference '
                           'for primary alcohols and corresponding aldehydes '
                           'for aliphatic substrates, in the oxidative '
                           'direction activity steeply increases with chain '
                           'length until 1-propanol and then decreases '
                           'slightly again with growing chain length, '
                           'alpha,beta-unsaturated ketones like 3-penten-2-one '
                           'and cyclohexenone are not converted by ADH, almost '
                           'no conversion of methanol (0.2%) and (+)-carvone '
                           '(0.4%) is detected <197>; #110# no activity '
                           'towards methanol <210>; #114# substrates are a '
                           'broad range of alkyl alcohols from ethanol to '
                           '1-triacontanol <215>; #123# the physiological '
                           'direction of the catalytic reaction is reduction '
                           'rather than oxidation <219>; #124# the enzyme '
                           'displays a preference for the reduction of '
                           'alicyclic, bicyclic and aromatic ketones and '
                           'alpha-ketoesters, but is poorly active on '
                           'aliphatic, cyclic and aromatic alcohols, showing '
                           'no activity on aldehydes <218>; #123# the enzyme '
                           'shows no activity on aliphatic linear and branched '
                           'alcohols, except for a poor activity on '
                           '2-propyn-1-ol, 3-methyl-1-butanol and 2-pentanol; '
                           'however, it shows a discrete activity on aliphatic '
                           'cyclic and bicyclic alcohols. Benzyl alcohol and '
                           '4-bromobenzyl alcohol are not found to be '
                           'substrates. The S and R enantiomers of '
                           'a-(trifluoromethyl)benzyl alcohol and methyl and '
                           'ethyl mandelates show no apparent activity with '
                           'SaADH. The enzyme shows poor activity on '
                           '(+/-)-1-phenyl-1-propanol, 1-(1-naphthyl)ethanol '
                           'and the two enantiomers of 1-(2-naphthyl)ethanol. '
                           'The enzyme is not active on aliphatic and aromatic '
                           'aldehydes, and on aliphatic linear, branched and '
                           'cyclic ketones except for 3-methylcyclohexanone. '
                           'Catalytic inactivity is observed with acetophenone '
                           'and (S)-a-(trifluoromethyl)benzyl <219>; #127# '
                           'methanol, formaldehyde, and acetone are no '
                           'substrates for HpADH3 <222>; #48# no activity with '
                           'methanol, 1-butanol, glycerol or 2-propanol <223>; '
                           '#128# substrate specificity and '
                           'enantiospecificity, overview. The (R)-specific '
                           'alcohol dehydrogenase requires NADH and reduces '
                           'various kinds of carbonyl compounds, including '
                           'ketones and aldehydes. AFPDH reduces '
                           'acetylpyridine derivatives, beta-keto esters, and '
                           'some ketones compounds with high '
                           'enantiospecificity, overview. No activity with '
                           '2-chlorobenzaldehyde and 2-tetralone, poor '
                           'activity with 1-tetralone, pyruvate, '
                           '2-oxobutyrate, oxalacetate, cyclopentanone, '
                           'cyclohexanone, cycloheptanone, and dipropylketone. '
                           'No activity with 1,2-propanediol, '
                           '3-chloro-1,2-propanediol, 3-bromo-1,2-propanediol, '
                           'glycerol, 1-pentanol, poor activity with '
                           '1-butanol, 1-propanol, ethanol, and methanol '
                           '<225>; #85# the enzyme exhibits broad substrate '
                           'specificity towards aliphatic ketones, '
                           'cycloalkanones, aromatic ketones, and ketoesters '
                           '<226>; #132# the enzyme shows broad substrate '
                           'specificity and prefers aliphatic alcohols and '
                           'ketones. There are no large differences in the '
                           'reactivities between primary and secondary '
                           'alcohols. The enzyme produces (S)-alcohols from '
                           'the corresponding ketones. The values of the '
                           'enantiomeric excess increase with the increase of '
                           'chain length except for the reduction of '
                           '2-hexanone. The highest enantioselectivity is '
                           'shown with the reduction of 2-nonanone <239>; '
                           '#133# the NAD+-dependent HvADH1 shows a preference '
                           'for short-chain alcohols, no activity with '
                           'methanol <237>; #143# broad substrate specificity '
                           'with a preference for the reduction of ketones and '
                           'the oxidation of secondary alcohols <138>; #124# '
                           'enzyme displays a preference for the reduction of '
                           'alicyclic, bicyclic and aromatic ketones and '
                           'alpha-keto esters, but is poorly active on '
                           'aliphatic, cyclic and aromatic alcohols, and shows '
                           'no activity on aldehydes <219>; #150# enzyme '
                           'reduces aldehydes to (R)-alcohols with more than '
                           '99.8% enantiomeric excess <243>; #151# enzyme '
                           'selectively reduces the C=O bond of allylic '
                           'aldehydes/ketones to the corresponding '
                           'alpha,beta-unsaturated alcohols and also has the '
                           'capacity of stereoselectively reducing aromatic '
                           'ketones to (S)-enantioselective alcohols. The '
                           'enzyme preferentially catalyzes oxidation of '
                           'allylic/benzyl aldehydes <244>; #71# ethanol '
                           'dehydrogenase activity of Thermoanaerobium brockii '
                           'is both NAD and NADP linked, reversible, and not '
                           'inhibited by low levels of reaction products '
                           '<103>; #119,142# mutation at the substrate-binding '
                           'site, or at a dimer interface, alters kinetic '
                           'properties and protein oligomeric structure, '
                           'active site flexibility is correlated with subunit '
                           'interactions 20 A away <260>; #6# the enzyme '
                           'transfers the pro-S hydrogen of [4R-(2)H]NADH and '
                           'exhibits Prelog specificity <269>; #41# acycloNAD+ '
                           'i.e. NAD+-analogue, where the nicotinamide ribosyl '
                           'moiety has been replaced by the nicotinamide '
                           '(2-hydroxyethoxy)methyl moiety. There is no '
                           'detectable reduction of acycloNAD+ by secondary '
                           'alcohols although these alcohols serve as '
                           'competitive inhibitors. AcycloNAD+ converts horse '
                           'liver ADH from a broad spectrum alcohol '
                           'dehydrogenase, capable of utilizing either primary '
                           'or secondary alcohols, into an exclusively primary '
                           'alcohol dehydrogenase <275>; #51# bifunctional '
                           'enzyme consisting of an N-terminal acetaldehyde '
                           'dehydrogenase (ALDH) and a C-terminal alcohol '
                           'dehydrogenase (ADH). The specificity constant '
                           '(kcat/Km) is 47fold higher for acetaldehyde '
                           'reductase than that for ethanol dehydrogenase '
                           '<279>; #153# enzyme is an alcohol dehydrogenase '
                           'with additional activity for all-trans-retinol, '
                           'reaction of EC 1.1.1.184 <272>; #155# enzyme shows '
                           'activity as a reductase specific for (S)-acetoin, '
                           'EC 1.1.1.76, and both diacetyl reductase (EC '
                           '1.1.1.304) and NAD+-dependent alcohol '
                           'dehydrogenase (EC 1.1.1.1) activities <271>; #160# '
                           'the enzyme additionally catalyzes selective '
                           'reduction of 3-quinuclidinone to '
                           '(R)-3-quinuclidinol, with 84% ee and 62% '
                           'conversion after 22 h <274>; #162# Candida '
                           'albicans ADH1 is a bifunctional enzyme that '
                           'catalyzes methylglyoxal oxidation and reduction, '
                           'cf. EC 1.2.1.23 <287>; #161# the enzyme catalyzes '
                           'NAD(H)-dependent oxidation of various alcohols and '
                           'reduction of aldehydes, with a marked preference '
                           'for substrates with functional group at the '
                           'terminal carbon atom <286>; #166# almost no '
                           'activity with D-arabinonate, D-lyxonate, '
                           'D-galactonate, glycerol, meso-erythritol, '
                           'D-ribitol, D-arabitol, D-xylitol, and D-mannitol. '
                           'No activity with propanal, butanal, hexanal, and '
                           '4-oxobutanoic acid <292>; #165# the enzyme '
                           'catalyzes the reduction of acetophenone '
                           'derivatives to the corresponding (S)-chiral '
                           'alcohols in an enantiomerically pure form. The '
                           'substituents on the benzene ring of the aryl '
                           'ketones exert some effect on the enzyme activity, '
                           'although the influence is not dramatic. The '
                           'enantioselectivity of the reduction is not '
                           'affected by the substituents and pattern of the '
                           'substitution. The alpha-chlorinated acetophenone '
                           'shows a much higher activity than the '
                           'unsubstituted one (more than 10 times) <294>) {',
                'data': 'more = ?',
                'refs': [38,
                         47,
                         59,
                         68,
                         82,
                         94,
                         103,
                         105,
                         108,
                         113,
                         118,
                         120,
                         126,
                         137,
                         138,
                         139,
                         144,
                         146,
                         151,
                         156,
                         169,
                         172,
                         180,
                         185,
                         188,
                         197,
                         204,
                         210,
                         211,
                         214,
                         215,
                         218,
                         219,
                         222,
                         223,
                         225,
                         226,
                         237,
                         239,
                         243,
                         244,
                         260,
                         269,
                         271,
                         272,
                         274,
                         275,
                         279,
                         286,
                         287,
                         292,
                         294]}]),
             ('ST',
              [{'bto': 'BTO_0003833',
                'comment': '#106,109# isozyme ADH4 <214>',
                'data': 'buccal mucosa',
                'refs': [214]}]),
             ('SY',
              [{'comment': '#109# isozyme <214>',
                'data': 'ADH4',
                'refs': [124, 174, 177, 214, 252]}]),
             ('references',
              {1: {'info': 'Talbot, B.G.; Qureshi, A.A.; Cohen, R.; Thirion, '
                           'J.P.: Purification and properties of two distinct '
                           'groups of ADH isozymes from Chinese hamster liver. '
                           'Biochem. Genet. (1981) 19, 813-829.',
                   'pubmed': 6794566},
               2: {'info': 'Fong, W.P.: Isolation and characterization of '
                           'grass carp (Ctenopharyngodon idellus) liver '
                           'alcohol dehydrogenase. Comp. Biochem. Physiol. B '
                           '(1991) 98, 297-302.'},
               3: {'info': 'Pessione, E.; Pergola, L.; Cavaletto, M.; Giunta, '
                           'C.; Trotta, A.; Vanni, A.: Extraction, '
                           'purification and characterization of ADH1 from the '
                           'budding yeast Kluyveromyces marxianus. Ital. J. '
                           'Biochem. (1990) 39, 71-82.',
                   'pubmed': 2193901},
               4: {'info': 'Leblova, S.; El Ahmad, M.: Characterization of '
                           'alcohol dehydrogenase isolated from germinating '
                           'bean (Vicia faba) seeds. Collect. Czech. Chem. '
                           'Commun. (1989) 54, 2519-2527.'},
               5: {'info': 'Keung, W.M.; Ho, Y.W.; Fong, W.P.; Lee, C.Y.: '
                           'Isolation and characterization of shrew (Suncus '
                           'murinus) liver alcohol dehydrogenase. Comp. '
                           'Biochem. Physiol. B (1989) 93, 169-173.',
                   'pubmed': 2666017},
               6: {'info': 'Tong, W.F.; Lin, S.W.: Purification and '
                           'biochemical properties of rice alcohol '
                           'dehydrogenase. Bot. Bull. Acad. Sin. (1988) 29, '
                           '245-253.'},
               7: {'info': 'Van Geyt, J.; Jacobs, M.; Triest, L.: '
                           'Characterization of alcohol dehydrogenase in Najas '
                           'marina L. Aquat. Bot. (1987) 28, 129-141.'},
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
                           '(1982) 7, 237-250.'},
               9: {'info': 'Edenberg, H.J.; Brown, C.J.; Carr, L.G.; Ho, W.H.; '
                           'Hu, M.W.: Alcohol dehydrogenase gene expression '
                           'and cloning of the mouse chi-like ADH. Adv. Exp. '
                           'Med. Biol. (1991) 284, 253-262.',
                   'pubmed': 2053480},
               10: {'info': 'Herrera, E.; Zorzano, A.; Fresneda, V.: '
                            'Comparative kinetics of human and rat liver '
                            'alcohol dehydrogenase. Biochem. Soc. Trans. '
                            '(1983) 11, 729-730.'},
               11: {'info': 'Dafeldecker, W.P.; Vallee, B.L.: Organ-specific '
                            'human alcohol dehydrogenase: isolation and '
                            'characterization of isozymes from testis. '
                            'Biochem. Biophys. Res. Commun. (1986) 134, '
                            '1056-1063.',
                    'pubmed': 2936344},
               12: {'info': 'Woronick, C.L.: Alcohol dehydrogenase from human '
                            'liver. Methods Enzymol. (1975) 41B, 369-374.',
                    'pubmed': 236461},
               13: {'info': 'Wagner, F.W.; Burger, A.R.; Vallee, B.L.: Kinetic '
                            'properties of human liver alcohol dehydrogenase: '
                            'oxidation of alcohols by class I isoenzymes. '
                            'Biochemistry (1983) 22, 1857-1863.',
                    'pubmed': 6342669},
               14: {'info': 'Ditlow, C.C.; Holmquist, B.; Morelock, M.M.; '
                            'Vallee, B.L.: Physical and enzymatic properties '
                            'of a class II alcohol dehydrogenase isozyme of '
                            'human liver: pi-ADH. Biochemistry (1984) 23, '
                            '6363-6368.',
                    'pubmed': 6397223},
               15: {'info': 'Yin, S.J.; Bosron, W.F.; Magnes, L.J.; Li, T.K.: '
                            'Human liver alcohol dehydrogenase: purification '
                            'and kinetic characterization of the beta 2 beta '
                            '2, beta 2 beta 1, alpha beta 2, and beta 2 gamma '
                            '1 Oriental isoenzymes. Biochemistry (1984) 23, '
                            '5847-5853.',
                    'pubmed': 6395883},
               16: {'info': 'Wagner, F.W.; Pares, X.; Holmquist, B.; Vallee, '
                            'B.L.: Physical and enzymatic properties of a '
                            'class III isozyme of human liver alcohol '
                            'dehydrogenase: chi-ADH. Biochemistry (1984) 23, '
                            '2193-2199.',
                    'pubmed': 6375718},
               17: {'info': 'Bosron, W.F.; Magnes, L.J.; Li, T.K.: Kinetic and '
                            'electrophoretic properties of native and '
                            'recombined isoenzymes of human liver alcohol '
                            'dehydrogenase. Biochemistry (1983) 22, 1852-1857.',
                    'pubmed': 6342668},
               18: {'info': 'Bosron, W.F.; Li, T.K.: Isolation and '
                            'characterization of an anodic form of human liver '
                            'alcohol dehydrogenase. Biochem. Biophys. Res. '
                            'Commun. (1977) 74, 85-91.',
                    'pubmed': 836289},
               19: {'info': 'Schneider-Bernloehr, H.; Formicka-Kozlowska, G.; '
                            'Buehler, R.; Wartburg, J.P.; Zeppezauer, M.: '
                            'Active-site-specific zinc-depleted and '
                            'reconstituted cobalt(II) human-liver alcohol '
                            'dehydrogenase. Preparation, characterization and '
                            'complexation with NADH and '
                            'trans-4-(N,N-dimethylamino)-cinnamaldehyde. Eur. '
                            'J. Biochem. (1988) 173, 275-280.',
                    'pubmed': 3360008},
               20: {'info': 'Burnell, J.C.; Li, T.K.; Bosron, W.F.: '
                            'Purification and steady-state kinetic '
                            'characterization of human liver beta 3 beta 3 '
                            'alcohol dehydrogenase. Biochemistry (1989) 28, '
                            '6810-6815.',
                    'pubmed': 2819035},
               21: {'info': 'Pares, X.; Vallee, B.L.: New human liver alcohol '
                            'dehydrogenase forms with unique kinetic '
                            'characteristics. Biochem. Biophys. Res. Commun. '
                            '(1981) 98, 122-130.',
                    'pubmed': 7011320},
               22: {'info': 'Bosron, W.F.; Li, T.K.; Vallee, B.L.: New '
                            'molecular forms of human liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'ADHIndianapolis. Proc. Natl. Acad. Sci. USA '
                            '(1980) 77, 5784-5788.',
                    'pubmed': 7003596},
               23: {'info': 'Bosron, W.F.; Li, T.K.; Dafeldecker, W.P.; '
                            'Vallee, B.L.: Human liver pig-alcohol '
                            'dehydrogenase: kinetic and molecular properties. '
                            'Biochemistry (1979) 18, 1101-1105.',
                    'pubmed': 427099},
               24: {'info': 'Dafeldecker, W.P.; Pares, X.; Vallee, B.L.; '
                            'Bosron, W.F.; Li, T.K.: Simian liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'isoenzymes from Saimiri sciureus. Biochemistry '
                            '(1981) 20, 856-861.',
                    'pubmed': 7011375},
               25: {'info': 'Dafeldecker, W.P.; Meadow, P.E.; Pares, X.; '
                            'Vallee, B.L.: Simian liver alcohol dehydrogenase: '
                            'isolation and characterization of isoenzymes from '
                            'Macaca mulatta. Biochemistry (1981) 20, '
                            '6729-6734.',
                    'pubmed': 7030395},
               26: {'info': 'Kvassman, J.; Pettersson, G.: Kinetics of '
                            'coenzyme binding to liver alcohol dehydrogenase '
                            'in the pH range 10-12. Eur. J. Biochem. (1987) '
                            '166, 167-172.',
                    'pubmed': 3595610},
               27: {'info': 'Andersson, L.; Mosbach, K.: Alcohol dehydrogenase '
                            'from horse liver by affinity chromatography. '
                            'Methods Enzymol. (1982) 89, 435-445.',
                    'pubmed': 6755178},
               28: {'info': 'Pietruszko, R.: Alcohol dehydrogenase from horse '
                            'liver, steroid-active SS isoenzyme. Methods '
                            'Enzymol. (1982) 89, 429-435.'},
               29: {'info': 'Dahl, K.H.; Eklund, H.; McKinley-McKee, J.S.: '
                            'Enantioselective affinity labelling of horse '
                            'liver alcohol dehydrogenase. Correlation of '
                            'inactivation kinetics with the three-dimensional '
                            'structure of the enzyme. Biochem. J. (1983) 211, '
                            '391-396.',
                    'pubmed': 6347187},
               30: {'info': 'Ramaswamy, S.: Dynamics in alcohol dehydrogenase '
                            'elucidated from crystallographic investigations. '
                            'Adv. Exp. Med. Biol. (1999) 7, 275-284.',
                    'pubmed': 10352696},
               31: {'info': 'Adolph, H.W.; Maurer, P.; Schneider-Bernloehr, '
                            'H.; Sartorius, C.; Zeppezauer, M.: Substrate '
                            'specificity and stereoselectivity of horse liver '
                            'alcohol dehydrogenase. Kinetic evaluation of '
                            'binding and activation parameters controlling the '
                            'catalytic cycles of unbranched, acyclic secondary '
                            'alcohols and ketones as substrates of the native '
                            'and active-site-specific Co(II)-substituted '
                            'enzyme. Eur. J. Biochem. (1991) 201, 615-625.',
                    'pubmed': 1935957},
               32: {'info': 'Freudenreich, C.; Samama, J.P.; Biellmann, J.F.: '
                            'Design of inhibitors from the three-dimensional '
                            'structure of alcohol dehydrogenase. Chemical '
                            'synthesis and enzymatic properties. J. Am. Chem. '
                            'Soc. (1984) 106, 3344-3353.'},
               33: {'info': 'Samama, J.P.; Hirsch, D.; Goulas, P.; Biellmann, '
                            'J.F.: Dependence of the substrate specificity and '
                            'kinetic mechanism of horse-liver alcohol '
                            'dehydrogenase on the size of the C-3 pyridinium '
                            'substituent. 3-Benzoylpyridine-adenine '
                            'dinucleotide. Eur. J. Biochem. (1986) 159, '
                            '375-380.',
                    'pubmed': 3758068},
               34: {'info': 'Eklund, H.: Coenzyme binding in alcohol '
                            'dehydrogenase. Biochem. Soc. Trans. (1989) 17, '
                            '293-296.',
                    'pubmed': 2753206},
               35: {'info': 'Dworschack, R.T.; Plapp, B.V.: Kinetics of native '
                            'and activated isozymes of horse liver alcohol '
                            'dehydrogenase. Biochemistry (1977) 16, 111-116.',
                    'pubmed': 831772},
               36: {'info': 'Maret, W.; Andersson, I.; Dietrich, H.; '
                            'Schneider-Bernloehr, H.; Einarsson, R.; '
                            'Zeppezauer, M.: Site-specific substituted '
                            'cobalt(II) horse liver alcohol dehydrogenases. '
                            'Preparation and characterization in solution, '
                            'crystalline and immobilized state. Eur. J. '
                            'Biochem. (1979) 98, 501-512.',
                    'pubmed': 488110},
               37: {'info': 'Skerker, P.S.; Clark, D.S.: Thermostability of '
                            'alcohol dehydrogenase: evidence for distinct '
                            'subunits with different deactivation properties. '
                            'Biotechnol. Bioeng. (1989) 33, 62-71.',
                    'pubmed': 18587844},
               38: {'info': 'Benach, J.; Atrian, S.; Gonzalez-Duarte, R.; '
                            'Ladenstein, R.: The catalytic reaction and '
                            'inhibition mechanism of Drosophila alcohol '
                            'dehydrogenase: observation of an enzyme-bound '
                            'NAD-ketone adduct at 1.4 A resolution by X-ray '
                            'crystallography. J. Mol. Biol. (1999) 289, '
                            '335-355.',
                    'pubmed': 10366509},
               39: {'info': 'Tsai, C.S.: Multifunctionality of liver alcohol '
                            'dehydrogenase: kinetic and mechanistic studies of '
                            'esterase reaction. Arch. Biochem. Biophys. (1982) '
                            '213, 635-642.',
                    'pubmed': 7041828},
               40: {'info': 'Favilla, R.; Cavatorta, P.; Mazzini, A.; Fava, '
                            'A.: The peroxidatic reaction catalyzed by horse '
                            'liver alcohol dehydrogenase. 2. Steady-state '
                            'kinetics and inactivation. Eur. J. Biochem. '
                            '(1980) 104, 223-227.',
                    'pubmed': 6989598},
               41: {'info': 'Ryzewski, C.N.; Pietruszko, R.: Kinetic mechanism '
                            'of horse liver alcohol dehydrogenase SS. '
                            'Biochemistry (1980) 19, 4843-4848.',
                    'pubmed': 7000185},
               42: {'info': 'Ryzewski, C.N.; Pietruszko, R.: Horse liver '
                            'alcohol dehydrogenase SS: purification and '
                            'characterization of the homogenous isoenzyme. '
                            'Arch. Biochem. Biophys. (1977) 183, 73-82.',
                    'pubmed': 20851},
               43: {'info': 'Winberg, J.O.; McKinley-McKee, J.S.: Drosophila '
                            'melanogaster alcohol dehydrogenase: '
                            'product-inhibition studies. Biochem. J. (1994) '
                            '301, 901-909.',
                    'pubmed': 8053914},
               44: {'info': 'von Bahr-Lindstroem, H.; Andersson, L.; Mosbach, '
                            'K.; Joernvall, H.: Purification and '
                            'characterization of chicken liver alcohol '
                            'dehydrogenase. FEBS Lett. (1978) 89, 293-297.',
                    'pubmed': 658420},
               45: {'info': 'Hoshino, T.; Ishigura, I.; Ohta, Y.: Rabbit liver '
                            'alcohol dehydrogenase: purification and '
                            'properties. J. Biochem. (1985) 97, 1163-1172.',
                    'pubmed': 3161873},
               46: {'info': 'Keung, W.M.; Yip, P.K.: Rabbit liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'class I isozymes. Biochem. Biophys. Res. Commun. '
                            '(1989) 158, 445-453.',
                    'pubmed': 2916992},
               47: {'info': 'Keung, W.M.: A genuine organ specific alcohol '
                            'dehydrogenase from hamster testes: isolation, '
                            'characterization and developmental changes. '
                            'Biochem. Biophys. Res. Commun. (1988) 156, 38-45.',
                    'pubmed': 3178842},
               48: {'info': 'Algar, E.M.; Seeley, T.L.; Holmes, R.S.: '
                            'Purification and molecular properties of mouse '
                            'alcohol dehydrogenase isozymes. Eur. J. Biochem. '
                            '(1983) 137, 139-147.',
                    'pubmed': 6360682},
               49: {'info': 'Julia, P.; Farres, J.; Pares, X.: '
                            'Characterization of three isoenzymes of rat '
                            'alcohol dehydrogenase. Tissue distribution and '
                            'physical and enzymatic properties. Eur. J. '
                            'Biochem. (1987) 162, 179-189.',
                    'pubmed': 3816781},
               50: {'info': 'Pares, X.; Moreno, A.; Cederlund, E.; Hoeoeg, '
                            'J.O.; Joernvall, H.: Class IV mammalian alcohol '
                            'dehydrogenase. Structural data of the rat stomach '
                            'enzyme reveal a new class well separated from '
                            'those already characterized. FEBS Lett. (1990) '
                            '277, 115-118.',
                    'pubmed': 2269340},
               51: {'info': 'Mezey, E.; Potter, J.J.: Separation and partial '
                            'characterization of multiple forms of rat liver '
                            'alcohol dehydrogenase. Arch. Biochem. Biophys. '
                            '(1983) 225, 787-794.',
                    'pubmed': 6354095},
               52: {'info': 'Hjelmqvist, L.; Shafqqat, J.; Siddiqi, A.R.; '
                            'Joernvall, H.: Linking of isoenzyme and class '
                            'variability patterns in the emergence of novel '
                            'alcohol dehydrogenase functions. Characterization '
                            'of isozymes in Uromastix hardwickii. Eur. J. '
                            'Biochem. (1996) 236, 563-570.',
                    'pubmed': 8612630},
               53: {'info': 'Kedishvili, N.Y.; Bosron, W.F.; Stone, C.L.; '
                            'Hurley, T.D.; Peggs, C.F.; Thomasson, H.R.; '
                            'Popov, K.M.; Carr, L.G.; Edenberg, H.J.; Li, '
                            'T.K.: Expression and kinetic characterization of '
                            'recombinant human stomach alcohol dehydrogenase. '
                            'Active-site amino acid sequence explains '
                            'substrate specificity copared with liver '
                            'isozymes. J. Biol. Chem. (1995) 270, 3625-3630.',
                    'pubmed': 7876099},
               54: {'info': 'Plapp, B.V.; Sogin, D.C.; Dworschack, R.T.; '
                            'Bohlken, D.P.; Woenckhaus, C.: Kinetics of native '
                            'and modified liver alcohol dehydrogenase with '
                            'coenzyme analogues: isomerization of '
                            'enzyme-nicotinamide adenine dinucleotide complex. '
                            'Biochemistry (1986) 25, 5396-5402.',
                    'pubmed': 3778867},
               55: {'info': 'Li, H.; Hallows, W.H.; Punzi, J.S.; Marquez, '
                            'V.E.; Carrell, H.L.; Pankiewicz, K.W.; Watanabe, '
                            'K.A.; Goldstein, B.M.: Crystallographic studies '
                            'of two alcohol dehydrogenase-bound analogues of '
                            'thiazole-4-carboxamide adenine dinucleotide '
                            '(TAD), the active anabolite of the antitumor '
                            'agent tiazofurin. Biochemistry (1994) 33, 23-32.',
                    'pubmed': 8286346},
               56: {'info': 'Pearl, L.H.; Demasi, D.; Hemmings, A.M.; Sica, '
                            "F.; Mazzarella, L.; Raia, C.A.; D'Auria, S.; "
                            'Rossi, M.: Crystallization and preliminary X-ray '
                            'analysis of an NAD(+)-dependent alcohol '
                            'dehydrogenase fromthe extreme thermophilic '
                            'archaebacterium Sulfolobus solfataricus. J. Mol. '
                            'Biol. (1993) 229, 782-784.',
                    'pubmed': 8433371},
               57: {'info': 'Shafqat, J.; Hjelmqvist, L.; Joernvall, H.: Liver '
                            'class-I alcohol dehydrogenase isozyme '
                            'relationships and constant patterns in a variable '
                            'basic structure. Distinctions from '
                            'characterization of an ethanol dehydrogenase in '
                            'cobra, Naja naja. Eur. J. Biochem. (1996) 236, '
                            '571-578.',
                    'pubmed': 8612631},
               58: {'info': 'Retzios, A.; Thatcher, D.R.: Characterization of '
                            'the Adhf and Adhus alleloenzymes of Drosophila '
                            'melanogaster (fruitfly) alcohol dehydrogenase. '
                            'Biochem. Soc. Trans. (1981) 9, 298-299.'},
               59: {'info': 'Bauermeister, A.; Sargent, J.: Purification and '
                            'properties of an alcohol dehydrogenase from the '
                            'liver and intestinal caecum of rainbow trout '
                            '(Salmo gairdnerii). Biochem. Soc. Trans. (1978) '
                            '6, 222-224.',
                    'pubmed': 640168},
               60: {'info': 'Nussrallah, B.A.; Dam, R.; Wagner, F.W.: '
                            'Characterization of Coturnix quail liver alcohol '
                            'dehydrogenase enzymes. Biochemistry (1989) 28, '
                            '6245-6251.',
                    'pubmed': 2789998},
               61: {'info': 'Winberg, J.O.; Hovik, R.; McKinley-McKee, J.S.; '
                            'Juan, E.; Gonzalez-Duarte, R.: Biochemical '
                            'properties of alcohol dehydrogenase from '
                            'Drosophila lebanonensis. Biochem. J. (1986) 235, '
                            '481-490.',
                    'pubmed': 2943270},
               62: {'info': 'Winberg, J.O.; McKinley-McKee, J.S.: Drosophila '
                            'melanogaster alcohol dehydrogenase. Biochemical '
                            'properties of the NAD+-plus-acetone-induced '
                            'isoenzyme conversion. Biochem. J. (1988) 251, '
                            '223-227.',
                    'pubmed': 3134011},
               63: {'info': 'Heinstra, P.W.H.; Thoerig, G.E.W.; Scharloo, W.; '
                            'Drenth, W.; Nolte, R.J.M.: Kinetics and '
                            'thermodynamics of ethanol oxidation catalyzed by '
                            'genetic variants of the alcohol dehydrogenase '
                            'from Drosophila melanogaster and D. simulans. '
                            'Biochim. Biophys. Acta (1988) 967, 224-233.',
                    'pubmed': 3142528},
               64: {'info': 'Juan, E.; Gonzalez-Duarte, R.: Determination of '
                            'some biochemical and structural features of '
                            'alcohol dehydrogenases from Drosophila simulans '
                            'and Drosophila virilis. Comparison of their '
                            'properties with the Drosophila melanogaster Adhs '
                            'enzyme. Biochem. J. (1981) 195, 61-69.',
                    'pubmed': 6796069},
               65: {'info': 'Lee, C.Y.: Alcohol dehydrogenase from Drosophila '
                            'melanogaster. Methods Enzymol. (1982) 89, '
                            '445-450.'},
               66: {'info': 'Rella, R.; Raia, C.A.; Pensa, M.; Pisani, F.M.; '
                            'Gambacorta, A.; de Rosa, M.; Rossi, M.: A novel '
                            'archaebacterial NAD+-dependent alcohol '
                            'dehydrogenase. Purification and properties. Eur. '
                            'J. Biochem. (1987) 167, 475-479.',
                    'pubmed': 3115775},
               67: {'info': 'Wills, C.; Kratofil, P.; Londo, D.; Martin, T.: '
                            'Characterization of the two alcohol '
                            'dehydrogenases of Zymomonas mobilis. Arch. '
                            'Biochem. Biophys. (1981) 210, 775-785.',
                    'pubmed': 7030207},
               68: {'info': 'Kinoshita, S.; Kakizono, T.; Kadota, K.; Das, K.; '
                            'Taguchi, H.: Purification of two alcohol '
                            'dehydrogenases from Zymomonas mobilis and their '
                            'properties. Appl. Microbiol. Biotechnol. (1985) '
                            '22, 249-254.'},
               69: {'info': 'Grondal, E.J.M.; Betz, A.; Kreuzberg, K.: Partial '
                            'purification and properties of alcohol '
                            'dehydrogenase from unicellular green alga '
                            'Chlamydomonas moewusii. Phytochemistry (1983) 22, '
                            '1695-1699.'},
               70: {'info': 'Ammendola, S.; Raia, C.A.; Caruso, C.; '
                            "Camardella, L.; D'Auria, S.; De Rosa, M.; Rossi, "
                            'M.: Thermostable NAD(+)-dependent alcohol '
                            'dehydrogenase from Sulfolobus solfataricus: gene '
                            'and protein sequence determination and '
                            'relationship to other alcohol dehydrogenases. '
                            'Biochemistry (1992) 31, 12514-12523.',
                    'pubmed': 1463738},
               71: {'info': 'Tihanyi, K.; Talbot, B.; Brzezinski, R.; Thirion, '
                            'J.P.: Purification and characterization of '
                            'alcohol dehydrogenase from soybean. '
                            'Phytochemistry (1989) 28, 1335-1338.'},
               72: {'info': 'Liang, Z.Q.; Hayase, F.; Nishimura, T.; Kato, H.: '
                            'Purification and characterization of '
                            'NAD-dependent alcohol dehydrogenase and '
                            'NADH-dependent 2-oxoaldehyde reductase from '
                            'parsley. Agric. Biol. Chem. (1990) 54, '
                            '1717-1719.'},
               73: {'info': 'Hatanaka, A.; Harada, T.: Purification and '
                            'properties of alcohol dehydrogenase from tea '
                            'seeds. Agric. Biol. Chem. (1972) 36, 2033-2035.'},
               74: {'info': 'Stiborova, M.; Leblova, S.: Kinetics of the '
                            'reaction catalysed by rape alcohol dehydrogenase. '
                            'Phytochemistry (1979) 18, 23-24.'},
               75: {'info': 'Lai, Y.K.; Chandlee, J.M.; Scandalios, J.G.: '
                            'Purification and characterization of three '
                            'non-allelic alcohol dehydrogenase isoenzymes in '
                            'maize. Biochim. Biophys. Acta (1982) 706, 9-18.'},
               76: {'info': 'Leblova, S.; Ehlichova, D.: Purification and some '
                            'properties of alcohol dehydrogenase from maize. '
                            'Phytochemistry (1972) 11, 1345-1346.'},
               77: {'info': 'Langston, P.J.; Pace, C.N.; Hart, G.E.: Wheat '
                            'alcohol dehydrogenase iszymes. Purification, '
                            'characterization, and gene expression. Plant '
                            'Physiol. (1980) 65, 518-522.',
                    'pubmed': 16661226},
               78: {'info': 'Langston, P.J.; Hart, G.E.; Pace, C.N.: '
                            'Purification and partial characterization of '
                            'alcohol dehydrogenase from wheat. Arch. Biochem. '
                            'Biophys. (1979) 196, 611-618.',
                    'pubmed': 485168},
               79: {'info': 'Mayne, M.G.; Lea, P.J.: Properties of three sets '
                            'of isoenzymes of alcohol dehydrogenase isolated '
                            'from barley (Hordeum vulgare). Phytochemistry '
                            '(1985) 24, 1433-1438.'},
               80: {'info': 'Shimomura, S.; Beevers, H.: Alcohol dehydrogenase '
                            'inactivator from rice seedlings. Properties and '
                            'intracellular location. Plant Physiol. (1983) 71, '
                            '742-746.',
                    'pubmed': 16662899},
               81: {'info': 'Creaser, E.H.; Porter, R.L.; Britt, K.A.; '
                            'Pateman, J.A.; Doy, C.H.: Purification and '
                            'preliminary characterization of alcohol '
                            'dehydrogenase from Aspergillus nidulans. Biochem. '
                            'J. (1985) 225, 449-454.',
                    'pubmed': 3156582},
               82: {'info': 'Yabe, M.; Shitara, K.; Kawashima, J.; Shinoyama, '
                            'H.; Ando, A.; Fujii, T.: Purification and '
                            'properties of an alcohol dehydrogenase isozyme '
                            'from a methanol-using yeast, Candida sp. N-16. '
                            'Biosci. Biotechnol. Biochem. (1992) 56, 338-339.'},
               83: {'info': 'Morosoli, R.; Begin-Heick, N.: The partial '
                            'purification and characterization of cytosol '
                            'alcohol dehydrogenase from Astasia. Biochem. J. '
                            '(1974) 141, 469-475.',
                    'pubmed': 4455216},
               84: {'info': 'Rudge, J.; Bickerstaff, G.F.: Purification and '
                            'properties of an alcohol dehydrogenase from '
                            'Sporotrichum pulverulentum. Enzyme Microb. '
                            'Technol. (1986) 8, 120-124.'},
               85: {'info': 'Indrati, R.; Ohita, Y.: Purification and '
                            'properties of alcohol dehydrogenase from a mutant '
                            'strain of Candida guilliermondii. Can. J. '
                            'Microbiol. (1992) 38, 953-957.'},
               86: {'info': 'Tkachenko, A.G.; Winston, G.W.: Interaction of '
                            'alcohol dehydrogenase with '
                            'tert-butylhydroperoxide: stimulation of the horse '
                            'liver and inhibition of the yeast enzyme. Arch. '
                            'Biochem. Biophys. (2000) 380, 165-173.',
                    'pubmed': 10900146},
               87: {'info': 'Drewke, C.; Ciriacy, M.: Overexpression, '
                            'purification and properties of alcohol '
                            'dehydrogenase IV from Saccharomyces cerevisiae. '
                            'Biochim. Biophys. Acta (1988) 950, 54-60.',
                    'pubmed': 3282541},
               88: {'info': 'Yamazaki, Y.; Maeda, H.; Satoh, A.; Hiromi, K.: A '
                            'kinetic study on the binding of monomeric and '
                            'polymeric derivatives of NAD+ to yeast alcohol '
                            'dehydrogenase. J. Biochem. (1984) 95, 109-115.',
                    'pubmed': 6368531},
               89: {'info': 'Mazid, M.A.; Laidler, K.J.: pH Dependence of free '
                            'and immobilized yeast alcohol dehydrogenase '
                            'kinetics. Can. J. Microbiol. (1982) 60, 100-107.',
                    'pubmed': 7044497},
               90: {'info': 'Dickinson, F.M.; Monger, G.P.: A study of the '
                            'kinetics and mechanism of yeast alcohol '
                            'dehydrogenase with a variety of substrates. '
                            'Biochem. J. (1973) 131, 261-270.',
                    'pubmed': 4352908},
               91: {'info': 'Ganzhorn, A.J.; Green, D.W.; Hershey, A.D.; '
                            'Gould, R.M.; Plapp, B.V.: Kinetic '
                            'characterization of yeast alcohol dehydrogenases. '
                            'Amino acid residue 294 and substrate specificity. '
                            'J. Biol. Chem. (1987) 262, 3754-3761.',
                    'pubmed': 3546317},
               92: {'info': 'Weinhold, E.G.; Benner, S.A.: Engineering yeast '
                            'alcohol dehydrogenase. Replacing Trp54 by Leu '
                            'broadens substrate specificity. Protein Eng. '
                            '(1995) 8, 457-461.',
                    'pubmed': 8532667},
               93: {'info': 'Pocker, Y.; Li, H.: Mechanistic enzymology of '
                            'liver alcohol dehydrogenase. Kinetic and '
                            'stereochemical characterization of retinal '
                            'oxidation and reduction. Adv. Exp.Med. Biol. '
                            '(1996) 6, 331-338.',
                    'pubmed': 9059637},
               94: {'info': 'Leskovac, V.; Trivic, S.; Anderson, B.M.: Use of '
                            'competitive dead-end inhibitors to determine the '
                            'chemical mechanism of action of yeast alcohol '
                            'dehydrogenase. Mol. Cell. Biochem. (1998) 178, '
                            '219-227.',
                    'pubmed': 9546603},
               95: {'info': 'Keung, W.M.: Isolation and characterization of '
                            'three alcohol dehydrogenase isozymes from Syrian '
                            'golden hamster. Alcohol. Clin. Exp. Res. (1996) '
                            '20, 213-220.',
                    'pubmed': 8730210},
               96: {'info': 'Yin, S.J.; Wang, M.F.; Liao, C.S.; Chen, C.M.; '
                            'Wu, C.W.: Identification of a human stomach '
                            'alcohol dehydrogenase with distinctive kinetic '
                            'properties. Biochem. Int. (1990) 22, 829-835.',
                    'pubmed': 2099148},
               97: {'info': 'Osterman, J.C.; Chiang, Y.; Markwell, J.: '
                            'Characterization of mutation-induced changes in '
                            'the maize (Zea mays L.) ADH1-1S1108 alcohol '
                            'dehydrogenase. Biochem. Genet. (1993) 31, '
                            '497-506.',
                    'pubmed': 8166623},
               98: {'info': 'Langeland, B.T.; Morris, D.L.; McKinley-McKee, '
                            'J.S.: Metal binding properties of thiols: '
                            'complexes with horse liver alcohol dehydrogenase. '
                            'Comp. Biochem. Physiol. B (1999) 123, 155-162.',
                    'pubmed': 10425719},
               99: {'info': 'Hensgens, C.M.H.; Vonck, J.; van Beeumen, J.; '
                            'Bruggen, E.F.J.; Hansen, T.A.: Purification and '
                            'characterization of an oxygen-labile, '
                            'NAD-dependent alcohol dehydrogenase from '
                            'Desulfovibrio gigas. J. Bacteriol. (1993) 175, '
                            '2859-2863.',
                    'pubmed': 8491707},
               100: {'info': 'Flores, B.M.; Stanley, S.L.; Yong, T.S.; Ali, '
                             'M.; Yang, W.; Diedrich, D.L.; Torian, B.E.: '
                             'Surface localization, regulation, and biologic '
                             'properties of the 96-kDA alcohol/aldehyde '
                             'dehydrogenase (EhADH2) of pathogenic Entamoeba '
                             'histolytica. J. Infect. Dis. (1996) 173, '
                             '226-231.',
                     'pubmed': 8537663},
               101: {'info': 'Persson, B.; Bergman, T.; Keung, W.M.; '
                             'Waldenstroem, U.; Holmquist, B.; Vallee, B.L.; '
                             'Joernvall, H.: Basic features of class-I alcohol '
                             'dehydrogenase variable and constant segments '
                             'coordinated by inter-class and intra-class '
                             'variabvility. Conclusions from characterization '
                             'of the alligator enzyme. Eur. J. Biochem. (1993) '
                             '216, 49-56.',
                     'pubmed': 8365416},
               102: {'info': 'Gergel, D.; Cederbaum, A.I.: Inhibition of the '
                             'catalytic activity of alcohol dehydrogenase by '
                             'nitric oxide is associated with S nitrosylation '
                             'and the release of zinc. Biochemistry (1996) 35, '
                             '16186-16194.',
                     'pubmed': 8973191},
               103: {'info': 'Lamed, R.; Zeikus, J.G.: Ethanol production by '
                             'thermophilic bacteria: relationship between '
                             'fermentation product yields of and catabolic '
                             'enzyme activities in Clostridium thermocellum '
                             'and Thermoanaerobium brockii. J. Bacteriol. '
                             '(1980) 144, 569-578.',
                     'pubmed': 7430065},
               105: {'info': 'Hadizadeh, M.; Keyhani, E.: Detection and '
                             'kinetic properties of alcohol dehydrogenase in '
                             'dormant corm of Crocus sativus L. Acta Hortic. '
                             '(2004) 650, 127-139.'},
               108: {'info': 'Esposito, L.; Bruno, I.; Sica, F.; Raia, C.A.; '
                             'Giordano, A.; Rossi, M.; Mazzarella, L.; Zagari, '
                             'A.: Crystal structure of a ternary complex of '
                             'the alcohol dehydrogenase from Sulfolobus '
                             'solfataricus. Biochemistry (2003) 42, '
                             '14397-14407.',
                     'pubmed': 14661950},
               110: {'info': 'Stroemberg, P.; Svensson, S.; Berst, K.B.; '
                             'Plapp, B.V.; Höög, J.O.: Enzymatic mechanism of '
                             'low-activity mouse alcohol dehydrogenase 2. '
                             'Biochemistry (2004) 43, 1323-1328.',
                     'pubmed': 14756569},
               111: {'info': 'LeBrun, L.A.; Park, D.H.; Ramaswamy, S.; Plapp, '
                             'B.V.: Participation of histidine-51 in catalysis '
                             'by horse liver alcohol dehydrogenase. '
                             'Biochemistry (2004) 43, 3014-3026.',
                     'pubmed': 15023053},
               112: {'info': 'Ceccarelli, C.; Liang, Z.X.; Strickler, M.; '
                             'Prehna, G.; Goldstein, B.M.; Klinman, J.P.; '
                             'Bahnson, B.J.: Crystal structure and amide H/D '
                             'exchange of binary complexes of alcohol '
                             'dehydrogenase from Bacillus stearothermophilus: '
                             'insight into thermostability and cofactor '
                             'binding. Biochemistry (2004) 43, 5266-5277.',
                     'pubmed': 15122892},
               113: {'info': 'Chinnawirotpisan, P.; Matsushita, K.; Toyama, '
                             'H.; Adachi, O.; Limtong, S.; Theeragool, G.: '
                             'Purification and characterization of two '
                             'NAD-dependent alcohol dehydrogenases (ADHs) '
                             'induced in the quinoprotein ADH-deficient mutant '
                             'of Acetobacter pasteurianus SKU1108. Biosci. '
                             'Biotechnol. Biochem. (2003) 67, 958-965.',
                     'pubmed': 12834271},
               114: {'info': 'Kosjek, B.; Stampfer, W.; Pogorevc, M.; '
                             'Goessler, W.; Faber, K.; Kroutil, W.: '
                             'Purification and characterization of a '
                             'chemotolerant alcohol dehydrogenase applicable '
                             'to coupled redox reactions. Biotechnol. Bioeng. '
                             '(2004) 86, 55-62.',
                     'pubmed': 15007841},
               115: {'info': 'Stroemberg, P.; Svensson, S.; Hedberg, J.J.; '
                             'Nordling, E.; Hoog, J.O.: Identification and '
                             'characterisation of two allelic forms of human '
                             'alcohol dehydrogenase 2. Cell. Mol. Life Sci. '
                             '(2002) 59, 552-559.',
                     'pubmed': 11964133},
               116: {'info': 'Plapp, B.V.; Berst, K.B.: Specificity of human '
                             'alcohol dehydrogenase 1C*2 (gamma2gamma2) for '
                             'steroids and simulation of the uncompetitive '
                             'inhibition of ethanol metabolism. Chem. Biol. '
                             'Interact. (2003) 143-144, 183-193.',
                     'pubmed': 12604203},
               117: {'info': 'Fontaine, F.R.; Dunlop, R.A.; Petersen, D.R.; '
                             'Burcham, P.C.: Oxidative bioactivation of crotyl '
                             'alcohol to the toxic endogenous aldehyde '
                             'crotonaldehyde: association of protein '
                             'carbonylation with toxicity in mouse '
                             'hepatocytes. Chem. Res. Toxicol. (2002) 15, '
                             '1051-1058.',
                     'pubmed': 12184789},
               118: {'info': 'Yoon, S.Y.; Noh, H.S.; Kim, E.H.; Kong, K.H.: '
                             'The highly stable alcohol dehydrogenase of '
                             'Thermomicrobium roseum: purification and '
                             'molecular characterization. Comp. Biochem. '
                             'Physiol. B (2002) 132, 415-422.',
                     'pubmed': 12031468},
               120: {'info': 'Leskovac, V.; Trivic, S.; Pericin, D.: The three '
                             'zinc-containing alcohol dehydrogenases from '
                             "bakers' yeast, Saccharomyces cerevisiae. FEMS "
                             'Yeast Res. (2002) 2, 481-494.',
                     'pubmed': 12702265},
               121: {'info': 'Miroliaei, M.; Nemat-Gorgani, M.: Effect of '
                             'organic solvents on stability and activity of '
                             'two related alcohol dehydrogenases: a '
                             'comparative study. Int. J. Biochem. Cell Biol. '
                             '(2002) 34, 169-175.',
                     'pubmed': 11809419},
               124: {'info': 'Chou, C.F.; Lai, C.L.; Chang, Y.C.; Duester, G.; '
                             'Yin, S.J.: Kinetic mechanism of human class IV '
                             'alcohol dehydrogenase functioning as retinol '
                             'dehydrogenase. J. Biol. Chem. (2002) 277, '
                             '25209-25216.',
                     'pubmed': 11997393},
               125: {'info': 'Rosell, A.; Valencia, E.; Ochoa, W.F.; Fita, I.; '
                             'Pares, X.; Farres, J.: Complete reversal of '
                             'coenzyme specificity by concerted mutation of '
                             'three consecutive residues in alcohol '
                             'dehydrogenase. J. Biol. Chem. (2003) 278, '
                             '40573-40580.',
                     'pubmed': 12902331},
               126: {'info': 'Shim, E.J.; Jeon, S.H.; Kong, K.H.: '
                             'Overexpression, purification, and biochemical '
                             'characterization of the thermostable '
                             'NAD-dependent alcohol dehydrogenase from '
                             'Bacillus stearothermophilus. J. Microbiol. '
                             'Biotechnol. (2003) 13, 738-744.'},
               127: {'info': 'Guy, J.E.; Isupov, M.N.; Littlechild, J.A.: The '
                             'structure of an alcohol dehydrogenase from the '
                             'hyperthermophilic archaeon Aeropyrum pernix. J. '
                             'Mol. Biol. (2003) 331, 1041-1051.',
                     'pubmed': 12927540},
               128: {'info': 'Avila, E.E.; Martinez-Alcaraz, E.R.; '
                             'Barbosa-Sabanero, G.; Rivera-Baron, E.I.; '
                             'Arias-Negrete, S.; Zazueta-Sandoval, R.: '
                             'Subcellular localization of the NAD+-dependent '
                             'alcohol dehydrogenase in Entamoeba histolytica '
                             'trophozoites. J. Parasitol. (2002) 88, 217-222.',
                     'pubmed': 12058720},
               129: {'info': 'Levin, I.; Meiri, G.; Peretz, M.; Burstein, Y.; '
                             'Frolow, F.: The ternary complex of Pseudomonas '
                             'aeruginosa alcohol dehydrogenase with NADH and '
                             'ethylene glycol. Protein Sci. (2004) 13, '
                             '1547-1556.',
                     'pubmed': 15152088},
               130: {'info': 'Koumanov, A.; Benach, J.; Atrian, S.; '
                             'Gonzalez-Duarte, R.; Karshikoff, A.; Ladenstein, '
                             'R.: The catalytic mechanism of Drosophila '
                             'alcohol dehydrogenase: evidence for a proton '
                             'relay modulated by the coupled ionization of the '
                             'active site lysine/tyrosine pair and a NAD+ '
                             'ribose OH switch. Proteins (2003) 51, 289-298.',
                     'pubmed': 12660997},
               135: {'info': 'Nosova, T.; Jousimies-Somer, H.; Kaihovaara, P.; '
                             'Jokelainen, K.; Heine, R.; Salaspuro, M.: '
                             'Characteristics of alcohol dehydrogenases of '
                             'certain aerobic bacteria representing human '
                             'colonic flora. Alcohol. Clin. Exp. Res. (1997) '
                             '21, 489-494.',
                     'pubmed': 9161610},
               136: {'info': 'Duron-Castellanos, A.; Zazueta-Novoa, V.; '
                             'Silva-Jimenez, H.; Alvarado-Caudillo, Y.; Pena '
                             'Cabrera, E.; Zazueta-Sandoval, R.: Detection of '
                             'NAD+dependent alcohol dehydrogenase activities '
                             'in YR-1 strain of Mucor circinelloides, a '
                             'potential bioremediator of petroleum '
                             'contaminated soils. Appl. Biochem. Biotechnol. '
                             '(2005) 121-124, 279-288.',
                     'pubmed': 15917606},
               137: {'info': 'Inoue, K.; Makino, Y.; Itoh, N.: Purification '
                             'and characterization of a novel alcohol '
                             'dehydrogenase from Leifsonia sp. strain S749: a '
                             'promising biocatalyst for an asymmetric hydrogen '
                             'transfer bioreduction. Appl. Environ. Microbiol. '
                             '(2005) 71, 3633-3641.',
                     'pubmed': 16000771},
               138: {'info': 'Machielsen, R.; Uria, A.R.; Kengen, S.W.; van '
                             'der Oost, J.: Production and characterization of '
                             'a thermostable alcohol dehydrogenase that '
                             'belongs to the aldo-keto reductase uperfamily. '
                             'Appl. Environ. Microbiol. (2006) 72, 233-238.',
                     'pubmed': 16391048},
               139: {'info': 'Park, H.; Kidman, G.; Northrop, D.B.: Effects of '
                             'pressure on deuterium isotope effects of yeast '
                             'alcohol dehydrogenase using alternative '
                             'substrates. Arch. Biochem. Biophys. (2005) 433, '
                             '335-340.',
                     'pubmed': 15581588},
               140: {'info': 'Kalnenieks, U.; Galinina, N.; Toma, M.M.: '
                             'Physiological regulation of the properties of '
                             'alcohol dehydrogenase II (ADH II) of Zymomonas '
                             'mobilis: NADH renders ADH II resistant to '
                             'cyanide and aeration. Arch. Microbiol. (2005) '
                             '183, 450-455.',
                     'pubmed': 16027951},
               141: {'info': 'Haseba, T.; Duester, G.; Shimizu, A.; Yamamoto, '
                             'I.; Kameyama, K.; Ohno, Y.: In vivo contribution '
                             'of class III alcohol dehydrogenase (ADH3) to '
                             'alcohol metabolism through activation by '
                             'cytoplasmic solution hydrophobicity. Biochim. '
                             'Biophys. Acta (2006) 1762, 276-283.',
                     'pubmed': 16431092},
               143: {'info': 'Negoro, M.; Wakabayashi, I.: Enhancement of '
                             'alcohol dehydrogenase activity in vitro by '
                             'acetylsalicylic acid. Eur. J. Pharmacol. (2005) '
                             '523, 25-28.',
                     'pubmed': 16226743},
               144: {'info': 'Kazuoka, T.; Oikawa, T.; Muraoka, I.; Kuroda, '
                             'S.; Soda, K.: A cold-active and thermostable '
                             'alcohol dehydrogenase of a psychrotorelant from '
                             'Antarctic seawater, Flavobacterium frigidimaris '
                             'KUC-1. Extremophiles (2007) 11, 257-267.',
                     'pubmed': 17072683},
               146: {'info': 'Defilippi, B.G.; Dandekar, A.M.; Kader, A.A.: '
                             'Relationship of ethylene biosynthesis to '
                             'volatile production, related enzymes, and '
                             'precursor availability in apple peel and flesh '
                             'tissues. J. Agric. Food Chem. (2005) 53, '
                             '3133-3141.',
                     'pubmed': 15826070},
               147: {'info': 'Koutsompogeras, P.; Kyriacou, A.; Zabetakis, I.: '
                             'Characterizing NAD-dependent alcohol '
                             'dehydrogenase enzymes of Methylobacterium '
                             'extorquens and strawberry (Fragaria x ananassa '
                             'cv. Elsanta). J. Agric. Food Chem. (2006) 54, '
                             '235-242.',
                     'pubmed': 16390205},
               148: {'info': 'Ikegaya, K.: Kinetic analysis about the effects '
                             'of neutral salts on the thermal stability of '
                             'yeast alcohol dehydrogenase. J. Biochem. (2005) '
                             '137, 349-354.',
                     'pubmed': 15809336},
               149: {'info': 'Hirano, J.; Miyamoto, K.; Ohta, H.: Purification '
                             'and characterization of the alcohol '
                             'dehydrogenase with a broad substrate specificity '
                             'originated from 2-phenylethanol-assimilating '
                             'Brevibacterium sp. KU 1309. J. Biosci. Bioeng. '
                             '(2005) 100, 318-322.',
                     'pubmed': 16243283},
               151: {'info': 'Manriquez, D.; El-Sharkawy, I.; Flores, F.B.; '
                             'El-Yahyaoui, F.; Regad, F.; Bouzayen, M.; '
                             'Latche, A.; Pech, J.C.: Two highly divergent '
                             'alcohol dehydrogenases of melon exhibit fruit '
                             'ripening-specific expression and distinct '
                             'biochemical characteristics. Plant Mol. Biol. '
                             '(2006) 61, 675-685.',
                     'pubmed': 16897483},
               152: {'info': 'Sica, F.; Demasi, D.; Mazzarella, D.L.; Zagari, '
                             "A.; Capasso, S.; Pearl, L.H.; D'Auria, S.; Raia, "
                             'C.A.; Rossi, M.: Elimination of twinning in '
                             'crystals of Sulfolobus sofataricus alcohol '
                             'dehydrogenase holo-enzyme by growth in agarose '
                             'gels. Acta Crystallogr. Sect. D (1994) 50, '
                             '508-511.',
                     'pubmed': 15299411},
               153: {'info': 'Raia, C.A.; Caruso, C.; Marino, M.; Vespa, N.; '
                             'Rossi, M.: Activation of Sulfolobus solfataricus '
                             'alcohol dehydrogenase by modification of '
                             'cysteine residue 38 with iodoacetic acid. '
                             'Biochemistry (1996) 35, 638-647.',
                     'pubmed': 8555238},
               154: {'info': 'Giordano, A.; Cannio, R.; La Cara, F.; '
                             'Bartolucci, S.; Rossi, M.; Raia, C.A.: Asn249Tyr '
                             'substitution at the coenzyme binding domain '
                             'activates Sulfolobus solfataricus alcohol '
                             'dehydrogenase and increases its thermal '
                             'stability.. Biochemistry (1999) 38, 3043-3054.',
                     'pubmed': 10074357},
               156: {'info': 'Tasaki, Y.; Yoshikawa, H.; Tamura, H.: Isolation '
                             'and characterization of an alcohol dehydrogenase '
                             'gene from the octylphenol polyethoxylate '
                             'degrader Pseudomonas putida S-5. Biosci. '
                             'Biotechnol. Biochem. (2006) 70, 1855-1863.',
                     'pubmed': 16926497},
               157: {'info': 'Esposito, L.; Bruno, I.; Sica, F.; Raia, C.A.; '
                             'Giordano, A.; Rossi, M.; Mazzarella, L.; Zagari, '
                             'A.: Structural study of a single-point mutant of '
                             'Sulfolobus solfataricus alcohol dehydrogenase '
                             'with enhanced activity.. FEBS Lett. (2003) 539, '
                             '14-18.',
                     'pubmed': 12650918},
               158: {'info': 'Cannio, R.; Fiorentino, G.; Rossi, M.; '
                             'Bartolucci, S.: The alcohol dehydrogenase gene: '
                             'distribution among Sulfolobales and regulation '
                             'in Sulfolobus solfataricus. FEMS Microbiol. '
                             'Lett. (1999) 170, 31-39.',
                     'pubmed': 9919650},
               159: {'info': 'Cannio, R.; Fiorentino, G.; Carpinelli, P.; '
                             'Rossi, M.; Bartolucci, S.: Cloning and '
                             'overexpression in Escherichia coli of the genes '
                             'encoding NAD-dependent alcohol dehydrogenase '
                             'from two Sulfolobus species. J. Bacteriol. '
                             '(1996) 178, 301-305.',
                     'pubmed': 8550434},
               161: {'info': 'Esposito, L.; Sica, F.; Raia, C.A.; Giordano, '
                             'A.; Rossi, M.; Mazzarella, L.; Zagari, A.: '
                             'Crystal structure of the alcohol dehydrogenase '
                             'from the hyperthermophilic archaeon Sulfolobus '
                             'solfataricus at 1.85 A resolution. J. Mol. Biol. '
                             '(2002) 318, 463-477.',
                     'pubmed': 12051852},
               162: {'info': 'Chong, P.K.; Burja, A.M.; Radianingtyas, H.; '
                             'Fazeli, A.; Wright, P.C.: Proteome and '
                             'transcriptional analysis of ethanol-grown '
                             'Sulfolobus solfataricus P2 reveals ADH2, a '
                             'potential alcohol dehydrogenase. J. Proteome '
                             'Res. (2007) 6, 3985-3994.',
                     'pubmed': 17824633},
               163: {'info': 'Raia, C.A.; Giordano, A.; Rossi, M.: Alcohol '
                             'dehydrogenase from Sulfolobus solfataricus. '
                             'Methods Enzymol. (2001) 331, 176-195.',
                     'pubmed': 11265460},
               164: {'info': 'Casadio, R.; Martelli, P.L.; Giordano, A.; '
                             'Rossi, M.; Raia, C.A.: A low-resolution 3D model '
                             'of the tetrameric alcohol dehydrogenase from '
                             'Sulfolobus solfataricus. Protein Eng. (2002) 15, '
                             '215-223.',
                     'pubmed': 11932492},
               165: {'info': 'Ammendola, S.; Raucci, G.; Incani, O.; Mele, A.; '
                             'Tramontano, A.; Wallace, A.: Replacing the '
                             'glutamate ligand in the structural zinc site of '
                             'Sulfolobus solfataricus alcohol dehydrogenase '
                             'with a cysteine decreases thermostability.. '
                             'Protein Eng. (1995) 8, 31-37.',
                     'pubmed': 7770449},
               169: {'info': 'Pennacchio, A.; Pucci, B.; Secundo, F.; La Cara, '
                             'F.; Rossi, M.; Raia, C.A.: Purification and '
                             'characterization of a novel recombinant highly '
                             'enantioselective short-chain NAD(H)-dependent '
                             'alcohol dehydrogenase from Thermus thermophilus. '
                             'Appl. Environ. Microbiol. (2008) 74, 3949-3958.',
                     'pubmed': 18456852},
               171: {'info': 'Kotrbova-Kozak, A.; Kotrba, P.; Inui, M.; '
                             'Sajdok, J.; Yukawa, H.: Transcriptionally '
                             'regulated adhA gene encodes alcohol '
                             'dehydrogenase required for ethanol and '
                             'n-propanol utilization in Corynebacterium '
                             'glutamicum R. Appl. Microbiol. Biotechnol. '
                             '(2007) 76, 1347-1356.',
                     'pubmed': 17646983},
               172: {'info': 'Park, Y.C.; San, K.Y.; Bennett, G.N.: '
                             'Characterization of alcohol dehydrogenase 1 and '
                             '3 from Neurospora crassa FGSC2489. Appl. '
                             'Microbiol. Biotechnol. (2007) 76, 349-356.',
                     'pubmed': 17516063},
               173: {'info': 'Hess, M.; Antranikian, G.: Archaeal alcohol '
                             'dehydrogenase active at increased temperatures '
                             'and in the presence of organic solvents. Appl. '
                             'Microbiol. Biotechnol. (2008) 77, 1003-1013.',
                     'pubmed': 17989975},
               174: {'info': 'Crichton, P.G.; Affourtit, C.; Moore, A.L.: '
                             'Identification of a mitochondrial alcohol '
                             'dehydrogenase in Schizosaccharomyces pombe: new '
                             'insights into energy metabolism. Biochem. J. '
                             '(2007) 401, 459-464.',
                     'pubmed': 16999687},
               177: {'info': 'Lertwattanasakul, N.; Sootsuwan, K.; Limtong, '
                             'S.; Thanonkeo, P.; Yamada, M.: Comparison of the '
                             'gene expression patterns of alcohol '
                             'dehydrogenase isozymes in the thermotolerant '
                             'yeast Kluyveromyces marxianus and their '
                             'physiological functions. Biosci. Biotechnol. '
                             'Biochem. (2007) 71, 1170-1182.',
                     'pubmed': 17485854},
               180: {'info': 'Jelski, W.; Zalewski, B.; Szmitkowski, M.: The '
                             'activity of class I, II, III, and IV alcohol '
                             'dehydrogenase (ADH) isoenzymes and aldehyde '
                             'dehydrogenase (ALDH) in liver cancer. Digest. '
                             'Dis. Sci. (2008) 53, 2550-2555.',
                     'pubmed': 18224440},
               181: {'info': 'Cao, Y.; Liao, L.; Xu, X.W.; Oren, A.; Wang, C.; '
                             'Zhu, X.F.; Wu, M.: Characterization of alcohol '
                             'dehydrogenase from the haloalkaliphilic archaeon '
                             'Natronomonas pharaonis. Extremophiles (2008) 12, '
                             '471-476.',
                     'pubmed': 18189118},
               185: {'info': 'Yamada-Onodera, K.; Fukui, M.; Tani, Y.: '
                             'Purification and characterization of alcohol '
                             'dehydrogenase reducing N-benzyl-3-pyrrolidinone '
                             'from Geotrichum capitatum. J. Biosci. Bioeng. '
                             '(2007) 103, 174-178.',
                     'pubmed': 17368401},
               188: {'info': 'Kizaki, N.; Yasohara, Y.; Nagashima, N.; '
                             'Hasegawa, J.: Characterization of novel alcohol '
                             'dehydrogenase of Devosia riboflavina involved in '
                             'stereoselective reduction of 3-pyrrolidinone '
                             'derivatives. J. Mol. Catal. B (2008) 51, 73-80.'},
               194: {'info': 'Jelski, W.; Szmitkowski, M.: Alcohol '
                             'dehydrogenase (ADH) and aldehyde dehydrogenase '
                             '(ALDH) in the cancer diseases. Clin. Chim. Acta '
                             '(2008) 395, 1-5.',
                     'pubmed': 18505683},
               195: {'info': 'Peng, H.; Wu, G.; Shao, W.: The aldehyde/alcohol '
                             'dehydrogenase (AdhE) in relation to the ethanol '
                             'formation in Thermoanaerobacter ethanolicus '
                             'JW200. Anaerobe (2008) 14, 125-127.',
                     'pubmed': 17981479},
               196: {'info': 'Zhao, Q.; Hou, Y.; Gong, G.H.; Yu, M.A.; Jiang, '
                             'L.; Liao, F.: Characterization of alcohol '
                             'dehydrogenase from permeabilized brewers yeast '
                             'cells immobilized on the derived attapulgite '
                             'nanofibers. Appl. Biochem. Biotechnol. (2009) '
                             '160, 2287-2299.',
                     'pubmed': 19578994},
               197: {'info': 'Hoellrigl, V.; Hollmann, F.; Kleeb, A.C.; '
                             'Buehler, K.; Schmid, A.: TADH, the thermostable '
                             'alcohol dehydrogenase from Thermus sp. ATN1: a '
                             'versatile new biocatalyst for organic synthesis. '
                             'Appl. Microbiol. Biotechnol. (2008) 81, 263-273.',
                     'pubmed': 18704396},
               198: {'info': 'Plapp, B.V.: Conformational changes and '
                             'catalysis by alcohol dehydrogenase. Arch. '
                             'Biochem. Biophys. (2010) 493, 3-12.',
                     'pubmed': 19583966},
               200: {'info': 'Staab, C.A.; Hellgren, M.; Hoeoeg, J.O.: Medium- '
                             'and short-chain dehydrogenase/reductase gene and '
                             'protein families: Dual functions of alcohol '
                             'dehydrogenase 3: implications with focus on '
                             'formaldehyde dehydrogenase and '
                             'S-nitrosoglutathione reductase activities. Cell. '
                             'Mol. Life Sci. (2008) 65, 3950-3960.',
                     'pubmed': 19011746},
               201: {'info': 'Bergman, T.; Zhang, K.; Palmberg, C.; Joernvall, '
                             'H.; Auld, D.S.: Zinc binding to peptide analogs '
                             'of the structural zinc site in alcohol '
                             'dehydrogenase: implications for an entatic '
                             'state. Cell. Mol. Life Sci. (2008) 65, '
                             '4019-4027.',
                     'pubmed': 18850316},
               202: {'info': 'Pal, S.; Park, D.H.; Plapp, B.V.: Activity of '
                             'yeast alcohol dehydrogenases on benzyl alcohols '
                             'and benzaldehydes: characterization of ADH1 from '
                             'Saccharomyces carlsbergensis and transition '
                             'state analysis. Chem. Biol. Interact. (2009) '
                             '178, 16-23.',
                     'pubmed': 19022233},
               203: {'info': 'Miyawaki, O.; Ma, G.; Horie, T.; Hibi, A.; '
                             'Ishikawa, T.; Kimura, S.: Thermodynamic, '
                             'kinetic, and operational stabilities of yeast '
                             'alcohol dehydrogenase in sugar and compatible '
                             'osmolyte solutions. Enzyme Microb. Technol. '
                             '(2008) 43, 495-499.'},
               204: {'info': 'Cea, G.; Wilson, L.; Bolivar, J.; Markovits, A.; '
                             'Illanes, A.: Effect of chain length on the '
                             'activity of free and immobilized alcohol '
                             'dehydrogenase towards aliphatic alcohols. Enzyme '
                             'Microb. Technol. (2009) 44, 135-138.'},
               205: {'info': 'Barzegar, A.; Moosavi-Movahedi, A.; Pedersen, '
                             'J.; Miroliaei, M.: Comparative thermostability '
                             'of mesophilic and thermophilic alcohol '
                             'dehydrogenases: Stability-determining roles of '
                             'proline residues and loop conformations. Enzyme '
                             'Microb. Technol. (2009) 45, 73-79.'},
               206: {'info': 'Jelski, W.; Orywal, K.; Panek, B.; Gacko, M.; '
                             'Mroczko, B.; Szmitkowski, M.: The activity of '
                             'class I, II, III and IV of alcohol dehydrogenase '
                             '(ADH) isoenzymes and aldehyde dehydrogenase '
                             '(ALDH) in the wall of abdominal aortic '
                             'aneurysms. Exp. Mol. Pathol. (2009) 87, 59-62.',
                     'pubmed': 19332052},
               207: {'info': 'Pennacchio, A.; Esposito, L.; Zagari, A.; Rossi, '
                             'M.; Raia, C.A.: Role of Tryptophan 95 in '
                             'substrate specificity and structural stability '
                             'of Sulfolobus solfataricus alcohol '
                             'dehydrogenase. Extremophiles (2009) 13, 751-761.',
                     'pubmed': 19588068},
               208: {'info': 'Carvalho, E.; Solferini, V.; Matioli, S.: '
                             'Alcohol dehydrogenase activities and ethanol '
                             'tolerance in Anastrepha (Diptera, Tephritidae) '
                             'fruit-fly species and their hybrids. Genet. Mol. '
                             'Biol. (2009) 32, 177-185.',
                     'pubmed': 21637665},
               209: {'info': 'Devi, P.G.; Chakraborty, P.K.; Dasgupta, D.: '
                             'Inhibition of a Zn(II)-containing enzyme, '
                             'alcohol dehydrogenase, by anticancer '
                             'antibiotics, mithramycin and chromomycin A3. J. '
                             'Biol. Inorg. Chem. (2009) 14, 347-359.',
                     'pubmed': 19034537},
               210: {'info': 'Jeon, Y.J.; Fong, J.C.; Riyanti, E.I.; Neilan, '
                             'B.A.; Rogers, P.L.; Svenson, C.J.: Heterologous '
                             'expression of the alcohol dehydrogenase (adhI) '
                             'gene from Geobacillus thermoglucosidasius strain '
                             'M10EXG. J. Biotechnol. (2008) 135, 127-133.',
                     'pubmed': 18436321},
               211: {'info': 'Palma-Gutierrez, H.; Rodriguez-Zavala, J.; '
                             'Jasso-Chavez, R.; Moreno-Sanchez, R.; Saavedra, '
                             'E.: Gene cloning and biochemical '
                             'characterization of an alcohol dehydrogenase '
                             'from Euglena gracilis. J. Eukaryot. Microbiol. '
                             '(2008) 55, 554-561.',
                     'pubmed': 19120802},
               212: {'info': 'Haseba, T.; Sugimoto, J.; Sato, S.; Abe, Y.; '
                             'Ohno, Y.: Phytophenols in whisky lower blood '
                             'acetaldehyde level by depressing alcohol '
                             'metabolism through inhibition of alcohol '
                             'dehydrogenase 1 (class I) in mice. Metab. Clin. '
                             'Exp. (2008) 57, 1753-1759.',
                     'pubmed': 19013301},
               213: {'info': 'Marino-Marmolejo, E.N.; De Leon-Rodriguez, A.; '
                             'de la Rosa, A.P.; Santos, L.: Heterologous '
                             'expression and characterization of an alcohol '
                             'dehydrogenase from the archeon Thermoplasma '
                             'acidophilum. Mol. Biotechnol. (2009) 42, 61-67.',
                     'pubmed': 19058034},
               214: {'info': 'Kollock, R.; Frank, H.; Seidel, A.; Meinl, W.; '
                             'Glatt, H.: Oxidation of alcohols and reduction '
                             'of aldehydes derived from methyl- and '
                             'dimethylpyrenes by cDNA-expressed human alcohol '
                             'dehydrogenases. Toxicology (2008) 245, 65-75.',
                     'pubmed': 18242813},
               215: {'info': 'Liu, X.; Dong, Y.; Zhang, J.; Zhang, A.; Wang, '
                             'L.; Feng, L.: Two novel metal-independent '
                             'long-chain alkyl alcohol dehydrogenases from '
                             'Geobacillus thermodenitrificans NG80-2. '
                             'Microbiology (2009) 155, 2078-2085.',
                     'pubmed': 19383697},
               217: {'info': 'Yanai, H.; Doi, K.; Ohshima, T.: Sulfolobus '
                             'tokodaii ST0053 produces a novel thermostable, '
                             'NAD-dependent medium-chain alcohol '
                             'dehydrogenase. Appl. Environ. Microbiol. (2009) '
                             '75, 1758-1763.',
                     'pubmed': 19139244},
               218: {'info': 'Pennacchio, A.; Sannino, V.; Sorrentino, G.; '
                             'Rossi, M.; Raia, C.A.; Esposito, L.: Biochemical '
                             'and structural characterization of recombinant '
                             'short-chain NAD(H)-dependent '
                             'dehydrogenase/reductase from Sulfolobus '
                             'acidocaldarius highly enantioselective on diaryl '
                             'diketone benzil. Appl. Microbiol. Biotechnol. '
                             '(2013) 97, 3949-3964.',
                     'pubmed': 22805786},
               219: {'info': 'Pennacchio, A.; Giordano, A.; Pucci, B.; Rossi, '
                             'M.; Raia, C.A.: Biochemical characterization of '
                             'a recombinant short-chain NAD(H)-dependent '
                             'dehydrogenase/reductase from Sulfolobus '
                             'acidocaldarius. Extremophiles (2010) 14, '
                             '193-204.',
                     'pubmed': 20049620},
               220: {'info': 'Giordano, A.; Raia, C.A.: Steady-state '
                             'fluorescence properties of S. solfataricus '
                             'alcohol dehydrogenase and its selenomethionyl '
                             'derivative. J. Fluoresc. (2003) 13, 17-24.'},
               221: {'info': 'Giordano, A.; Russo, C.; Raia, C.A.; Kuznetsova, '
                             'I.M.; Stepanenko, O.V.; Turoverov, K.K.: Highly '
                             'UV-absorbing complex in '
                             'selenomethionine-substituted alcohol '
                             'dehydrogenase from Sulfolobus solfataricus. J. '
                             'Proteome Res. (2004) 3, 613-620.',
                     'pubmed': 15253444},
               222: {'info': 'Suwannarangsee, S.; Kim, S.; Kim, O.C.; Oh, '
                             'D.B.; Seo, J.W.; Kim, C.H.; Rhee, S.K.; Kang, '
                             'H.A.; Chulalaksananukul, W.; Kwon, O.: '
                             'Characterization of alcohol dehydrogenase 3 of '
                             'the thermotolerant methylotrophic yeast '
                             'Hansenula polymorpha. Appl. Microbiol. '
                             'Biotechnol. (2012) 96, 697-709.',
                     'pubmed': 22249723},
               223: {'info': 'Elleuche, S.; Fodor, K.; Klippel, B.; von der '
                             'Heyde, A.; Wilmanns, M.; Antranikian, G.: '
                             'Structural and biochemical characterisation of a '
                             'NAD+-dependent alcohol dehydrogenase from '
                             'Oenococcus oeni as a new model molecule for '
                             'industrial biotechnology applications. Appl. '
                             'Microbiol. Biotechnol. (2013) 97, 8963-8975.',
                     'pubmed': 23385476},
               225: {'info': 'Kawano, S.; Yano, M.; Hasegawa, J.; Yasohara, '
                             'Y.: Purification and characterization of an '
                             'NADH-dependent alcohol dehydrogenase from '
                             'Candida maris for the synthesis of optically '
                             'active 1-(pyridyl)ethanol derivatives. Biosci. '
                             'Biotechnol. Biochem. (2011) 75, 1055-1060.',
                     'pubmed': 21670533},
               226: {'info': 'Zhou, S.; Zhang, S.C.; Lai, D.Y.; Zhang, S.L.; '
                             'Chen, Z.M.: Biocatalytic characterization of a '
                             'short-chain alcohol dehydrogenase with broad '
                             'substrate specificity from thermophilic '
                             'Carboxydothermus hydrogenoformans. Biotechnol. '
                             'Lett. (2013) 35, 359-365.',
                     'pubmed': 23160740},
               227: {'info': 'Cederlund, E.; Hedlund, J.; Hjelmqvist, L.; '
                             'Jonsson, A.; Shafqat, J.; Norin, A.; Keung, '
                             'W.M.; Persson, B.; Joernvall, H.: '
                             'Characterization of new medium-chain alcohol '
                             'dehydrogenases adds resolution to duplications '
                             'of the class I/III and the sub-class I genes. '
                             'Chem. Biol. Interact. (2011) 191, 8-13.',
                     'pubmed': 21329683},
               229: {'info': 'Orywal, K.; Jelski, W.; Zdrodowski, M.; '
                             'Szmitkowski, M.: The activity of class I, II, '
                             'III and IV alcohol dehydrogenase isoenzymes and '
                             'aldehyde dehydrogenase in cervical cancer. Clin. '
                             'Biochem. (2011) 44, 1231-1234.',
                     'pubmed': 21784063},
               230: {'info': 'Kube, J.; Brokamp, C.; Machielsen, R.; van der '
                             'Oost, J.; Maerkl, H.: Influence of temperature '
                             'on the production of an archaeal thermoactive '
                             'alcohol dehydrogenase from Pyrococcus furiosus '
                             'with recombinant Escherichia coli. Extremophiles '
                             '(2006) 10, 221-227.',
                     'pubmed': 16463078},
               231: {'info': 'Wang, N.; Shi, H.; Yao, Q.; Zhou, Y.; Kang, L.; '
                             'Chen, H.; Chen, K.: Cloning, expression and '
                             'characterization of alcohol dehydrogenases in '
                             'the silkworm Bombyx mori. Genet. Mol. Biol. '
                             '(2011) 34, 240-243.',
                     'pubmed': 21734824},
               232: {'info': 'Giersberg, M.; Degelmann, A.; Bode, R.; Piontek, '
                             'M.; Kunze, G.: Production of a thermostable '
                             'alcohol dehydrogenase from Rhodococcus ruber in '
                             'three different yeast species using the '
                             'Xplor\x022 transformation/expression platform. '
                             'J. Ind. Microbiol. Biotechnol. (2012) 39, '
                             '1385-1396.',
                     'pubmed': 22584819},
               233: {'info': 'Komatsu, S.; Deschamps, T.; Thibaut, D.; Hiraga, '
                             'S.; Kato, M.; Chiba, M.; Hashiguchi, A.; Tougou, '
                             'M.; Shimamura, S.; Yasue, H.: Characterization '
                             'of a novel flooding stress-responsive alcohol '
                             'dehydrogenase expressed in soybean roots. Plant '
                             'Mol. Biol. (2011) 77, 309-322.',
                     'pubmed': 21811849},
               234: {'info': 'Pennacchio, A.; Rossi, M.; Raia, C.A.: Synthesis '
                             'of cinnamyl alcohol from cinnamaldehyde with '
                             'Bacillus stearothermophilus alcohol '
                             'dehydrogenase as the isolated enzyme and in '
                             'recombinant E. coli cells. Appl. Biochem. '
                             'Biotechnol. (2013) 170, 1482-1490.',
                     'pubmed': 23686507},
               237: {'info': 'Timpson, L.M.; Liliensiek, A.K.; Alsafadi, D.; '
                             'Cassidy, J.; Sharkeym M.A.; Liddell, S.; Allers, '
                             'T.; Paradisi, F.: A comparison of two novel '
                             'alcohol dehydrogenase enzymes (ADH1 and ADH2) '
                             'from the extreme halophile Haloferax volcanii. '
                             'Appl. Microbiol. Biotechnol. (2012) 97, 195-203.',
                     'pubmed': 22526808},
               239: {'info': 'Hirakawa, H.; Kamiya, N.; Kawarabayashi, Y.; '
                             'Nagamune, T.: Properties of an alcohol '
                             'dehydrogenase from the hyperthermophilic '
                             'archaeon Aeropyrum pernix K1. J. Biosci. Bioeng. '
                             '(2004) 97, 202-206.',
                     'pubmed': 16233615},
               243: {'info': 'Wu, X.; Zhang, C.; Orita, I.; Imanaka, T.; '
                             'Fukui, T.; Xing, X.H.: Thermostable alcohol '
                             'dehydrogenase from Thermococcus kodakarensis '
                             'KOD1 for enantioselective bioconversion of '
                             'aromatic secondary alcohols. Appl. Environ. '
                             'Microbiol. (2013) 79, 2209-2217.',
                     'pubmed': 23354700},
               244: {'info': 'Ying, X.; Wang, Y.; Xiong, B.; Wu, T.; Xie, L.; '
                             'Yu, M.; Wang, Z.: Characterization of an '
                             'allylic/benzyl alcohol dehydrogenase from '
                             'Yokenella sp. strain WZY002, an organism '
                             'potentially useful for the synthesis of '
                             'alpha,beta-unsaturated alcohols from allylic '
                             'aldehydes and ketones. Appl. Environ. Microbiol. '
                             '(2014) 80, 2399-2409.',
                     'pubmed': 24509923},
               246: {'info': 'Kirmair, L.; Seiler, D.L.; Skerra, A.: Stability '
                             'engineering of the Geobacillus '
                             'stearothermophilus alcohol dehydrogenase and '
                             'application for the synthesis of a polyamide 12 '
                             'precursor. Appl. Microbiol. Biotechnol. (2015) '
                             '99, 10501-10513.',
                     'pubmed': 26329849},
               252: {'info': 'Liang, J.J.; Zhang, M.L.; Ding, M.; Mai, Z.M.; '
                             'Wu, S.X.; Du, Y.; Feng, J.X.: Alcohol '
                             'dehydrogenases from Kluyveromyces marxianus: '
                             'heterologous expression in Escherichia coli and '
                             'biochemical characterization. BMC Biotechnol. '
                             '(2014) 14, 45.',
                     'pubmed': 24885162},
               254: {'info': 'Kontani, A.; Masuda, M.; Matsumura, H.; '
                             'Nakamura, N.; Yohda, M.; Ohno, H.: A bioanode '
                             'using thermostable alcohol dehydrogenase for an '
                             'ethanol biofuel cell operating at high '
                             'temperatures. Electroanalysis (2014) 26, '
                             '682-686.'},
               255: {'info': 'Willies, S.; Isupov, M.; Littlechild, J.: '
                             'Thermophilic enzymes and their applications in '
                             'biocatalysis: a robust aldo-keto reductase. '
                             'Environ. Technol. (2010) 31, 1159-1167.',
                     'pubmed': 20718298},
               256: {'info': 'Guagliardi, A.; Martino, M.; Iaccarino, I.; De '
                             'Rosa, M.; Rossi, M.; Bartolucci, S.: '
                             'Purification and characterization of the alcohol '
                             'dehydrogenase from a novel strain of Bacillus '
                             'stearothermophilus growing at 70°C. Int. J. '
                             'Biochem. Cell Biol. (1996) 28, 239-246.',
                     'pubmed': 8729010},
               257: {'info': 'Meadows, C.W.; Tsang, J.E.; Klinman, J.P.: '
                             'Picosecond-resolved fluorescence studies of '
                             'substrate and cofactor-binding domain mutants in '
                             'a thermophilic alcohol dehydrogenase uncover an '
                             'extended network of communication. J. Am. Chem. '
                             'Soc. (2014) 136, 14821-14833.',
                     'pubmed': 25314615},
               260: {'info': 'Nagel, Z.D.; Cun, S.; Klinman, J.P.: '
                             'Identification of a long-range protein network '
                             'that modulates active site dynamics in '
                             'extremophilic alcohol dehydrogenases. J. Biol. '
                             'Chem. (2013) 288, 14087-14097.',
                     'pubmed': 23525111},
               269: {'info': 'Pennacchio, A.; Giordano, A.; Esposito, L.; '
                             'Langella, E.; Rossi, M.; Raia, C.A.: Insight '
                             'into the stereospecificity of short-chain '
                             'thermus thermophilus alcohol dehydrogenase '
                             'showing pro-S hydride transfer and prelog '
                             'enantioselectivity. Protein Pept. Lett. (2010) '
                             '17, 437-443.',
                     'pubmed': 19807673},
               271: {'info': 'Takeda, M.; Anamizu, S.; Motomatsu, S.; Chen, '
                             'X.; Thapa Chhetri, R.: Identification and '
                             'characterization of a mycobacterial '
                             'NAD+-dependent alcohol dehydrogenase with '
                             'superior reduction of diacetyl to (S)-acetoin. '
                             'Biosci. Biotechnol. Biochem. (2014) 78, '
                             '1879-1886.',
                     'pubmed': 25082080},
               272: {'info': 'Hong, S.H.; Ngo, H.P.; Kang, L.W.; Oh, D.K.: '
                             'Characterization of alcohol dehydrogenase from '
                             'Kangiella koreensis and its application to '
                             'production of all-trans-retinol. Biotechnol. '
                             'Lett. (2015) 37, 849-856.',
                     'pubmed': 25481533},
               274: {'info': 'Spickermann, D.; Hausmann, S.; Degering, C.; '
                             'Schwaneberg, U.; Leggewie, C.: Engineering of '
                             'highly selective variants of Parvibaculum '
                             'lavamentivorans alcohol dehydrogenase. '
                             'ChemBioChem (2014) 15, 2050-2052.',
                     'pubmed': 25169816},
               275: {'info': 'Malver, O.; Sebastian, M.J.; Oppenheimer, N.J.: '
                             'Alteration in substrate specificity of horse '
                             'liver alcohol dehydrogenase by an acyclic '
                             'nicotinamide analog of NAD(+). DNA Repair (2014) '
                             '23, 95-100.',
                     'pubmed': 25280628},
               277: {'info': 'Moosavi-Movahedi, F.; Saboury, A.A.; Alijanvand, '
                             'H.H.; Bohlooli, M.; Salami, M.; '
                             'Moosavi-Movahedi, A.A.: Thermal inactivation and '
                             'conformational lock studies on horse liver '
                             'alcohol dehydrogenase: structural mechanism. '
                             'Int. J. Biol. Macromol. (2013) 58, 66-72.',
                     'pubmed': 23548863},
               279: {'info': 'Tsuji, K.; Yoon, K.S.; Ogo, S.: Biochemical '
                             'characterization of a bifunctional '
                             'acetaldehyde-alcohol dehydrogenase purified from '
                             'a facultative anaerobic bacterium Citrobacter '
                             'sp. S-77. J. Biosci. Bioeng. (2016) 121, '
                             '253-258.',
                     'pubmed': 26216639},
               284: {'info': 'Cheng, F.; Hu, T.; An, Y.; Huang, J.; Xu, Y.: '
                             'Purification and enzymatic characterization of '
                             'alcohol dehydrogenase from Arabidopsis thaliana. '
                             'Protein Expr. Purif. (2013) 90, 74-77.',
                     'pubmed': 23707506},
               286: {'info': 'Ashraf, R.; Rashid, N.; Kanai, T.; Imanaka, T.; '
                             'Akhtar, M.:  Pcal_1311, an alcohol dehydrogenase '
                             'homologue from Pyrobaculum calidifontis, '
                             'displays NADH-dependent high aldehyde reductase '
                             'activity. Extremophiles (2017)  FEHLT,  0000 .',
                     'pubmed': 29022135},
               287: {'info': 'Kwak, M.K.; Ku, M.; Kang, S.O.:  NAD+-linked '
                             'alcohol dehydrogenase 1 regulates methylglyoxal '
                             'concentration in Candida albicans. FEBS Lett. '
                             '(2014)  588,  1144-1153 .',
                     'pubmed': 24607541},
               288: {'info': 'Tsuji, K.; Yoon, K.S.; Ogo, S.:  Biochemical '
                             'characterization of a bifunctional '
                             'acetaldehyde-alcohol dehydrogenase purified from '
                             'a facultative anaerobic bacterium Citrobacter '
                             'sp. S-77. J. Biosci. Bioeng. (2016)  121,  '
                             '253-258 .',
                     'pubmed': 26216639},
               289: {'info': 'Abdallah, W.; Solanki, K.; Banta, S.:  Insertion '
                             'of a calcium-responsive beta-roll domain into a '
                             'thermostable alcohol dehydrogenase enables '
                             'tunable control over cofactor selectivity. ACS '
                             'Catal. (2018)  8,  1602-1613 .'},
               290: {'info': 'Campbell, E.; Wheeldon, I.; Banta, S.:  '
                             'Broadening the cofactor specificity of a '
                             'thermostable alcohol dehydrogenase using '
                             'rational protein design introduces novel kinetic '
                             'transient behavior. Biotechnol. Bioeng. (2010)  '
                             '107,  763-774 .',
                     'pubmed': 20632378},
               292: {'info': 'Beer, B.; Pick, A.; Doering, M.; Lommes, P.; '
                             'Sieber, V.:  Substrate scope of a dehydrogenase '
                             'from Sphingomonas species A1 and its potential '
                             'application in the synthesis of rare sugars and '
                             'sugar derivatives. Microb. Biotechnol. (2018)  '
                             '11,  747-758 .',
                     'pubmed': 29697194},
               293: {'info': 'Solanki, K.; Abdallah, W.; Banta, S.:  '
                             'Engineering the cofactor specificity of an '
                             'alcohol dehydrogenase via single mutations or '
                             "insertions distal to the 2'-phosphate group of "
                             'NADP(H). Protein Eng. Des. Sel. (2017)  30,  '
                             '373-380 .',
                     'pubmed': 28201792},
               294: {'info': 'Zhu, D.; Malik, H.; Hua, L.:  Asymmetric ketone '
                             'reduction by a hyperthermophilic alcohol '
                             'dehydrogenase. The substrate specificity, '
                             'enantioselectivity and tolerance of organic '
                             'solvents. Tetrahedron Asymmetry (2006)  17,  '
                             '3010-3014 .'}}),
             ('tissues', {'BTO_0003833'})])
--------------------------------------------------------------------------------
OrderedDict([('protein_id', 8),
             ('ec', '1.1.1.1'),
             ('organism', 'Homo sapiens'),
             ('taxonomy', 9606),
             ('uniprot', None),
             ('AP',
              [{'comment': '#24# isozyme ADH2 is a target for anti-amoebic '
                           'agents <123>; #8# organ simulations indicate that '
                           'higher therapeutic acetaminophen (0.5 mM) inhibits '
                           '16% of allotype ADH1B*1/*1 hepatic ADH activity at '
                           '2-20 mM ethanol and that therapeutic salicylate '
                           '(1.5 mM) inhibits 30-31% of the allotype '
                           'ADH1B*2/*2 activity, suggesting potential '
                           'significant inhibitions of ethanol first-pass '
                           'metabolism in these allelotypes <273>',
                'data': 'medicine',
                'refs': [123, 273]}]),
             ('CF',
              [{'comment': '#13,24,44,61,110,112,166# dependent on '
                           '<113,114,126,128,197,210,292>; #162# specific for '
                           '<287>; #46,95# dependent <153,154,159>; #163# '
                           'preferred cofactor <288>; #41# kinetics of '
                           'coenzyme binding in the pH-range 10-12 <26>; #4# '
                           'NAD+-plus-acetone-induced conversion <62>; #41# '
                           'NAD+ acts as an activator which induces an active '
                           'form of the enzyme <34>; #41# preferred substrate '
                           '<42>; #84# activity with mutants G223D/T224I and '
                           'G223D/T224I/H225N <125>; #10# cofactor binding '
                           'mode <120>; #13# dependent on, cofactor binding '
                           'mechanism and conformation from crystal structure '
                           'analysis <112>; #87# the monomer consists of a '
                           'catalytic and a cofactor-binding domain, the '
                           'cofactor is bound between 2 domains in a cleft '
                           '<127>; #7,27,34,50,66# strongly preferred as '
                           'cofactor <135>; #92# specific for NAD+, no '
                           'activity with NADP+, pro-R stereospecificity for '
                           'hydrogen transfer <144>; #98# ADH1 preferrs NAD+ '
                           '205fold better than NADP+ as cofactor <172>; #15# '
                           'ADH3 does not react with NADP+ <172>; #143# '
                           'preferred over NADP+ <138>; #6# strict requirement '
                           'for NAD(H) as the coenzyme. Critical role of the '
                           'D37 residue in discriminating NAD(H) from NADP(H) '
                           '<169>; #111# shows NAD+ as the preferred co-factor '
                           'over NADP+ <213>; #41# the binding of NAD+ is '
                           'kinetically limited by a unimolecular '
                           'isomerization (corresponding to the conformational '
                           'change) that is controlled by deprotonation of the '
                           'catalytic zinc-water to produce a '
                           'negatively-charged zinc-hydroxide, which can '
                           'attract the positively-charged nicotinamide ring '
                           '<198>; #114# NAD+ is prefered over NADP+ <215>; '
                           '#115# NADP+ is prefered over NAD+ <215>; #124# '
                           'strict requirement for NAD(H) as the coenzyme, no '
                           'activity with NADP+. The specificity constant '
                           'value is 6fold higher for NADH than NAD+ <218>; '
                           '#123# the enzyme transfers the deuteride to the '
                           'Si-face of NAD+ <219>; #48# Adh3 is strictly '
                           'dependent on NAD+/NADH, and shows no activity with '
                           'NADP+/NADPH as cofactor <223>; #133# exclusively '
                           'NAD+ dependent <237>; #51# 57fold preferred over '
                           'NADP+ <279>; #23# H255R single mutant exhibits an '
                           'increased binding affinity toward NADP+ and a '
                           'concomitant reduction in affinity for NAD+ <290>; '
                           '#23# insertion of an RTX domain from the adenylate '
                           'cyclase of Bordetella pertussis into a loop near '
                           'the catalytic active site of the thermostable '
                           'alcohol dehydrogenase D from Pyrococcus furiosus. '
                           'The resultant chimera, beta-AdhD, gains the '
                           'calcium-binding ability of the beta-roll, retains '
                           'the thermostable activity of AdhD, and exhibits '
                           'reduced overall alcohol dehydrogenase activity. '
                           'The addition of calcium to beta-AdhD '
                           'preferentially inhibits NAD+-dependent activity in '
                           'comparison to NADP+-dependent activity. Calcium is '
                           'a competitive inhibitor of AdhD, and the addition '
                           'of the RTX domain introduces calcium-dependent '
                           'noncompetitive inhibition to beta-AdhD affecting '
                           'NAD+-dependent activity <289>',
                'data': 'NAD+',
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
                         20,
                         21,
                         22,
                         23,
                         24,
                         25,
                         26,
                         27,
                         28,
                         29,
                         30,
                         31,
                         32,
                         33,
                         34,
                         35,
                         36,
                         37,
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
                         49,
                         50,
                         51,
                         52,
                         53,
                         54,
                         55,
                         56,
                         57,
                         58,
                         59,
                         60,
                         61,
                         62,
                         63,
                         64,
                         65,
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
                         89,
                         90,
                         91,
                         92,
                         93,
                         94,
                         95,
                         96,
                         97,
                         98,
                         99,
                         100,
                         101,
                         102,
                         103,
                         105,
                         110,
                         111,
                         112,
                         113,
                         114,
                         115,
                         116,
                         118,
                         120,
                         121,
                         124,
                         125,
                         126,
                         127,
                         128,
                         129,
                         130,
                         135,
                         136,
                         137,
                         138,
                         139,
                         141,
                         143,
                         144,
                         146,
                         148,
                         149,
                         152,
                         153,
                         154,
                         156,
                         157,
                         158,
                         159,
                         161,
                         162,
                         163,
                         164,
                         165,
                         169,
                         172,
                         180,
                         194,
                         195,
                         196,
                         197,
                         198,
                         200,
                         201,
                         202,
                         203,
                         204,
                         205,
                         206,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         215,
                         217,
                         218,
                         219,
                         220,
                         221,
                         222,
                         223,
                         225,
                         226,
                         227,
                         229,
                         230,
                         231,
                         232,
                         233,
                         234,
                         237,
                         243,
                         252,
                         254,
                         256,
                         257,
                         260,
                         269,
                         272,
                         279,
                         286,
                         287,
                         288,
                         289,
                         290,
                         292,
                         293]},
               {'comment': '#128# required <225>; #44,61# dependent on '
                           '<113,114>; #46# dependent <155>; #163# preferred '
                           'cofactor <288>; #41# kinetics of coenzyme binding '
                           'in the pH range 10-12 <26>; #41# preferred '
                           'coenzyme <42>; #84# activity with mutants '
                           'G223D/T224I and G223D/T224I/H225N <125>; #10# '
                           'cofactor binding mode <120>; #124# strictly '
                           'required <219>; #6# strict requirement for NAD(H) '
                           'as the coenzyme. Critical role of the D37 residue '
                           'in discriminating NAD(H) from NADP(H) <169>; #124# '
                           'strict requirement for NAD(H) as the coenzyme, no '
                           'activity with NADPH. The specificity constant '
                           'value is 6fold higher for NADH than NAD+ <218>; '
                           '#123# the specificity constant value is 21-fold '
                           'higher for NADH than NAD+. No activity with '
                           'NADP(H) <219>; #48# Adh3 is strictly dependent on '
                           'NAD+/NADH, and shows no activity with NADP+/NADPH '
                           'as cofactor <223>; #6# the enzyme transfers the '
                           'pro-S hydrogen of [4R-(2)H]NADH and exhibits '
                           'Prelog specificity <269>; #164# the cofactor NADH '
                           'can be recycled with D-glucose '
                           'dehydrogenase/D-glucose system or in a coupled '
                           'substrate approach using isopropanol as the '
                           'hydrogen donor <291>',
                'data': 'NADH',
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
                         20,
                         21,
                         22,
                         23,
                         24,
                         25,
                         26,
                         27,
                         28,
                         29,
                         30,
                         31,
                         32,
                         33,
                         34,
                         35,
                         36,
                         37,
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
                         49,
                         50,
                         51,
                         52,
                         53,
                         54,
                         55,
                         56,
                         57,
                         58,
                         59,
                         60,
                         61,
                         62,
                         63,
                         64,
                         65,
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
                         89,
                         90,
                         91,
                         92,
                         93,
                         94,
                         95,
                         96,
                         97,
                         98,
                         99,
                         100,
                         101,
                         102,
                         105,
                         110,
                         113,
                         114,
                         118,
                         120,
                         123,
                         124,
                         125,
                         129,
                         131,
                         132,
                         133,
                         134,
                         137,
                         140,
                         149,
                         151,
                         155,
                         157,
                         158,
                         161,
                         163,
                         169,
                         200,
                         215,
                         217,
                         218,
                         219,
                         222,
                         223,
                         225,
                         226,
                         231,
                         232,
                         233,
                         234,
                         241,
                         246,
                         252,
                         253,
                         256,
                         259,
                         265,
                         269,
                         272,
                         281,
                         285,
                         286,
                         287,
                         288,
                         290,
                         291]}]),
             ('CL',
              [{'data': '(5-7 genes encoding ADH, DNA and amino acid sequence '
                        'determination and analysis, polymorphism and allelic '
                        'frequencies analysis, gene ADH2 possesses 2 allelic '
                        'forms with Ile308 or Val308, expression of ADH2 '
                        'alloenzymes in Escherichia coli)',
                'refs': [115]},
               {'data': '(class IV enzyme, expression in Escherichia coli)',
                'refs': [53]},
               {'data': '(expression of ADH1C*2 in Escherichia coli)',
                'refs': [116]},
               {'data': '(expression of ADH4 in Escherichia coli)',
                'refs': [124]},
               {'data': '(expression of human ADH1 in an in vitro '
                        'transcription/translation system, N-terminally '
                        'GST-tagged ADH1 in COS cells and in Escherichia coli)',
                'refs': [228]},
               {'data': '(expression of isozymes in Escherichia coli strain '
                        'BL21)',
                'refs': [119]}]),
             ('CR',
              [{'data': '(isozyme alphaalpha in complex with inhibitor '
                        'N-cyclopentyl-N-cyclobutylformamide, isozyme '
                        'beta(1)beta(1) in complex with inhibitors '
                        'N-benzylformamide and N-heptylformamide, and isozyme '
                        'gamma(2)gamma(2) in complex with inhibitor '
                        'N-1-methylheptylformamide, X-ray diffraction '
                        'structure determination and analysis at 1.45-2.5 A '
                        'resolution, structure modeling)',
                'refs': [109]},
               {'data': '', 'refs': [12]}]),
             ('EN',
              [{'comment': '#8# isozyme alphaalpha, altered active site '
                           'structure and inhibitor binding <109>',
                'data': 'A93F',
                'refs': [109]},
               {'comment': '#8# isozyme gamma(2)gamma(2), altered active site '
                           'structure and inhibitor binding <109>',
                'data': 'S48T',
                'refs': [109]},
               {'comment': '#8# isozyme gamma(2)gamma(2), altered active site '
                           'structure and inhibitor binding <109>',
                'data': 'V141L',
                'refs': [109]}]),
             ('GS',
              [{'data': '(100fold purified enzyme is destroyed by freezing)',
                'refs': [12]}]),
             ('ID', '1.1.1.1'),
             ('IN',
              [{'comment': '#46# competitive inhibitor <163>; #8# 1 mM, 31% '
                           'inhibition <23>; #8# class III enzyme is '
                           'completely insensitive to inhibition <11,16>; #8# '
                           'poor inhibitor, class II isoenzyme <14>; #8# no '
                           'inhibition by 12 mM <21>; #8# competitive against '
                           'ethanol <96>; #36# isoenzyme AA-ADH, BB-ADH and '
                           'TT-ADH <95>; #5# inhibits cell protein '
                           'carbonylation following exposure to crotyl alcohol '
                           '<117>',
                'data': '4-Methylpyrazole',
                'refs': [2,
                         11,
                         14,
                         16,
                         21,
                         23,
                         24,
                         25,
                         95,
                         96,
                         117,
                         135,
                         163,
                         214]},
               {'comment': '#101# 1 mM, complete inhibition <185>; #36# mixed '
                           'type inhibition <47>; #92# 1 mM, 38% inhibition '
                           '<144>; #5# inhibition of isoenzyme A2 and C2, no '
                           'inhibition of isoenzyme B2 <48>; #42# 0.2 mM, '
                           'strong inhibition <68>; #26# 1 mM, 6% inhibition '
                           '<188>',
                'data': '1,10-phenanthroline',
                'refs': [2,
                         14,
                         21,
                         24,
                         25,
                         45,
                         47,
                         48,
                         68,
                         69,
                         75,
                         95,
                         144,
                         185,
                         188]},
               {'comment': '#78# competitive <38>; #88# strong inhibition '
                           '<118>; #8# 0.05 mM, 50% inhibition <10>; #46# '
                           'competitive inhibitor <163>; #78# competitive '
                           'towards ethanol <61>; #9# 0.1-10 mM, ADH-2 is '
                           'practically insensitive, ADH-3 is very sensitive '
                           '<49>; #9# 0.05 mM, complete inhibition <10>; #8# '
                           'no inhibition at 1.0 mM <23>; #43,79# organism has '
                           'a pyrazole-sensitive isoenzyme and a '
                           'pyrazole-insensitive enzyme <24,25>; #69# '
                           'pyrazole-sensitive enzyme forms ADH-1, ADH-2, '
                           'ADH-3 and the pyrazole-insensitive form ADH-An '
                           '<60>; #5# inhibition of isoenzyme A2 and C2. '
                           'Isoenzyme B2 is insensitive to pyrazole inhibition '
                           'with trans-2-hexen-1-ol as substrate <48>',
                'data': 'pyrazole',
                'refs': [10,
                         12,
                         23,
                         24,
                         25,
                         38,
                         45,
                         48,
                         49,
                         60,
                         61,
                         71,
                         94,
                         118,
                         163,
                         212]},
               {'comment': '#8# dead-end inhibitor to the enzyme-cofactor '
                           'complex, inhibition of oxidation reaction <116>',
                'data': '3-butylthiolan 1-oxide',
                'refs': [116]},
               {'comment': '#8# competitive against substrate cyclohexanone '
                           '<116>',
                'data': '4-androsten-3,17-dione',
                'refs': [116]},
               {'data': '4-bromopyrazole', 'refs': [23]},
               {'data': '4-cyanopyrazole', 'refs': [23]},
               {'data': '4-nitropyrazole', 'refs': [23]},
               {'data': '4-octylpyrazole', 'refs': [12]},
               {'data': '4-pentylpyrazole', 'refs': [12, 23]},
               {'data': '4-propylpyrazole', 'refs': [23]},
               {'comment': '#8# i.e. 5alpha-dihydrotestosterone, allosteric, '
                           'competitive against substrate cyclohexanone, '
                           'noncompetitive against NAD+ nd ethanol <116>',
                'data': '5alpha-androstan-17beta-ol-3-one',
                'refs': [116]},
               {'data': '8-Amino-6-methoxyquinoline', 'refs': [12]},
               {'comment': '#8# 1 mM, 4.4% inhibition of hepatic allotype '
                           'ADH1B*1/*1 activity, 2.8% inhibition of hepatic '
                           'allotype ADH1B*2/*2 activity <273>',
                'data': 'Acetylsalicylate',
                'refs': [273]},
               {'comment': '#8# inhibits isozyme gamma(2)gamma(2) <109>',
                'data': 'N-1-methylheptylformamide',
                'refs': [109]},
               {'comment': '#8# inhibits isozyme beta(1)beta(1) <109>',
                'data': 'N-benzylformamide',
                'refs': [109]},
               {'comment': '#8# inhibits isozyme alphaalpha, complex structure '
                           '<109>',
                'data': 'N-cyclopentyl-N-cyclobutylformamide',
                'refs': [109]},
               {'comment': '#8# inhibits isozyme beta(1)beta(1) <109>',
                'data': 'N-heptylformamide',
                'refs': [109]},
               {'data': 'NADP+', 'refs': [21]},
               {'comment': '#8# 0.5 mM, 16% inhibition of hepatic allotype '
                           'ADH1B*1/*1 activity, 6.1% inhibition of hepatic '
                           'allotype ADH1B*2/*2 activity <273>',
                'data': 'acetaminophen',
                'refs': [273]},
               {'comment': '#8# product inhibition <124>',
                'data': 'all-trans-retinal',
                'refs': [124]},
               {'comment': '#8# weak feedback inhibition <124>',
                'data': 'all-trans-retinoic acid',
                'refs': [124]},
               {'comment': '#8# 0.2 mM, 2.5% inhibition of hepatic allotype '
                           'ADH1B*1/*1 activity, 12% inhibition of hepatic '
                           'allotype ADH1B*2/*2 activity <273>',
                'data': 'cimetidine',
                'refs': [273]},
               {'comment': '#8# 1.5 mM, 12% inhibition of hepatic allotype '
                           'ADH1B*1/*1 activity, 31% inhibition of hepatic '
                           'allotype ADH1B*2/*2 activity <273>',
                'data': 'salicylate',
                'refs': [273]},
               {'data': 'sulfonic acid', 'refs': [21]},
               {'comment': '#8# competitive against retinol, noncompetitive '
                           'against NAD+ <124>',
                'data': 'trifluoroethanol',
                'refs': [91, 124]},
               {'comment': '#10# Zn2+ chelator and inhibitor of ADH <209>',
                'data': 'dipicolinic acid',
                'refs': [21, 24, 209]},
               {'comment': '#26# 1 mM, 31% inhibition <188>; #46# 15 mM, 85% '
                           'inhibition <66>; #61# 67% inhibition of ADH II at '
                           '5 mM, 45% inhibition of ADH I at 1 mM, '
                           'irreversible inhibition, addition of Mg2+ and Zn2+ '
                           'increase the inhibitory effect <113>; #58# 25% '
                           'inhibition at 10.5 mM, 44% inhibition at 21 mM '
                           '<147>; #57# 31% inhibition at 10.5 mM, 92% '
                           'inhibition at 21 mM <147>; #46# loses 30% of its '
                           'activity immediately on addition of EDTA <163>; '
                           '#112# 2.3% relative activity at 10 mM <197>; #124# '
                           '1 mM, 93% of initial activity <219>',
                'data': 'EDTA',
                'refs': [14,
                         24,
                         25,
                         66,
                         76,
                         99,
                         113,
                         147,
                         163,
                         188,
                         197,
                         219,
                         223]},
               {'comment': '#8# substrate inhibition, competitive against '
                           'retinol, noncompetitive against NADH <124>',
                'data': 'Isobutyramide',
                'refs': [124, 175]},
               {'data': "2,2'-bipyridine", 'refs': [14, 25]},
               {'comment': '#46# competitive inhibitor <163>',
                'data': '4-iodopyrazole',
                'refs': [23, 163]},
               {'data': '8-hydroxyquinoline 5-sulfonic acid', 'refs': [21, 24]},
               {'comment': '#36# competitive <47>; #8# 1 mM, 28% inhibition '
                           '<23>; #12# class I ADHs migrate towards cathode on '
                           'starch gel and are very sensitive to '
                           '4-methylpyrazole inhibition, class II ADH migrates '
                           'slowly towards anode and is less sensitive to '
                           '4-methylpyrazole, class II ADH migrates rapidly '
                           'towards anode and is insensitive to '
                           '4-methylpyrazole <46>; #9# 0.1-10 mM, ADH-2 is '
                           'practically insensitive, ADH-3 is very sensitive '
                           '<49>; #9# competitive inhibitor of all four '
                           'isoenzymes <51>',
                'data': '4-methoxypyrazole',
                'refs': [23, 45, 46, 47, 49, 51, 53, 91]},
               {'comment': '#8# competitive, stabilizes the retinoid '
                           'compounds, elevates the Km values of the '
                           'substrates, most effective at 0.1% w/v <107>; #99# '
                           '10% (w/v), 89% inhibition <173>; #112# 13% '
                           'relative activity at 10% (v/v) <197>',
                'data': 'Tween 80',
                'refs': [107, 173, 197]}]),
             ('KI',
              [{'comment': '#8# pH 7.3, 37°C, versus cyclohexanone <116>',
                'data': '0.0047 {4-androsten-3,17-dione}',
                'refs': [116],
                'substrate': '4-androsten-3,17-dione',
                'units': 'mM',
                'value': 0.0047},
               {'comment': '#8# pH 7.3, 37°C, versus cyclohexanone <116>',
                'data': '0.0047 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [116],
                'substrate': '5alpha-androstan-17beta-ol-3-one',
                'units': 'mM',
                'value': 0.0047},
               {'comment': '#8# pH 7.3, 37°C, versus ethanol <116>',
                'data': '0.014 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [116],
                'substrate': '5alpha-androstan-17beta-ol-3-one',
                'units': 'mM',
                'value': 0.014},
               {'comment': '#8# pH 7.3, 37°C, versus NAD+ <116>',
                'data': '0.028 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [116],
                'substrate': '5alpha-androstan-17beta-ol-3-one',
                'units': 'mM',
                'value': 0.028},
               {'comment': '#8# inhibition kinetics <116>',
                'data': '-999 {more}',
                'refs': [116, 123, 124],
                'units': 'mM'}]),
             ('KM',
              [{'comment': '#41,71# kinetics <117,121>; #10# pH-dependence of '
                           'Km-value <89>; #4,75# kinetics of ethanol '
                           'oxidation <63>; #41# kinetics of native and '
                           'modified enzyme with coenzyme analogues <54>; #41# '
                           'Km-values of active-site Co(II)substituted enzyme '
                           '<31>; #8# Km values for the class I isoenzymes '
                           'with the substrates ethanol, methanol, ethylene '
                           'glycol, benzyl alcohol, octanol, cyclohexanol and '
                           '16-hydroxyhexadecanoic acid <13>; #8# steady-state '
                           'kinetics <116>; #41# detailed kinetic mechanism, '
                           'steady-state kinetics for wild-type and mutant '
                           'enzymes, investigation of pH-dependency <111>; '
                           '#78# detailed kinetics, computational analysis of '
                           'the reaction mechanism <130>; #5# Km for isozymes '
                           'ADH1, and ADH4 for all retinoid substrates in '
                           'forward and reverse reaction <119>; #8# Km for '
                           'isozymes ADH1B1, ADH1B2, and ADH4 for all retinoid '
                           'substrates in forward and reverse reaction <119>; '
                           '#85,90,163# Michaelis-Menten kinetics '
                           '<105,226,288>; #8# steady-state kinetics, kinetic '
                           'mechanism <124>; #8# steady-state kinetics, MW 25 '
                           'kDa <115>; #10# wild-type and mutant forms of the '
                           '3 isozymes, steady-state kinetics, detailed '
                           'kinetic analysis, at different pH values and '
                           'temperatures <120>; #5# effects of tert-butanol, '
                           'butyramide, valeramide and capronamide on KM-value '
                           'for ethanol <141>; #23# kinetic data füor '
                           'wild-type enzyme and chimeric enzyme created by '
                           'insertion of an RTX domain from the adenylate '
                           'cyclase of Bordetella pertussis into a loop near '
                           'the catalytic active site of the thermostable '
                           'alcohol dehydrogenase D (AdhD) from Pyrococcus '
                           'furiosus <289>',
                'data': '-999 {more}',
                'refs': [13,
                         22,
                         23,
                         31,
                         54,
                         63,
                         75,
                         83,
                         89,
                         105,
                         111,
                         115,
                         116,
                         117,
                         119,
                         120,
                         121,
                         124,
                         130,
                         141,
                         226,
                         288,
                         289],
                'units': 'mM'},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# recombinant allozyme Val308, pH 7.5, 25°C '
                           '<115>',
                'data': '10.6 {ethanol}',
                'refs': [115, 135],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 10.6},
               {'chebi': 'CHEBI_16908',
                'data': '0.0025 {NADH}',
                'refs': [16],
                'substrate': 'NADH',
                'units': 'mM',
                'value': 0.0025},
               {'comment': '#8# pH 7.3, 37°C, ADH1C*2 (gamma2gamma2) <116>',
                'data': '0.0036 {5alpha-androstan-17beta-ol-3-one}',
                'refs': [116],
                'substrate': '5alpha-androstan-17beta-ol-3-one',
                'units': 'mM',
                'value': 0.0036},
               {'comment': '#8# pH 7.3, 37°C, ADH1C*2 (gamma2gamma2) <116>',
                'data': '0.0036 {5beta-pregnan-3,20-dione}',
                'refs': [116],
                'substrate': '5beta-pregnan-3,20-dione',
                'units': 'mM',
                'value': 0.0036},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B1 <107>',
                'data': '0.004 {4-hydroxy-retinol}',
                'refs': [107],
                'substrate': '4-hydroxy-retinol',
                'units': 'mM',
                'value': 0.004},
               {'chebi': 'CHEBI_16908',
                'comment': '#8# isoenzyme beta1,beta1 <16>',
                'data': '0.0064 {NADH}',
                'refs': [16],
                'substrate': 'NADH',
                'units': 'mM',
                'value': 0.0064},
               {'chebi': 'CHEBI_16908',
                'comment': '#8# isoenzyme gamma1,gamma1 <16>',
                'data': '0.007 {NADH}',
                'refs': [16],
                'substrate': 'NADH',
                'units': 'mM',
                'value': 0.007},
               {'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '0.007 {Octanol}',
                'refs': [14],
                'substrate': 'Octanol',
                'units': 'mM',
                'value': 0.007},
               {'chebi': 'CHEBI_17987',
                'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '0.007 {benzyl alcohol}',
                'refs': [14],
                'substrate': 'benzyl alcohol',
                'units': 'mM',
                'value': 0.007},
               {'comment': '#8# isoenzyme beta1,beta1 <17>; #8# isoenzyme '
                           'beta2,beta2 <16>',
                'data': '0.0074 {NAD+}',
                'refs': [16, 17],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.0074},
               {'comment': '#8# isoenzyme gamma1,gamma1 <16,17>',
                'data': '0.0079 {NAD+}',
                'refs': [16, 17],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.0079},
               {'comment': '#8# isoenzyme alpha,gamma1 <13>',
                'data': '0.008 {Cyclohexanol}',
                'refs': [13],
                'substrate': 'Cyclohexanol',
                'units': 'mM',
                'value': 0.008},
               {'comment': '#8# isoenzyme gamma2,gamma2 <16,17>',
                'data': '0.0087 {NAD+}',
                'refs': [16, 17],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.0087},
               {'comment': '#8# recombinant allozyme Ile308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.009 {Octanol}',
                'refs': [115],
                'substrate': 'Octanol',
                'units': 'mM',
                'value': 0.009},
               {'chebi': 'CHEBI_17336',
                'data': '0.009 {all-trans-retinol}',
                'refs': [53],
                'substrate': 'all-trans-retinol',
                'units': 'mM',
                'value': 0.009},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.011 {4-hydroxy-retinol}',
                'refs': [107],
                'substrate': '4-hydroxy-retinol',
                'units': 'mM',
                'value': 0.011},
               {'chebi': 'CHEBI_78272',
                'comment': '#8# isozyme ADH1B1, pH 7.5, 25°C <119>',
                'data': '0.011 {9-cis-retinol}',
                'refs': [119],
                'substrate': '9-cis-retinol',
                'units': 'mM',
                'value': 0.011},
               {'chebi': 'CHEBI_16908',
                'comment': '#8# isoenzyme alpha,alpha <16>',
                'data': '0.011 {NADH}',
                'refs': [16],
                'substrate': 'NADH',
                'units': 'mM',
                'value': 0.011},
               {'chebi': 'CHEBI_17898',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH1B1 <107>',
                'data': '0.011 {all-trans-retinal}',
                'refs': [107],
                'substrate': 'all-trans-retinal',
                'units': 'mM',
                'value': 0.011},
               {'chebi': 'CHEBI_50211',
                'comment': '#8# recombinant allozyme Ile308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.011 {retinol}',
                'refs': [115],
                'substrate': 'retinol',
                'units': 'mM',
                'value': 0.011},
               {'chebi': 'CHEBI_17898',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.012 {all-trans-retinal}',
                'refs': [107],
                'substrate': 'all-trans-retinal',
                'units': 'mM',
                'value': 0.012},
               {'chebi': 'CHEBI_50211',
                'comment': '#8# recombinant allozyme Val308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.012 {retinol}',
                'refs': [115],
                'substrate': 'retinol',
                'units': 'mM',
                'value': 0.012},
               {'comment': '#8# isoenzyme alpha,alpha <16,17>',
                'data': '0.013 {NAD+}',
                'refs': [16, 17],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.013},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '0.015 {4-hydroxy-retinol}',
                'refs': [107],
                'substrate': '4-hydroxy-retinol',
                'units': 'mM',
                'value': 0.015},
               {'comment': '#8# recombinant allozyme Val308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.016 {Octanol}',
                'refs': [115],
                'substrate': 'Octanol',
                'units': 'mM',
                'value': 0.016},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '0.017 {4-oxo-retinal}',
                'refs': [107],
                'substrate': '4-oxo-retinal',
                'units': 'mM',
                'value': 0.017},
               {'chebi': 'CHEBI_16302',
                'comment': '#8# isozyme ADH1B2, pH 7.5, 25°C <119>',
                'data': '0.018 {11-cis-retinol}',
                'refs': [119],
                'substrate': '11-cis-retinol',
                'units': 'mM',
                'value': 0.018},
               {'data': '0.022 {NAD+}',
                'refs': [12],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.022},
               {'chebi': 'CHEBI_78272',
                'comment': '#8# isozyme ADH1B2, pH 7.5, 25°C <119>',
                'data': '0.023 {9-cis-retinol}',
                'refs': [119],
                'substrate': '9-cis-retinol',
                'units': 'mM',
                'value': 0.023},
               {'chebi': 'CHEBI_17336',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '0.023 {all-trans-retinol}',
                'refs': [107],
                'substrate': 'all-trans-retinol',
                'units': 'mM',
                'value': 0.023},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.024 {3,4-dihydro-retinol}',
                'refs': [107],
                'substrate': '3,4-dihydro-retinol',
                'units': 'mM',
                'value': 0.024},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.025 {3,4-dihydro-retinal}',
                'refs': [107],
                'substrate': '3,4-dihydro-retinal',
                'units': 'mM',
                'value': 0.025},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B1 <107>',
                'data': '0.025 {4-oxo-retinal}',
                'refs': [107],
                'substrate': '4-oxo-retinal',
                'units': 'mM',
                'value': 0.025},
               {'data': '0.025 {NAD+}',
                'refs': [16],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.025},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '0.026 {3,4-dihydro-retinal}',
                'refs': [107],
                'substrate': '3,4-dihydro-retinal',
                'units': 'mM',
                'value': 0.026},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.027 {4-oxo-retinal}',
                'refs': [107],
                'substrate': '4-oxo-retinal',
                'units': 'mM',
                'value': 0.027},
               {'comment': '#8# pH 7.3, 37°C, ADH1C*2 (gamma2gamma2) <116>',
                'data': '0.027 {5beta-Pregnan-3beta-ol-20-one}',
                'refs': [116],
                'substrate': '5beta-Pregnan-3beta-ol-20-one',
                'units': 'mM',
                'value': 0.027},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '0.028 {3,4-dihydro-retinol}',
                'refs': [107],
                'substrate': '3,4-dihydro-retinol',
                'units': 'mM',
                'value': 0.028},
               {'chebi': 'CHEBI_88817',
                'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '0.032 {3-Phenyl-1-propanol}',
                'refs': [14],
                'substrate': '3-Phenyl-1-propanol',
                'units': 'mM',
                'value': 0.032},
               {'chebi': 'CHEBI_17336',
                'comment': '#8# isozyme ADH1B2, pH 7.5, 25°C <119>; #8# pH '
                           '7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.033 {all-trans-retinol}',
                'refs': [107, 119],
                'substrate': 'all-trans-retinol',
                'units': 'mM',
                'value': 0.033},
               {'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '0.034 {Vanillyl alcohol}',
                'refs': [14],
                'substrate': 'Vanillyl alcohol',
                'units': 'mM',
                'value': 0.034},
               {'chebi': 'CHEBI_17898',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '0.034 {all-trans-retinal}',
                'refs': [107],
                'substrate': 'all-trans-retinal',
                'units': 'mM',
                'value': 0.034},
               {'chebi': 'CHEBI_16302',
                'comment': '#8# isozyme ADH1B1, pH 7.5, 25°C <119>',
                'data': '0.035 {11-cis-retinol}',
                'refs': [119],
                'substrate': '11-cis-retinol',
                'units': 'mM',
                'value': 0.035},
               {'data': '0.044 {Pentanol}',
                'refs': [96],
                'substrate': 'Pentanol',
                'units': 'mM',
                'value': 0.044},
               {'comment': '#8# pH 7.3, 37°C, ADH1C*2 (gamma2gamma2) <116>',
                'data': '0.046 {5beta-androstan-17beta-ol-3-one}',
                'refs': [116],
                'substrate': '5beta-androstan-17beta-ol-3-one',
                'units': 'mM',
                'value': 0.046},
               {'data': '0.047 {12-hydroxydodecanoate}',
                'refs': [96],
                'substrate': '12-hydroxydodecanoate',
                'units': 'mM',
                'value': 0.047},
               {'data': '0.048 {12-hydroxydodecanoate}',
                'refs': [53],
                'substrate': '12-hydroxydodecanoate',
                'units': 'mM',
                'value': 0.048},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme beta1,beta1 <17>',
                'data': '0.049 {ethanol}',
                'refs': [15, 17],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 0.049},
               {'data': '0.056 {12-Hydroxydodecanoic acid}',
                'refs': [11],
                'substrate': '12-Hydroxydodecanoic acid',
                'units': 'mM',
                'value': 0.056},
               {'comment': '#8# pH 7.3, 37°C, ADH1C*2 (gamma2gamma2) <116>',
                'data': '0.058 {5beta-androstan-3beta-ol-17-one}',
                'refs': [116],
                'substrate': '5beta-androstan-3beta-ol-17-one',
                'units': 'mM',
                'value': 0.058},
               {'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '0.06 {16-hydroxyhexadecanoate}',
                'refs': [14],
                'substrate': '16-hydroxyhexadecanoate',
                'units': 'mM',
                'value': 0.06},
               {'comment': '#8# isoenzyme alpha,gamma1 <13>',
                'data': '0.08 {Octanol}',
                'refs': [13],
                'substrate': 'Octanol',
                'units': 'mM',
                'value': 0.08},
               {'chebi': 'CHEBI_15343',
                'comment': '#8# isoenzyme beta1,beta1 <15>; #8# isoenzyme '
                           'beta1,beta1, 0.1 M sodium phosphate buffer, pH '
                           '7.5, at 25 °C <20>',
                'data': '0.085 {acetaldehyde}',
                'refs': [15, 20],
                'substrate': 'acetaldehyde',
                'units': 'mM',
                'value': 0.085},
               {'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '0.09 {Pentanol}',
                'refs': [14],
                'substrate': 'Pentanol',
                'units': 'mM',
                'value': 0.09},
               {'data': '0.13 {Hexanol}',
                'refs': [53],
                'substrate': 'Hexanol',
                'units': 'mM',
                'value': 0.13},
               {'chebi': 'CHEBI_17987',
                'data': '0.15 {benzyl alcohol}',
                'refs': [96],
                'substrate': 'benzyl alcohol',
                'units': 'mM',
                'value': 0.15},
               {'chebi': 'CHEBI_17890',
                'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '0.2 {tryptophol}',
                'refs': [14],
                'substrate': 'tryptophol',
                'units': 'mM',
                'value': 0.2},
               {'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '0.23 {12-hydroxydodecanoate}',
                'refs': [14],
                'substrate': '12-hydroxydodecanoate',
                'units': 'mM',
                'value': 0.23},
               {'chebi': 'CHEBI_15343',
                'comment': '#8# isoenzyme gamma2,gamma2 <15>; #8# isoenzymes '
                           'beta2,beta2 <15>; #8# isoenzyme beta2,beta2, 0.1 M '
                           'sodium phosphate buffer, pH 7.5, 25°C <20>',
                'data': '0.24 {acetaldehyde}',
                'refs': [15, 20],
                'substrate': 'acetaldehyde',
                'units': 'mM',
                'value': 0.24},
               {'data': '0.24 {butanol}',
                'refs': [96],
                'substrate': 'butanol',
                'units': 'mM',
                'value': 0.24},
               {'comment': '#8# pH 7.3, 37°C, ADH1C*2 (gamma2gamma2) <116>',
                'data': '0.25 {5beta-cholanic acid-3-one}',
                'refs': [116],
                'substrate': '5beta-cholanic acid-3-one',
                'units': 'mM',
                'value': 0.25},
               {'data': '0.28 {Pentanol}',
                'refs': [53],
                'substrate': 'Pentanol',
                'units': 'mM',
                'value': 0.28},
               {'chebi': 'CHEBI_15343',
                'comment': '#8# isoenzyme gamma1,gamma1 <15>',
                'data': '0.33 {acetaldehyde}',
                'refs': [15],
                'substrate': 'acetaldehyde',
                'units': 'mM',
                'value': 0.33},
               {'data': '0.34 {NAD+}',
                'refs': [96],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.34},
               {'data': '0.55 {1-Octanol}',
                'refs': [11],
                'substrate': '1-Octanol',
                'units': 'mM',
                'value': 0.55},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme gamma2,gamma2 <15>',
                'data': '0.63 {ethanol}',
                'refs': [15],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 0.63},
               {'data': '0.79 {butanol}',
                'refs': [53],
                'substrate': 'butanol',
                'units': 'mM',
                'value': 0.79},
               {'data': '0.8 {Octanol}',
                'refs': [21],
                'substrate': 'Octanol',
                'units': 'mM',
                'value': 0.8},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme beta2,beta2, 0.1 M sodium phosphate '
                           'buffer, pH 7.5, 25°C <20>',
                'data': '0.84 {ethanol}',
                'refs': [20],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 0.84},
               {'data': '0.91 {Propanol}',
                'refs': [96],
                'substrate': 'Propanol',
                'units': 'mM',
                'value': 0.91},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme beta2,beta2 <15>',
                'data': '0.94 {ethanol}',
                'refs': [15],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 0.94},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme gamma1,gamma1 <15>',
                'data': '1 {ethanol}',
                'refs': [15],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 1.0},
               {'data': '1.2 {Octanol}',
                'refs': [16],
                'substrate': 'Octanol',
                'units': 'mM',
                'value': 1.2},
               {'data': '1.39 {Propanol}',
                'refs': [53],
                'substrate': 'Propanol',
                'units': 'mM',
                'value': 1.39},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme beta1,beta1 <17>',
                'data': '1.6 {ethanol}',
                'refs': [17],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 1.6},
               {'chebi': 'CHEBI_16236',
                'data': '1.8 {ethanol}',
                'refs': [10],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 1.8},
               {'chebi': 'CHEBI_17790',
                'data': '10.4 {methanol}',
                'refs': [12],
                'substrate': 'methanol',
                'units': 'mM',
                'value': 10.4},
               {'chebi': 'CHEBI_16908',
                'comment': '#8# isoenzyme beta2,beta2, 0.1 M sodium phosphate '
                           'buffer, pH 7.5, 25°C <20>',
                'data': '105 {NADH}',
                'refs': [20],
                'substrate': 'NADH',
                'units': 'mM',
                'value': 105.0},
               {'data': '11 {Vanillyl alcohol}',
                'refs': [16],
                'substrate': 'Vanillyl alcohol',
                'units': 'mM',
                'value': 11.0},
               {'data': '120 {(S)-2-butanol}',
                'refs': [53],
                'substrate': '(S)-2-butanol',
                'units': 'mM',
                'value': 120.0},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '120 {ethanol}',
                'refs': [14],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 120.0},
               {'chebi': 'CHEBI_17790',
                'comment': '#8# isoenzyme alpha,gamma1 <13>',
                'data': '150 {methanol}',
                'refs': [13],
                'substrate': 'methanol',
                'units': 'mM',
                'value': 150.0},
               {'data': '17 {Hexanol}',
                'refs': [21],
                'substrate': 'Hexanol',
                'units': 'mM',
                'value': 17.0},
               {'chebi': 'CHEBI_16236',
                'data': '18 {ethanol}',
                'refs': [96],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 18.0},
               {'comment': '#8# isoenzyme beta2,beta2, 0.1 M sodium phosphate '
                           'buffer, pH 7.5, 25°C <20>',
                'data': '180 {NAD+}',
                'refs': [20],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 180.0},
               {'chebi': 'CHEBI_17935',
                'data': '2.4 {octanal}',
                'refs': [16],
                'substrate': 'octanal',
                'units': 'mM',
                'value': 2.4},
               {'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '210 {Cyclohexanol}',
                'refs': [14],
                'substrate': 'Cyclohexanol',
                'units': 'mM',
                'value': 210.0},
               {'comment': '#8# isoenzyme beta1,beta1 <13>',
                'data': '23 {Cyclohexanol}',
                'refs': [13],
                'substrate': 'Cyclohexanol',
                'units': 'mM',
                'value': 23.0},
               {'chebi': 'CHEBI_16908',
                'comment': '#8# isoenzyme beta3,beta3, 0.1 M sodium phospahte '
                           'buffer, pH 7.5, 25°C <20>',
                'data': '260 {NADH}',
                'refs': [20],
                'substrate': 'NADH',
                'units': 'mM',
                'value': 260.0},
               {'data': '27 {1-Pentanol}',
                'refs': [11],
                'substrate': '1-Pentanol',
                'units': 'mM',
                'value': 27.0},
               {'chebi': 'CHEBI_30742',
                'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '290 {ethylene glycol}',
                'refs': [14],
                'substrate': 'ethylene glycol',
                'units': 'mM',
                'value': 290.0},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme gamma1,gamma1 <17>',
                'data': '3.2 {ethanol}',
                'refs': [17, 211],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 3.2},
               {'chebi': 'CHEBI_15343',
                'comment': '#8# isoenzyme beta3,beta3, 0.1 M sodium phospahte '
                           'buffer, pH 7.5, 25°C <20>',
                'data': '3.4 {acetaldehyde}',
                'refs': [20],
                'substrate': 'acetaldehyde',
                'units': 'mM',
                'value': 3.4},
               {'chebi': 'CHEBI_28816',
                'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '310 {2-deoxy-D-ribose}',
                'refs': [14],
                'substrate': '2-deoxy-D-ribose',
                'units': 'mM',
                'value': 310.0},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme beta3,beta3, 0.1 M sodium phospahte '
                           'buffer, pH 7.5, 25°C <20>',
                'data': '36 {ethanol}',
                'refs': [20],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 36.0},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme alpha,alpha <15,17>',
                'data': '4.2 {ethanol}',
                'refs': [15, 17],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 4.2},
               {'chebi': 'CHEBI_15343',
                'comment': '#8# isoenzyme alpha,alpha <15>',
                'data': '4.3 {acetaldehyde}',
                'refs': [15],
                'substrate': 'acetaldehyde',
                'units': 'mM',
                'value': 4.3},
               {'chebi': 'CHEBI_30742',
                'comment': '#8# isoenzyme alpha,gamma1 <13>',
                'data': '50 {ethylene glycol}',
                'refs': [13],
                'substrate': 'ethylene glycol',
                'units': 'mM',
                'value': 50.0},
               {'comment': '#8# 0.1 M glycine-NaOH buffer, pH 10.0, 25°C <14>',
                'data': '560 {2-propanol}',
                'refs': [14],
                'substrate': '2-propanol',
                'units': 'mM',
                'value': 560.0},
               {'chebi': 'CHEBI_16908',
                'comment': '#8# isoenzyme beta1,beta1, 0.1 M sodium phosphate '
                           'buffer, pH 7.5, at 25 °C <20>',
                'data': '6.4 {NADH}',
                'refs': [20],
                'substrate': 'NADH',
                'units': 'mM',
                'value': 6.4},
               {'comment': '#8# isoenzyme beta1,beta1, 0.1 M sodium phosphate '
                           'buffer, pH 7.5, at 25 °C <20>',
                'data': '7.4 {NAD+}',
                'refs': [20],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 7.4},
               {'comment': '#8# isoenzyme beta3,beta3, 0.1 M sodium phospahte '
                           'buffer, pH 7.5, 25°C <20>',
                'data': '710 {NAD+}',
                'refs': [20],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 710.0},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# recombinant allozyme Ile308, pH 7.5, 25°C '
                           '<115>',
                'data': '9 {ethanol}',
                'refs': [115],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 9.0},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme alpha,alpha <17>; #119# mutant '
                           'C257L, pH 8.0, 60°C <246>',
                'data': '1.5 {ethanol}',
                'refs': [17, 246],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 1.5},
               {'chebi': 'CHEBI_16236',
                'comment': '#12# pH 10.8 <45>; #127# pH 9.0, 22°C, recombinant '
                           'enzyme <222>',
                'data': '0.45 {ethanol}',
                'refs': [12, 45, 222],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 0.45},
               {'comment': '#8# isoenzyme beta1,beta1 <16>; #124# 65°C, pH '
                           '10.5 <218>',
                'data': '0.18 {NAD+}',
                'refs': [16, 218],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.18},
               {'chebi': 'CHEBI_16908',
                'comment': '#8# isoenzyme beta2,beta2 <16>; #150# cosubstrate '
                           'acetoin, pH 6.0, 70°C <243>',
                'data': '0.105 {NADH}',
                'refs': [16, 243],
                'substrate': 'NADH',
                'units': 'mM',
                'value': 0.105},
               {'chebi': 'CHEBI_16236',
                'comment': '#16# isoenzyme III <79>; #8# isoenzyme '
                           'alpha,gamma1 <13>; #8# isoenzyme gamma2,gamma2 '
                           '<17>',
                'data': '1.7 {ethanol}',
                'refs': [13, 17, 79],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 1.7},
               {'comment': '#8# recombinant allozyme Ile308, pH 7.5, 25°C '
                           '<115>; #23# 45°C, pH 8.8, cosubstrate: '
                           '2,3-butanediol, wild-type enzyme <290>',
                'data': '0.063 {NAD+}',
                'refs': [115, 290],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.063},
               {'chebi': 'CHEBI_16236',
                'comment': '#31# 70°C, pH 9.0, 50 mM Tris-HCl, 4 M NaCl <181>; '
                           '#8# isoenzyme beta1,beta1, 0.1 M sodium phosphate '
                           'buffer, pH 7.5, at 25 °C <20>',
                'data': '0.022 {ethanol}',
                'refs': [20, 181],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 0.022},
               {'chebi': 'CHEBI_17336',
                'comment': '#36# isoenzyme BB-ADH <95>; #8# isozyme ADH1B1, pH '
                           '7.5, 25°C <119>; #8# pH 7.5, 25°C, isozyme ADH1B1 '
                           '<107>',
                'data': '0.03 {all-trans-retinol}',
                'refs': [95, 107, 119],
                'substrate': 'all-trans-retinol',
                'units': 'mM',
                'value': 0.03},
               {'chebi': 'CHEBI_16236',
                'comment': '#36# isoenzyme TT-ADH <95>',
                'data': '28 {ethanol}',
                'refs': [53, 95],
                'substrate': 'ethanol',
                'units': 'mM',
                'value': 28.0},
               {'comment': '#55# oxidation of ethanol <99>; #8# recombinant '
                           'allozyme Val308, pH 7.5, 25°C <115>',
                'data': '0.074 {NAD+}',
                'refs': [99, 115],
                'substrate': 'NAD+',
                'units': 'mM',
                'value': 0.074},
               {'comment': '#9# isoenzyme ADH-1, pH 10.0 <49>',
                'data': '0.1 {12-hydroxydodecanoate}',
                'refs': [16, 49],
                'substrate': '12-hydroxydodecanoate',
                'units': 'mM',
                'value': 0.1}]),
             ('LO',
              [{'comment': '#61# 2 isozymes <113>; #24# enzyme polymer forms '
                           'rod-like helical particles <128>',
                'data': 'cytosol',
                'refs': [113, 128, 135, 194, 214]}]),
             ('ME',
              [{'comment': '#10# activates <87>; #110# dependent on <210>; '
                           '#46# zinc-containing metalloenzyme <164>; '
                           '#5,41,87# catalytic zinc ion <110,111,127>; #46# '
                           'zinc-containing enzyme <161>; #5# 1 catalytic and '
                           '1 structural zinc ion per subunit <119>; #27# 1 '
                           'catalytic and 1 structural zinc ion per subunit, '
                           'coordination complex geometry <129>; #13# 1 '
                           'catalytic zinc ion and 1 structural zinc ion per '
                           'enzyme subunit <112>; #44# 1 tightly bound ion per '
                           'subunit <114>; #61# ADH I contains 1 Zn2+ per '
                           'subunit, while ADH II does not contains any metal '
                           'ions <113>; #10# all isozymes, amino acid residues '
                           'involved in zinc in binding are Cys46, Cys174, '
                           'His67, Glu68, Asp49, and Thr48, binding mode '
                           '<120>; #8# catalytic zinc <109>; #10# included '
                           'into the crystal strcuture <104>; #10# native '
                           'enzyme contains catalytic zinc ions <122>; #46# '
                           'the catalytic active site zinc ion is bound to '
                           'Glu69 in the apoenzyme state, but not in the '
                           'ternary complex state <108>; #94# ADH is a '
                           'putative zinc-dependent alcohol dehydrogenase '
                           '<162>; #46# contains a zinc ion which is directly '
                           'involved in the structural stabilization of enzyme '
                           'molecule <155>; #46# contains eight zinc atoms per '
                           'tetramer <163>; #6# 1 mM ZnSO4, 1.14fold '
                           'activation <169>; #26# 1 mM ZnSO4, 1.3fold '
                           'activation <188>; #5# 2 atoms are included in each '
                           '40 kDa subunit, while one of the zinc ions is '
                           'considered to serve a structural function only, '
                           'the other zinc ion functions as a Lewis acid and '
                           'activates the substrate in the active site, which '
                           'is located in a cleft between the catalytic and '
                           'the coenzyme binding domain <200>; #10# contains '
                           'Zn2+ <209>; #111# maximum activity is reached at '
                           '0.5 mM Zn2+,Ta1316 ADH is able to tolerate high '
                           'concentrations of Zn2+ <213>; #41# zinc '
                           'metalloenzyme with two zinc atoms per subunit '
                           '<201>; #122# the enzyme likely contains 2 Zn2+ '
                           '<217>; #6# 1 mM, 114% of initial activity <169>; '
                           '#149# stimulation. Crystal structure of alcohol '
                           'dehydrogenase domain contains 0.43 Zn atoms per '
                           'protein monomer <241>; #10# 0.5 mM, substrate '
                           'glycolaldehyde, 32.9% residual activity <285>; '
                           '#161# Pcal_1311 is contains two zinc atoms per '
                           'subunit. Twofold increase in enzyme activity of '
                           'Pcal_1311 when produced in the presence of 25 '
                           'microM Zn2+ as compared to the protein produced in '
                           'tap water <286>',
                'data': 'Zn2+',
                'refs': [87,
                         104,
                         108,
                         109,
                         110,
                         111,
                         112,
                         113,
                         114,
                         119,
                         120,
                         122,
                         127,
                         129,
                         155,
                         161,
                         162,
                         163,
                         164,
                         169,
                         188,
                         200,
                         201,
                         209,
                         210,
                         211,
                         213,
                         217,
                         241,
                         285,
                         286]},
               {'comment': '#105# zinc enzyme <220>; #18# required for '
                           'activity, tightly bound within the enzyme <75>; '
                           '#5# isoenzyme A2 contains 2.7 mol of zinc per mol '
                           'of enzyme, isoenzyme b2 contains 1.9 mol of zinc '
                           'per mol of enzyme, isoenzyme C2 contains 3.2 mol '
                           'of zinc per mol of enzyme. A and C subunits each '
                           'contain two atoms of zinc, with at least one being '
                           'involved catalytically, the b subunit probably '
                           'contains a single non-catalytic zinc atom <48>; '
                           '#9# ADH-1 contains 3.9 mol of zinc per mol of '
                           'subunit, ADH-2 contains 4.2 mol of zinc per mol of '
                           'subunit <49>; #8# enzyme contains 7.59 zinc atoms '
                           'per molecule <96>; #79# contains 3.9 gatom of zinc '
                           'per mol of enzyme <24>; #46# 2 mM required for '
                           'optimal activity <66>; #41# substitution of '
                           'catalytic and /or noncatalytic zinc ions by '
                           'cobaltous ions <36>; #41# contains 4 zinc atoms '
                           'per molecule <42>; #8,12# contains 3.8 mol of Zn '
                           'per mol of protein <16,45>; #42# enzyme form ADH I '
                           'and ADH II contain one zinc atom per subunit <67>; '
                           '#14# contains 1 zinc atom per subunit <81>; #36# '
                           'isoenzyme AA-ADH contains 4.3 zinc atoms per '
                           'dimeric molecule, isoenzyme BB-ADH contains 3.7 '
                           'zinc atoms per dimeric molecule, isoenzyme AA-ADH '
                           'contains 4.1 zinc atoms per dimeric molecule <95>; '
                           '#55# contains 1.2 Zn atom per subunit <99>; #68# '
                           'contains 4 zinc atoms per dimer <69>; #8# zinc '
                           'containing enzyme <12>; #8# from beta1gamma1 and '
                           'gamma1gamma1 isoenzyme the active-site zinc is '
                           'extracted much more slowly than from beta1beta1 '
                           'isoenzyme. Characterization of '
                           'active-site-specific zinc-depleted and '
                           'reconstituted cobalt(II) alcohol dehydrogenase '
                           '<19>; #8# contains 3.7 gatom of zinc per mol of '
                           'enzyme <23>; #8# 3.6-4.2 gatom of zinc per mol '
                           '<21>; #43# contains 3.7-4.2 mol of zinc per mol of '
                           'enzyme <25>; #103# KmADH3 appears to belong to the '
                           'zinc-containing Adh family <177>; #104# KmADH4 '
                           'appears to belong to the zinc-containing Adh '
                           'family <177>',
                'data': 'Zinc',
                'refs': [12,
                         16,
                         19,
                         21,
                         23,
                         24,
                         25,
                         36,
                         42,
                         45,
                         48,
                         49,
                         66,
                         67,
                         69,
                         70,
                         75,
                         81,
                         95,
                         96,
                         99,
                         177,
                         220]}]),
             ('MW',
              [{'comment': '#112# SDS-PAGE <197>; #106# isozyme ADH2, apparent '
                           'molecular weight deduced from electrophoretic '
                           'mobility <214>; #109# isozyme ADH4, calculated '
                           'from amino acid sequence <214>; #92,132# 4 * '
                           '40000, SDS-PAGE <144,239>; #8,10,36,53,79# 2 * '
                           '40000, SDS-PAGE <16,23,24,59,87,95>; #1,8,80,131# '
                           'x * 40000, SDS-PAGE <11,44,52,227>; #9# 2 * 40000, '
                           'ADH-3, SDS-PAGE <49>; #42# 2 * 40000, enzyme form '
                           'ADHI <68>',
                'data': '40000',
                'refs': [11,
                         16,
                         23,
                         24,
                         44,
                         49,
                         52,
                         59,
                         68,
                         87,
                         95,
                         144,
                         197,
                         214,
                         227,
                         239,
                         272]},
               {'comment': '#8# ultracentrifugation under non-denaturing '
                           'conditions <23>',
                'data': '78000',
                'refs': [23]},
               {'comment': '#8# amino acid analysis, ultracentrifugation <18>',
                'data': '78000-85000',
                'refs': [18]},
               {'comment': '#8# ultracentrifugal analysis <21>',
                'data': '79000-84000',
                'refs': [21]},
               {'comment': '#8# equilibrium sedimentation <16>',
                'data': '82700',
                'refs': [16]},
               {'comment': '#70# 4 * 42000, SDS-PAGE <84>; #8# x * 42000, '
                           'SDS-PAGE <14>; #68# 2 * 42000, SDS-PAGE <69>; #8# '
                           '2 * 42000, anodic enzyme form, SDS-PAGE <18>; #69# '
                           '2 * 42000, enzyme form ADH-2 and ADH-3, SDS-PAGE '
                           '<60>; #61# 3 * 42000, ADH I, SDS-PAGE <113>; #23# '
                           'fusion protein, bet-AshD <289>',
                'data': '42000',
                'refs': [14, 18, 60, 69, 84, 113, 289]},
               {'comment': '#36# 2 * 41000, SDS-PAGE <47>; #8# 2 * 41000, '
                           'class III isoenzyme chi ADH, SDS-PAGE <16>',
                'data': '41000',
                'refs': [16, 47]}]),
             ('NSP',
              [{'comment': '#8# ADH4 might be involved in biosynthesis of '
                           'retinoic acid <124>',
                'data': 'all-trans-retinol + NAD+ = all-trans-retinal + NADH',
                'refs': [124, 200]},
               {'comment': '#8# ADH4 might be involved in biosynthesis of '
                           'retinoic acid <124>) {r',
                'data': 'all-trans-retinol + NAD+ = all-trans-retinal + NADH',
                'refs': [124, 200]},
               {'comment': '#5# role of the major liver isoenzyme A2 in '
                           'ethanol metabolism <48>; #41# plays an important '
                           'role in the metabolism of ethanol <102>; #8# '
                           'chi-ADH plays an important role in the metabolism '
                           'of long chain alcohols and aldehydes <21>; #8# the '
                           'anodic enzyme form may contribute significantly to '
                           'alcohol elimination in man, particularly at high '
                           'concentrations when the other enzyme species are '
                           'saturated <18>; #8# the enzyme plays a significant '
                           'role in first-pass metabolism of ethanol in human '
                           '<96>; #8# enzyme is responsible for the major '
                           'ethanol oxidation capacity in the body. The '
                           'products acetaldehyde and NADH are responsible for '
                           'the most of the toxic effects and metabolic '
                           'disturbances produced by ethanol ingestion <10>; '
                           '#10# rate-limiting step of the alcoholic '
                           'fermentation <122>; #5# DH3 plays an important '
                           'role in systemic ethanol metabolism at higher '
                           'levels of blood ethanol through activation by '
                           'cytoplasmic solution hydrophobicity <141>',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [10, 18, 21, 48, 96, 102, 116, 122, 141, 181]},
               {'comment': '#5# role of the major liver isoenzyme A2 in '
                           'ethanol metabolism <48>; #41# plays an important '
                           'role in the metabolism of ethanol <102>; #8# '
                           'chi-ADH plays an important role in the metabolism '
                           'of long chain alcohols and aldehydes <21>; #8# the '
                           'anodic enzyme form may contribute significantly to '
                           'alcohol elimination in man, particularly at high '
                           'concentrations when the other enzyme species are '
                           'saturated <18>; #8# the enzyme plays a significant '
                           'role in first-pass metabolism of ethanol in human '
                           '<96>; #8# enzyme is responsible for the major '
                           'ethanol oxidation capacity in the body. The '
                           'products acetaldehyde and NADH are responsible for '
                           'the most of the toxic effects and metabolic '
                           'disturbances produced by ethanol ingestion <10>; '
                           '#10# rate-limiting step of the alcoholic '
                           'fermentation <122>; #5# DH3 plays an important '
                           'role in systemic ethanol metabolism at higher '
                           'levels of blood ethanol through activation by '
                           'cytoplasmic solution hydrophobicity <141>) {r',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [10, 18, 21, 48, 96, 102, 116, 122, 141, 181]},
               {'comment': '#5# role of the major liver isoenzyme A2 in '
                           'ethanol metabolism <48>; #41# plays an important '
                           'role in the metabolism of ethanol <102>; #8# '
                           'chi-ADH plays an important role in the metabolism '
                           'of long chain alcohols and aldehydes <21>; #8# the '
                           'anodic enzyme form may contribute significantly to '
                           'alcohol elimination in man, particularly at high '
                           'concentrations when the other enzyme species are '
                           'saturated <18>; #8# the enzyme plays a significant '
                           'role in first-pass metabolism of ethanol in human '
                           '<96>; #8# enzyme is responsible for the major '
                           'ethanol oxidation capacity in the body. The '
                           'products acetaldehyde and NADH are responsible for '
                           'the most of the toxic effects and metabolic '
                           'disturbances produced by ethanol ingestion <10>; '
                           '#10# rate-limiting step of the alcoholic '
                           'fermentation <122>; #5# DH3 plays an important '
                           'role in systemic ethanol metabolism at higher '
                           'levels of blood ethanol through activation by '
                           'cytoplasmic solution hydrophobicity <141>) {',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [10, 18, 21, 48, 96, 102, 116, 122, 141, 181]},
               {'data': '1-butanol + NAD+ = butanal + NADH + H+',
                'refs': [229]},
               {'data': '1-butanol + NAD+ = butanal + NADH + H+ {r}',
                'refs': [229]},
               {'data': 'isobutyramide + NAD+ = ? {r}', 'refs': [124]},
               {'comment': '#10# constitutive enzyme <94>; #42# key enzyme in '
                           'ethanol production <68>; #52# one constitutive '
                           'enzyme, ADH-MI and one inducible enzyme, ADH-MII '
                           '<82>; #53# enzyme may be involved in the '
                           'metabolism of dietary wax esters in salmonid fish '
                           '<59>; #78# the enzyme oxidizes alcohols to '
                           'aldehydes or ketones both for detoxification and '
                           'metabolic purposes <38>; #36# involvement in the '
                           'development of male hamster reproductive system '
                           '<47>; #60# alcohol dehydrogenase activity may not '
                           'limit alcohol supply for ester production during '
                           'ripening <146>; #41# activity is severely reduced '
                           'towards aliphatic alcohols of more than 8 carbon '
                           'atoms for the free enzyme, but not so with '
                           'immobilized HLAD, exhibiting an activity towards '
                           'C22 and C24 aliphatic alcohols higher than 50% of '
                           'the highest value, obtained with C8 <204>; #8# '
                           'differences in the activities of total ADH and '
                           'class I ADH isoenzyme between cancer liver tissues '
                           'and healthy hepatocytes may be a factor in ethanol '
                           'metabolism disorders, which can intensify '
                           'carcinogenesis <180>; #112# TADH is a '
                           'NAD(H)-dependent enzyme and shows a very broad '
                           'substrate spectrum producing exclusively the '
                           '(S)-enantiomer in high enantiomeric excess (more '
                           'than 99%) during asymmetric reduction of ketones '
                           '<197>; #123# the physiological direction of the '
                           'catalytic reaction is reduction rather than '
                           'oxidation <219>) {',
                'data': 'more = ?',
                'refs': [38, 47, 59, 68, 82, 94, 146, 180, 197, 204, 219]}]),
             ('PHO',
              [{'comment': '#5,8# assay at <107,124,200>; #55# reduction of '
                           'acetaldehyde <99>; #3# reduction of substrate <4>; '
                           '#75# and second optimum at pH 9.9 <64>; #46# '
                           'reduction of anisaldehyde <66>; #8# kinetic '
                           'analysis assay at <115>; #10# Zn-ADH, Co-ADH, and '
                           'Cu-ADH <122>; #10# enzyme covalently immobilized '
                           'to magnetic Fe3O4 nanoparticles via glutaraldehyde '
                           '<182>; #10# immobilized enzyme, at 25°C <196>; #8# '
                           'assay at, class IV enzyme, reduction reaction '
                           '<229>',
                'data': '7.5',
                'refs': [4,
                         64,
                         66,
                         99,
                         107,
                         115,
                         122,
                         124,
                         182,
                         196,
                         200,
                         229]},
               {'comment': '#3# oxidation of substrate <4>; #18# wild-type '
                           'enzyme ADH1-1S <97>; #46# oxidation of benzyl '
                           'alcohol <66>; #8# isoenzyme beta2,beta2 <20>; '
                           '#128# oxidation reaction <225>; #61# assay at, '
                           'forward reaction, ADH I and ADH II <113>; #8# '
                           'isozyme ADH1B2, assay at <119>; #46# mutant enzyme '
                           'N249Y <154>; #8# assay at, total ADH activity '
                           '<229>',
                'data': '8.5',
                'refs': [4, 20, 66, 97, 105, 113, 119, 154, 225, 229]},
               {'comment': '#41# assay at <111>; #119# oxidation of ethanol '
                           '<256>; #4,72# and a second optimum at pH 9.5 <64>; '
                           '#18# mutant enzyme ADH1-1S1108 <97>; #48# aldehyde '
                           'reduction <223>; #8# assay at, class III enzyme, '
                           'reduction reaction <229>; #132# reduction of '
                           '2-pentanone <239>; #151# oxidation of crotyl '
                           'aclohol <244>',
                'data': '8',
                'refs': [64, 97, 106, 111, 215, 223, 229, 239, 244, 252, 256]},
               {'comment': '#5# assay at <119>; #73# oxidation of ethanol <2>; '
                           '#8# isoenzyme beta1,beta1 <20>; #8# isozyme '
                           'ADH1B1, ADH4, assay at <119>; #122# oxidation of '
                           '1-hexanol <217>; #132# oxidation of 2-pentanol '
                           '<239>',
                'data': '10.5',
                'refs': [2, 10, 20, 119, 217, 239, 284]},
               {'comment': '#8# and a second optimum at pH 10.0-10.5, ADH '
                           'Indianapolis form 2 and 3 <22>',
                'data': '10-10.5',
                'refs': [22]},
               {'comment': '#8# and a second optimum at pH 10.0-10.5, ADH '
                           'Indianapolis form 2 and 3 <22>',
                'data': '7-7.5',
                'refs': [22, 211]},
               {'comment': '#8# acetaldehyde reduction of isoenzyme '
                           'beta2,beta2 <15>',
                'data': '7.4',
                'refs': [15]},
               {'comment': '#8# assay at, class II enzyme, reduction reaction '
                           '<229>',
                'data': '7.6',
                'refs': [229]},
               {'comment': '#8# ethanol oxidation, isoenzyme beta2,beta2, '
                           'beta2,beta1, alpha,beta2 and beta2gamma1 <15>',
                'data': '8.5-8.8',
                'refs': [15]},
               {'comment': '#163# assay at <288>; #164# assay <291>; #8# '
                           'isoenzyme beta3,beta3 <20>; #8# ADH Indianapolis '
                           'form 1 <22>; #122# reduction of benzaldehyde '
                           '<217>; #10# free enzyme, at 25°C <196>',
                'data': '7',
                'refs': [20, 22, 82, 132, 196, 217, 252, 288, 291]},
               {'comment': '#12# and a second lower maximum at pH 7.5 <45>',
                'data': '10.8',
                'refs': [12, 45]},
               {'comment': '#129# assay at <230>; #42# enzyme form ADH-II, '
                           'oxidation of ethanol <67,68>; #8# standard assay '
                           'at <115>; #124# alcohol oxidation reaction <218>; '
                           '#133# optimally active with 1-butanol at pH 10.0 '
                           'with 4 M KCl <237>; #161# glycine\x96NaOH buffer, '
                           'highest activity for oxidation of ethanol <286>',
                'data': '10',
                'refs': [67, 68, 75, 96, 115, 118, 218, 230, 237, 286]},
               {'comment': '#8# acetaldehyde reduction, isoenzyme beta1,beta1 '
                           '<15>',
                'data': '5.9',
                'refs': [15, 133]},
               {'comment': '#8,41# assay at <116,117>',
                'data': '7.3',
                'refs': [116, 117]},
               {'comment': '#47# oxidation of 2-phenylethanol <149>',
                'data': '10.4',
                'refs': [14, 149]}]),
             ('PHR',
              [{'comment': '#8# pH 8.0: about 40% of maximal activity, pH '
                           '10.5: about 85% of maximal activity <96>',
                'data': '8-10.5',
                'refs': [96]},
               {'comment': '#8# about 30% of maximal activity at pH 8.0 and at '
                           'pH 12.0 <14>; #47# pH 8.0: about 50% of maximal '
                           'activity, pH 12.0: about 50% of maximal activity, '
                           'oxidation of 2-phenylethanol <149>; #31# pH 8.0: '
                           'about 70% of maximal activity, pH 12: about 60% of '
                           'maximal activity <181>',
                'data': '8-12',
                'refs': [14, 149, 181]}]),
             ('PHS',
              [{'comment': '#8# stable <12>', 'data': '7-10.6', 'refs': [12]}]),
             ('PU',
              [{'data': '(anodic enzyme form)', 'refs': [18]},
               {'data': '(class I isoenzymes)', 'refs': [13]},
               {'data': '(class II isoenzyme: pi-ADH)', 'refs': [14]},
               {'data': '(class III isoenzyme chi-ADH)', 'refs': [16]},
               {'data': '(isoenzyme beta3,beta3)', 'refs': [20]},
               {'data': '(recombinant ADH2 alloenzymes from Escherichia coli '
                        'by DEAE and AMP or blue Sepharose chromatography, and '
                        'ultrafiltration)',
                'refs': [115]},
               {'data': '(recombinant enzyme from Escherichia coli by DEAE ion '
                        "exchange, 5'-AMP-resin affinity, and Mono Q ion "
                        'exchange chromatography)',
                'refs': [124]},
               {'data': '(recombinant isozymes from Escherichia coli strain '
                        'BL21)',
                'refs': [119]},
               {'data': '', 'refs': [12, 15]}]),
             ('RE',
              {'a primary alcohol + NAD+ = an aldehyde + NADH + H+ (#4,41# '
               'ordered bi-bi mechanism <31,43>; #4,75# rapid equilibrium '
               'random mechanism <63>; #8# ordered bi bi mechanism with '
               'cofactor adding first to form a binary enzyme complex <23>; '
               '#41# isoenzyme EE and SS: ordered bi bi mechanism <35>; '
               '#10,33# mechanism is predominantly ordered with ethanol, but '
               'partially random with butanol <91>; #41# kinetic mechanism is '
               'random for ethanol oxidation and compulsory ordered for '
               'acetaldehyde reduction <41>; #38# oxidizes ethanol in an '
               'ordered bi-bi mechanism with NAD+ as the first substrate fixed '
               '<85>; #10# compulsory-order mechanism with the rate-limiting '
               'step being the dissociation of the product enzyme-NAD+ complex '
               '<90>; #28,68,78# Theorell-Chance mechanism <38,69,74>; #44# '
               'sequential reaction mechanism <114>; #87# active site '
               'structure <127>; #78# catalytic mechanism involves a proton '
               'relay modulated by the coupled ionization of the active site '
               'Lys155/Tyr151 pair, and a NAD+ ribose 2-OH switch, other '
               'active site residues are Ser138 and Trp144, ionization '
               'properties, substrate binding, overview <130>; #8# class IV '
               'alcohol dehydrogenase also functions as retinol dehydrogenase, '
               'reaction and kinetic mechanism: asymmetric rapid equilibrium '
               'random mechanism with 2 dead-end ternary complexes fro retinol '
               'oxidation and a rapid equilibrium ordered mechanism with one '
               'dead-end ternary complex for retinal reduction, a unique '
               'mechanistic form fro zinc-containing ADH in the medium chain '
               'dehydrogenase/reductase superfamily of enzymes <124>; #10# '
               'detailed determination of the reaction and kinetic mechanisms, '
               'active site structure and determination of amino acid residues '
               'involved in catalysis, 3 isozymes <120>; #5# ordered bibi '
               'mechanism, structural and functional implications of amino '
               'acid residue 47 <110>; #41# ordered sequential bibi reaction '
               'mechanism, modeling of oxidation kinetic mechanism <117>; #41# '
               'reaction mechanism, His51 is involved, but not essential, in '
               'catalysis facilitating the deprotonation of the hydroxyl group '
               'of water or alcohol ligated to the catalytic zinc <111>; #8# '
               'Ser48 is involved in catalysis, isozyme gamma(2)gamma(2) '
               '<109>; #27# the catalytic triad consists of Cys44, His67, and '
               'Cys154, active site structure <129>)',
               'a secondary alcohol + NAD+ = a ketone + NADH + H+'}),
             ('RN', {'alcohol dehydrogenase'}),
             ('RT', {'reduction', 'redox reaction', 'oxidation'}),
             ('SA',
              [{'data': '0.6',
                'refs': [16],
                'units': 'µmol/min/mg',
                'value': 0.6},
               {'data': '0.65',
                'refs': [21],
                'units': 'µmol/min/mg',
                'value': 0.65},
               {'data': '1.47',
                'refs': [14],
                'units': 'µmol/min/mg',
                'value': 1.47},
               {'data': '3.3',
                'refs': [12],
                'units': 'µmol/min/mg',
                'value': 3.3},
               {'comment': '#9# ADH-3 <49>',
                'data': '1.3',
                'refs': [18, 49],
                'units': 'µmol/min/mg',
                'value': 1.3}]),
             ('SN', {'alcohol:NAD+ oxidoreductase'}),
             ('SP',
              [{'comment': '#88# best substrate <118>; #8# class III isoenzyme '
                           'chi-ADH oxidizes ethanol very poorly <16>; #8# no '
                           'oxidation with class III enzyme <11>; #9# '
                           'isoenzyme ADH-1 and ADH-3, no activity with '
                           'isoenzyme ADH-2 <49>; #55# the reduction of '
                           'acetaldehyde is 4.9fold faster than the oxidation '
                           'of ethanol <99>; #52# the reduction of '
                           'acetaldehyde of ADH-MII is about 7times higher '
                           'than that of the oxidation of ethanol <82>; #5# no '
                           'activity with isoenzyme B2, oxidized by isoenzyme '
                           'A2 and C2 <48>; #5# role of the major liver '
                           'isoenzyme A2 in ethanol metabolism <48>; #41# '
                           'plays an important role in the metabolism of '
                           'ethanol <102>; #8# chi-ADH plays an important role '
                           'in the metabolism of long chain alcohols and '
                           'aldehydes <21>; #8# the anodic enzyme form may '
                           'contribute significantly to alcohol elimination in '
                           'man, particularly at high concentrations when the '
                           'other enzyme species are saturated <18>; #8# the '
                           'enzyme plays a significant role in first-pass '
                           'metabolism of ethanol in human <96>; #8# enzyme is '
                           'responsible for the major ethanol oxidation '
                           'capacity in the body. The products acetaldehyde '
                           'and NADH are responsible for the most of the toxic '
                           'effects and metabolic disturbances produced by '
                           'ethanol ingestion <10>; #10# rate-limiting step of '
                           'the alcoholic fermentation <122>; #41# '
                           'isomerization of the enzyme-NAD+ complex is the '
                           'rate-limiting step for acetaldehyde reduction by '
                           'the wild-type enzyme <111>; #90# no cooperativity '
                           'between the 2 active sites of the enzyme <105>; '
                           '#5# DH3 plays an important role in systemic '
                           'ethanol metabolism at higher levels of blood '
                           'ethanol through activation by cytoplasmic solution '
                           'hydrophobicity <141>; #47# 76% of the activity '
                           'with 2-phenylethanol <149>; #13# proton and '
                           'hydride equivalent transfer in the alcohol '
                           'dehydrogenase enzymatic reaction are modulated by '
                           'the correlated motions between NAD+ and the '
                           'cofactor domain <176>) |#61# acetaldehyde is the '
                           'best substrate for isozyme ADH I <113>',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [2,
                         6,
                         10,
                         11,
                         12,
                         13,
                         14,
                         16,
                         17,
                         18,
                         20,
                         21,
                         24,
                         25,
                         28,
                         35,
                         41,
                         42,
                         43,
                         45,
                         47,
                         48,
                         49,
                         51,
                         52,
                         53,
                         59,
                         60,
                         64,
                         65,
                         67,
                         68,
                         69,
                         71,
                         72,
                         73,
                         74,
                         75,
                         76,
                         77,
                         78,
                         81,
                         82,
                         83,
                         84,
                         87,
                         90,
                         92,
                         95,
                         96,
                         97,
                         99,
                         101,
                         102,
                         105,
                         111,
                         113,
                         115,
                         116,
                         117,
                         118,
                         119,
                         120,
                         121,
                         122,
                         126,
                         128,
                         135,
                         141,
                         147,
                         149,
                         170,
                         172,
                         176,
                         181]},
               {'comment': '#88# best substrate <118>; #8# class III isoenzyme '
                           'chi-ADH oxidizes ethanol very poorly <16>; #8# no '
                           'oxidation with class III enzyme <11>; #9# '
                           'isoenzyme ADH-1 and ADH-3, no activity with '
                           'isoenzyme ADH-2 <49>; #55# the reduction of '
                           'acetaldehyde is 4.9fold faster than the oxidation '
                           'of ethanol <99>; #52# the reduction of '
                           'acetaldehyde of ADH-MII is about 7times higher '
                           'than that of the oxidation of ethanol <82>; #5# no '
                           'activity with isoenzyme B2, oxidized by isoenzyme '
                           'A2 and C2 <48>; #5# role of the major liver '
                           'isoenzyme A2 in ethanol metabolism <48>; #41# '
                           'plays an important role in the metabolism of '
                           'ethanol <102>; #8# chi-ADH plays an important role '
                           'in the metabolism of long chain alcohols and '
                           'aldehydes <21>; #8# the anodic enzyme form may '
                           'contribute significantly to alcohol elimination in '
                           'man, particularly at high concentrations when the '
                           'other enzyme species are saturated <18>; #8# the '
                           'enzyme plays a significant role in first-pass '
                           'metabolism of ethanol in human <96>; #8# enzyme is '
                           'responsible for the major ethanol oxidation '
                           'capacity in the body. The products acetaldehyde '
                           'and NADH are responsible for the most of the toxic '
                           'effects and metabolic disturbances produced by '
                           'ethanol ingestion <10>; #10# rate-limiting step of '
                           'the alcoholic fermentation <122>; #41# '
                           'isomerization of the enzyme-NAD+ complex is the '
                           'rate-limiting step for acetaldehyde reduction by '
                           'the wild-type enzyme <111>; #90# no cooperativity '
                           'between the 2 active sites of the enzyme <105>; '
                           '#5# DH3 plays an important role in systemic '
                           'ethanol metabolism at higher levels of blood '
                           'ethanol through activation by cytoplasmic solution '
                           'hydrophobicity <141>; #47# 76% of the activity '
                           'with 2-phenylethanol <149>; #13# proton and '
                           'hydride equivalent transfer in the alcohol '
                           'dehydrogenase enzymatic reaction are modulated by '
                           'the correlated motions between NAD+ and the '
                           'cofactor domain <176>) |#61# acetaldehyde is the '
                           'best substrate for isozyme ADH I <113>| {r',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [2,
                         6,
                         10,
                         11,
                         12,
                         13,
                         14,
                         16,
                         17,
                         18,
                         20,
                         21,
                         24,
                         25,
                         28,
                         35,
                         41,
                         42,
                         43,
                         45,
                         47,
                         48,
                         49,
                         51,
                         52,
                         53,
                         59,
                         60,
                         64,
                         65,
                         67,
                         68,
                         69,
                         71,
                         72,
                         73,
                         74,
                         75,
                         76,
                         77,
                         78,
                         81,
                         82,
                         83,
                         84,
                         87,
                         90,
                         92,
                         95,
                         96,
                         97,
                         99,
                         101,
                         102,
                         105,
                         111,
                         113,
                         115,
                         116,
                         117,
                         118,
                         119,
                         120,
                         121,
                         122,
                         126,
                         128,
                         135,
                         141,
                         147,
                         149,
                         170,
                         172,
                         176,
                         181]},
               {'comment': '#88# best substrate <118>; #8# class III isoenzyme '
                           'chi-ADH oxidizes ethanol very poorly <16>; #8# no '
                           'oxidation with class III enzyme <11>; #9# '
                           'isoenzyme ADH-1 and ADH-3, no activity with '
                           'isoenzyme ADH-2 <49>; #55# the reduction of '
                           'acetaldehyde is 4.9fold faster than the oxidation '
                           'of ethanol <99>; #52# the reduction of '
                           'acetaldehyde of ADH-MII is about 7times higher '
                           'than that of the oxidation of ethanol <82>; #5# no '
                           'activity with isoenzyme B2, oxidized by isoenzyme '
                           'A2 and C2 <48>; #5# role of the major liver '
                           'isoenzyme A2 in ethanol metabolism <48>; #41# '
                           'plays an important role in the metabolism of '
                           'ethanol <102>; #8# chi-ADH plays an important role '
                           'in the metabolism of long chain alcohols and '
                           'aldehydes <21>; #8# the anodic enzyme form may '
                           'contribute significantly to alcohol elimination in '
                           'man, particularly at high concentrations when the '
                           'other enzyme species are saturated <18>; #8# the '
                           'enzyme plays a significant role in first-pass '
                           'metabolism of ethanol in human <96>; #8# enzyme is '
                           'responsible for the major ethanol oxidation '
                           'capacity in the body. The products acetaldehyde '
                           'and NADH are responsible for the most of the toxic '
                           'effects and metabolic disturbances produced by '
                           'ethanol ingestion <10>; #10# rate-limiting step of '
                           'the alcoholic fermentation <122>; #41# '
                           'isomerization of the enzyme-NAD+ complex is the '
                           'rate-limiting step for acetaldehyde reduction by '
                           'the wild-type enzyme <111>; #90# no cooperativity '
                           'between the 2 active sites of the enzyme <105>; '
                           '#5# DH3 plays an important role in systemic '
                           'ethanol metabolism at higher levels of blood '
                           'ethanol through activation by cytoplasmic solution '
                           'hydrophobicity <141>; #47# 76% of the activity '
                           'with 2-phenylethanol <149>; #13# proton and '
                           'hydride equivalent transfer in the alcohol '
                           'dehydrogenase enzymatic reaction are modulated by '
                           'the correlated motions between NAD+ and the '
                           'cofactor domain <176>) |#61# acetaldehyde is the '
                           'best substrate for isozyme ADH I <113>| {',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH',
                'refs': [2,
                         6,
                         10,
                         11,
                         12,
                         13,
                         14,
                         16,
                         17,
                         18,
                         20,
                         21,
                         24,
                         25,
                         28,
                         35,
                         41,
                         42,
                         43,
                         45,
                         47,
                         48,
                         49,
                         51,
                         52,
                         53,
                         59,
                         60,
                         64,
                         65,
                         67,
                         68,
                         69,
                         71,
                         72,
                         73,
                         74,
                         75,
                         76,
                         77,
                         78,
                         81,
                         82,
                         83,
                         84,
                         87,
                         90,
                         92,
                         95,
                         96,
                         97,
                         99,
                         101,
                         102,
                         105,
                         111,
                         113,
                         115,
                         116,
                         117,
                         118,
                         119,
                         120,
                         121,
                         122,
                         126,
                         128,
                         135,
                         141,
                         147,
                         149,
                         170,
                         172,
                         176,
                         181]},
               {'comment': '#10# no activity <87>; #42# very low activity '
                           '<67>; #55# 3% of the activity with ethanol <99>',
                'data': 'propan-2-ol + NAD+ = acetone + NADH',
                'refs': [14,
                         43,
                         45,
                         61,
                         64,
                         65,
                         66,
                         67,
                         68,
                         81,
                         84,
                         85,
                         87,
                         90,
                         92,
                         97,
                         99]},
               {'comment': '#10# no activity <87>; #42# very low activity '
                           '<67>; #55# 3% of the activity with ethanol <99>) {',
                'data': 'propan-2-ol + NAD+ = acetone + NADH',
                'refs': [14,
                         43,
                         45,
                         61,
                         64,
                         65,
                         66,
                         67,
                         68,
                         81,
                         84,
                         85,
                         87,
                         90,
                         92,
                         97,
                         99]},
               {'data': 'propanol + NADH = propionaldehyde + NADH',
                'refs': [20,
                         45,
                         53,
                         59,
                         61,
                         65,
                         66,
                         67,
                         68,
                         71,
                         75,
                         77,
                         78,
                         83,
                         84,
                         85,
                         87,
                         90,
                         96,
                         97,
                         99]},
               {'data': 'propanol + NADH = propionaldehyde + NADH {}',
                'refs': [20,
                         45,
                         53,
                         59,
                         61,
                         65,
                         66,
                         67,
                         68,
                         71,
                         75,
                         77,
                         78,
                         83,
                         84,
                         85,
                         87,
                         90,
                         96,
                         97,
                         99]},
               {'comment': '#18# no activity <97>; #18# weak activity <75>; '
                           '#41# (R)-2-butanol and (S)-2-butanol <31>',
                'data': 'butan-2-ol + NAD+ = butan-2-one + NADH',
                'refs': [20,
                         31,
                         47,
                         53,
                         59,
                         61,
                         64,
                         66,
                         75,
                         83,
                         84,
                         85,
                         92,
                         95,
                         97]},
               {'comment': '#18# no activity <97>; #18# weak activity <75>; '
                           '#41# (R)-2-butanol and (S)-2-butanol <31>) {',
                'data': 'butan-2-ol + NAD+ = butan-2-one + NADH',
                'refs': [20,
                         31,
                         47,
                         53,
                         59,
                         61,
                         64,
                         66,
                         75,
                         83,
                         84,
                         85,
                         92,
                         95,
                         97]},
               {'comment': '#10# weak <87>; #42# activity with ADH I, no '
                           'activity with ADH II <68>; #42# oxidized by enzyme '
                           'form ADH-I, no activity with enzyme form ADH-II '
                           '<67>; #9# pH 10.0: oxidized by ADH-1 and ADH-3, no '
                           'activity with isoenzyme ADH-2 <49>',
                'data': 'butanol + NAD+ = butyraldehyde + NADH',
                'refs': [16,
                         18,
                         20,
                         42,
                         45,
                         47,
                         49,
                         53,
                         59,
                         60,
                         61,
                         64,
                         66,
                         67,
                         68,
                         75,
                         77,
                         78,
                         83,
                         85,
                         87,
                         90,
                         95,
                         96,
                         97,
                         101]},
               {'comment': '#10# weak <87>; #42# activity with ADH I, no '
                           'activity with ADH II <68>; #42# oxidized by enzyme '
                           'form ADH-I, no activity with enzyme form ADH-II '
                           '<67>; #9# pH 10.0: oxidized by ADH-1 and ADH-3, no '
                           'activity with isoenzyme ADH-2 <49>) {',
                'data': 'butanol + NAD+ = butyraldehyde + NADH',
                'refs': [16,
                         18,
                         20,
                         42,
                         45,
                         47,
                         49,
                         53,
                         59,
                         60,
                         61,
                         64,
                         66,
                         67,
                         68,
                         75,
                         77,
                         78,
                         83,
                         85,
                         87,
                         90,
                         95,
                         96,
                         97,
                         101]},
               {'data': '7-cis-retinol + NAD+ = 7-cis-retinal + NADH',
                'refs': [119]},
               {'data': 'octanol + NAD+ = octanal + NADH',
                'refs': [110, 115, 200]},
               {'comment': '#48# best substrate <223>; #111# 100% activity '
                           '<213>; #100# no activity with NADP+, in reverse '
                           'reaction no activity with NADPH <171>; #31# the '
                           'enzyme is highly specific for ethanol with NAD+ as '
                           'the coenzyme <181>; #112# 88% activity compared to '
                           'cyclohexanol <197>; #106# substrate for isozyme '
                           'ADH1C, extremely poor substrate for isozyme ADH3 '
                           '<214>; #106# substrate for isozyme ADH2 <214>; '
                           '#109# substrate for isozyme ADH4 <214>; #133# the '
                           'enzyme shows a preference for short-chain alcohols '
                           'ethanol and 1-propanol <237>; #155# 12% of the '
                           'activity with butan-1-ol <271>; #161# 33% of the '
                           'activity with 1,4-butanediol <286>) |#119# 83% of '
                           'the activity with butan-2-ol <256>',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [66,
                         103,
                         136,
                         139,
                         140,
                         143,
                         144,
                         147,
                         148,
                         153,
                         159,
                         161,
                         162,
                         163,
                         171,
                         173,
                         174,
                         181,
                         194,
                         195,
                         196,
                         197,
                         203,
                         205,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         222,
                         223,
                         231,
                         233,
                         237,
                         239,
                         246,
                         252,
                         256,
                         271,
                         277,
                         279,
                         284,
                         286,
                         288]},
               {'comment': '#48# best substrate <223>; #111# 100% activity '
                           '<213>; #100# no activity with NADP+, in reverse '
                           'reaction no activity with NADPH <171>; #31# the '
                           'enzyme is highly specific for ethanol with NAD+ as '
                           'the coenzyme <181>; #112# 88% activity compared to '
                           'cyclohexanol <197>; #106# substrate for isozyme '
                           'ADH1C, extremely poor substrate for isozyme ADH3 '
                           '<214>; #106# substrate for isozyme ADH2 <214>; '
                           '#109# substrate for isozyme ADH4 <214>; #133# the '
                           'enzyme shows a preference for short-chain alcohols '
                           'ethanol and 1-propanol <237>; #155# 12% of the '
                           'activity with butan-1-ol <271>; #161# 33% of the '
                           'activity with 1,4-butanediol <286>) |#119# 83% of '
                           'the activity with butan-2-ol <256>| {r',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [66,
                         103,
                         136,
                         139,
                         140,
                         143,
                         144,
                         147,
                         148,
                         153,
                         159,
                         161,
                         162,
                         163,
                         171,
                         173,
                         174,
                         181,
                         194,
                         195,
                         196,
                         197,
                         203,
                         205,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         222,
                         223,
                         231,
                         233,
                         237,
                         239,
                         246,
                         252,
                         256,
                         271,
                         277,
                         279,
                         284,
                         286,
                         288]},
               {'comment': '#48# best substrate <223>; #111# 100% activity '
                           '<213>; #100# no activity with NADP+, in reverse '
                           'reaction no activity with NADPH <171>; #31# the '
                           'enzyme is highly specific for ethanol with NAD+ as '
                           'the coenzyme <181>; #112# 88% activity compared to '
                           'cyclohexanol <197>; #106# substrate for isozyme '
                           'ADH1C, extremely poor substrate for isozyme ADH3 '
                           '<214>; #106# substrate for isozyme ADH2 <214>; '
                           '#109# substrate for isozyme ADH4 <214>; #133# the '
                           'enzyme shows a preference for short-chain alcohols '
                           'ethanol and 1-propanol <237>; #155# 12% of the '
                           'activity with butan-1-ol <271>; #161# 33% of the '
                           'activity with 1,4-butanediol <286>) |#119# 83% of '
                           'the activity with butan-2-ol <256>| {',
                'data': 'ethanol + NAD+ = acetaldehyde + NADH + H+',
                'refs': [66,
                         103,
                         136,
                         139,
                         140,
                         143,
                         144,
                         147,
                         148,
                         153,
                         159,
                         161,
                         162,
                         163,
                         171,
                         173,
                         174,
                         181,
                         194,
                         195,
                         196,
                         197,
                         203,
                         205,
                         207,
                         208,
                         209,
                         210,
                         211,
                         212,
                         213,
                         214,
                         222,
                         223,
                         231,
                         233,
                         237,
                         239,
                         246,
                         252,
                         256,
                         271,
                         277,
                         279,
                         284,
                         286,
                         288]},
               {'comment': '#8# ADH4 might be involved in biosynthesis of '
                           'retinoic acid <124>',
                'data': 'all-trans-retinol + NAD+ = all-trans-retinal + NADH',
                'refs': [47, 53, 93, 95, 107, 119, 124, 200]},
               {'comment': '#8# ADH4 might be involved in biosynthesis of '
                           'retinoic acid <124>) {r',
                'data': 'all-trans-retinol + NAD+ = all-trans-retinal + NADH',
                'refs': [47, 53, 93, 95, 107, 119, 124, 200]},
               {'comment': '#42# activity with ADH I, no activity with ADH II '
                           '<68>',
                'data': 'hexanol + NAD+ = n-hexanal + NADH',
                'refs': [20, 21, 42, 48, 53, 68, 84, 92, 95, 101]},
               {'comment': '#42# activity with ADH I, no activity with ADH II '
                           '<68>) {',
                'data': 'hexanol + NAD+ = n-hexanal + NADH',
                'refs': [20, 21, 42, 48, 53, 68, 84, 92, 95, 101]},
               {'comment': '#69# no activity <60>; #8# class III isoenzyme '
                           'chi-ADH shows no activity <16>; #5# oxidized by '
                           'isoenzyme A2, no activity with isoenzyme B2 and C2 '
                           '<48>',
                'data': 'ethylene glycol + NAD+ = ? + NADH',
                'refs': [13, 14, 16, 48, 60, 85]},
               {'comment': '#69# no activity <60>; #8# class III isoenzyme '
                           'chi-ADH shows no activity <16>; #5# oxidized by '
                           'isoenzyme A2, no activity with isoenzyme B2 and C2 '
                           '<48>) {',
                'data': 'ethylene glycol + NAD+ = ? + NADH',
                'refs': [13, 14, 16, 48, 60, 85]},
               {'data': '11-cis-retinol + NAD+ = 11-cis-retinal + NADH',
                'refs': [93, 119]},
               {'comment': '#5,8# no activity with isozyme ADH1 <119>',
                'data': '13-cis-retinol + NAD+ = 13-cis-retinal + NADH',
                'refs': [93, 119]},
               {'data': '9-cis-retinol + NAD+ = 9-cis-retinal + NADH',
                'refs': [93, 119]},
               {'comment': '#5# oxidized by isoenzyme A2 and B2, no activity '
                           'with isoenzyme C2 <48>',
                'data': 'pentanal + NAD+ = pentanone + NADH',
                'refs': [14, 16, 18, 20, 24, 25, 48, 53, 84, 92, 96]},
               {'comment': '#8,18,38,42,69,70# no activity '
                           '<21,60,67,68,75,84,85>; #88# low activity <118>; '
                           '#52# reaction is extremly weak <82>; #8# anodic '
                           'enzyme form shows no activity <18>; #12# no '
                           'activity at pH 7.5, slight activity at pH 10.8 '
                           '<45>; #5# weak activity with isoenzyme A2, no '
                           'activity with isoenzyme B2 and C2 <48>; #9# '
                           'oxidized with ADH-3, no activity with ADH-1 and '
                           'ADH-2 <49>; #8# class I isoenzymes <13>; #8# no '
                           'activity with isoenzyme beta3,beta3 <20>; #79# '
                           'reaction is catalyzed by the pyrazole-sensitive '
                           'enzyme, no activity with the pyrazole-insensitive '
                           'enzyme <24>; #43# reaction is catalyzed by the '
                           'cathodic pyrazole-sensitive enzyme, no activity by '
                           'the cathodic pyrazole-insensitive enzyme and by '
                           'the anodic pyrazole-insensitive enzyme <25>; #8# '
                           'activity detected with class II isoenzyme pi-ADH '
                           '<14>; #8# oxidized by isoenzyme beta1,beta1 <20>; '
                           '#8# class III isoenzyme chi-ADH shows no activity '
                           '<16>; #8# no activity with class III enzyme <11>; '
                           '#111# 49.9% activity compared to ethanol <213>',
                'data': 'methanol + NAD+ = formaldehyde + NADH + H+',
                'refs': [11,
                         12,
                         13,
                         14,
                         16,
                         18,
                         20,
                         21,
                         24,
                         25,
                         45,
                         48,
                         49,
                         59,
                         60,
                         67,
                         68,
                         75,
                         82,
                         84,
                         85,
                         101,
                         118,
                         147,
                         171,
                         173,
                         213]},
               {'comment': '#8,18,38,42,69,70# no activity '
                           '<21,60,67,68,75,84,85>; #88# low activity <118>; '
                           '#52# reaction is extremly weak <82>; #8# anodic '
                           'enzyme form shows no activity <18>; #12# no '
                           'activity at pH 7.5, slight activity at pH 10.8 '
                           '<45>; #5# weak activity with isoenzyme A2, no '
                           'activity with isoenzyme B2 and C2 <48>; #9# '
                           'oxidized with ADH-3, no activity with ADH-1 and '
                           'ADH-2 <49>; #8# class I isoenzymes <13>; #8# no '
                           'activity with isoenzyme beta3,beta3 <20>; #79# '
                           'reaction is catalyzed by the pyrazole-sensitive '
                           'enzyme, no activity with the pyrazole-insensitive '
                           'enzyme <24>; #43# reaction is catalyzed by the '
                           'cathodic pyrazole-sensitive enzyme, no activity by '
                           'the cathodic pyrazole-insensitive enzyme and by '
                           'the anodic pyrazole-insensitive enzyme <25>; #8# '
                           'activity detected with class II isoenzyme pi-ADH '
                           '<14>; #8# oxidized by isoenzyme beta1,beta1 <20>; '
                           '#8# class III isoenzyme chi-ADH shows no activity '
                           '<16>; #8# no activity with class III enzyme <11>; '
                           '#111# 49.9% activity compared to ethanol <213>) '
                           '{ir',
                'data': 'methanol + NAD+ = formaldehyde + NADH + H+',
                'refs': [11,
                         12,
                         13,
                         14,
                         16,
                         18,
                         20,
                         21,
                         24,
                         25,
                         45,
                         48,
                         49,
                         59,
                         60,
                         67,
                         68,
                         75,
                         82,
                         84,
                         85,
                         101,
                         118,
                         147,
                         171,
                         173,
                         213]},
               {'comment': '#8,18,38,42,69,70# no activity '
                           '<21,60,67,68,75,84,85>; #88# low activity <118>; '
                           '#52# reaction is extremly weak <82>; #8# anodic '
                           'enzyme form shows no activity <18>; #12# no '
                           'activity at pH 7.5, slight activity at pH 10.8 '
                           '<45>; #5# weak activity with isoenzyme A2, no '
                           'activity with isoenzyme B2 and C2 <48>; #9# '
                           'oxidized with ADH-3, no activity with ADH-1 and '
                           'ADH-2 <49>; #8# class I isoenzymes <13>; #8# no '
                           'activity with isoenzyme beta3,beta3 <20>; #79# '
                           'reaction is catalyzed by the pyrazole-sensitive '
                           'enzyme, no activity with the pyrazole-insensitive '
                           'enzyme <24>; #43# reaction is catalyzed by the '
                           'cathodic pyrazole-sensitive enzyme, no activity by '
                           'the cathodic pyrazole-insensitive enzyme and by '
                           'the anodic pyrazole-insensitive enzyme <25>; #8# '
                           'activity detected with class II isoenzyme pi-ADH '
                           '<14>; #8# oxidized by isoenzyme beta1,beta1 <20>; '
                           '#8# class III isoenzyme chi-ADH shows no activity '
                           '<16>; #8# no activity with class III enzyme <11>; '
                           '#111# 49.9% activity compared to ethanol <213>) {r',
                'data': 'methanol + NAD+ = formaldehyde + NADH + H+',
                'refs': [11,
                         12,
                         13,
                         14,
                         16,
                         18,
                         20,
                         21,
                         24,
                         25,
                         45,
                         48,
                         49,
                         59,
                         60,
                         67,
                         68,
                         75,
                         82,
                         84,
                         85,
                         101,
                         118,
                         147,
                         171,
                         173,
                         213]},
               {'comment': '#8,18,38,42,69,70# no activity '
                           '<21,60,67,68,75,84,85>; #88# low activity <118>; '
                           '#52# reaction is extremly weak <82>; #8# anodic '
                           'enzyme form shows no activity <18>; #12# no '
                           'activity at pH 7.5, slight activity at pH 10.8 '
                           '<45>; #5# weak activity with isoenzyme A2, no '
                           'activity with isoenzyme B2 and C2 <48>; #9# '
                           'oxidized with ADH-3, no activity with ADH-1 and '
                           'ADH-2 <49>; #8# class I isoenzymes <13>; #8# no '
                           'activity with isoenzyme beta3,beta3 <20>; #79# '
                           'reaction is catalyzed by the pyrazole-sensitive '
                           'enzyme, no activity with the pyrazole-insensitive '
                           'enzyme <24>; #43# reaction is catalyzed by the '
                           'cathodic pyrazole-sensitive enzyme, no activity by '
                           'the cathodic pyrazole-insensitive enzyme and by '
                           'the anodic pyrazole-insensitive enzyme <25>; #8# '
                           'activity detected with class II isoenzyme pi-ADH '
                           '<14>; #8# oxidized by isoenzyme beta1,beta1 <20>; '
                           '#8# class III isoenzyme chi-ADH shows no activity '
                           '<16>; #8# no activity with class III enzyme <11>; '
                           '#111# 49.9% activity compared to ethanol <213>) {',
                'data': 'methanol + NAD+ = formaldehyde + NADH + H+',
                'refs': [11,
                         12,
                         13,
                         14,
                         16,
                         18,
                         20,
                         21,
                         24,
                         25,
                         45,
                         48,
                         49,
                         59,
                         60,
                         67,
                         68,
                         75,
                         82,
                         84,
                         85,
                         101,
                         118,
                         147,
                         171,
                         173,
                         213]},
               {'comment': '#18# no activity <75>; #5# oxidized by isoenzyme '
                           'A2 and C2 no activity with isoenzyme B2 <48>; #9# '
                           'oxidation with isoenzyme ADH-1 and ADH-3, no '
                           'activity with isoenzyme ADH-2 <49>',
                'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH',
                'refs': [13,
                         14,
                         16,
                         42,
                         47,
                         48,
                         49,
                         60,
                         66,
                         70,
                         75,
                         96,
                         110,
                         147]},
               {'comment': '#18# no activity <75>; #5# oxidized by isoenzyme '
                           'A2 and C2 no activity with isoenzyme B2 <48>; #9# '
                           'oxidation with isoenzyme ADH-1 and ADH-3, no '
                           'activity with isoenzyme ADH-2 <49>) {r',
                'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH',
                'refs': [13,
                         14,
                         16,
                         42,
                         47,
                         48,
                         49,
                         60,
                         66,
                         70,
                         75,
                         96,
                         110,
                         147]},
               {'comment': '#18# no activity <75>; #5# oxidized by isoenzyme '
                           'A2 and C2 no activity with isoenzyme B2 <48>; #9# '
                           'oxidation with isoenzyme ADH-1 and ADH-3, no '
                           'activity with isoenzyme ADH-2 <49>) {',
                'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH',
                'refs': [13,
                         14,
                         16,
                         42,
                         47,
                         48,
                         49,
                         60,
                         66,
                         70,
                         75,
                         96,
                         110,
                         147]},
               {'comment': '#18# no activity <75>; #5# oxidized by isoenzyme '
                           'A2, no activity with isoenzymes B2 and C2 <48>; '
                           '#43# reaction is catalyzed by the cathodic '
                           'pyrazole-sensitive enzyme, no activity with the '
                           'cathodic pyrazole-insensitive enzyme and by the '
                           'anodic pyrazole-insensitive enzyme <25>',
                'data': 'cyclohexanol + NAD+ = cyclohexanone + NADH',
                'refs': [13, 14, 25, 47, 48, 49, 60, 61, 75, 77, 78, 95, 101]},
               {'comment': '#18# no activity <75>; #5# oxidized by isoenzyme '
                           'A2, no activity with isoenzymes B2 and C2 <48>; '
                           '#43# reaction is catalyzed by the cathodic '
                           'pyrazole-sensitive enzyme, no activity with the '
                           'cathodic pyrazole-insensitive enzyme and by the '
                           'anodic pyrazole-insensitive enzyme <25>) {',
                'data': 'cyclohexanol + NAD+ = cyclohexanone + NADH',
                'refs': [13, 14, 25, 47, 48, 49, 60, 61, 75, 77, 78, 95, 101]},
               {'comment': '#70# weak activity <84>; #42# activity with ADH I, '
                           'no activity with ADH II <68>',
                'data': 'octan-1-ol + NAD+ = n-octanal + NADH',
                'refs': [11, 13, 14, 21, 25, 48, 49, 60, 68, 75, 84, 85, 101]},
               {'comment': '#13# broad substrate specificity <126>; #10# '
                           'constitutive enzyme <94>; #42# key enzyme in '
                           'ethanol production <68>; #52# one constitutive '
                           'enzyme, ADH-MI and one inducible enzyme, ADH-MII '
                           '<82>; #53# enzyme may be involved in the '
                           'metabolism of dietary wax esters in salmonid fish '
                           '<59>; #78# the enzyme oxidizes alcohols to '
                           'aldehydes or ketones both for detoxification and '
                           'metabolic purposes <38>; #36# involvement in the '
                           'development of male hamster reproductive system '
                           '<47>; #88# enzyme shows high substrate specificity '
                           'towards primary aliphatic alcohols, no activity '
                           'with 2-butanol, tert-butanol, isoamyl alcohol, '
                           'isobutyl alcohol, 1,6-hexadiol, and mono-, di-, '
                           'and triethanolamine <118>; #90# no activity with '
                           'methanol, 2-propanol, and isoamyl alcohol <105>; '
                           '#10# substrate specificity and stereospecificity, '
                           'substrate binding pocket structure of the 3 '
                           'isozymes, involving Met294, Trp57, and Trp93 '
                           '<120>; #61# substrate specificity of the 2 '
                           'isozmyes with various substrates, overview, '
                           'isozymes are highly specific for the '
                           '(R)-stereoisomers and enantioselctive for the '
                           'R(-)isomers <113>; #46# the enzyme undergoes a '
                           'substantial conformational change in the apo-holo '
                           'transition, accompanied by loop movements at the '
                           'domain interface <108>; #60# alcohol dehydrogenase '
                           'activity may not limit alcohol supply for ester '
                           'production during ripening <146>; #54# Cm-ADH2 '
                           'cannot reduce branched aldehydes <151>; #10# '
                           'effects of pressure on deuterium isotope effects '
                           'of yeast alcohol dehydrogenase using alternative '
                           'substrates <139>; #92# no activity with methanol '
                           '<144>; #93# the enzyme does not act on short-chain '
                           'normal alkyl alcohols, including methanol and '
                           'ethanol <137>; #96# no activity towards methanol, '
                           'ethanol, 1-propanol, triethylene glycol, '
                           'polyethylene glycol 400, polyethylene glycol 1000, '
                           'D-sorbitol, D-sorbose, formaldehyde, acetaldehyde, '
                           'propionaldehyde, butyraldehyde, and valeraldehyde '
                           '<156>; #98# ADH1 preferrs primary alcohols '
                           'containing C3-C8 carbons to secondary alcohols '
                           'such as 2-propanol and 2-butanol. ADH1 possesses '
                           'specific carboxylate ester-forming activity <172>; '
                           '#101# no activity detected with: '
                           'N-benzyl-2-pyrrolidinone, 2-pyrrolidinone, '
                           '3-hexanone, 4-hydroxy-2-butanone, '
                           '(R)-N-benzyl-3-pyrrolidinol, ethanol, '
                           '1,3-propanediol, 1-butanol, 1,4-butanediol, '
                           '1,2,3-butanetriol, 1,2,4-butanetriol, acetol, '
                           '2-phenyl-1-propanol, 3-phenyl-1-propanol, benzyl '
                           'alcohol and glycerol. No activity with NADP+ or '
                           'NADPH <185>; #6# preference for reduction of '
                           'aromatic ketones and alpha-keto esters, and poor '
                           'activity on aromatic alcohols and aldehydes <169>; '
                           '#26# when NADH is replaced with NADPH, the '
                           'reaction rate is reduced by 0.6% <188>; #41# '
                           'activity is severely reduced towards aliphatic '
                           'alcohols of more than 8 carbon atoms for the free '
                           'enzyme, but not so with immobilized HLAD, '
                           'exhibiting an activity towards C22 and C24 '
                           'aliphatic alcohols higher than 50% of the highest '
                           'value, obtained with C8 <204>; #8# differences in '
                           'the activities of total ADH and class I ADH '
                           'isoenzyme between cancer liver tissues and healthy '
                           'hepatocytes may be a factor in ethanol metabolism '
                           'disorders, which can intensify carcinogenesis '
                           '<180>; #112# TADH is a NAD(H)-dependent enzyme and '
                           'shows a very broad substrate spectrum producing '
                           'exclusively the (S)-enantiomer in high '
                           'enantiomeric excess (more than 99%) during '
                           'asymmetric reduction of ketones <197>; #106# '
                           '1-octanal is no substrate for isozyme ADH1C <214>; '
                           '#106# 1-octanal is no substrate for isozyme ADH2 '
                           '<214>; #109# 1-octanal is no substrate for isozyme '
                           'ADH4 <214>; #112# ADH exhibits a clear preference '
                           'for primary alcohols and corresponding aldehydes '
                           'for aliphatic substrates, in the oxidative '
                           'direction activity steeply increases with chain '
                           'length until 1-propanol and then decreases '
                           'slightly again with growing chain length, '
                           'alpha,beta-unsaturated ketones like 3-penten-2-one '
                           'and cyclohexenone are not converted by ADH, almost '
                           'no conversion of methanol (0.2%) and (+)-carvone '
                           '(0.4%) is detected <197>; #110# no activity '
                           'towards methanol <210>; #114# substrates are a '
                           'broad range of alkyl alcohols from ethanol to '
                           '1-triacontanol <215>; #123# the physiological '
                           'direction of the catalytic reaction is reduction '
                           'rather than oxidation <219>; #124# the enzyme '
                           'displays a preference for the reduction of '
                           'alicyclic, bicyclic and aromatic ketones and '
                           'alpha-ketoesters, but is poorly active on '
                           'aliphatic, cyclic and aromatic alcohols, showing '
                           'no activity on aldehydes <218>; #123# the enzyme '
                           'shows no activity on aliphatic linear and branched '
                           'alcohols, except for a poor activity on '
                           '2-propyn-1-ol, 3-methyl-1-butanol and 2-pentanol; '
                           'however, it shows a discrete activity on aliphatic '
                           'cyclic and bicyclic alcohols. Benzyl alcohol and '
                           '4-bromobenzyl alcohol are not found to be '
                           'substrates. The S and R enantiomers of '
                           'a-(trifluoromethyl)benzyl alcohol and methyl and '
                           'ethyl mandelates show no apparent activity with '
                           'SaADH. The enzyme shows poor activity on '
                           '(+/-)-1-phenyl-1-propanol, 1-(1-naphthyl)ethanol '
                           'and the two enantiomers of 1-(2-naphthyl)ethanol. '
                           'The enzyme is not active on aliphatic and aromatic '
                           'aldehydes, and on aliphatic linear, branched and '
                           'cyclic ketones except for 3-methylcyclohexanone. '
                           'Catalytic inactivity is observed with acetophenone '
                           'and (S)-a-(trifluoromethyl)benzyl <219>; #127# '
                           'methanol, formaldehyde, and acetone are no '
                           'substrates for HpADH3 <222>; #48# no activity with '
                           'methanol, 1-butanol, glycerol or 2-propanol <223>; '
                           '#128# substrate specificity and '
                           'enantiospecificity, overview. The (R)-specific '
                           'alcohol dehydrogenase requires NADH and reduces '
                           'various kinds of carbonyl compounds, including '
                           'ketones and aldehydes. AFPDH reduces '
                           'acetylpyridine derivatives, beta-keto esters, and '
                           'some ketones compounds with high '
                           'enantiospecificity, overview. No activity with '
                           '2-chlorobenzaldehyde and 2-tetralone, poor '
                           'activity with 1-tetralone, pyruvate, '
                           '2-oxobutyrate, oxalacetate, cyclopentanone, '
                           'cyclohexanone, cycloheptanone, and dipropylketone. '
                           'No activity with 1,2-propanediol, '
                           '3-chloro-1,2-propanediol, 3-bromo-1,2-propanediol, '
                           'glycerol, 1-pentanol, poor activity with '
                           '1-butanol, 1-propanol, ethanol, and methanol '
                           '<225>; #85# the enzyme exhibits broad substrate '
                           'specificity towards aliphatic ketones, '
                           'cycloalkanones, aromatic ketones, and ketoesters '
                           '<226>; #132# the enzyme shows broad substrate '
                           'specificity and prefers aliphatic alcohols and '
                           'ketones. There are no large differences in the '
                           'reactivities between primary and secondary '
                           'alcohols. The enzyme produces (S)-alcohols from '
                           'the corresponding ketones. The values of the '
                           'enantiomeric excess increase with the increase of '
                           'chain length except for the reduction of '
                           '2-hexanone. The highest enantioselectivity is '
                           'shown with the reduction of 2-nonanone <239>; '
                           '#133# the NAD+-dependent HvADH1 shows a preference '
                           'for short-chain alcohols, no activity with '
                           'methanol <237>; #143# broad substrate specificity '
                           'with a preference for the reduction of ketones and '
                           'the oxidation of secondary alcohols <138>; #124# '
                           'enzyme displays a preference for the reduction of '
                           'alicyclic, bicyclic and aromatic ketones and '
                           'alpha-keto esters, but is poorly active on '
                           'aliphatic, cyclic and aromatic alcohols, and shows '
                           'no activity on aldehydes <219>; #150# enzyme '
                           'reduces aldehydes to (R)-alcohols with more than '
                           '99.8% enantiomeric excess <243>; #151# enzyme '
                           'selectively reduces the C=O bond of allylic '
                           'aldehydes/ketones to the corresponding '
                           'alpha,beta-unsaturated alcohols and also has the '
                           'capacity of stereoselectively reducing aromatic '
                           'ketones to (S)-enantioselective alcohols. The '
                           'enzyme preferentially catalyzes oxidation of '
                           'allylic/benzyl aldehydes <244>; #71# ethanol '
                           'dehydrogenase activity of Thermoanaerobium brockii '
                           'is both NAD and NADP linked, reversible, and not '
                           'inhibited by low levels of reaction products '
                           '<103>; #119,142# mutation at the substrate-binding '
                           'site, or at a dimer interface, alters kinetic '
                           'properties and protein oligomeric structure, '
                           'active site flexibility is correlated with subunit '
                           'interactions 20 A away <260>; #6# the enzyme '
                           'transfers the pro-S hydrogen of [4R-(2)H]NADH and '
                           'exhibits Prelog specificity <269>; #41# acycloNAD+ '
                           'i.e. NAD+-analogue, where the nicotinamide ribosyl '
                           'moiety has been replaced by the nicotinamide '
                           '(2-hydroxyethoxy)methyl moiety. There is no '
                           'detectable reduction of acycloNAD+ by secondary '
                           'alcohols although these alcohols serve as '
                           'competitive inhibitors. AcycloNAD+ converts horse '
                           'liver ADH from a broad spectrum alcohol '
                           'dehydrogenase, capable of utilizing either primary '
                           'or secondary alcohols, into an exclusively primary '
                           'alcohol dehydrogenase <275>; #51# bifunctional '
                           'enzyme consisting of an N-terminal acetaldehyde '
                           'dehydrogenase (ALDH) and a C-terminal alcohol '
                           'dehydrogenase (ADH). The specificity constant '
                           '(kcat/Km) is 47fold higher for acetaldehyde '
                           'reductase than that for ethanol dehydrogenase '
                           '<279>; #153# enzyme is an alcohol dehydrogenase '
                           'with additional activity for all-trans-retinol, '
                           'reaction of EC 1.1.1.184 <272>; #155# enzyme shows '
                           'activity as a reductase specific for (S)-acetoin, '
                           'EC 1.1.1.76, and both diacetyl reductase (EC '
                           '1.1.1.304) and NAD+-dependent alcohol '
                           'dehydrogenase (EC 1.1.1.1) activities <271>; #160# '
                           'the enzyme additionally catalyzes selective '
                           'reduction of 3-quinuclidinone to '
                           '(R)-3-quinuclidinol, with 84% ee and 62% '
                           'conversion after 22 h <274>; #162# Candida '
                           'albicans ADH1 is a bifunctional enzyme that '
                           'catalyzes methylglyoxal oxidation and reduction, '
                           'cf. EC 1.2.1.23 <287>; #161# the enzyme catalyzes '
                           'NAD(H)-dependent oxidation of various alcohols and '
                           'reduction of aldehydes, with a marked preference '
                           'for substrates with functional group at the '
                           'terminal carbon atom <286>; #166# almost no '
                           'activity with D-arabinonate, D-lyxonate, '
                           'D-galactonate, glycerol, meso-erythritol, '
                           'D-ribitol, D-arabitol, D-xylitol, and D-mannitol. '
                           'No activity with propanal, butanal, hexanal, and '
                           '4-oxobutanoic acid <292>; #165# the enzyme '
                           'catalyzes the reduction of acetophenone '
                           'derivatives to the corresponding (S)-chiral '
                           'alcohols in an enantiomerically pure form. The '
                           'substituents on the benzene ring of the aryl '
                           'ketones exert some effect on the enzyme activity, '
                           'although the influence is not dramatic. The '
                           'enantioselectivity of the reduction is not '
                           'affected by the substituents and pattern of the '
                           'substitution. The alpha-chlorinated acetophenone '
                           'shows a much higher activity than the '
                           'unsubstituted one (more than 10 times) <294>) {',
                'data': 'more = ?',
                'refs': [38,
                         47,
                         59,
                         68,
                         82,
                         94,
                         103,
                         105,
                         108,
                         113,
                         118,
                         120,
                         126,
                         137,
                         138,
                         139,
                         144,
                         146,
                         151,
                         156,
                         169,
                         172,
                         180,
                         185,
                         188,
                         197,
                         204,
                         210,
                         211,
                         214,
                         215,
                         218,
                         219,
                         222,
                         223,
                         225,
                         226,
                         237,
                         239,
                         243,
                         244,
                         260,
                         269,
                         271,
                         272,
                         274,
                         275,
                         279,
                         286,
                         287,
                         292,
                         294]},
               {'comment': '#8# substrate of isozyme ADH4 <194>) {r',
                'data': '(2E)-4-hydroxynon-2-enal + NADH + H+ = '
                        '(2E)-non-2-ene-1,4-diol + NAD+',
                'refs': [194]},
               {'data': '16-hydroxyhexadecanoate + NAD+ = 16-oxohexadecanoic '
                        'acid + NADH',
                'refs': [13, 14]},
               {'data': '17beta-hydroxyetiocholan-3-one + NAD+ = '
                        'ethiocholan-3,17-dione + NADH',
                'refs': [16]},
               {'data': '2-deoxy-D-ribose + NAD+ = ? + NADH', 'refs': [14]},
               {'data': '3,4-dihydro-retinol + NAD+ = 3,4-dihydro-retinal {r}',
                'refs': [107]},
               {'data': '3-phenyl-1-propanol + NAD+ = 3-phenyl-1-propanone + '
                        'NADH',
                'refs': [13, 14]},
               {'data': '3-phenyl-1-propanol + NAD+ = 3-phenyl-1-propanone + '
                        'NADH {}',
                'refs': [13, 14]},
               {'data': '3-pyridylcarbinol + NAD+ = pyridine-3-carbaldehyde + '
                        'NADH',
                'refs': [18]},
               {'data': '4-hydroxy-retinol + NAD+ = 4-oxo-retinal + NADH {r}',
                'refs': [107]},
               {'comment': '#8# fluorogenic substrate of class I and II '
                           'isozymes <229>',
                'data': '4-methoxy-1-naphthaldehyde + NAD+ = '
                        '4-methoxy-1-naphthol + NADH + H+',
                'refs': [229]},
               {'comment': '#8# substrate for class I ADH <180>',
                'data': '4-methoxy-1-naphthaldehyde + NAD+ = '
                        '4-methoxy-1-naphthyl alcohol + NADH + H+',
                'refs': [180]},
               {'comment': '#8# substrate for class I ADH <206>) {r',
                'data': '4-methoxy-1-naphthaldehyde + NADH + H+ = '
                        '4-methoxynaphthalene-1-carbaldehyde + NAD+',
                'refs': [206]},
               {'comment': '#8# photometric assay substrate <229>',
                'data': '4-nitrosodimethylaniline + NAD+ = ? + NADH + H+',
                'refs': [229]},
               {'comment': '#8# low activity <116>',
                'data': '5alpha-pregnan-3beta-ol-20-one + NAD+ = '
                        '5alpha-pregnan-3,20-dione + NADH',
                'refs': [116]},
               {'comment': '#8# low activity <116>',
                'data': '5beta-cholanic acid-3-one + NADH = 5beta-cholanic '
                        'acid-3-ol + NAD+',
                'refs': [116]},
               {'data': '5beta-pregnan-3,20-dione + NADH = ?', 'refs': [116]},
               {'data': '5beta-pregnan-3beta-ol-20-one + NAD+ = '
                        '5beta-pregnan-3,20-dione + NADH',
                'refs': [116]},
               {'comment': '#8# substrate for class II ADH <206>) {r',
                'data': '6-methoxy-2-naphthaldehyde + NADH + H+ = '
                        '(6-methoxynaphthalen-2-yl)methanol + NAD+',
                'refs': [206]},
               {'comment': '#8# substrate for class II ADH <180>',
                'data': '6-methoxy-2-naphthaldehyde + NADH + H+ = '
                        '6-methoxy-2-naphthyl alcohol + NAD+',
                'refs': [180]},
               {'comment': '#8# class II isozyme, reductive activity <229>',
                'data': '6-methoxy-2-naphthaldehyde + NADH + H+ = '
                        '6-methoxy-2-naphtol + NAD+',
                'refs': [229]},
               {'data': 'digitose + NAD+ = ? + NADH', 'refs': [16]},
               {'data': 'hexanol + NAD+ = hexanal + NADH', 'refs': [119]},
               {'data': 'isobutyl alcohol + NAD+ = ? + NADH', 'refs': [20]},
               {'data': 'isobutyramide + NAD+ = ? {r}', 'refs': [124]},
               {'data': 'isopentenyl alcohol + NAD+ = isopentanone + NADH',
                'refs': [20]},
               {'comment': '#8# substrate of class IV ADH <180>',
                'data': 'm-nitrobenzaldehyde + NAD+ = m-nitrobenzyl alcohol + '
                        'NADH + H+',
                'refs': [180]},
               {'data': 'n-butanol + NAD+ = butylaldehyde + NADH + H+',
                'refs': [180, 206]},
               {'data': 'n-butanol + NAD+ = butylaldehyde + NADH + H+ {r}',
                'refs': [180, 206]},
               {'comment': '#8# substrate of isozyme ADH4 <194>) {r',
                'data': 'p-nitrobenzaldehyde + NADH + H+ = p-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [194]},
               {'data': 'phenylalaninol + NAD+ = ? + NADH', 'refs': [16]},
               {'comment': '#8# substrate of isozyme ADH4 <194>) {r',
                'data': 'retinal + NADH + H+ = retinol + NAD+',
                'refs': [194]},
               {'data': 'retinol + NAD+ = retinal + NADH', 'refs': [115]},
               {'data': 'trans-4-(N,N-dimethylamino)-cinnamaldehyde + NADH = '
                        'trans-4-(N,N-dimethylamino)-cinnamyl alcohol + NAD+',
                'refs': [19]},
               {'data': 'tryptophol + NAD+ = ? + NADH', 'refs': [14]},
               {'data': 'vanillyl alcohol + NAD+ = vanillin + NADH',
                'refs': [14, 16]},
               {'data': 'n-butanol + NAD+ = n-butanal + NADH',
                'refs': [120, 186]},
               {'data': 'n-butanol + NAD+ = n-butanal + NADH {r}',
                'refs': [120, 186]},
               {'comment': '#96# 100% activity <156>; #47# 199% of the '
                           'activity with 2-phenylethanol <149>; #112# 47% '
                           'activity compared to cyclohexanol <197>; #132# '
                           'i.e. phenylmethanol <239>) |#112# 154% activity '
                           'compared to cyclohexanone <197>; #112# 178% '
                           'activity compared to cyclohexanone <197>; #119# '
                           '33% of the activity with butan-2-ol <256>',
                'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH + H+',
                'refs': [147,
                         149,
                         153,
                         154,
                         156,
                         159,
                         180,
                         197,
                         202,
                         205,
                         207,
                         239,
                         256,
                         257,
                         260]},
               {'comment': '#96# 100% activity <156>; #47# 199% of the '
                           'activity with 2-phenylethanol <149>; #112# 47% '
                           'activity compared to cyclohexanol <197>; #132# '
                           'i.e. phenylmethanol <239>) |#112# 154% activity '
                           'compared to cyclohexanone <197>; #112# 178% '
                           'activity compared to cyclohexanone <197>; #119# '
                           '33% of the activity with butan-2-ol <256>| {r',
                'data': 'benzyl alcohol + NAD+ = benzaldehyde + NADH + H+',
                'refs': [147,
                         149,
                         153,
                         154,
                         156,
                         159,
                         180,
                         197,
                         202,
                         205,
                         207,
                         239,
                         256,
                         257,
                         260]},
               {'comment': '#143# 38% of the activity with acetoin <138>',
                'data': 'cyclohexanone + NADH + H+ = cyclohexanol + NAD+',
                'refs': [116, 138, 218]},
               {'comment': '#143# 38% of the activity with acetoin <138>) {r',
                'data': 'cyclohexanone + NADH + H+ = cyclohexanol + NAD+',
                'refs': [116, 138, 218]},
               {'comment': '#8# class IV isozyme, reductive activity <229>',
                'data': '3-nitrobenzaldehyde + NADH + H+ = 3-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [225, 229]},
               {'comment': '#8# class IV isozyme, reductive activity <229>) {r',
                'data': '3-nitrobenzaldehyde + NADH + H+ = 3-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [225, 229]},
               {'comment': '#96# 30% activity compared to benzyl alcohol '
                           '<156>; #31# 15.7% of the activity with ethanol '
                           '<181>; #98# about 80% of activity with ethanol, '
                           'ADH1 <172>; #112# 142% activity compared to '
                           'cyclohexanol <197>; #111# 67.7% activity compared '
                           'to ethanol <213>',
                'data': '1-butanol + NAD+ = butanal + NADH + H+',
                'refs': [144,
                         147,
                         156,
                         172,
                         181,
                         197,
                         207,
                         210,
                         213,
                         222,
                         223,
                         229,
                         239,
                         286]},
               {'comment': '#96# 30% activity compared to benzyl alcohol '
                           '<156>; #31# 15.7% of the activity with ethanol '
                           '<181>; #98# about 80% of activity with ethanol, '
                           'ADH1 <172>; #112# 142% activity compared to '
                           'cyclohexanol <197>; #111# 67.7% activity compared '
                           'to ethanol <213>) {r',
                'data': '1-butanol + NAD+ = butanal + NADH + H+',
                'refs': [144,
                         147,
                         156,
                         172,
                         181,
                         197,
                         207,
                         210,
                         213,
                         222,
                         223,
                         229,
                         239,
                         286]},
               {'comment': '#8# low activity <116>',
                'data': '5beta-androstan-17beta-ol-3-one + NAD+ = '
                        '5beta-androstan-3,17-dione + NADH',
                'refs': [116]},
               {'data': '5beta-androstan-3beta-ol-17-one + NAD+ = '
                        '5beta-androstan-3,17-dione + NADH',
                'refs': [116]},
               {'comment': '#70# weak activity <84>; #41# (R)-2-octanol and '
                           '(S)-2-octanol <31>',
                'data': 'octan-2-ol + NAD+ = octan-2-one + NADH',
                'refs': [16, 31, 61, 84]},
               {'comment': '#42# activity with ADH I, no activity with ADH II '
                           '<68>',
                'data': 'furfuryl alcohol + NAD+ = furfural + NADH',
                'refs': [16, 68]},
               {'comment': '#42# activity with ADH I, no activity with ADH II '
                           '<68>) {r',
                'data': 'furfuryl alcohol + NAD+ = furfural + NADH',
                'refs': [16, 68]},
               {'data': '5alpha-androstan-17beta-ol-3-one + NADH + H+ = '
                        '3beta,17beta-dihydroxy-5alpha-androstan + NAD+',
                'refs': [51, 116]},
               {'data': '5alpha-androstan-17beta-ol-3-one + NADH + H+ = '
                        '3beta,17beta-dihydroxy-5alpha-androstan + NAD+ {}',
                'refs': [51, 116]},
               {'comment': '#8# substrate of class IV ADH isozyme <206>) {r',
                'data': 'm-nitrobenzaldehyde + NADH + H+ = m-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [49, 206]},
               {'comment': '#8# substrate of class IV ADH isozyme <206>) {',
                'data': 'm-nitrobenzaldehyde + NADH + H+ = m-nitrobenzyl '
                        'alcohol + NAD+',
                'refs': [49, 206]},
               {'comment': '#42# activity with ADH I, no activity with ADH II '
                           '<68>',
                'data': 'pentanol + NAD+ = n-pentanal + NADH',
                'refs': [11, 45, 49, 60, 61, 68, 69, 71, 75, 77, 78, 85]},
               {'comment': '#36# oxidized at pH 10, not oxidized at pH 7.5 '
                           '<47>',
                'data': '12-hydroxydodecanoate + NAD+ = 12-oxododecanoic acid '
                        '+ NADH',
                'refs': [11, 14, 16, 47, 49, 53, 60, 95, 96]},
               {'comment': '#36# oxidized at pH 10, not oxidized at pH 7.5 '
                           '<47>) {',
                'data': '12-hydroxydodecanoate + NAD+ = 12-oxododecanoic acid '
                        '+ NADH',
                'refs': [11, 14, 16, 47, 49, 53, 60, 95, 96]},
               {'data': 'octanal + NADH + H+ = octanol + NAD+',
                'refs': [16, 49, 60]}]),
             ('SS',
              [{'data': '(4°C, 10 mM HEPES buffer, 1 mM dithioerythritol, pH '
                        '7.5, stable for 2 weeks)',
                'refs': [16]},
               {'data': '(4°C, 5 mM Na phosphate, pH 7.5, the half-life is 24 '
                        'h. 0.01 mM ethanol effectively stabilizes for several '
                        'weeks)',
                'refs': [18]},
               {'data': '(4°C, 5 mM Na-phosphate, pH 7.5, 50% loss of activity '
                        'after 1 day. Enzyme can be stabilized for up to 2 '
                        'weeks by storage in buffer containing 10 mM ethanol)',
                'refs': [23]},
               {'data': '(4°C, pH 7.5, stable for 2-3 weeks)', 'refs': [14]}]),
             ('ST',
              [{'bto': 'BTO_0000759',
                'comment': '#5# isoenzyme A2 and B2 <48>; #36# isoenzyme '
                           'AA-ADH and BB-ADH most abundant in <95>; #8# '
                           'isozyme ADH1C*2 <116>; #9# females show 70% higher '
                           'hepatic alcohol dehydrogenase activity and display '
                           '60% lower voluntary ethanol intake than males. '
                           'Following ethanol administration (1 g/kg ip), '
                           'females generate a transient blood acetaldehyde '
                           'increase with levels that are 2.5fold greater than '
                           'in males. Castration of males leads to an increase '
                           'alcohol dehydrogenase activity the appearance of '
                           'an acetaldehyde burst a reduction of voluntary '
                           'ethanol intake comparable with that of females '
                           '<167>; #8# the activities of total alcohol '
                           'dehydrogenase, aldehyde dehydrogenase and class I '
                           'alcohol dehydrogenase isoenzyme between cancer '
                           'liver tissues and healthy hepatocytes might be a '
                           'factor in ethanol metabolism disorders which can '
                           'intensify carcinogenesis <186>; #106# isozymes '
                           'ADH1C and ADH3 <214>; #8# most abundant in the '
                           'liver <180>; #8# the total alcohol dehydrogenase '
                           'activity is significantly higher in cancer tissues '
                           'than in healthy liver <194>; #131# class III ADH '
                           '<227>',
                'data': 'liver',
                'refs': [1,
                         2,
                         5,
                         10,
                         12,
                         13,
                         14,
                         15,
                         16,
                         17,
                         18,
                         19,
                         20,
                         21,
                         22,
                         23,
                         24,
                         25,
                         26,
                         27,
                         28,
                         29,
                         30,
                         31,
                         32,
                         33,
                         34,
                         35,
                         36,
                         37,
                         39,
                         40,
                         41,
                         42,
                         44,
                         45,
                         46,
                         48,
                         49,
                         51,
                         52,
                         54,
                         55,
                         59,
                         60,
                         86,
                         92,
                         93,
                         95,
                         98,
                         101,
                         111,
                         116,
                         117,
                         143,
                         167,
                         175,
                         178,
                         180,
                         186,
                         194,
                         198,
                         200,
                         201,
                         204,
                         205,
                         212,
                         214,
                         224,
                         227,
                         275]},
               {'bto': 'BTO_0000575',
                'comment': '#8# the activities of total alcohol dehydrogenase, '
                           'aldehyde dehydrogenase and class I alcohol '
                           'dehydrogenase isoenzyme between cancer liver '
                           'tissues and healthy hepatocytes might be a factor '
                           'in ethanol metabolism disorders which can '
                           'intensify carcinogenesis <186>',
                'data': 'hepatocyte',
                'refs': [117, 186]},
               {'bto': 'BTO_0001175',
                'comment': '#5,8# isozyme ADH4 <119>',
                'data': 'retina',
                'refs': [119]},
               {'bto': 'BTO_0001307',
                'comment': '#5# isoenzyme C2 <48>; #8# stomach mucosa, '
                           'mue-alcohol dehydrogenase <96>; #8# isozymes ADH5 '
                           'and ADH4, the total alcohol dehydrogenase activity '
                           'is significantly higher in cancer tissues than in '
                           'healthy stomach <194>',
                'data': 'stomach',
                'refs': [48, 49, 50, 53, 96, 125, 194]},
               {'bto': 'BTO_0000604',
                'data': 'adenocarcinoma cell',
                'refs': [229]},
               {'bto': 'BTO_0000135',
                'comment': '#8# the activity of the class I ADH isoenzyme is '
                           'significantly lower in the wall of aortic aneurysm '
                           'than in healthy aorta <206>',
                'data': 'aorta',
                'refs': [206]},
               {'bto': 'BTO_0000133',
                'comment': '#8# among all tested classes of ADH isoenzymes, '
                           'only class I has higher activity in serum of '
                           'patients with breast cancer in stage IV. The total '
                           'ADH activity is not significantly higher in '
                           'patients with breast cancer than in healthy '
                           'controls. The changes in activity, especially in '
                           'class I ADH, appear to be caused by isoenzymes '
                           'being released from the organ damaged by '
                           'metastatic disease <150>; #8# the total ADH '
                           'activity is significantly higher (44%) among '
                           'patients with cancer than healthy ones. The '
                           'activity of class I ADH isoenzymes is elevated '
                           'only in the serum of patients with metastatic '
                           'liver cancer. This increase of activity seems to '
                           'be caused by the enzyme released from liver cancer '
                           'cells and primary tumors originating in other '
                           'organs <186>',
                'data': 'blood serum',
                'refs': [150, 186]},
               {'bto': 'BTO_0000180',
                'data': 'cervical cancer cell',
                'refs': [229]},
               {'bto': 'BTO_0001613',
                'comment': '#8# the total alcohol dehydrogenase activity is '
                           'significantly higher in cancer tissues than in '
                           'healthy colorectum <194>',
                'data': 'colorectum',
                'refs': [194]},
               {'bto': 'BTO_0000959',
                'comment': '#8# isozyme ADH4, the total alcohol dehydrogenase '
                           'activity is significantly higher in cancer tissues '
                           'than in healthy esophagus <194>',
                'data': 'esophagus',
                'refs': [194]},
               {'bto': 'BTO_0000608', 'data': 'hepatoma cell', 'refs': [180]},
               {'bto': 'BTO_0001239', 'data': 'serum', 'refs': [194]},
               {'bto': 'BTO_0001253', 'data': 'skin', 'refs': [194]},
               {'bto': 'BTO_0000286',
                'comment': '#8# isozyme ADH4 <194>',
                'data': 'cornea',
                'refs': [49, 194]},
               {'bto': 'BTO_0000671',
                'comment': '#8# isozyme ADH1 <194>; #9# high expression level '
                           'of ADH5 <228>',
                'data': 'kidney',
                'refs': [49, 194, 228]},
               {'bto': 'BTO_0000763',
                'comment': '#8# isozyme ADH1 <194>',
                'data': 'lung',
                'refs': [49, 194]},
               {'bto': 'BTO_0000988',
                'comment': '#8# total activity of alcohol dehydrogenase is not '
                           'significantly different in cancer and normal '
                           'cells. The differences between enzymes of drinkers '
                           'and nondrinkers in both cancer and healthy tissue '
                           'are not significant <191>',
                'data': 'pancreas',
                'refs': [49, 191]},
               {'bto': 'BTO_0001424', 'data': 'uterus', 'refs': [49, 229]},
               {'bto': 'BTO_0001363',
                'comment': '#8# the class III enzyme contributes by far the '
                           'bulk of the total alcohol dehydrogenase activity '
                           '<11>; #36# isoenzyme TT-ADH is only found in '
                           'testis <95>; #36# activity increases during the '
                           'prepubertal development <47>',
                'data': 'testis',
                'refs': [11, 47, 49, 95]}]),
             ('SU',
              [{'comment': '#8# x * 42000, SDS-PAGE <14>; #73# x * 28000, '
                           'SDS-PAGE <2>; #1,8,80,131# x * 40000, SDS-PAGE '
                           '<11,44,52,227>; #24# x * 96000, SDS-PAGE <128>; '
                           '#85# x * 30000, SDS-PAGE <226>; #158# x * 85000, '
                           'SDS-PAGE <283>; #14# x * 37500, SDS-PAGE <81>; '
                           '#25# x * 31997, amino acid sequence calculation '
                           '<106>; #98# x * 37443, ADH1, calculated from '
                           'sequence <172>; #15# x * 37983, ADH3, calculated '
                           'from sequence <172>; #31# x * 41300, SDS-PAGE '
                           '<181>; #126# x * 31000, recombinant His6-tagged '
                           'enzyme, SDS-PAGE <231>; #151# x * 36411, '
                           'calculated, x * 37000, SDS-PAGE <244>; #103# x * '
                           '37066, calculated <177>; #104# x * 37311, '
                           'calculated <177>; #149# x * 96000, wild-type, '
                           'SDS-PAGE <241>; #153# x * 40000, SDS-PAGE, x * '
                           '39900, calculated <272>; #158# x * 88000, '
                           'calculated from sequence <283>',
                'data': '?',
                'refs': [2,
                         11,
                         14,
                         44,
                         52,
                         81,
                         106,
                         128,
                         172,
                         177,
                         181,
                         226,
                         227,
                         231,
                         241,
                         244,
                         272,
                         283]},
               {'comment': '#16# 2 * 45000, SDS-PAGE <79>; #26,78# 2 * 28000, '
                           'SDS-PAGE <61,188>; #67,81# 2 * 58000, SDS-PAGE '
                           '<77,78>; #18# 2 * 35000, SDS-PAGE <75>; #44# 2 * '
                           '38000, SDS-PAGE <114>; #8,10,36,53,79# 2 * 40000, '
                           'SDS-PAGE <16,23,24,59,87,95>; #36# 2 * 41000, '
                           'SDS-PAGE <47>; #68# 2 * 42000, SDS-PAGE <69>; #45# '
                           '2 * 46000, SDS-PAGE <6>; #88# 2 * 43000, SDS-PAGE '
                           '<118>; #12# 2 * 36000, SDS-PAGE <45>; #21,46# 2 * '
                           '37000, SDS-PAGE <66,70,72,165>; #42# 2 * 38000, '
                           'enzyme form ADHII, SDS-PAGE <68>; #8# 2 * 41000, '
                           'class III isoenzyme chi ADH, SDS-PAGE <16>; #9# 2 '
                           '* 43000, ADH-1, SDS-PAGE <49>; #8# 2 * 42000, '
                           'anodic enzyme form, SDS-PAGE <18>; #69# 2 * 42000, '
                           'enzyme form ADH-2 and ADH-3, SDS-PAGE <60>; #5# 2 '
                           '* 47000, isoenzyme C2, SDS-PAGE <48>; #5# 2 * '
                           '39000, isoenzyme B2, SDS-PAGE <48>; #9# 2 * 40000, '
                           'ADH-3, SDS-PAGE <49>; #9# 2 * 39000, ADH-2, '
                           'SDS-PAGE <49>; #12# 2 * 41700, enzyme form CM-I: a '
                           'polypeptide chain + C polypeptide chain, enzyme '
                           'form CM-II: B-chain + C-chain, enzyme form CM III, '
                           'homodimer of C chains, SDS-PAGE <46>; #5# 2 * '
                           '43000, isoenzyme A2, SDS-PAGE <48>; #42# 2 * '
                           '40000, enzyme form ADHI <68>; #4,72,75# 2 * 27800, '
                           'SDS-PAGE <64>; #42# 2 * 34700, enzyme form ADH-I, '
                           'SDS-PAGE <67>; #3# 2 * 30000 <4>; #42# 2 * 31100, '
                           'enzyme form ADH-II, SDS-PAGE <67>; #61# 2 * 31000, '
                           'ADH II, SDS-PAGE <113>; #46# dimer of dimers, '
                           'X-ray crystallography <161>; #100# 2 * 36900, '
                           'SDS-PAGE <171>; #44# 2 * 38000, recombinant '
                           'enzyme, SDS-PAGE <232>; #149# 2 * 48600, alcohol '
                           'dehydrogenase domain, SDS-PAGE. Unlike the native '
                           'ADHE, the alcohol dehydrogenase domain alone does '
                           'not assemble into spirosome structures <241>; #20# '
                           '2 * 40700, calculated <284>; #161# 2 * 37555, '
                           'calculated <286>',
                'data': 'dimer',
                'refs': [4,
                         6,
                         16,
                         18,
                         21,
                         23,
                         24,
                         45,
                         46,
                         47,
                         48,
                         49,
                         59,
                         60,
                         61,
                         64,
                         66,
                         67,
                         68,
                         69,
                         70,
                         71,
                         72,
                         75,
                         77,
                         78,
                         79,
                         87,
                         95,
                         113,
                         114,
                         118,
                         161,
                         165,
                         171,
                         188,
                         194,
                         205,
                         232,
                         241,
                         284,
                         286]},
               {'comment': '#27# quaternary organization and stability, '
                           'overview <129>; #8# structure modelling <115>; '
                           '#48# Adh3 forms a Ni2+-containing homodimer in its '
                           'active form, crystal structure analysis, larger '
                           'aggregates are inactive <223>; #124# tetramer '
                           'structure results from chemical crosslinking '
                           'experiments <219>',
                'data': 'More',
                'refs': [115, 129, 219, 223]}]),
             ('SY',
              [{'comment': '#10# mutant enzyme S109P/L116S/Y294C <193>',
                'data': 'alcohol dehydrogenase 1',
                'refs': [190, 193, 212, 228]},
               {'data': 'ADH',
                'refs': [108,
                         111,
                         113,
                         115,
                         117,
                         118,
                         119,
                         126,
                         127,
                         129,
                         152,
                         153,
                         154,
                         155,
                         157,
                         158,
                         159,
                         160,
                         161,
                         163,
                         164,
                         194,
                         196,
                         197,
                         199,
                         200,
                         201,
                         203,
                         205,
                         206,
                         207,
                         208,
                         209,
                         211,
                         213,
                         229,
                         231,
                         233,
                         248,
                         251,
                         261,
                         292]},
               {'data': 'ADH1B', 'refs': [273]},
               {'data': 'ADH1C*1', 'refs': [116]},
               {'data': 'ADH1C*2', 'refs': [116]},
               {'data': 'ALDH', 'refs': [229]},
               {'data': 'aldehyde dehydrogenase', 'refs': [229]},
               {'comment': '#8# isoenzyme <206>; #8# isozyme <180>',
                'data': 'class I ADH',
                'refs': [180, 206, 229]},
               {'comment': '#8# isoenzyme <206>; #8# isozyme <180>',
                'data': 'class II ADH',
                'refs': [180, 206, 229]},
               {'data': 'class III ADH', 'refs': [229]},
               {'comment': '#8# isozyme <180>',
                'data': 'class IV ADH',
                'refs': [180, 229]},
               {'comment': '#10# isozyme <202>',
                'data': 'ADH1',
                'refs': [156, 172, 202, 215, 228, 252, 282, 287]},
               {'comment': '#109# isozyme <214>',
                'data': 'ADH4',
                'refs': [124, 174, 177, 214, 252]}]),
             ('TN',
              [{'comment': '#8# turnover-numbers for the class I isoenzymes '
                           'with the substrates ethanol, methanol, ethylene '
                           'glycol, benzyl alcohol, octanol, cyclohexanol and '
                           '16-hydroxyhexadecanoic acid <13>; #41# Km-values '
                           'of active-site Co(II)substituted enzyme <31>; '
                           '#4,75# kinetics of ethanol oxidation <63>; #5# '
                           'kcat for isozymes ADH1, and ADH4 for all retinoid '
                           'substrates in forward and reverse reaction <119>; '
                           '#8# kcat for isozymes ADH1B1, ADH1B2, and ADH4 for '
                           'all retinoid substrates in forward and reverse '
                           'reaction <119>; #5# effects of tert-butanol, '
                           'butyramide, valeramide and capronamide on '
                           'turnover-number of ethanol <141>; #23# kinetic '
                           'data füor wild-type enzyme and chimeric enzyme '
                           'created by insertion of an RTX domain from the '
                           'adenylate cyclase of Bordetella pertussis into a '
                           'loop near the catalytic active site of the '
                           'thermostable alcohol dehydrogenase D (AdhD) from '
                           'Pyrococcus furiosus <289>',
                'data': '-999 {more}',
                'refs': [13, 28, 31, 63, 119, 141, 289],
                'units': '1/s'},
               {'chebi': 'CHEBI_17898',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH1B1 <107>',
                'data': '0.018 {all-trans-retinal}',
                'refs': [107],
                'substrate': 'all-trans-retinal',
                'units': '1/s',
                'value': 0.018},
               {'chebi': 'CHEBI_17336',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH1B1 <107>',
                'data': '0.028 {all-trans-retinol}',
                'refs': [107],
                'substrate': 'all-trans-retinol',
                'units': '1/s',
                'value': 0.028},
               {'comment': '#8# recombinant allozyme Ile308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.038 {Octanol}',
                'refs': [115],
                'substrate': 'Octanol',
                'units': '1/s',
                'value': 0.038},
               {'comment': '#8# recombinant allozyme Val308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.04 {Octanol}',
                'refs': [115],
                'substrate': 'Octanol',
                'units': '1/s',
                'value': 0.04},
               {'chebi': 'CHEBI_50211',
                'comment': '#8# recombinant allozyme Ile308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.087 {retinol}',
                'refs': [115],
                'substrate': 'retinol',
                'units': '1/s',
                'value': 0.087},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.088 {3,4-dihydro-retinol}',
                'refs': [107],
                'substrate': '3,4-dihydro-retinol',
                'units': '1/s',
                'value': 0.088},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B1 <107>',
                'data': '0.092 {4-hydroxy-retinol}',
                'refs': [107],
                'substrate': '4-hydroxy-retinol',
                'units': '1/s',
                'value': 0.092},
               {'chebi': 'CHEBI_17790',
                'data': '0.102 {methanol}',
                'refs': [12],
                'substrate': 'methanol',
                'units': '1/s',
                'value': 0.102},
               {'chebi': 'CHEBI_50211',
                'comment': '#8# recombinant allozyme Val308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.11 {retinol}',
                'refs': [115],
                'substrate': 'retinol',
                'units': '1/s',
                'value': 0.11},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B1 <107>',
                'data': '0.167 {4-oxo-retinal}',
                'refs': [107],
                'substrate': '4-oxo-retinal',
                'units': '1/s',
                'value': 0.167},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# recombinant allozyme Ile308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.167 {ethanol}',
                'refs': [115],
                'substrate': 'ethanol',
                'units': '1/s',
                'value': 0.167},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# recombinant allozyme Val308, pH 7.5, 25°C '
                           '<115>',
                'data': '0.175 {ethanol}',
                'refs': [115],
                'substrate': 'ethanol',
                'units': '1/s',
                'value': 0.175},
               {'data': '0.183 {1-Pentanol}',
                'refs': [11],
                'substrate': '1-Pentanol',
                'units': '1/s',
                'value': 0.183},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.22 {3,4-dihydro-retinal}',
                'refs': [107],
                'substrate': '3,4-dihydro-retinal',
                'units': '1/s',
                'value': 0.22},
               {'data': '0.245 {Pentanol}',
                'refs': [16],
                'substrate': 'Pentanol',
                'units': '1/s',
                'value': 0.245},
               {'chebi': 'CHEBI_17336',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.25 {all-trans-retinol}',
                'refs': [107],
                'substrate': 'all-trans-retinol',
                'units': '1/s',
                'value': 0.25},
               {'data': '0.333 {12-Hydroxydodecanoic acid}',
                'refs': [11],
                'substrate': '12-Hydroxydodecanoic acid',
                'units': '1/s',
                'value': 0.333},
               {'chebi': 'CHEBI_17336',
                'data': '0.4 {all-trans-retinol}',
                'refs': [53],
                'substrate': 'all-trans-retinol',
                'units': '1/s',
                'value': 0.4},
               {'data': '0.467 {Vanillyl alcohol}',
                'refs': [16],
                'substrate': 'Vanillyl alcohol',
                'units': '1/s',
                'value': 0.467},
               {'chebi': 'CHEBI_17898',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '0.55 {all-trans-retinal}',
                'refs': [107],
                'substrate': 'all-trans-retinal',
                'units': '1/s',
                'value': 0.55},
               {'data': '0.583 {Cyclohexanol}',
                'refs': [14],
                'substrate': 'Cyclohexanol',
                'units': '1/s',
                'value': 0.583},
               {'comment': '#8# pH 7.5, anodic enzyme form <18>',
                'data': '0.667 {Pentanol}',
                'refs': [18],
                'substrate': 'Pentanol',
                'units': '1/s',
                'value': 0.667},
               {'comment': '#8# pH 7.5, anodic enzyme form <18>',
                'data': '0.683 {3-Pyridylcarbinol}',
                'refs': [18],
                'substrate': '3-Pyridylcarbinol',
                'units': '1/s',
                'value': 0.683},
               {'comment': '#8# pH 7.5, anodic enzyme form <18>',
                'data': '0.7 {butanol}',
                'refs': [18],
                'substrate': 'butanol',
                'units': '1/s',
                'value': 0.7},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# pH 7.5, anodic enzyme form <18>',
                'data': '0.7 {ethanol}',
                'refs': [18],
                'substrate': 'ethanol',
                'units': '1/s',
                'value': 0.7},
               {'comment': '#8# pH 7.5, anodic enzyme form <18>',
                'data': '0.717 {NAD+}',
                'refs': [18],
                'substrate': 'NAD+',
                'units': '1/s',
                'value': 0.717},
               {'data': '0.75 {2-propanol}',
                'refs': [14],
                'substrate': '2-propanol',
                'units': '1/s',
                'value': 0.75},
               {'chebi': 'CHEBI_30742',
                'data': '0.75 {ethylene glycol}',
                'refs': [14],
                'substrate': 'ethylene glycol',
                'units': '1/s',
                'value': 0.75},
               {'chebi': 'CHEBI_17336',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '0.9 {all-trans-retinol}',
                'refs': [107],
                'substrate': 'all-trans-retinol',
                'units': '1/s',
                'value': 0.9},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '1.22 {3,4-dihydro-retinal}',
                'refs': [107],
                'substrate': '3,4-dihydro-retinal',
                'units': '1/s',
                'value': 1.22},
               {'chebi': 'CHEBI_17898',
                'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '1.83 {all-trans-retinal}',
                'refs': [107],
                'substrate': 'all-trans-retinal',
                'units': '1/s',
                'value': 1.83},
               {'chebi': 'CHEBI_17890',
                'data': '1.83 {tryptophol}',
                'refs': [14],
                'substrate': 'tryptophol',
                'units': '1/s',
                'value': 1.83},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# pH 10.0, anodic enzyme form <18>',
                'data': '10.2 {ethanol}',
                'refs': [18],
                'substrate': 'ethanol',
                'units': '1/s',
                'value': 10.2},
               {'data': '16 {Pentanol}',
                'refs': [53],
                'substrate': 'Pentanol',
                'units': '1/s',
                'value': 16.0},
               {'data': '17.2 {Propanol}',
                'refs': [53],
                'substrate': 'Propanol',
                'units': '1/s',
                'value': 17.2},
               {'data': '19.5 {Hexanol}',
                'refs': [53],
                'substrate': 'Hexanol',
                'units': '1/s',
                'value': 19.5},
               {'data': '2.17 {(S)-2-butanol}',
                'refs': [53],
                'substrate': '(S)-2-butanol',
                'units': '1/s',
                'value': 2.17},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '2.5 {3,4-dihydro-retinol}',
                'refs': [107],
                'substrate': '3,4-dihydro-retinol',
                'units': '1/s',
                'value': 2.5},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# per active site <12>',
                'data': '2.5 {ethanol}',
                'refs': [12],
                'substrate': 'ethanol',
                'units': '1/s',
                'value': 2.5},
               {'data': '2.83 {1-Octanol}',
                'refs': [11],
                'substrate': '1-Octanol',
                'units': '1/s',
                'value': 2.83},
               {'chebi': 'CHEBI_28816',
                'data': '2.83 {2-deoxy-D-ribose}',
                'refs': [14],
                'substrate': '2-deoxy-D-ribose',
                'units': '1/s',
                'value': 2.83},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '2.83 {4-hydroxy-retinol}',
                'refs': [107],
                'substrate': '4-hydroxy-retinol',
                'units': '1/s',
                'value': 2.83},
               {'data': '2.95 {12-hydroxydodecanoate}',
                'refs': [53],
                'substrate': '12-hydroxydodecanoate',
                'units': '1/s',
                'value': 2.95},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '20 {4-oxo-retinal}',
                'refs': [107],
                'substrate': '4-oxo-retinal',
                'units': '1/s',
                'value': 20.0},
               {'data': '3.03 {12-hydroxydodecanoate}',
                'refs': [16],
                'substrate': '12-hydroxydodecanoate',
                'units': '1/s',
                'value': 3.03},
               {'chebi': 'CHEBI_17935',
                'data': '3.33 {octanal}',
                'refs': [16],
                'substrate': 'octanal',
                'units': '1/s',
                'value': 3.33},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme gamma1,gamma1 <13>',
                'data': '3.83 {ethanol}',
                'refs': [13],
                'substrate': 'ethanol',
                'units': '1/s',
                'value': 3.83},
               {'chebi': 'CHEBI_16236',
                'data': '30.7 {ethanol}',
                'refs': [53],
                'substrate': 'ethanol',
                'units': '1/s',
                'value': 30.7},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH4 <107>',
                'data': '34.2 {4-hydroxy-retinol}',
                'refs': [107],
                'substrate': '4-hydroxy-retinol',
                'units': '1/s',
                'value': 34.2},
               {'data': '34.8 {butanol}',
                'refs': [53],
                'substrate': 'butanol',
                'units': '1/s',
                'value': 34.8},
               {'data': '4 {12-hydroxydodecanoate}',
                'refs': [14],
                'substrate': '12-hydroxydodecanoate',
                'units': '1/s',
                'value': 4.0},
               {'chebi': 'CHEBI_16236',
                'comment': '#8# isoenzyme alpha,gamma1 <13>',
                'data': '4 {ethanol}',
                'refs': [13],
                'substrate': 'ethanol',
                'units': '1/s',
                'value': 4.0},
               {'comment': '#8# isoenzyme alpha,gamma1 <13>',
                'data': '4.33 {Octanol}',
                'refs': [13],
                'substrate': 'Octanol',
                'units': '1/s',
                'value': 4.33},
               {'chebi': 'CHEBI_17987',
                'comment': '#8# isoenzyme alpha,gamma1 <13>',
                'data': '4.67 {benzyl alcohol}',
                'refs': [13],
                'substrate': 'benzyl alcohol',
                'units': '1/s',
                'value': 4.67},
               {'data': '6.17 {16-hydroxyhexadecanoate}',
                'refs': [14],
                'substrate': '16-hydroxyhexadecanoate',
                'units': '1/s',
                'value': 6.17},
               {'data': '7.33 {Octanol}',
                'refs': [16],
                'substrate': 'Octanol',
                'units': '1/s',
                'value': 7.33},
               {'chebi': 'CHEBI_88817',
                'data': '7.5 {3-Phenyl-1-propanol}',
                'refs': [14],
                'substrate': '3-Phenyl-1-propanol',
                'units': '1/s',
                'value': 7.5},
               {'comment': '#8# pH 7.5, 25°C, isozyme ADH1B2 <107>',
                'data': '7.83 {4-oxo-retinal}',
                'refs': [107],
                'substrate': '4-oxo-retinal',
                'units': '1/s',
                'value': 7.83},
               {'chebi': 'CHEBI_16236',
                'data': '7.83 {ethanol}',
                'refs': [14],
                'substrate': 'ethanol',
                'units': '1/s',
                'value': 7.83},
               {'data': '8 {Pentanol}',
                'refs': [14],
                'substrate': 'Pentanol',
                'units': '1/s',
                'value': 8.0},
               {'data': '8.33 {Octanol}',
                'refs': [14],
                'substrate': 'Octanol',
                'units': '1/s',
                'value': 8.33},
               {'data': '8.67 {Vanillyl alcohol}',
                'refs': [14],
                'substrate': 'Vanillyl alcohol',
                'units': '1/s',
                'value': 8.67},
               {'chebi': 'CHEBI_17987',
                'data': '9.17 {benzyl alcohol}',
                'refs': [14],
                'substrate': 'benzyl alcohol',
                'units': '1/s',
                'value': 9.17}]),
             ('TO',
              [{'comment': '#5,8,10# assay at <107,115,119,121,124,229,295>; '
                           '#61# assay at, forward and reverse reaction <113>; '
                           '#10# free enzyme, at 25°C <196>',
                'data': '25',
                'refs': [106,
                         107,
                         113,
                         115,
                         119,
                         121,
                         124,
                         131,
                         196,
                         229,
                         295]},
               {'comment': '#8,41# assay at <116>',
                'data': '30-37',
                'refs': [116]}]),
             ('TS',
              [{'comment': '#8# unstable at room temperature and above <12>',
                'data': '23',
                'refs': [12]},
               {'comment': '#41# distinct subunits have different deactivation '
                           'properties <37>; #10# effect of salts in the high '
                           'concentration range on the thermal stability '
                           '<148>; #41# alpha-cyclodextrin causes thermal '
                           'stabilization and delays the onset of secondary '
                           'structural unfolding and aggregation by approx. '
                           '10°C and the midpoint temperatures by more than '
                           '5°C. alpha-Cyclodextrin diminishes the '
                           'deactivation of the enzyme, decreasing the '
                           'deactivation constant by more than 50%, and '
                           'clearly reveals the stabilization of the enzyme '
                           'not only structurally but also kinetically at '
                           'higher temperatures <178>; #44# temperature '
                           'stability profiles of recombinantly expressed '
                           'enzymes, overview <232>',
                'data': '-999',
                'refs': [37, 112, 115, 148, 178, 232]}]),
             ('references',
              {1: {'info': 'Talbot, B.G.; Qureshi, A.A.; Cohen, R.; Thirion, '
                           'J.P.: Purification and properties of two distinct '
                           'groups of ADH isozymes from Chinese hamster liver. '
                           'Biochem. Genet. (1981) 19, 813-829.',
                   'pubmed': 6794566},
               2: {'info': 'Fong, W.P.: Isolation and characterization of '
                           'grass carp (Ctenopharyngodon idellus) liver '
                           'alcohol dehydrogenase. Comp. Biochem. Physiol. B '
                           '(1991) 98, 297-302.'},
               3: {'info': 'Pessione, E.; Pergola, L.; Cavaletto, M.; Giunta, '
                           'C.; Trotta, A.; Vanni, A.: Extraction, '
                           'purification and characterization of ADH1 from the '
                           'budding yeast Kluyveromyces marxianus. Ital. J. '
                           'Biochem. (1990) 39, 71-82.',
                   'pubmed': 2193901},
               4: {'info': 'Leblova, S.; El Ahmad, M.: Characterization of '
                           'alcohol dehydrogenase isolated from germinating '
                           'bean (Vicia faba) seeds. Collect. Czech. Chem. '
                           'Commun. (1989) 54, 2519-2527.'},
               5: {'info': 'Keung, W.M.; Ho, Y.W.; Fong, W.P.; Lee, C.Y.: '
                           'Isolation and characterization of shrew (Suncus '
                           'murinus) liver alcohol dehydrogenase. Comp. '
                           'Biochem. Physiol. B (1989) 93, 169-173.',
                   'pubmed': 2666017},
               6: {'info': 'Tong, W.F.; Lin, S.W.: Purification and '
                           'biochemical properties of rice alcohol '
                           'dehydrogenase. Bot. Bull. Acad. Sin. (1988) 29, '
                           '245-253.'},
               7: {'info': 'Van Geyt, J.; Jacobs, M.; Triest, L.: '
                           'Characterization of alcohol dehydrogenase in Najas '
                           'marina L. Aquat. Bot. (1987) 28, 129-141.'},
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
                           '(1982) 7, 237-250.'},
               9: {'info': 'Edenberg, H.J.; Brown, C.J.; Carr, L.G.; Ho, W.H.; '
                           'Hu, M.W.: Alcohol dehydrogenase gene expression '
                           'and cloning of the mouse chi-like ADH. Adv. Exp. '
                           'Med. Biol. (1991) 284, 253-262.',
                   'pubmed': 2053480},
               10: {'info': 'Herrera, E.; Zorzano, A.; Fresneda, V.: '
                            'Comparative kinetics of human and rat liver '
                            'alcohol dehydrogenase. Biochem. Soc. Trans. '
                            '(1983) 11, 729-730.'},
               11: {'info': 'Dafeldecker, W.P.; Vallee, B.L.: Organ-specific '
                            'human alcohol dehydrogenase: isolation and '
                            'characterization of isozymes from testis. '
                            'Biochem. Biophys. Res. Commun. (1986) 134, '
                            '1056-1063.',
                    'pubmed': 2936344},
               12: {'info': 'Woronick, C.L.: Alcohol dehydrogenase from human '
                            'liver. Methods Enzymol. (1975) 41B, 369-374.',
                    'pubmed': 236461},
               13: {'info': 'Wagner, F.W.; Burger, A.R.; Vallee, B.L.: Kinetic '
                            'properties of human liver alcohol dehydrogenase: '
                            'oxidation of alcohols by class I isoenzymes. '
                            'Biochemistry (1983) 22, 1857-1863.',
                    'pubmed': 6342669},
               14: {'info': 'Ditlow, C.C.; Holmquist, B.; Morelock, M.M.; '
                            'Vallee, B.L.: Physical and enzymatic properties '
                            'of a class II alcohol dehydrogenase isozyme of '
                            'human liver: pi-ADH. Biochemistry (1984) 23, '
                            '6363-6368.',
                    'pubmed': 6397223},
               15: {'info': 'Yin, S.J.; Bosron, W.F.; Magnes, L.J.; Li, T.K.: '
                            'Human liver alcohol dehydrogenase: purification '
                            'and kinetic characterization of the beta 2 beta '
                            '2, beta 2 beta 1, alpha beta 2, and beta 2 gamma '
                            '1 Oriental isoenzymes. Biochemistry (1984) 23, '
                            '5847-5853.',
                    'pubmed': 6395883},
               16: {'info': 'Wagner, F.W.; Pares, X.; Holmquist, B.; Vallee, '
                            'B.L.: Physical and enzymatic properties of a '
                            'class III isozyme of human liver alcohol '
                            'dehydrogenase: chi-ADH. Biochemistry (1984) 23, '
                            '2193-2199.',
                    'pubmed': 6375718},
               17: {'info': 'Bosron, W.F.; Magnes, L.J.; Li, T.K.: Kinetic and '
                            'electrophoretic properties of native and '
                            'recombined isoenzymes of human liver alcohol '
                            'dehydrogenase. Biochemistry (1983) 22, 1852-1857.',
                    'pubmed': 6342668},
               18: {'info': 'Bosron, W.F.; Li, T.K.: Isolation and '
                            'characterization of an anodic form of human liver '
                            'alcohol dehydrogenase. Biochem. Biophys. Res. '
                            'Commun. (1977) 74, 85-91.',
                    'pubmed': 836289},
               19: {'info': 'Schneider-Bernloehr, H.; Formicka-Kozlowska, G.; '
                            'Buehler, R.; Wartburg, J.P.; Zeppezauer, M.: '
                            'Active-site-specific zinc-depleted and '
                            'reconstituted cobalt(II) human-liver alcohol '
                            'dehydrogenase. Preparation, characterization and '
                            'complexation with NADH and '
                            'trans-4-(N,N-dimethylamino)-cinnamaldehyde. Eur. '
                            'J. Biochem. (1988) 173, 275-280.',
                    'pubmed': 3360008},
               20: {'info': 'Burnell, J.C.; Li, T.K.; Bosron, W.F.: '
                            'Purification and steady-state kinetic '
                            'characterization of human liver beta 3 beta 3 '
                            'alcohol dehydrogenase. Biochemistry (1989) 28, '
                            '6810-6815.',
                    'pubmed': 2819035},
               21: {'info': 'Pares, X.; Vallee, B.L.: New human liver alcohol '
                            'dehydrogenase forms with unique kinetic '
                            'characteristics. Biochem. Biophys. Res. Commun. '
                            '(1981) 98, 122-130.',
                    'pubmed': 7011320},
               22: {'info': 'Bosron, W.F.; Li, T.K.; Vallee, B.L.: New '
                            'molecular forms of human liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'ADHIndianapolis. Proc. Natl. Acad. Sci. USA '
                            '(1980) 77, 5784-5788.',
                    'pubmed': 7003596},
               23: {'info': 'Bosron, W.F.; Li, T.K.; Dafeldecker, W.P.; '
                            'Vallee, B.L.: Human liver pig-alcohol '
                            'dehydrogenase: kinetic and molecular properties. '
                            'Biochemistry (1979) 18, 1101-1105.',
                    'pubmed': 427099},
               24: {'info': 'Dafeldecker, W.P.; Pares, X.; Vallee, B.L.; '
                            'Bosron, W.F.; Li, T.K.: Simian liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'isoenzymes from Saimiri sciureus. Biochemistry '
                            '(1981) 20, 856-861.',
                    'pubmed': 7011375},
               25: {'info': 'Dafeldecker, W.P.; Meadow, P.E.; Pares, X.; '
                            'Vallee, B.L.: Simian liver alcohol dehydrogenase: '
                            'isolation and characterization of isoenzymes from '
                            'Macaca mulatta. Biochemistry (1981) 20, '
                            '6729-6734.',
                    'pubmed': 7030395},
               26: {'info': 'Kvassman, J.; Pettersson, G.: Kinetics of '
                            'coenzyme binding to liver alcohol dehydrogenase '
                            'in the pH range 10-12. Eur. J. Biochem. (1987) '
                            '166, 167-172.',
                    'pubmed': 3595610},
               27: {'info': 'Andersson, L.; Mosbach, K.: Alcohol dehydrogenase '
                            'from horse liver by affinity chromatography. '
                            'Methods Enzymol. (1982) 89, 435-445.',
                    'pubmed': 6755178},
               28: {'info': 'Pietruszko, R.: Alcohol dehydrogenase from horse '
                            'liver, steroid-active SS isoenzyme. Methods '
                            'Enzymol. (1982) 89, 429-435.'},
               29: {'info': 'Dahl, K.H.; Eklund, H.; McKinley-McKee, J.S.: '
                            'Enantioselective affinity labelling of horse '
                            'liver alcohol dehydrogenase. Correlation of '
                            'inactivation kinetics with the three-dimensional '
                            'structure of the enzyme. Biochem. J. (1983) 211, '
                            '391-396.',
                    'pubmed': 6347187},
               30: {'info': 'Ramaswamy, S.: Dynamics in alcohol dehydrogenase '
                            'elucidated from crystallographic investigations. '
                            'Adv. Exp. Med. Biol. (1999) 7, 275-284.',
                    'pubmed': 10352696},
               31: {'info': 'Adolph, H.W.; Maurer, P.; Schneider-Bernloehr, '
                            'H.; Sartorius, C.; Zeppezauer, M.: Substrate '
                            'specificity and stereoselectivity of horse liver '
                            'alcohol dehydrogenase. Kinetic evaluation of '
                            'binding and activation parameters controlling the '
                            'catalytic cycles of unbranched, acyclic secondary '
                            'alcohols and ketones as substrates of the native '
                            'and active-site-specific Co(II)-substituted '
                            'enzyme. Eur. J. Biochem. (1991) 201, 615-625.',
                    'pubmed': 1935957},
               32: {'info': 'Freudenreich, C.; Samama, J.P.; Biellmann, J.F.: '
                            'Design of inhibitors from the three-dimensional '
                            'structure of alcohol dehydrogenase. Chemical '
                            'synthesis and enzymatic properties. J. Am. Chem. '
                            'Soc. (1984) 106, 3344-3353.'},
               33: {'info': 'Samama, J.P.; Hirsch, D.; Goulas, P.; Biellmann, '
                            'J.F.: Dependence of the substrate specificity and '
                            'kinetic mechanism of horse-liver alcohol '
                            'dehydrogenase on the size of the C-3 pyridinium '
                            'substituent. 3-Benzoylpyridine-adenine '
                            'dinucleotide. Eur. J. Biochem. (1986) 159, '
                            '375-380.',
                    'pubmed': 3758068},
               34: {'info': 'Eklund, H.: Coenzyme binding in alcohol '
                            'dehydrogenase. Biochem. Soc. Trans. (1989) 17, '
                            '293-296.',
                    'pubmed': 2753206},
               35: {'info': 'Dworschack, R.T.; Plapp, B.V.: Kinetics of native '
                            'and activated isozymes of horse liver alcohol '
                            'dehydrogenase. Biochemistry (1977) 16, 111-116.',
                    'pubmed': 831772},
               36: {'info': 'Maret, W.; Andersson, I.; Dietrich, H.; '
                            'Schneider-Bernloehr, H.; Einarsson, R.; '
                            'Zeppezauer, M.: Site-specific substituted '
                            'cobalt(II) horse liver alcohol dehydrogenases. '
                            'Preparation and characterization in solution, '
                            'crystalline and immobilized state. Eur. J. '
                            'Biochem. (1979) 98, 501-512.',
                    'pubmed': 488110},
               37: {'info': 'Skerker, P.S.; Clark, D.S.: Thermostability of '
                            'alcohol dehydrogenase: evidence for distinct '
                            'subunits with different deactivation properties. '
                            'Biotechnol. Bioeng. (1989) 33, 62-71.',
                    'pubmed': 18587844},
               38: {'info': 'Benach, J.; Atrian, S.; Gonzalez-Duarte, R.; '
                            'Ladenstein, R.: The catalytic reaction and '
                            'inhibition mechanism of Drosophila alcohol '
                            'dehydrogenase: observation of an enzyme-bound '
                            'NAD-ketone adduct at 1.4 A resolution by X-ray '
                            'crystallography. J. Mol. Biol. (1999) 289, '
                            '335-355.',
                    'pubmed': 10366509},
               39: {'info': 'Tsai, C.S.: Multifunctionality of liver alcohol '
                            'dehydrogenase: kinetic and mechanistic studies of '
                            'esterase reaction. Arch. Biochem. Biophys. (1982) '
                            '213, 635-642.',
                    'pubmed': 7041828},
               40: {'info': 'Favilla, R.; Cavatorta, P.; Mazzini, A.; Fava, '
                            'A.: The peroxidatic reaction catalyzed by horse '
                            'liver alcohol dehydrogenase. 2. Steady-state '
                            'kinetics and inactivation. Eur. J. Biochem. '
                            '(1980) 104, 223-227.',
                    'pubmed': 6989598},
               41: {'info': 'Ryzewski, C.N.; Pietruszko, R.: Kinetic mechanism '
                            'of horse liver alcohol dehydrogenase SS. '
                            'Biochemistry (1980) 19, 4843-4848.',
                    'pubmed': 7000185},
               42: {'info': 'Ryzewski, C.N.; Pietruszko, R.: Horse liver '
                            'alcohol dehydrogenase SS: purification and '
                            'characterization of the homogenous isoenzyme. '
                            'Arch. Biochem. Biophys. (1977) 183, 73-82.',
                    'pubmed': 20851},
               43: {'info': 'Winberg, J.O.; McKinley-McKee, J.S.: Drosophila '
                            'melanogaster alcohol dehydrogenase: '
                            'product-inhibition studies. Biochem. J. (1994) '
                            '301, 901-909.',
                    'pubmed': 8053914},
               44: {'info': 'von Bahr-Lindstroem, H.; Andersson, L.; Mosbach, '
                            'K.; Joernvall, H.: Purification and '
                            'characterization of chicken liver alcohol '
                            'dehydrogenase. FEBS Lett. (1978) 89, 293-297.',
                    'pubmed': 658420},
               45: {'info': 'Hoshino, T.; Ishigura, I.; Ohta, Y.: Rabbit liver '
                            'alcohol dehydrogenase: purification and '
                            'properties. J. Biochem. (1985) 97, 1163-1172.',
                    'pubmed': 3161873},
               46: {'info': 'Keung, W.M.; Yip, P.K.: Rabbit liver alcohol '
                            'dehydrogenase: isolation and characterization of '
                            'class I isozymes. Biochem. Biophys. Res. Commun. '
                            '(1989) 158, 445-453.',
                    'pubmed': 2916992},
               47: {'info': 'Keung, W.M.: A genuine organ specific alcohol '
                            'dehydrogenase from hamster testes: isolation, '
                            'characterization and developmental changes. '
                            'Biochem. Biophys. Res. Commun. (1988) 156, 38-45.',
                    'pubmed': 3178842},
               48: {'info': 'Algar, E.M.; Seeley, T.L.; Holmes, R.S.: '
                            'Purification and molecular properties of mouse '
                            'alcohol dehydrogenase isozymes. Eur. J. Biochem. '
                            '(1983) 137, 139-147.',
                    'pubmed': 6360682},
               49: {'info': 'Julia, P.; Farres, J.; Pares, X.: '
                            'Characterization of three isoenzymes of rat '
                            'alcohol dehydrogenase. Tissue distribution and '
                            'physical and enzymatic properties. Eur. J. '
                            'Biochem. (1987) 162, 179-189.',
                    'pubmed': 3816781},
               50: {'info': 'Pares, X.; Moreno, A.; Cederlund, E.; Hoeoeg, '
                            'J.O.; Joernvall, H.: Class IV mammalian alcohol '
                            'dehydrogenase. Structural data of the rat stomach '
                            'enzyme reveal a new class well separated from '
                            'those already characterized. FEBS Lett. (1990) '
                            '277, 115-118.',
                    'pubmed': 2269340},
               51: {'info': 'Mezey, E.; Potter, J.J.: Separation and partial '
                            'characterization of multiple forms of rat liver '
                            'alcohol dehydrogenase. Arch. Biochem. Biophys. '
                            '(1983) 225, 787-794.',
                    'pubmed': 6354095},
               52: {'info': 'Hjelmqvist, L.; Shafqqat, J.; Siddiqi, A.R.; '
                            'Joernvall, H.: Linking of isoenzyme and class '
                            'variability patterns in the emergence of novel '
                            'alcohol dehydrogenase functions. Characterization '
                            'of isozymes in Uromastix hardwickii. Eur. J. '
                            'Biochem. (1996) 236, 563-570.',
                    'pubmed': 8612630},
               53: {'info': 'Kedishvili, N.Y.; Bosron, W.F.; Stone, C.L.; '
                            'Hurley, T.D.; Peggs, C.F.; Thomasson, H.R.; '
                            'Popov, K.M.; Carr, L.G.; Edenberg, H.J.; Li, '
                            'T.K.: Expression and kinetic characterization of '
                            'recombinant human stomach alcohol dehydrogenase. '
                            'Active-site amino acid sequence explains '
                            'substrate specificity copared with liver '
                            'isozymes. J. Biol. Chem. (1995) 270, 3625-3630.',
                    'pubmed': 7876099},
               54: {'info': 'Plapp, B.V.; Sogin, D.C.; Dworschack, R.T.; '
                            'Bohlken, D.P.; Woenckhaus, C.: Kinetics of native '
                            'and modified liver alcohol dehydrogenase with '
                            'coenzyme analogues: isomerization of '
                            'enzyme-nicotinamide adenine dinucleotide complex. '
                            'Biochemistry (1986) 25, 5396-5402.',
                    'pubmed': 3778867},
               55: {'info': 'Li, H.; Hallows, W.H.; Punzi, J.S.; Marquez, '
                            'V.E.; Carrell, H.L.; Pankiewicz, K.W.; Watanabe, '
                            'K.A.; Goldstein, B.M.: Crystallographic studies '
                            'of two alcohol dehydrogenase-bound analogues of '
                            'thiazole-4-carboxamide adenine dinucleotide '
                            '(TAD), the active anabolite of the antitumor '
                            'agent tiazofurin. Biochemistry (1994) 33, 23-32.',
                    'pubmed': 8286346},
               56: {'info': 'Pearl, L.H.; Demasi, D.; Hemmings, A.M.; Sica, '
                            "F.; Mazzarella, L.; Raia, C.A.; D'Auria, S.; "
                            'Rossi, M.: Crystallization and preliminary X-ray '
                            'analysis of an NAD(+)-dependent alcohol '
                            'dehydrogenase fromthe extreme thermophilic '
                            'archaebacterium Sulfolobus solfataricus. J. Mol. '
                            'Biol. (1993) 229, 782-784.',
                    'pubmed': 8433371},
               57: {'info': 'Shafqat, J.; Hjelmqvist, L.; Joernvall, H.: Liver '
                            'class-I alcohol dehydrogenase isozyme '
                            'relationships and constant patterns in a variable '
                            'basic structure. Distinctions from '
                            'characterization of an ethanol dehydrogenase in '
                            'cobra, Naja naja. Eur. J. Biochem. (1996) 236, '
                            '571-578.',
                    'pubmed': 8612631},
               58: {'info': 'Retzios, A.; Thatcher, D.R.: Characterization of '
                            'the Adhf and Adhus alleloenzymes of Drosophila '
                            'melanogaster (fruitfly) alcohol dehydrogenase. '
                            'Biochem. Soc. Trans. (1981) 9, 298-299.'},
               59: {'info': 'Bauermeister, A.; Sargent, J.: Purification and '
                            'properties of an alcohol dehydrogenase from the '
                            'liver and intestinal caecum of rainbow trout '
                            '(Salmo gairdnerii). Biochem. Soc. Trans. (1978) '
                            '6, 222-224.',
                    'pubmed': 640168},
               60: {'info': 'Nussrallah, B.A.; Dam, R.; Wagner, F.W.: '
                            'Characterization of Coturnix quail liver alcohol '
                            'dehydrogenase enzymes. Biochemistry (1989) 28, '
                            '6245-6251.',
                    'pubmed': 2789998},
               61: {'info': 'Winberg, J.O.; Hovik, R.; McKinley-McKee, J.S.; '
                            'Juan, E.; Gonzalez-Duarte, R.: Biochemical '
                            'properties of alcohol dehydrogenase from '
                            'Drosophila lebanonensis. Biochem. J. (1986) 235, '
                            '481-490.',
                    'pubmed': 2943270},
               62: {'info': 'Winberg, J.O.; McKinley-McKee, J.S.: Drosophila '
                            'melanogaster alcohol dehydrogenase. Biochemical '
                            'properties of the NAD+-plus-acetone-induced '
                            'isoenzyme conversion. Biochem. J. (1988) 251, '
                            '223-227.',
                    'pubmed': 3134011},
               63: {'info': 'Heinstra, P.W.H.; Thoerig, G.E.W.; Scharloo, W.; '
                            'Drenth, W.; Nolte, R.J.M.: Kinetics and '
                            'thermodynamics of ethanol oxidation catalyzed by '
                            'genetic variants of the alcohol dehydrogenase '
                            'from Drosophila melanogaster and D. simulans. '
                            'Biochim. Biophys. Acta (1988) 967, 224-233.',
                    'pubmed': 3142528},
               64: {'info': 'Juan, E.; Gonzalez-Duarte, R.: Determination of '
                            'some biochemical and structural features of '
                            'alcohol dehydrogenases from Drosophila simulans '
                            'and Drosophila virilis. Comparison of their '
                            'properties with the Drosophila melanogaster Adhs '
                            'enzyme. Biochem. J. (1981) 195, 61-69.',
                    'pubmed': 6796069},
               65: {'info': 'Lee, C.Y.: Alcohol dehydrogenase from Drosophila '
                            'melanogaster. Methods Enzymol. (1982) 89, '
                            '445-450.'},
               66: {'info': 'Rella, R.; Raia, C.A.; Pensa, M.; Pisani, F.M.; '
                            'Gambacorta, A.; de Rosa, M.; Rossi, M.: A novel '
                            'archaebacterial NAD+-dependent alcohol '
                            'dehydrogenase. Purification and properties. Eur. '
                            'J. Biochem. (1987) 167, 475-479.',
                    'pubmed': 3115775},
               67: {'info': 'Wills, C.; Kratofil, P.; Londo, D.; Martin, T.: '
                            'Characterization of the two alcohol '
                            'dehydrogenases of Zymomonas mobilis. Arch. '
                            'Biochem. Biophys. (1981) 210, 775-785.',
                    'pubmed': 7030207},
               68: {'info': 'Kinoshita, S.; Kakizono, T.; Kadota, K.; Das, K.; '
                            'Taguchi, H.: Purification of two alcohol '
                            'dehydrogenases from Zymomonas mobilis and their '
                            'properties. Appl. Microbiol. Biotechnol. (1985) '
                            '22, 249-254.'},
               69: {'info': 'Grondal, E.J.M.; Betz, A.; Kreuzberg, K.: Partial '
                            'purification and properties of alcohol '
                            'dehydrogenase from unicellular green alga '
                            'Chlamydomonas moewusii. Phytochemistry (1983) 22, '
                            '1695-1699.'},
               70: {'info': 'Ammendola, S.; Raia, C.A.; Caruso, C.; '
                            "Camardella, L.; D'Auria, S.; De Rosa, M.; Rossi, "
                            'M.: Thermostable NAD(+)-dependent alcohol '
                            'dehydrogenase from Sulfolobus solfataricus: gene '
                            'and protein sequence determination and '
                            'relationship to other alcohol dehydrogenases. '
                            'Biochemistry (1992) 31, 12514-12523.',
                    'pubmed': 1463738},
               71: {'info': 'Tihanyi, K.; Talbot, B.; Brzezinski, R.; Thirion, '
                            'J.P.: Purification and characterization of '
                            'alcohol dehydrogenase from soybean. '
                            'Phytochemistry (1989) 28, 1335-1338.'},
               72: {'info': 'Liang, Z.Q.; Hayase, F.; Nishimura, T.; Kato, H.: '
                            'Purification and characterization of '
                            'NAD-dependent alcohol dehydrogenase and '
                            'NADH-dependent 2-oxoaldehyde reductase from '
                            'parsley. Agric. Biol. Chem. (1990) 54, '
                            '1717-1719.'},
               73: {'info': 'Hatanaka, A.; Harada, T.: Purification and '
                            'properties of alcohol dehydrogenase from tea '
                            'seeds. Agric. Biol. Chem. (1972) 36, 2033-2035.'},
               74: {'info': 'Stiborova, M.; Leblova, S.: Kinetics of the '
                            'reaction catalysed by rape alcohol dehydrogenase. '
                            'Phytochemistry (1979) 18, 23-24.'},
               75: {'info': 'Lai, Y.K.; Chandlee, J.M.; Scandalios, J.G.: '
                            'Purification and characterization of three '
                            'non-allelic alcohol dehydrogenase isoenzymes in '
                            'maize. Biochim. Biophys. Acta (1982) 706, 9-18.'},
               76: {'info': 'Leblova, S.; Ehlichova, D.: Purification and some '
                            'properties of alcohol dehydrogenase from maize. '
                            'Phytochemistry (1972) 11, 1345-1346.'},
               77: {'info': 'Langston, P.J.; Pace, C.N.; Hart, G.E.: Wheat '
                            'alcohol dehydrogenase iszymes. Purification, '
                            'characterization, and gene expression. Plant '
                            'Physiol. (1980) 65, 518-522.',
                    'pubmed': 16661226},
               78: {'info': 'Langston, P.J.; Hart, G.E.; Pace, C.N.: '
                            'Purification and partial characterization of '
                            'alcohol dehydrogenase from wheat. Arch. Biochem. '
                            'Biophys. (1979) 196, 611-618.',
                    'pubmed': 485168},
               79: {'info': 'Mayne, M.G.; Lea, P.J.: Properties of three sets '
                            'of isoenzymes of alcohol dehydrogenase isolated '
                            'from barley (Hordeum vulgare). Phytochemistry '
                            '(1985) 24, 1433-1438.'},
               80: {'info': 'Shimomura, S.; Beevers, H.: Alcohol dehydrogenase '
                            'inactivator from rice seedlings. Properties and '
                            'intracellular location. Plant Physiol. (1983) 71, '
                            '742-746.',
                    'pubmed': 16662899},
               81: {'info': 'Creaser, E.H.; Porter, R.L.; Britt, K.A.; '
                            'Pateman, J.A.; Doy, C.H.: Purification and '
                            'preliminary characterization of alcohol '
                            'dehydrogenase from Aspergillus nidulans. Biochem. '
                            'J. (1985) 225, 449-454.',
                    'pubmed': 3156582},
               82: {'info': 'Yabe, M.; Shitara, K.; Kawashima, J.; Shinoyama, '
                            'H.; Ando, A.; Fujii, T.: Purification and '
                            'properties of an alcohol dehydrogenase isozyme '
                            'from a methanol-using yeast, Candida sp. N-16. '
                            'Biosci. Biotechnol. Biochem. (1992) 56, 338-339.'},
               83: {'info': 'Morosoli, R.; Begin-Heick, N.: The partial '
                            'purification and characterization of cytosol '
                            'alcohol dehydrogenase from Astasia. Biochem. J. '
                            '(1974) 141, 469-475.',
                    'pubmed': 4455216},
               84: {'info': 'Rudge, J.; Bickerstaff, G.F.: Purification and '
                            'properties of an alcohol dehydrogenase from '
                            'Sporotrichum pulverulentum. Enzyme Microb. '
                            'Technol. (1986) 8, 120-124.'},
               85: {'info': 'Indrati, R.; Ohita, Y.: Purification and '
                            'properties of alcohol dehydrogenase from a mutant '
                            'strain of Candida guilliermondii. Can. J. '
                            'Microbiol. (1992) 38, 953-957.'},
               86: {'info': 'Tkachenko, A.G.; Winston, G.W.: Interaction of '
                            'alcohol dehydrogenase with '
                            'tert-butylhydroperoxide: stimulation of the horse '
                            'liver and inhibition of the yeast enzyme. Arch. '
                            'Biochem. Biophys. (2000) 380, 165-173.',
                    'pubmed': 10900146},
               87: {'info': 'Drewke, C.; Ciriacy, M.: Overexpression, '
                            'purification and properties of alcohol '
                            'dehydrogenase IV from Saccharomyces cerevisiae. '
                            'Biochim. Biophys. Acta (1988) 950, 54-60.',
                    'pubmed': 3282541},
               88: {'info': 'Yamazaki, Y.; Maeda, H.; Satoh, A.; Hiromi, K.: A '
                            'kinetic study on the binding of monomeric and '
                            'polymeric derivatives of NAD+ to yeast alcohol '
                            'dehydrogenase. J. Biochem. (1984) 95, 109-115.',
                    'pubmed': 6368531},
               89: {'info': 'Mazid, M.A.; Laidler, K.J.: pH Dependence of free '
                            'and immobilized yeast alcohol dehydrogenase '
                            'kinetics. Can. J. Microbiol. (1982) 60, 100-107.',
                    'pubmed': 7044497},
               90: {'info': 'Dickinson, F.M.; Monger, G.P.: A study of the '
                            'kinetics and mechanism of yeast alcohol '
                            'dehydrogenase with a variety of substrates. '
                            'Biochem. J. (1973) 131, 261-270.',
                    'pubmed': 4352908},
               91: {'info': 'Ganzhorn, A.J.; Green, D.W.; Hershey, A.D.; '
                            'Gould, R.M.; Plapp, B.V.: Kinetic '
                            'characterization of yeast alcohol dehydrogenases. '
                            'Amino acid residue 294 and substrate specificity. '
                            'J. Biol. Chem. (1987) 262, 3754-3761.',
                    'pubmed': 3546317},
               92: {'info': 'Weinhold, E.G.; Benner, S.A.: Engineering yeast '
                            'alcohol dehydrogenase. Replacing Trp54 by Leu '
                            'broadens substrate specificity. Protein Eng. '
                            '(1995) 8, 457-461.',
                    'pubmed': 8532667},
               93: {'info': 'Pocker, Y.; Li, H.: Mechanistic enzymology of '
                            'liver alcohol dehydrogenase. Kinetic and '
                            'stereochemical characterization of retinal '
                            'oxidation and reduction. Adv. Exp.Med. Biol. '
                            '(1996) 6, 331-338.',
                    'pubmed': 9059637},
               94: {'info': 'Leskovac, V.; Trivic, S.; Anderson, B.M.: Use of '
                            'competitive dead-end inhibitors to determine the '
                            'chemical mechanism of action of yeast alcohol '
                            'dehydrogenase. Mol. Cell. Biochem. (1998) 178, '
                            '219-227.',
                    'pubmed': 9546603},
               95: {'info': 'Keung, W.M.: Isolation and characterization of '
                            'three alcohol dehydrogenase isozymes from Syrian '
                            'golden hamster. Alcohol. Clin. Exp. Res. (1996) '
                            '20, 213-220.',
                    'pubmed': 8730210},
               96: {'info': 'Yin, S.J.; Wang, M.F.; Liao, C.S.; Chen, C.M.; '
                            'Wu, C.W.: Identification of a human stomach '
                            'alcohol dehydrogenase with distinctive kinetic '
                            'properties. Biochem. Int. (1990) 22, 829-835.',
                    'pubmed': 2099148},
               97: {'info': 'Osterman, J.C.; Chiang, Y.; Markwell, J.: '
                            'Characterization of mutation-induced changes in '
                            'the maize (Zea mays L.) ADH1-1S1108 alcohol '
                            'dehydrogenase. Biochem. Genet. (1993) 31, '
                            '497-506.',
                    'pubmed': 8166623},
               98: {'info': 'Langeland, B.T.; Morris, D.L.; McKinley-McKee, '
                            'J.S.: Metal binding properties of thiols: '
                            'complexes with horse liver alcohol dehydrogenase. '
                            'Comp. Biochem. Physiol. B (1999) 123, 155-162.',
                    'pubmed': 10425719},
               99: {'info': 'Hensgens, C.M.H.; Vonck, J.; van Beeumen, J.; '
                            'Bruggen, E.F.J.; Hansen, T.A.: Purification and '
                            'characterization of an oxygen-labile, '
                            'NAD-dependent alcohol dehydrogenase from '
                            'Desulfovibrio gigas. J. Bacteriol. (1993) 175, '
                            '2859-2863.',
                    'pubmed': 8491707},
               100: {'info': 'Flores, B.M.; Stanley, S.L.; Yong, T.S.; Ali, '
                             'M.; Yang, W.; Diedrich, D.L.; Torian, B.E.: '
                             'Surface localization, regulation, and biologic '
                             'properties of the 96-kDA alcohol/aldehyde '
                             'dehydrogenase (EhADH2) of pathogenic Entamoeba '
                             'histolytica. J. Infect. Dis. (1996) 173, '
                             '226-231.',
                     'pubmed': 8537663},
               101: {'info': 'Persson, B.; Bergman, T.; Keung, W.M.; '
                             'Waldenstroem, U.; Holmquist, B.; Vallee, B.L.; '
                             'Joernvall, H.: Basic features of class-I alcohol '
                             'dehydrogenase variable and constant segments '
                             'coordinated by inter-class and intra-class '
                             'variabvility. Conclusions from characterization '
                             'of the alligator enzyme. Eur. J. Biochem. (1993) '
                             '216, 49-56.',
                     'pubmed': 8365416},
               102: {'info': 'Gergel, D.; Cederbaum, A.I.: Inhibition of the '
                             'catalytic activity of alcohol dehydrogenase by '
                             'nitric oxide is associated with S nitrosylation '
                             'and the release of zinc. Biochemistry (1996) 35, '
                             '16186-16194.',
                     'pubmed': 8973191},
               103: {'info': 'Lamed, R.; Zeikus, J.G.: Ethanol production by '
                             'thermophilic bacteria: relationship between '
                             'fermentation product yields of and catabolic '
                             'enzyme activities in Clostridium thermocellum '
                             'and Thermoanaerobium brockii. J. Bacteriol. '
                             '(1980) 144, 569-578.',
                     'pubmed': 7430065},
               104: {'info': 'Kim, K.J.; Howard, A.J.: Crystallization and '
                             'preliminary X-ray diffraction analysis of the '
                             'trigonal crystal form of Saccharomyces '
                             'cerevisiae alcohol dehydrogenase I: evidence for '
                             'the existence of Zn ions in the crystal. Acta '
                             'Crystallogr. Sect. D (2002) 58, 1332-1334.',
                     'pubmed': 12136146},
               105: {'info': 'Hadizadeh, M.; Keyhani, E.: Detection and '
                             'kinetic properties of alcohol dehydrogenase in '
                             'dormant corm of Crocus sativus L. Acta Hortic. '
                             '(2004) 650, 127-139.'},
               106: {'info': 'Hildebrandt, P.; Musidlowska, A.; Bornscheuer, '
                             'U.T.; Altenbuchner, J.: Cloning, functional '
                             'expression and biochemical characterization of a '
                             'stereoselective alcohol dehydrogenase from '
                             'Pseudomonas fluorescens DSM50106. Appl. '
                             'Microbiol. Biotechnol. (2002) 59, 483-487.',
                     'pubmed': 12172614},
               107: {'info': 'Martras, S.; Alvarez, R.; Gallego, O.; '
                             'Dominguez, M.; de Lera, A.R.; Farres, J.; Pares, '
                             'X.: Kinetics of human alcohol dehydrogenase with '
                             'ring-oxidized retinoids: effect of Tween 80. '
                             'Arch. Biochem. Biophys. (2004) 430, 210-217.',
                     'pubmed': 15369820},
               108: {'info': 'Esposito, L.; Bruno, I.; Sica, F.; Raia, C.A.; '
                             'Giordano, A.; Rossi, M.; Mazzarella, L.; Zagari, '
                             'A.: Crystal structure of a ternary complex of '
                             'the alcohol dehydrogenase from Sulfolobus '
                             'solfataricus. Biochemistry (2003) 42, '
                             '14397-14407.',
                     'pubmed': 14661950},
               109: {'info': 'Gibbons, B.J.; Hurley, T.D.: Structure of three '
                             'class I human alcohol dehydrogenases complexed '
                             'with isoenzyme specific formamide inhibitors. '
                             'Biochemistry (2004) 43, 12555-12562.',
                     'pubmed': 15449945},
               110: {'info': 'Stroemberg, P.; Svensson, S.; Berst, K.B.; '
                             'Plapp, B.V.; Höög, J.O.: Enzymatic mechanism of '
                             'low-activity mouse alcohol dehydrogenase 2. '
                             'Biochemistry (2004) 43, 1323-1328.',
                     'pubmed': 14756569},
               111: {'info': 'LeBrun, L.A.; Park, D.H.; Ramaswamy, S.; Plapp, '
                             'B.V.: Participation of histidine-51 in catalysis '
                             'by horse liver alcohol dehydrogenase. '
                             'Biochemistry (2004) 43, 3014-3026.',
                     'pubmed': 15023053},
               112: {'info': 'Ceccarelli, C.; Liang, Z.X.; Strickler, M.; '
                             'Prehna, G.; Goldstein, B.M.; Klinman, J.P.; '
                             'Bahnson, B.J.: Crystal structure and amide H/D '
                             'exchange of binary complexes of alcohol '
                             'dehydrogenase from Bacillus stearothermophilus: '
                             'insight into thermostability and cofactor '
                             'binding. Biochemistry (2004) 43, 5266-5277.',
                     'pubmed': 15122892},
               113: {'info': 'Chinnawirotpisan, P.; Matsushita, K.; Toyama, '
                             'H.; Adachi, O.; Limtong, S.; Theeragool, G.: '
                             'Purification and characterization of two '
                             'NAD-dependent alcohol dehydrogenases (ADHs) '
                             'induced in the quinoprotein ADH-deficient mutant '
                             'of Acetobacter pasteurianus SKU1108. Biosci. '
                             'Biotechnol. Biochem. (2003) 67, 958-965.',
                     'pubmed': 12834271},
               114: {'info': 'Kosjek, B.; Stampfer, W.; Pogorevc, M.; '
                             'Goessler, W.; Faber, K.; Kroutil, W.: '
                             'Purification and characterization of a '
                             'chemotolerant alcohol dehydrogenase applicable '
                             'to coupled redox reactions. Biotechnol. Bioeng. '
                             '(2004) 86, 55-62.',
                     'pubmed': 15007841},
               115: {'info': 'Stroemberg, P.; Svensson, S.; Hedberg, J.J.; '
                             'Nordling, E.; Hoog, J.O.: Identification and '
                             'characterisation of two allelic forms of human '
                             'alcohol dehydrogenase 2. Cell. Mol. Life Sci. '
                             '(2002) 59, 552-559.',
                     'pubmed': 11964133},
               116: {'info': 'Plapp, B.V.; Berst, K.B.: Specificity of human '
                             'alcohol dehydrogenase 1C*2 (gamma2gamma2) for '
                             'steroids and simulation of the uncompetitive '
                             'inhibition of ethanol metabolism. Chem. Biol. '
                             'Interact. (2003) 143-144, 183-193.',
                     'pubmed': 12604203},
               117: {'info': 'Fontaine, F.R.; Dunlop, R.A.; Petersen, D.R.; '
                             'Burcham, P.C.: Oxidative bioactivation of crotyl '
                             'alcohol to the toxic endogenous aldehyde '
                             'crotonaldehyde: association of protein '
                             'carbonylation with toxicity in mouse '
                             'hepatocytes. Chem. Res. Toxicol. (2002) 15, '
                             '1051-1058.',
                     'pubmed': 12184789},
               118: {'info': 'Yoon, S.Y.; Noh, H.S.; Kim, E.H.; Kong, K.H.: '
                             'The highly stable alcohol dehydrogenase of '
                             'Thermomicrobium roseum: purification and '
                             'molecular characterization. Comp. Biochem. '
                             'Physiol. B (2002) 132, 415-422.',
                     'pubmed': 12031468},
               119: {'info': 'Martras, S.; Alvarez, R.; Martinez, S.E.; '
                             'Torres, D.; Gallego, O.; Duester, G.; Farres, '
                             'J.; de Lera, A.R.; Pares, X.: The specificity of '
                             'alcohol dehydrogenase with cis-retinoids. '
                             'Activity with 11-cis-retinol and localization in '
                             'retina. Eur. J. Biochem. (2004) 271, 1660-1670.',
                     'pubmed': 15096205},
               120: {'info': 'Leskovac, V.; Trivic, S.; Pericin, D.: The three '
                             'zinc-containing alcohol dehydrogenases from '
                             "bakers' yeast, Saccharomyces cerevisiae. FEMS "
                             'Yeast Res. (2002) 2, 481-494.',
                     'pubmed': 12702265},
               121: {'info': 'Miroliaei, M.; Nemat-Gorgani, M.: Effect of '
                             'organic solvents on stability and activity of '
                             'two related alcohol dehydrogenases: a '
                             'comparative study. Int. J. Biochem. Cell Biol. '
                             '(2002) 34, 169-175.',
                     'pubmed': 11809419},
               122: {'info': 'Vanni, A.; Anfossi, L.; Pessione, E.; '
                             'Giovannoli, C.: Catalytic and spectroscopic '
                             'characterisation of a copper-substituted alcohol '
                             'dehydrogenase from yeast. Int. J. Biol. '
                             'Macromol. (2002) 30, 41-45.',
                     'pubmed': 11893392},
               123: {'info': 'Espinosa, A.; Clark, D.; Stanley, S.L., Jr.: '
                             'Entamoeba histolytica alcohol dehydrogenase 2 '
                             '(EhADH2) as a target for anti-amoebic agents. J. '
                             'Antimicrob. Chemother. (2004) 54, 56-59.',
                     'pubmed': 15150165},
               124: {'info': 'Chou, C.F.; Lai, C.L.; Chang, Y.C.; Duester, G.; '
                             'Yin, S.J.: Kinetic mechanism of human class IV '
                             'alcohol dehydrogenase functioning as retinol '
                             'dehydrogenase. J. Biol. Chem. (2002) 277, '
                             '25209-25216.',
                     'pubmed': 11997393},
               125: {'info': 'Rosell, A.; Valencia, E.; Ochoa, W.F.; Fita, I.; '
                             'Pares, X.; Farres, J.: Complete reversal of '
                             'coenzyme specificity by concerted mutation of '
                             'three consecutive residues in alcohol '
                             'dehydrogenase. J. Biol. Chem. (2003) 278, '
                             '40573-40580.',
                     'pubmed': 12902331},
               126: {'info': 'Shim, E.J.; Jeon, S.H.; Kong, K.H.: '
                             'Overexpression, purification, and biochemical '
                             'characterization of the thermostable '
                             'NAD-dependent alcohol dehydrogenase from '
                             'Bacillus stearothermophilus. J. Microbiol. '
                             'Biotechnol. (2003) 13, 738-744.'},
               127: {'info': 'Guy, J.E.; Isupov, M.N.; Littlechild, J.A.: The '
                             'structure of an alcohol dehydrogenase from the '
                             'hyperthermophilic archaeon Aeropyrum pernix. J. '
                             'Mol. Biol. (2003) 331, 1041-1051.',
                     'pubmed': 12927540},
               128: {'info': 'Avila, E.E.; Martinez-Alcaraz, E.R.; '
                             'Barbosa-Sabanero, G.; Rivera-Baron, E.I.; '
                             'Arias-Negrete, S.; Zazueta-Sandoval, R.: '
                             'Subcellular localization of the NAD+-dependent '
                             'alcohol dehydrogenase in Entamoeba histolytica '
                             'trophozoites. J. Parasitol. (2002) 88, 217-222.',
                     'pubmed': 12058720},
               129: {'info': 'Levin, I.; Meiri, G.; Peretz, M.; Burstein, Y.; '
                             'Frolow, F.: The ternary complex of Pseudomonas '
                             'aeruginosa alcohol dehydrogenase with NADH and '
                             'ethylene glycol. Protein Sci. (2004) 13, '
                             '1547-1556.',
                     'pubmed': 15152088},
               130: {'info': 'Koumanov, A.; Benach, J.; Atrian, S.; '
                             'Gonzalez-Duarte, R.; Karshikoff, A.; Ladenstein, '
                             'R.: The catalytic mechanism of Drosophila '
                             'alcohol dehydrogenase: evidence for a proton '
                             'relay modulated by the coupled ionization of the '
                             'active site lysine/tyrosine pair and a NAD+ '
                             'ribose OH switch. Proteins (2003) 51, 289-298.',
                     'pubmed': 12660997},
               131: {'info': 'Kragl, U.; Kruse, W.; Hummel, W.; Wandrey, C.: '
                             'Enzyme engineering aspects of biocatalysis: '
                             'Cofactor regeneration as example. Biotechnol. '
                             'Bioeng. (1996) 52, 309-319.',
                     'pubmed': 18629898},
               132: {'info': 'Vicenzi, J.T.; Zmijewski, M.J.; Reinhard, M.R.; '
                             'Landen, B.E.; Muth, W.L.; Marler, P.G.: '
                             'Large-scale stereoselective enzymatic ketone '
                             'reduction with in-situ product removal via '
                             'polymeric adsorbent resins. Enzyme Microb. '
                             'Technol. (1997) 20, 494-499.'},
               133: {'info': 'Sit, S.Y.; Parker, R.A.; Motoc, I.; Han, W.; '
                             'Balasubramanian, N.: Synthesis, biological '
                             'profile, and quantitative structure-activity '
                             'relationship of a series of novel '
                             '3-hydroxy-3-methylglutaryl coenzyme A reductase '
                             'inhibitors. J. Med. Chem. (1990) 33, 2982-2999.',
                     'pubmed': 2231596},
               134: {'info': 'Blacklock, T.J.; Sohar, P.; Butcher, J.W.; '
                             'Lamanec, T.; Grabowski, E.J.J.: An '
                             'enantioselective synthesis of the '
                             'topically-active carbonic anhydrase inhibitor '
                             'MK-0507:5,6-dihydro-(s)-4-(ethylamino)-(s)-6-mehtyl-4H-thieno[2 '
                             '3-beta]thiopyran-2-sulfonamide 7,7-dioxide '
                             'hydrochloride. J. Org. Chem. (1993) 58, '
                             '1672-1679.'},
               135: {'info': 'Nosova, T.; Jousimies-Somer, H.; Kaihovaara, P.; '
                             'Jokelainen, K.; Heine, R.; Salaspuro, M.: '
                             'Characteristics of alcohol dehydrogenases of '
                             'certain aerobic bacteria representing human '
                             'colonic flora. Alcohol. Clin. Exp. Res. (1997) '
                             '21, 489-494.',
                     'pubmed': 9161610},
               136: {'info': 'Duron-Castellanos, A.; Zazueta-Novoa, V.; '
                             'Silva-Jimenez, H.; Alvarado-Caudillo, Y.; Pena '
                             'Cabrera, E.; Zazueta-Sandoval, R.: Detection of '
                             'NAD+dependent alcohol dehydrogenase activities '
                             'in YR-1 strain of Mucor circinelloides, a '
                             'potential bioremediator of petroleum '
                             'contaminated soils. Appl. Biochem. Biotechnol. '
                             '(2005) 121-124, 279-288.',
                     'pubmed': 15917606},
               137: {'info': 'Inoue, K.; Makino, Y.; Itoh, N.: Purification '
                             'and characterization of a novel alcohol '
                             'dehydrogenase from Leifsonia sp. strain S749: a '
                             'promising biocatalyst for an asymmetric hydrogen '
                             'transfer bioreduction. Appl. Environ. Microbiol. '
                             '(2005) 71, 3633-3641.',
                     'pubmed': 16000771},
               138: {'info': 'Machielsen, R.; Uria, A.R.; Kengen, S.W.; van '
                             'der Oost, J.: Production and characterization of '
                             'a thermostable alcohol dehydrogenase that '
                             'belongs to the aldo-keto reductase uperfamily. '
                             'Appl. Environ. Microbiol. (2006) 72, 233-238.',
                     'pubmed': 16391048},
               139: {'info': 'Park, H.; Kidman, G.; Northrop, D.B.: Effects of '
                             'pressure on deuterium isotope effects of yeast '
                             'alcohol dehydrogenase using alternative '
                             'substrates. Arch. Biochem. Biophys. (2005) 433, '
                             '335-340.',
                     'pubmed': 15581588},
               140: {'info': 'Kalnenieks, U.; Galinina, N.; Toma, M.M.: '
                             'Physiological regulation of the properties of '
                             'alcohol dehydrogenase II (ADH II) of Zymomonas '
                             'mobilis: NADH renders ADH II resistant to '
                             'cyanide and aeration. Arch. Microbiol. (2005) '
                             '183, 450-455.',
                     'pubmed': 16027951},
               141: {'info': 'Haseba, T.; Duester, G.; Shimizu, A.; Yamamoto, '
                             'I.; Kameyama, K.; Ohno, Y.: In vivo contribution '
                             'of class III alcohol dehydrogenase (ADH3) to '
                             'alcohol metabolism through activation by '
                             'cytoplasmic solution hydrophobicity. Biochim. '
                             'Biophys. Acta (2006) 1762, 276-283.',
                     'pubmed': 16431092},
               143: {'info': 'Negoro, M.; Wakabayashi, I.: Enhancement of '
                             'alcohol dehydrogenase activity in vitro by '
                             'acetylsalicylic acid. Eur. J. Pharmacol. (2005) '
                             '523, 25-28.',
                     'pubmed': 16226743},
               144: {'info': 'Kazuoka, T.; Oikawa, T.; Muraoka, I.; Kuroda, '
                             'S.; Soda, K.: A cold-active and thermostable '
                             'alcohol dehydrogenase of a psychrotorelant from '
                             'Antarctic seawater, Flavobacterium frigidimaris '
                             'KUC-1. Extremophiles (2007) 11, 257-267.',
                     'pubmed': 17072683},
               146: {'info': 'Defilippi, B.G.; Dandekar, A.M.; Kader, A.A.: '
                             'Relationship of ethylene biosynthesis to '
                             'volatile production, related enzymes, and '
                             'precursor availability in apple peel and flesh '
                             'tissues. J. Agric. Food Chem. (2005) 53, '
                             '3133-3141.',
                     'pubmed': 15826070},
               147: {'info': 'Koutsompogeras, P.; Kyriacou, A.; Zabetakis, I.: '
                             'Characterizing NAD-dependent alcohol '
                             'dehydrogenase enzymes of Methylobacterium '
                             'extorquens and strawberry (Fragaria x ananassa '
                             'cv. Elsanta). J. Agric. Food Chem. (2006) 54, '
                             '235-242.',
                     'pubmed': 16390205},
               148: {'info': 'Ikegaya, K.: Kinetic analysis about the effects '
                             'of neutral salts on the thermal stability of '
                             'yeast alcohol dehydrogenase. J. Biochem. (2005) '
                             '137, 349-354.',
                     'pubmed': 15809336},
               149: {'info': 'Hirano, J.; Miyamoto, K.; Ohta, H.: Purification '
                             'and characterization of the alcohol '
                             'dehydrogenase with a broad substrate specificity '
                             'originated from 2-phenylethanol-assimilating '
                             'Brevibacterium sp. KU 1309. J. Biosci. Bioeng. '
                             '(2005) 100, 318-322.',
                     'pubmed': 16243283},
               150: {'info': 'Jelski, W.; Chrostek, L.; Markiewicz, W.; '
                             'Szmitkowski, M.: Activity of alcohol '
                             'dehydrogenase (ADH) isoenzymes and aldehyde '
                             'dehydrogenase (ALDH) in the sera of patients '
                             'with breast cancer. J. Clin. Lab. Anal. (2006) '
                             '20, 105-108.',
                     'pubmed': 16721836},
               151: {'info': 'Manriquez, D.; El-Sharkawy, I.; Flores, F.B.; '
                             'El-Yahyaoui, F.; Regad, F.; Bouzayen, M.; '
                             'Latche, A.; Pech, J.C.: Two highly divergent '
                             'alcohol dehydrogenases of melon exhibit fruit '
                             'ripening-specific expression and distinct '
                             'biochemical characteristics. Plant Mol. Biol. '
                             '(2006) 61, 675-685.',
                     'pubmed': 16897483},
               152: {'info': 'Sica, F.; Demasi, D.; Mazzarella, D.L.; Zagari, '
                             "A.; Capasso, S.; Pearl, L.H.; D'Auria, S.; Raia, "
                             'C.A.; Rossi, M.: Elimination of twinning in '
                             'crystals of Sulfolobus sofataricus alcohol '
                             'dehydrogenase holo-enzyme by growth in agarose '
                             'gels. Acta Crystallogr. Sect. D (1994) 50, '
                             '508-511.',
                     'pubmed': 15299411},
               153: {'info': 'Raia, C.A.; Caruso, C.; Marino, M.; Vespa, N.; '
                             'Rossi, M.: Activation of Sulfolobus solfataricus '
                             'alcohol dehydrogenase by modification of '
                             'cysteine residue 38 with iodoacetic acid. '
                             'Biochemistry (1996) 35, 638-647.',
                     'pubmed': 8555238},
               154: {'info': 'Giordano, A.; Cannio, R.; La Cara, F.; '
                             'Bartolucci, S.; Rossi, M.; Raia, C.A.: Asn249Tyr '
                             'substitution at the coenzyme binding domain '
                             'activates Sulfolobus solfataricus alcohol '
                             'dehydrogenase and increases its thermal '
                             'stability.. Biochemistry (1999) 38, 3043-3054.',
                     'pubmed': 10074357},
               155: {'info': "Trincone, A.; Lama, L.; Rella, R.; D'Auria, S.; "
                             'Raia, C.A.; Nicolaus, B.: Determination of '
                             'hydride transfer stereospecificity of '
                             'NADH-dependent alcohol-aldehyde/ketone '
                             'oxidoreductase from Sulfolobus solfataricus. '
                             'Biochim. Biophys. Acta (1990) 1041, 94-96.',
                     'pubmed': 2121281},
               156: {'info': 'Tasaki, Y.; Yoshikawa, H.; Tamura, H.: Isolation '
                             'and characterization of an alcohol dehydrogenase '
                             'gene from the octylphenol polyethoxylate '
                             'degrader Pseudomonas putida S-5. Biosci. '
                             'Biotechnol. Biochem. (2006) 70, 1855-1863.',
                     'pubmed': 16926497},
               157: {'info': 'Esposito, L.; Bruno, I.; Sica, F.; Raia, C.A.; '
                             'Giordano, A.; Rossi, M.; Mazzarella, L.; Zagari, '
                             'A.: Structural study of a single-point mutant of '
                             'Sulfolobus solfataricus alcohol dehydrogenase '
                             'with enhanced activity.. FEBS Lett. (2003) 539, '
                             '14-18.',
                     'pubmed': 12650918},
               158: {'info': 'Cannio, R.; Fiorentino, G.; Rossi, M.; '
                             'Bartolucci, S.: The alcohol dehydrogenase gene: '
                             'distribution among Sulfolobales and regulation '
                             'in Sulfolobus solfataricus. FEMS Microbiol. '
                             'Lett. (1999) 170, 31-39.',
                     'pubmed': 9919650},
               159: {'info': 'Cannio, R.; Fiorentino, G.; Carpinelli, P.; '
                             'Rossi, M.; Bartolucci, S.: Cloning and '
                             'overexpression in Escherichia coli of the genes '
                             'encoding NAD-dependent alcohol dehydrogenase '
                             'from two Sulfolobus species. J. Bacteriol. '
                             '(1996) 178, 301-305.',
                     'pubmed': 8550434},
               160: {'info': 'Fiorentino, G.; Cannio, R.; Rossi, M.; '
                             'Bartolucci, S.: Transcriptional regulation of '
                             'the gene encoding an alcohol dehydrogenase in '
                             'the archaeon Sulfolobus solfataricus involves '
                             'multiple factors and control elements. J. '
                             'Bacteriol. (2003) 185, 3926-3934.',
                     'pubmed': 12813087},
               161: {'info': 'Esposito, L.; Sica, F.; Raia, C.A.; Giordano, '
                             'A.; Rossi, M.; Mazzarella, L.; Zagari, A.: '
                             'Crystal structure of the alcohol dehydrogenase '
                             'from the hyperthermophilic archaeon Sulfolobus '
                             'solfataricus at 1.85 A resolution. J. Mol. Biol. '
                             '(2002) 318, 463-477.',
                     'pubmed': 12051852},
               162: {'info': 'Chong, P.K.; Burja, A.M.; Radianingtyas, H.; '
                             'Fazeli, A.; Wright, P.C.: Proteome and '
                             'transcriptional analysis of ethanol-grown '
                             'Sulfolobus solfataricus P2 reveals ADH2, a '
                             'potential alcohol dehydrogenase. J. Proteome '
                             'Res. (2007) 6, 3985-3994.',
                     'pubmed': 17824633},
               163: {'info': 'Raia, C.A.; Giordano, A.; Rossi, M.: Alcohol '
                             'dehydrogenase from Sulfolobus solfataricus. '
                             'Methods Enzymol. (2001) 331, 176-195.',
                     'pubmed': 11265460},
               164: {'info': 'Casadio, R.; Martelli, P.L.; Giordano, A.; '
                             'Rossi, M.; Raia, C.A.: A low-resolution 3D model '
                             'of the tetrameric alcohol dehydrogenase from '
                             'Sulfolobus solfataricus. Protein Eng. (2002) 15, '
                             '215-223.',
                     'pubmed': 11932492},
               165: {'info': 'Ammendola, S.; Raucci, G.; Incani, O.; Mele, A.; '
                             'Tramontano, A.; Wallace, A.: Replacing the '
                             'glutamate ligand in the structural zinc site of '
                             'Sulfolobus solfataricus alcohol dehydrogenase '
                             'with a cysteine decreases thermostability.. '
                             'Protein Eng. (1995) 8, 31-37.',
                     'pubmed': 7770449},
               167: {'info': 'Quintanilla, M.E.; Tampier, L.; Sapag, A.; '
                             'Gerdtzen, Z.; Israel, Y.: Sex differences, '
                             'alcohol dehydrogenase, acetaldehyde burst, and '
                             'aversion to ethanol in the rat: a systems '
                             'perspective. Am. J. Physiol. Endocrinol. Metab. '
                             '(2007) 293, E531-E537.',
                     'pubmed': 17488809},
               169: {'info': 'Pennacchio, A.; Pucci, B.; Secundo, F.; La Cara, '
                             'F.; Rossi, M.; Raia, C.A.: Purification and '
                             'characterization of a novel recombinant highly '
                             'enantioselective short-chain NAD(H)-dependent '
                             'alcohol dehydrogenase from Thermus thermophilus. '
                             'Appl. Environ. Microbiol. (2008) 74, 3949-3958.',
                     'pubmed': 18456852},
               170: {'info': 'Maestre, O.; Garcia-Martinez, T.; Peinado, R.A.; '
                             'Mauricio, J.C.: Effects of ADH2 overexpression '
                             'in Saccharomyces bayanus during alcoholic '
                             'fermentation. Appl. Environ. Microbiol. (2008) '
                             '74, 702-707.',
                     'pubmed': 18065623},
               171: {'info': 'Kotrbova-Kozak, A.; Kotrba, P.; Inui, M.; '
                             'Sajdok, J.; Yukawa, H.: Transcriptionally '
                             'regulated adhA gene encodes alcohol '
                             'dehydrogenase required for ethanol and '
                             'n-propanol utilization in Corynebacterium '
                             'glutamicum R. Appl. Microbiol. Biotechnol. '
                             '(2007) 76, 1347-1356.',
                     'pubmed': 17646983},
               172: {'info': 'Park, Y.C.; San, K.Y.; Bennett, G.N.: '
                             'Characterization of alcohol dehydrogenase 1 and '
                             '3 from Neurospora crassa FGSC2489. Appl. '
                             'Microbiol. Biotechnol. (2007) 76, 349-356.',
                     'pubmed': 17516063},
               173: {'info': 'Hess, M.; Antranikian, G.: Archaeal alcohol '
                             'dehydrogenase active at increased temperatures '
                             'and in the presence of organic solvents. Appl. '
                             'Microbiol. Biotechnol. (2008) 77, 1003-1013.',
                     'pubmed': 17989975},
               174: {'info': 'Crichton, P.G.; Affourtit, C.; Moore, A.L.: '
                             'Identification of a mitochondrial alcohol '
                             'dehydrogenase in Schizosaccharomyces pombe: new '
                             'insights into energy metabolism. Biochem. J. '
                             '(2007) 401, 459-464.',
                     'pubmed': 16999687},
               175: {'info': 'Meijers, R.; Adolph, H.W.; Dauter, Z.; Wilson, '
                             'K.S.; Lamzin, V.S.; Cedergren-Zeppezauer, E.S.: '
                             'Structural evidence for a ligand coordination '
                             'switch in liver alcohol dehydrogenase. '
                             'Biochemistry (2007) 46, 5446-5454.',
                     'pubmed': 17429946},
               176: {'info': 'Zhang, X.; Bruice, T.C.: Temperature-dependent '
                             'structure of the E x S complex of Bacillus '
                             'stearothermophilus alcohol dehydrogenase. '
                             'Biochemistry (2007) 46, 837-843.',
                     'pubmed': 17223705},
               177: {'info': 'Lertwattanasakul, N.; Sootsuwan, K.; Limtong, '
                             'S.; Thanonkeo, P.; Yamada, M.: Comparison of the '
                             'gene expression patterns of alcohol '
                             'dehydrogenase isozymes in the thermotolerant '
                             'yeast Kluyveromyces marxianus and their '
                             'physiological functions. Biosci. Biotechnol. '
                             'Biochem. (2007) 71, 1170-1182.',
                     'pubmed': 17485854},
               178: {'info': 'Barzegar, A.; Moosavi-Movahedi, A.A.; '
                             'Rezaei-Zarchi, S.; Saboury, A.A.; Ganjali, M.R.; '
                             'Norouzi, P.; Hakimelahi, G.H.; Tsai, F.Y.: The '
                             'mechanisms underlying the effect of '
                             'alpha-cyclodextrin on the aggregation and '
                             'stability of alcohol dehydrogenase. Biotechnol. '
                             'Appl. Biochem. (2008) 49, 203-211.',
                     'pubmed': 17685894},
               180: {'info': 'Jelski, W.; Zalewski, B.; Szmitkowski, M.: The '
                             'activity of class I, II, III, and IV alcohol '
                             'dehydrogenase (ADH) isoenzymes and aldehyde '
                             'dehydrogenase (ALDH) in liver cancer. Digest. '
                             'Dis. Sci. (2008) 53, 2550-2555.',
                     'pubmed': 18224440},
               181: {'info': 'Cao, Y.; Liao, L.; Xu, X.W.; Oren, A.; Wang, C.; '
                             'Zhu, X.F.; Wu, M.: Characterization of alcohol '
                             'dehydrogenase from the haloalkaliphilic archaeon '
                             'Natronomonas pharaonis. Extremophiles (2008) 12, '
                             '471-476.',
                     'pubmed': 18189118},
               182: {'info': 'Li, G.Y.; Huang, K.L.; Jiang, Y.R.; Yang, D.L.; '
                             'Ding, P.: Preparation and characterization of '
                             'Saccharomyces cerevisiae alcohol dehydrogenase '
                             'immobilized on magnetic nanoparticles. Int. J. '
                             'Biol. Macromol. (2008) 42, 405-412.',
                     'pubmed': 18456317},
               185: {'info': 'Yamada-Onodera, K.; Fukui, M.; Tani, Y.: '
                             'Purification and characterization of alcohol '
                             'dehydrogenase reducing N-benzyl-3-pyrrolidinone '
                             'from Geotrichum capitatum. J. Biosci. Bioeng. '
                             '(2007) 103, 174-178.',
                     'pubmed': 17368401},
               186: {'info': 'Jelski, W.; Zalewski, B.; Szmitkowski, M.: '
                             'Alcohol dehydrogenase (ADH) isoenzymes and '
                             'aldehyde dehydrogenase (ALDH) activity in the '
                             'sera of patients with liver cancer. J. Clin. '
                             'Lab. Anal. (2008) 22, 204-209.',
                     'pubmed': 18484658},
               188: {'info': 'Kizaki, N.; Yasohara, Y.; Nagashima, N.; '
                             'Hasegawa, J.: Characterization of novel alcohol '
                             'dehydrogenase of Devosia riboflavina involved in '
                             'stereoselective reduction of 3-pyrrolidinone '
                             'derivatives. J. Mol. Catal. B (2008) 51, 73-80.'},
               190: {'info': 'Reverter-Branchat, G.; Cabiscol, E.; Tamarit, '
                             'J.; Sorolla, M.A.; Angeles de la Torre, M.; Ros, '
                             'J.: Chronological and replicative life-span '
                             'extension in Saccharomyces cerevisiae by '
                             'increased dosage of alcohol dehydrogenase 1. '
                             'Microbiology (2007) 153, 3667-3676.',
                     'pubmed': 17975074},
               191: {'info': 'Jelski, W.; Chrostek, L.; Szmitkowski, M.: The '
                             'activity of class I, II, III, and IV of alcohol '
                             'dehydrogenase isoenzymes and aldehyde '
                             'dehydrogenase in pancreatic cancer. Pancreas '
                             '(2007) 35, 142-146.',
                     'pubmed': 17632320},
               193: {'info': 'Laadan, B.; Almeida, J.R.; Radstroem, P.; '
                             'Hahn-Haegerdal, B.; Gorwa-Grauslund, M.: '
                             'Identification of an NADH-dependent '
                             '5-hydroxymethylfurfural-reducing alcohol '
                             'dehydrogenase in Saccharomyces cerevisiae. Yeast '
                             '(2008) 25, 191-198.',
                     'pubmed': 18302314},
               194: {'info': 'Jelski, W.; Szmitkowski, M.: Alcohol '
                             'dehydrogenase (ADH) and aldehyde dehydrogenase '
                             '(ALDH) in the cancer diseases. Clin. Chim. Acta '
                             '(2008) 395, 1-5.',
                     'pubmed': 18505683},
               195: {'info': 'Peng, H.; Wu, G.; Shao, W.: The aldehyde/alcohol '
                             'dehydrogenase (AdhE) in relation to the ethanol '
                             'formation in Thermoanaerobacter ethanolicus '
                             'JW200. Anaerobe (2008) 14, 125-127.',
                     'pubmed': 17981479},
               196: {'info': 'Zhao, Q.; Hou, Y.; Gong, G.H.; Yu, M.A.; Jiang, '
                             'L.; Liao, F.: Characterization of alcohol '
                             'dehydrogenase from permeabilized brewers yeast '
                             'cells immobilized on the derived attapulgite '
                             'nanofibers. Appl. Biochem. Biotechnol. (2009) '
                             '160, 2287-2299.',
                     'pubmed': 19578994},
               197: {'info': 'Hoellrigl, V.; Hollmann, F.; Kleeb, A.C.; '
                             'Buehler, K.; Schmid, A.: TADH, the thermostable '
                             'alcohol dehydrogenase from Thermus sp. ATN1: a '
                             'versatile new biocatalyst for organic synthesis. '
                             'Appl. Microbiol. Biotechnol. (2008) 81, 263-273.',
                     'pubmed': 18704396},
               198: {'info': 'Plapp, B.V.: Conformational changes and '
                             'catalysis by alcohol dehydrogenase. Arch. '
                             'Biochem. Biophys. (2010) 493, 3-12.',
                     'pubmed': 19583966},
               199: {'info': 'Markossian, K.A.; Golub, N.V.; Khanova, H.A.; '
                             'Levitsky, D.I.; Poliansky, N.B.; Muranov, K.O.; '
                             'Kurganov, B.I.: Mechanism of thermal aggregation '
                             'of yeast alcohol dehydrogenase I: role of '
                             'intramolecular chaperone. Biochim. Biophys. Acta '
                             '(2008) 1784, 1286-1293.',
                     'pubmed': 18515108},
               200: {'info': 'Staab, C.A.; Hellgren, M.; Hoeoeg, J.O.: Medium- '
                             'and short-chain dehydrogenase/reductase gene and '
                             'protein families: Dual functions of alcohol '
                             'dehydrogenase 3: implications with focus on '
                             'formaldehyde dehydrogenase and '
                             'S-nitrosoglutathione reductase activities. Cell. '
                             'Mol. Life Sci. (2008) 65, 3950-3960.',
                     'pubmed': 19011746},
               201: {'info': 'Bergman, T.; Zhang, K.; Palmberg, C.; Joernvall, '
                             'H.; Auld, D.S.: Zinc binding to peptide analogs '
                             'of the structural zinc site in alcohol '
                             'dehydrogenase: implications for an entatic '
                             'state. Cell. Mol. Life Sci. (2008) 65, '
                             '4019-4027.',
                     'pubmed': 18850316},
               202: {'info': 'Pal, S.; Park, D.H.; Plapp, B.V.: Activity of '
                             'yeast alcohol dehydrogenases on benzyl alcohols '
                             'and benzaldehydes: characterization of ADH1 from '
                             'Saccharomyces carlsbergensis and transition '
                             'state analysis. Chem. Biol. Interact. (2009) '
                             '178, 16-23.',
                     'pubmed': 19022233},
               203: {'info': 'Miyawaki, O.; Ma, G.; Horie, T.; Hibi, A.; '
                             'Ishikawa, T.; Kimura, S.: Thermodynamic, '
                             'kinetic, and operational stabilities of yeast '
                             'alcohol dehydrogenase in sugar and compatible '
                             'osmolyte solutions. Enzyme Microb. Technol. '
                             '(2008) 43, 495-499.'},
               204: {'info': 'Cea, G.; Wilson, L.; Bolivar, J.; Markovits, A.; '
                             'Illanes, A.: Effect of chain length on the '
                             'activity of free and immobilized alcohol '
                             'dehydrogenase towards aliphatic alcohols. Enzyme '
                             'Microb. Technol. (2009) 44, 135-138.'},
               205: {'info': 'Barzegar, A.; Moosavi-Movahedi, A.; Pedersen, '
                             'J.; Miroliaei, M.: Comparative thermostability '
                             'of mesophilic and thermophilic alcohol '
                             'dehydrogenases: Stability-determining roles of '
                             'proline residues and loop conformations. Enzyme '
                             'Microb. Technol. (2009) 45, 73-79.'},
               206: {'info': 'Jelski, W.; Orywal, K.; Panek, B.; Gacko, M.; '
                             'Mroczko, B.; Szmitkowski, M.: The activity of '
                             'class I, II, III and IV of alcohol dehydrogenase '
                             '(ADH) isoenzymes and aldehyde dehydrogenase '
                             '(ALDH) in the wall of abdominal aortic '
                             'aneurysms. Exp. Mol. Pathol. (2009) 87, 59-62.',
                     'pubmed': 19332052},
               207: {'info': 'Pennacchio, A.; Esposito, L.; Zagari, A.; Rossi, '
                             'M.; Raia, C.A.: Role of Tryptophan 95 in '
                             'substrate specificity and structural stability '
                             'of Sulfolobus solfataricus alcohol '
                             'dehydrogenase. Extremophiles (2009) 13, 751-761.',
                     'pubmed': 19588068},
               208: {'info': 'Carvalho, E.; Solferini, V.; Matioli, S.: '
                             'Alcohol dehydrogenase activities and ethanol '
                             'tolerance in Anastrepha (Diptera, Tephritidae) '
                             'fruit-fly species and their hybrids. Genet. Mol. '
                             'Biol. (2009) 32, 177-185.',
                     'pubmed': 21637665},
               209: {'info': 'Devi, P.G.; Chakraborty, P.K.; Dasgupta, D.: '
                             'Inhibition of a Zn(II)-containing enzyme, '
                             'alcohol dehydrogenase, by anticancer '
                             'antibiotics, mithramycin and chromomycin A3. J. '
                             'Biol. Inorg. Chem. (2009) 14, 347-359.',
                     'pubmed': 19034537},
               210: {'info': 'Jeon, Y.J.; Fong, J.C.; Riyanti, E.I.; Neilan, '
                             'B.A.; Rogers, P.L.; Svenson, C.J.: Heterologous '
                             'expression of the alcohol dehydrogenase (adhI) '
                             'gene from Geobacillus thermoglucosidasius strain '
                             'M10EXG. J. Biotechnol. (2008) 135, 127-133.',
                     'pubmed': 18436321},
               211: {'info': 'Palma-Gutierrez, H.; Rodriguez-Zavala, J.; '
                             'Jasso-Chavez, R.; Moreno-Sanchez, R.; Saavedra, '
                             'E.: Gene cloning and biochemical '
                             'characterization of an alcohol dehydrogenase '
                             'from Euglena gracilis. J. Eukaryot. Microbiol. '
                             '(2008) 55, 554-561.',
                     'pubmed': 19120802},
               212: {'info': 'Haseba, T.; Sugimoto, J.; Sato, S.; Abe, Y.; '
                             'Ohno, Y.: Phytophenols in whisky lower blood '
                             'acetaldehyde level by depressing alcohol '
                             'metabolism through inhibition of alcohol '
                             'dehydrogenase 1 (class I) in mice. Metab. Clin. '
                             'Exp. (2008) 57, 1753-1759.',
                     'pubmed': 19013301},
               213: {'info': 'Marino-Marmolejo, E.N.; De Leon-Rodriguez, A.; '
                             'de la Rosa, A.P.; Santos, L.: Heterologous '
                             'expression and characterization of an alcohol '
                             'dehydrogenase from the archeon Thermoplasma '
                             'acidophilum. Mol. Biotechnol. (2009) 42, 61-67.',
                     'pubmed': 19058034},
               214: {'info': 'Kollock, R.; Frank, H.; Seidel, A.; Meinl, W.; '
                             'Glatt, H.: Oxidation of alcohols and reduction '
                             'of aldehydes derived from methyl- and '
                             'dimethylpyrenes by cDNA-expressed human alcohol '
                             'dehydrogenases. Toxicology (2008) 245, 65-75.',
                     'pubmed': 18242813},
               215: {'info': 'Liu, X.; Dong, Y.; Zhang, J.; Zhang, A.; Wang, '
                             'L.; Feng, L.: Two novel metal-independent '
                             'long-chain alkyl alcohol dehydrogenases from '
                             'Geobacillus thermodenitrificans NG80-2. '
                             'Microbiology (2009) 155, 2078-2085.',
                     'pubmed': 19383697},
               217: {'info': 'Yanai, H.; Doi, K.; Ohshima, T.: Sulfolobus '
                             'tokodaii ST0053 produces a novel thermostable, '
                             'NAD-dependent medium-chain alcohol '
                             'dehydrogenase. Appl. Environ. Microbiol. (2009) '
                             '75, 1758-1763.',
                     'pubmed': 19139244},
               218: {'info': 'Pennacchio, A.; Sannino, V.; Sorrentino, G.; '
                             'Rossi, M.; Raia, C.A.; Esposito, L.: Biochemical '
                             'and structural characterization of recombinant '
                             'short-chain NAD(H)-dependent '
                             'dehydrogenase/reductase from Sulfolobus '
                             'acidocaldarius highly enantioselective on diaryl '
                             'diketone benzil. Appl. Microbiol. Biotechnol. '
                             '(2013) 97, 3949-3964.',
                     'pubmed': 22805786},
               219: {'info': 'Pennacchio, A.; Giordano, A.; Pucci, B.; Rossi, '
                             'M.; Raia, C.A.: Biochemical characterization of '
                             'a recombinant short-chain NAD(H)-dependent '
                             'dehydrogenase/reductase from Sulfolobus '
                             'acidocaldarius. Extremophiles (2010) 14, '
                             '193-204.',
                     'pubmed': 20049620},
               220: {'info': 'Giordano, A.; Raia, C.A.: Steady-state '
                             'fluorescence properties of S. solfataricus '
                             'alcohol dehydrogenase and its selenomethionyl '
                             'derivative. J. Fluoresc. (2003) 13, 17-24.'},
               221: {'info': 'Giordano, A.; Russo, C.; Raia, C.A.; Kuznetsova, '
                             'I.M.; Stepanenko, O.V.; Turoverov, K.K.: Highly '
                             'UV-absorbing complex in '
                             'selenomethionine-substituted alcohol '
                             'dehydrogenase from Sulfolobus solfataricus. J. '
                             'Proteome Res. (2004) 3, 613-620.',
                     'pubmed': 15253444},
               222: {'info': 'Suwannarangsee, S.; Kim, S.; Kim, O.C.; Oh, '
                             'D.B.; Seo, J.W.; Kim, C.H.; Rhee, S.K.; Kang, '
                             'H.A.; Chulalaksananukul, W.; Kwon, O.: '
                             'Characterization of alcohol dehydrogenase 3 of '
                             'the thermotolerant methylotrophic yeast '
                             'Hansenula polymorpha. Appl. Microbiol. '
                             'Biotechnol. (2012) 96, 697-709.',
                     'pubmed': 22249723},
               223: {'info': 'Elleuche, S.; Fodor, K.; Klippel, B.; von der '
                             'Heyde, A.; Wilmanns, M.; Antranikian, G.: '
                             'Structural and biochemical characterisation of a '
                             'NAD+-dependent alcohol dehydrogenase from '
                             'Oenococcus oeni as a new model molecule for '
                             'industrial biotechnology applications. Appl. '
                             'Microbiol. Biotechnol. (2013) 97, 8963-8975.',
                     'pubmed': 23385476},
               224: {'info': 'Muralidharan, F.N.; Muralidharan, V.B.: '
                             'Characterization of phytol-phytanate conversion '
                             'activity in rat liver. Biochim. Biophys. Acta '
                             '(1986) 883, 54-62.',
                     'pubmed': 3730426},
               225: {'info': 'Kawano, S.; Yano, M.; Hasegawa, J.; Yasohara, '
                             'Y.: Purification and characterization of an '
                             'NADH-dependent alcohol dehydrogenase from '
                             'Candida maris for the synthesis of optically '
                             'active 1-(pyridyl)ethanol derivatives. Biosci. '
                             'Biotechnol. Biochem. (2011) 75, 1055-1060.',
                     'pubmed': 21670533},
               226: {'info': 'Zhou, S.; Zhang, S.C.; Lai, D.Y.; Zhang, S.L.; '
                             'Chen, Z.M.: Biocatalytic characterization of a '
                             'short-chain alcohol dehydrogenase with broad '
                             'substrate specificity from thermophilic '
                             'Carboxydothermus hydrogenoformans. Biotechnol. '
                             'Lett. (2013) 35, 359-365.',
                     'pubmed': 23160740},
               227: {'info': 'Cederlund, E.; Hedlund, J.; Hjelmqvist, L.; '
                             'Jonsson, A.; Shafqat, J.; Norin, A.; Keung, '
                             'W.M.; Persson, B.; Joernvall, H.: '
                             'Characterization of new medium-chain alcohol '
                             'dehydrogenases adds resolution to duplications '
                             'of the class I/III and the sub-class I genes. '
                             'Chem. Biol. Interact. (2011) 191, 8-13.',
                     'pubmed': 21329683},
               228: {'info': 'Ostberg, L.J.; Stroemberg, P.; Hedberg, J.J.; '
                             'Persson, B.; Hoeoeg, J.O.: Analysis of mammalian '
                             'alcohol dehydrogenase 5 (ADH5): Characterisation '
                             'of rat ADH5 with comparisons to the '
                             'corresponding human variant. Chem. Biol. '
                             'Interact. (2013) 202, 97-103.',
                     'pubmed': 23159888},
               229: {'info': 'Orywal, K.; Jelski, W.; Zdrodowski, M.; '
                             'Szmitkowski, M.: The activity of class I, II, '
                             'III and IV alcohol dehydrogenase isoenzymes and '
                             'aldehyde dehydrogenase in cervical cancer. Clin. '
                             'Biochem. (2011) 44, 1231-1234.',
                     'pubmed': 21784063},
               230: {'info': 'Kube, J.; Brokamp, C.; Machielsen, R.; van der '
                             'Oost, J.; Maerkl, H.: Influence of temperature '
                             'on the production of an archaeal thermoactive '
                             'alcohol dehydrogenase from Pyrococcus furiosus '
                             'with recombinant Escherichia coli. Extremophiles '
                             '(2006) 10, 221-227.',
                     'pubmed': 16463078},
               231: {'info': 'Wang, N.; Shi, H.; Yao, Q.; Zhou, Y.; Kang, L.; '
                             'Chen, H.; Chen, K.: Cloning, expression and '
                             'characterization of alcohol dehydrogenases in '
                             'the silkworm Bombyx mori. Genet. Mol. Biol. '
                             '(2011) 34, 240-243.',
                     'pubmed': 21734824},
               232: {'info': 'Giersberg, M.; Degelmann, A.; Bode, R.; Piontek, '
                             'M.; Kunze, G.: Production of a thermostable '
                             'alcohol dehydrogenase from Rhodococcus ruber in '
                             'three different yeast species using the '
                             'Xplor\x022 transformation/expression platform. '
                             'J. Ind. Microbiol. Biotechnol. (2012) 39, '
                             '1385-1396.',
                     'pubmed': 22584819},
               233: {'info': 'Komatsu, S.; Deschamps, T.; Thibaut, D.; Hiraga, '
                             'S.; Kato, M.; Chiba, M.; Hashiguchi, A.; Tougou, '
                             'M.; Shimamura, S.; Yasue, H.: Characterization '
                             'of a novel flooding stress-responsive alcohol '
                             'dehydrogenase expressed in soybean roots. Plant '
                             'Mol. Biol. (2011) 77, 309-322.',
                     'pubmed': 21811849},
               234: {'info': 'Pennacchio, A.; Rossi, M.; Raia, C.A.: Synthesis '
                             'of cinnamyl alcohol from cinnamaldehyde with '
                             'Bacillus stearothermophilus alcohol '
                             'dehydrogenase as the isolated enzyme and in '
                             'recombinant E. coli cells. Appl. Biochem. '
                             'Biotechnol. (2013) 170, 1482-1490.',
                     'pubmed': 23686507},
               237: {'info': 'Timpson, L.M.; Liliensiek, A.K.; Alsafadi, D.; '
                             'Cassidy, J.; Sharkeym M.A.; Liddell, S.; Allers, '
                             'T.; Paradisi, F.: A comparison of two novel '
                             'alcohol dehydrogenase enzymes (ADH1 and ADH2) '
                             'from the extreme halophile Haloferax volcanii. '
                             'Appl. Microbiol. Biotechnol. (2012) 97, 195-203.',
                     'pubmed': 22526808},
               239: {'info': 'Hirakawa, H.; Kamiya, N.; Kawarabayashi, Y.; '
                             'Nagamune, T.: Properties of an alcohol '
                             'dehydrogenase from the hyperthermophilic '
                             'archaeon Aeropyrum pernix K1. J. Biosci. Bioeng. '
                             '(2004) 97, 202-206.',
                     'pubmed': 16233615},
               241: {'info': 'Extance, J.; Crennell, S.J.; Eley, K.; Cripps, '
                             'R.; Hough, D.W.; Danson, M.J.: Structure of a '
                             'bifunctional alcohol dehydrogenase involved in '
                             'bioethanol generation in Geobacillus '
                             'thermoglucosidasius. Acta Crystallogr. Sect. D '
                             '(2013) 69, 2104-2115.',
                     'pubmed': 24100328},
               243: {'info': 'Wu, X.; Zhang, C.; Orita, I.; Imanaka, T.; '
                             'Fukui, T.; Xing, X.H.: Thermostable alcohol '
                             'dehydrogenase from Thermococcus kodakarensis '
                             'KOD1 for enantioselective bioconversion of '
                             'aromatic secondary alcohols. Appl. Environ. '
                             'Microbiol. (2013) 79, 2209-2217.',
                     'pubmed': 23354700},
               244: {'info': 'Ying, X.; Wang, Y.; Xiong, B.; Wu, T.; Xie, L.; '
                             'Yu, M.; Wang, Z.: Characterization of an '
                             'allylic/benzyl alcohol dehydrogenase from '
                             'Yokenella sp. strain WZY002, an organism '
                             'potentially useful for the synthesis of '
                             'alpha,beta-unsaturated alcohols from allylic '
                             'aldehydes and ketones. Appl. Environ. Microbiol. '
                             '(2014) 80, 2399-2409.',
                     'pubmed': 24509923},
               246: {'info': 'Kirmair, L.; Seiler, D.L.; Skerra, A.: Stability '
                             'engineering of the Geobacillus '
                             'stearothermophilus alcohol dehydrogenase and '
                             'application for the synthesis of a polyamide 12 '
                             'precursor. Appl. Microbiol. Biotechnol. (2015) '
                             '99, 10501-10513.',
                     'pubmed': 26329849},
               248: {'info': 'Baek, A.H.; Jeon, E.Y.; Lee, S.M.; Park, J.B.: '
                             'Expression levels of chaperones influence '
                             'biotransformation activity of recombinant '
                             'Escherichia coli expressing Micrococcus luteus '
                             'alcohol dehydrogenase and Pseudomonas putida '
                             'Baeyer-Villiger monooxygenase. Biotechnol. '
                             'Bioeng. (2015) 112, 889-895.',
                     'pubmed': 25545273},
               251: {'info': 'Grimaldi, J.; Collins, C.H.; Belfort, G.: '
                             'Towards cell-free isobutanol production: '
                             'development of a novel immobilized enzyme '
                             'system. Biotechnol. Prog. (2016) 32, 66-73.',
                     'pubmed': 26560680},
               252: {'info': 'Liang, J.J.; Zhang, M.L.; Ding, M.; Mai, Z.M.; '
                             'Wu, S.X.; Du, Y.; Feng, J.X.: Alcohol '
                             'dehydrogenases from Kluyveromyces marxianus: '
                             'heterologous expression in Escherichia coli and '
                             'biochemical characterization. BMC Biotechnol. '
                             '(2014) 14, 45.',
                     'pubmed': 24885162},
               253: {'info': 'Kannuchamy, S.; Mukund, N.; Saleena, L.M.: '
                             'Genetic engineering of Clostridium thermocellum '
                             'DSM1313 for enhanced ethanol production. BMC '
                             'Biotechnol. (2016) 16, 34.',
                     'pubmed': 27213504},
               254: {'info': 'Kontani, A.; Masuda, M.; Matsumura, H.; '
                             'Nakamura, N.; Yohda, M.; Ohno, H.: A bioanode '
                             'using thermostable alcohol dehydrogenase for an '
                             'ethanol biofuel cell operating at high '
                             'temperatures. Electroanalysis (2014) 26, '
                             '682-686.'},
               256: {'info': 'Guagliardi, A.; Martino, M.; Iaccarino, I.; De '
                             'Rosa, M.; Rossi, M.; Bartolucci, S.: '
                             'Purification and characterization of the alcohol '
                             'dehydrogenase from a novel strain of Bacillus '
                             'stearothermophilus growing at 70°C. Int. J. '
                             'Biochem. Cell Biol. (1996) 28, 239-246.',
                     'pubmed': 8729010},
               257: {'info': 'Meadows, C.W.; Tsang, J.E.; Klinman, J.P.: '
                             'Picosecond-resolved fluorescence studies of '
                             'substrate and cofactor-binding domain mutants in '
                             'a thermophilic alcohol dehydrogenase uncover an '
                             'extended network of communication. J. Am. Chem. '
                             'Soc. (2014) 136, 14821-14833.',
                     'pubmed': 25314615},
               259: {'info': 'Lo, J.; Zheng, T.; Hon, S.; Olson, D.G.; Lynd, '
                             'L.R.: The bifunctional alcohol and aldehyde '
                             'dehydrogenase gene, adhE, is necessary for '
                             'ethanol production in Clostridium thermocellum '
                             'and Thermoanaerobacterium saccharolyticum. J. '
                             'Bacteriol. (2015) 197, 1386-1393.',
                     'pubmed': 25666131},
               260: {'info': 'Nagel, Z.D.; Cun, S.; Klinman, J.P.: '
                             'Identification of a long-range protein network '
                             'that modulates active site dynamics in '
                             'extremophilic alcohol dehydrogenases. J. Biol. '
                             'Chem. (2013) 288, 14087-14097.',
                     'pubmed': 23525111},
               261: {'info': 'Kondo, T.; Tezuka, H.; Ishii, J.; Matsuda, F.; '
                             'Ogino, C.; Kondo, A.: Genetic engineering to '
                             'enhance the Ehrlich pathway and alter carbon '
                             'flux for increased isobutanol production from '
                             'glucose by Saccharomyces cerevisiae. J. '
                             'Biotechnol. (2012) 159, 32-37.',
                     'pubmed': 22342368},
               265: {'info': 'Brown, S.; Guss, A.; Karpinets, T.; Parks, J.; '
                             'Smolin, N.; Yang, S.; Land, M.; Klingeman, D.; '
                             'Bhandiwad, A.; Rodriguez Jr., M.; Raman, B.; '
                             'Shao, X.; Mielenz, J.; Smith, J.; Keller, M.; '
                             'Lynd, L.: Mutant alcohol dehydrogenase leads to '
                             'improved ethanol tolerance in Clostridium '
                             'thermocellum. Proc. Natl. Acad. Sci. USA (2011) '
                             '108, 13752-13757.',
                     'pubmed': 21825121},
               269: {'info': 'Pennacchio, A.; Giordano, A.; Esposito, L.; '
                             'Langella, E.; Rossi, M.; Raia, C.A.: Insight '
                             'into the stereospecificity of short-chain '
                             'thermus thermophilus alcohol dehydrogenase '
                             'showing pro-S hydride transfer and prelog '
                             'enantioselectivity. Protein Pept. Lett. (2010) '
                             '17, 437-443.',
                     'pubmed': 19807673},
               271: {'info': 'Takeda, M.; Anamizu, S.; Motomatsu, S.; Chen, '
                             'X.; Thapa Chhetri, R.: Identification and '
                             'characterization of a mycobacterial '
                             'NAD+-dependent alcohol dehydrogenase with '
                             'superior reduction of diacetyl to (S)-acetoin. '
                             'Biosci. Biotechnol. Biochem. (2014) 78, '
                             '1879-1886.',
                     'pubmed': 25082080},
               272: {'info': 'Hong, S.H.; Ngo, H.P.; Kang, L.W.; Oh, D.K.: '
                             'Characterization of alcohol dehydrogenase from '
                             'Kangiella koreensis and its application to '
                             'production of all-trans-retinol. Biotechnol. '
                             'Lett. (2015) 37, 849-856.',
                     'pubmed': 25481533},
               273: {'info': 'Chi, Y.C.; Lee, S.L.; Lai, C.L.; Lee, Y.P.; Lee, '
                             'S.P.; Chiang, C.P.; Yin, S.J.: Ethanol oxidation '
                             'and the inhibition by drugs in human liver, '
                             'stomach and small intestine: Quantitative '
                             'assessment with numerical organ modeling of '
                             'alcohol dehydrogenase isozymes. Chem. Biol. '
                             'Interact. (2016) 258, 134-141.',
                     'pubmed': 27544634},
               274: {'info': 'Spickermann, D.; Hausmann, S.; Degering, C.; '
                             'Schwaneberg, U.; Leggewie, C.: Engineering of '
                             'highly selective variants of Parvibaculum '
                             'lavamentivorans alcohol dehydrogenase. '
                             'ChemBioChem (2014) 15, 2050-2052.',
                     'pubmed': 25169816},
               275: {'info': 'Malver, O.; Sebastian, M.J.; Oppenheimer, N.J.: '
                             'Alteration in substrate specificity of horse '
                             'liver alcohol dehydrogenase by an acyclic '
                             'nicotinamide analog of NAD(+). DNA Repair (2014) '
                             '23, 95-100.',
                     'pubmed': 25280628},
               277: {'info': 'Moosavi-Movahedi, F.; Saboury, A.A.; Alijanvand, '
                             'H.H.; Bohlooli, M.; Salami, M.; '
                             'Moosavi-Movahedi, A.A.: Thermal inactivation and '
                             'conformational lock studies on horse liver '
                             'alcohol dehydrogenase: structural mechanism. '
                             'Int. J. Biol. Macromol. (2013) 58, 66-72.',
                     'pubmed': 23548863},
               279: {'info': 'Tsuji, K.; Yoon, K.S.; Ogo, S.: Biochemical '
                             'characterization of a bifunctional '
                             'acetaldehyde-alcohol dehydrogenase purified from '
                             'a facultative anaerobic bacterium Citrobacter '
                             'sp. S-77. J. Biosci. Bioeng. (2016) 121, '
                             '253-258.',
                     'pubmed': 26216639},
               281: {'info': 'Keller, M.W.; Lipscomb, G.L.; Nguyen, D.M.; '
                             'Crowley, A.T.; Schut, G.J.; Scott, I.; Kelly, '
                             'R.M.; Adams, M.W.: Ethanol production by the '
                             'hyperthermophilic archaeon Pyrococcus furiosus '
                             'by expression of bacterial bifunctional alcohol '
                             'dehydrogenases. Microb. Biotechnol. (2017) 10, '
                             '1535-1545.',
                     'pubmed': 28194879},
               282: {'info': 'Laadan, B.; Wallace-Salinas, V.; Carlsson, A.J.; '
                             'Almeida, J.R.; Radstroem, P.; Gorwa-Grauslund, '
                             'M.F.: Furaldehyde substrate specificity and '
                             'kinetics of Saccharomyces cerevisiae alcohol '
                             'dehydrogenase 1 variants. Microb. Cell Fact. '
                             '(2014) 13, 112.',
                     'pubmed': 25287956},
               283: {'info': 'Atteia, A.; van Lis, R.; Mendoza-Hernández, G.; '
                             'Henze, K.; Martin, W.; Riveros-Rosas, H.; '
                             'González-Halphen, D.: Bifunctional '
                             'aldehyde/alcohol dehydrogenase (ADHE) in '
                             'chlorophyte algal mitochondria. Plant Mol. Biol. '
                             '(2003) 53, 175-188.',
                     'pubmed': 14756315},
               284: {'info': 'Cheng, F.; Hu, T.; An, Y.; Huang, J.; Xu, Y.: '
                             'Purification and enzymatic characterization of '
                             'alcohol dehydrogenase from Arabidopsis thaliana. '
                             'Protein Expr. Purif. (2013) 90, 74-77.',
                     'pubmed': 23707506},
               285: {'info': 'Wang, H.; Xiao, D.; Zhou, C.; Wang, L.; Wu, L.; '
                             'Lu, Y.; Xiang, Q.; Zhao, K.; Li, X.; Ma, M.: '
                             'YLL056C from Saccharomyces cerevisiae encodes a '
                             'novel protein with aldehyde reductase activity. '
                             'Appl. Microbiol. Biotechnol. (2017) 101, '
                             '4507-4520.',
                     'pubmed': 28265724},
               286: {'info': 'Ashraf, R.; Rashid, N.; Kanai, T.; Imanaka, T.; '
                             'Akhtar, M.:  Pcal_1311, an alcohol dehydrogenase '
                             'homologue from Pyrobaculum calidifontis, '
                             'displays NADH-dependent high aldehyde reductase '
                             'activity. Extremophiles (2017)  FEHLT,  0000 .',
                     'pubmed': 29022135},
               287: {'info': 'Kwak, M.K.; Ku, M.; Kang, S.O.:  NAD+-linked '
                             'alcohol dehydrogenase 1 regulates methylglyoxal '
                             'concentration in Candida albicans. FEBS Lett. '
                             '(2014)  588,  1144-1153 .',
                     'pubmed': 24607541},
               288: {'info': 'Tsuji, K.; Yoon, K.S.; Ogo, S.:  Biochemical '
                             'characterization of a bifunctional '
                             'acetaldehyde-alcohol dehydrogenase purified from '
                             'a facultative anaerobic bacterium Citrobacter '
                             'sp. S-77. J. Biosci. Bioeng. (2016)  121,  '
                             '253-258 .',
                     'pubmed': 26216639},
               289: {'info': 'Abdallah, W.; Solanki, K.; Banta, S.:  Insertion '
                             'of a calcium-responsive beta-roll domain into a '
                             'thermostable alcohol dehydrogenase enables '
                             'tunable control over cofactor selectivity. ACS '
                             'Catal. (2018)  8,  1602-1613 .'},
               290: {'info': 'Campbell, E.; Wheeldon, I.; Banta, S.:  '
                             'Broadening the cofactor specificity of a '
                             'thermostable alcohol dehydrogenase using '
                             'rational protein design introduces novel kinetic '
                             'transient behavior. Biotechnol. Bioeng. (2010)  '
                             '107,  763-774 .',
                     'pubmed': 20632378},
               291: {'info': 'Zhu, D.; Hyatt, B.; Hua, L.:  Enzymatic hydrogen '
                             'transfer reduction of alpha-chloro aromatic '
                             'ketones catalyzed by a hyperthermophilic alcohol '
                             'dehydrogenase. J. Mol. Catal. B (2009)  56, '
                             '272-276 .'},
               292: {'info': 'Beer, B.; Pick, A.; Doering, M.; Lommes, P.; '
                             'Sieber, V.:  Substrate scope of a dehydrogenase '
                             'from Sphingomonas species A1 and its potential '
                             'application in the synthesis of rare sugars and '
                             'sugar derivatives. Microb. Biotechnol. (2018)  '
                             '11,  747-758 .',
                     'pubmed': 29697194},
               293: {'info': 'Solanki, K.; Abdallah, W.; Banta, S.:  '
                             'Engineering the cofactor specificity of an '
                             'alcohol dehydrogenase via single mutations or '
                             "insertions distal to the 2'-phosphate group of "
                             'NADP(H). Protein Eng. Des. Sel. (2017)  30,  '
                             '373-380 .',
                     'pubmed': 28201792},
               294: {'info': 'Zhu, D.; Malik, H.; Hua, L.:  Asymmetric ketone '
                             'reduction by a hyperthermophilic alcohol '
                             'dehydrogenase. The substrate specificity, '
                             'enantioselectivity and tolerance of organic '
                             'solvents. Tetrahedron Asymmetry (2006)  17,  '
                             '3010-3014 .'},
               295: {'info': 'Aquino Neto, S.; Forti, J.; Zucolotto, V.; '
                             'Ciancaglini, P.; de Andrade, A.:  Development of '
                             'nanostructured bioanodes containing dendrimers '
                             'and dehydrogenases enzymes for application in '
                             'ethanol biofuel cells. Biosens. Bioelectron. '
                             '(2011)  26,  2922-2926 .',
                     'pubmed': 21177091}}),
             ('tissues',
              {'BTO_0000133',
               'BTO_0000135',
               'BTO_0000180',
               'BTO_0000286',
               'BTO_0000575',
               'BTO_0000604',
               'BTO_0000608',
               'BTO_0000671',
               'BTO_0000759',
               'BTO_0000763',
               'BTO_0000959',
               'BTO_0000988',
               'BTO_0001175',
               'BTO_0001239',
               'BTO_0001253',
               'BTO_0001307',
               'BTO_0001363',
               'BTO_0001424',
               'BTO_0001613'})])
--------------------------------------------------------------------------------
```

---
&copy; 2019 Matthias König (https://livermetabolism.com)