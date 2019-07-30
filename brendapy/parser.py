"""
Module for parsing the BRENDA ENZYME information from flat file.
The following information is available:

    AC    activating compound
    AP    application
    CF    cofactor
    CL    cloned
    CR    crystallization
    EN    engineering
    EXP    expression
    GI    general information on enzyme
    GS    general stability
    IC50    IC-50 Value
    ID    EC-class
    IN    inhibitors
    KKM    Kcat/KM-Value substrate in {...}
    KI    Ki-value    inhibitor in {...}
    KM    KM-value    substrate in {...}
    LO    localization
    ME    metals/ions
    MW    molecular weight
    NSP    natural substrates/products    reversibilty information in {...}
    OS    oxygen stability
    OSS    organic solvent stability
    PHO    pH-optimum
    PHR    pH-range
    PHS    pH stability
    PI    isoelectric point
    PM    posttranslation modification
    PR    protein
    PU    purification
    RE    reaction catalyzed
    RF    references
    REN    renatured
    RN    accepted name (IUPAC)
    RT    reaction type
    SA    specific activity
    SN    synonyms
    SP    substrates/products    reversibilty information in {...}
    SS    storage stability
    ST    source/tissue
    SU    subunits
    SY    systematic name
    TN    turnover number    substrate in {...}
    TO    temperature optimum
    TR    temperature range
    TS    temperature stability
"""
import os
import re
import logging
from collections import OrderedDict, defaultdict
from pprint import pprint

from brendapy import utils
from brendapy.settings import BRENDA_FILE


class BrendaParser(object):
    """ Parser for BRENDA information.

    The parser reads the BRENDA flat file into the
    parts for the ec numbers. Via the BrendaParser the
    information for the ec numbers can be accesses.
    """

    BRENDA_KEYS = {
        "AC", "AP", "CF", "CL", "CR", "EN", "EXP", "GI", "GS", "IC50",
        "ID", "IN", "KKM", "KI", "KM", "LO", "ME", "MW", "NSP", "OS",
        "OSS", "PHO", "PHR", "PHS", "PI", "PM", "PR", "PU", "RE", "RF",
        "REN", "RN", "RT", "SA", "SN", "SP", "SS", "ST", "SU", "SY", "TN",
        "TO", "TR", "TS"
    }
    PATTERN_RF = re.compile(r"^<(\d+?)> (.+) {Pubmed:\s*(\d*)\s*}")
    PATTERN_ALL = re.compile(r"^#([,\d\s]+?)#(.+)<([,\d\s]+)>")

    def __init__(self, brenda_file=BRENDA_FILE):
        """ Initialize parser and parse BRENDA file.

        :param brenda_file: BRENDA text file
        """
        self.brenda_file = brenda_file
        self.ec_text = BrendaParser.parse_entry_strings(self.brenda_file)
        self.ec_data = OrderedDict()  # only parse on demand

    def keys(self):
        """ Available ec keys.

        Information for these EC numbers is available in the
        parser object.

        :return: list of ec numbers
        """
        return self.ec_text.keys()

    @staticmethod
    def parse_entry_strings(filename):
        """ Reads the string entries from BRENDA file.

        :param filename: BRENDA database download
        :return: dict (ec, brenda_info)
        """
        logging.info(f"`parse_entry_strings` from `{filename}`")
        ec_data = OrderedDict()

        in_entry = False
        data_lines = []

        # read BRENDA file
        with open(filename, 'r') as bf:
            for line in bf.readlines():
                if line.startswith("*") or len(line) == 0:
                    continue

                # start of entry
                if line.startswith("ID\t"):
                    in_entry = True
                    ec = BrendaParser._get_ec_from_line(line)
                    data_lines = [line]
                # in entry
                if in_entry:
                    data_lines.append(line)
                # end of entry
                if in_entry and line.startswith("///"):
                    in_entry = False
                    entry = "".join(data_lines)
                    entry.replace('\xef\xbf\xbd', " ")
                    # store entry
                    ec_data[ec] = entry
                    data_lines = []

        return ec_data

    @utils.timeit
    def parse_info_dicts(self):
        """ Parses all info dicts.

        This takes around ~15s and prepares all proteins.
        """
        d = OrderedDict()
        for ec, ec_string in self.ec_text.items():
            d[ec] = BrendaParser._parse_info_dict(ec, ec_string)
        return d

    @staticmethod
    def _parse_info_dict(ec, ec_str):
        """
        :return:
        """
        results = defaultdict(OrderedDict)

        def store_item(bid, item):
            """ Store parsed item for bid.
            :param bid:
            :param item:
            :return:
            """
            if bid == "ID":
                results[bid] = item
            elif bid in {"RN", "RE", "RT", "SN"}:
                if isinstance(results[bid], OrderedDict):
                    results[bid] = {item}
                else:
                    results[bid].add(item)
            elif bid == "RF":
                match = BrendaParser.PATTERN_RF.match(item)
                if match:
                    rid, info, pubmed = match.group(1), match.group(2), match.group(3)
                    rid = int(rid)  # integer keys for all references
                    results[bid][rid] = {
                        # 'id': rid,
                        'info': info,
                        'pubmed': pubmed,
                    }
                else:
                    logging.error(f"{ec}_{bid}: could not be parsed: `{item}`")
            else:
                match = BrendaParser.PATTERN_ALL.match(item)
                if match:
                    ids, data, refs = match.group(1), match.group(2), match.group(3)
                    ids = ids.replace(' ', ",")  # fix the missing comma in ids
                    refs = ids.replace(' ', ",")  # fix the missing comma in refs
                    ids = [int(token) for token in ids.split(',')]
                    # get rid of brackets
                    info = {
                        'data': data.split('(')[0].strip(),
                        'refs': [int(token) for token in refs.split(',')]
                    }
                    if info['data'] in ['more', 'more = ?', '-999 {more}', '-999']:
                        logging.info(f"{ec}_{bid}: `more` information not stored: {info}")
                        return
                    if len(info['data']) == 0:
                        logging.info(f"{ec}_{bid}: `empty` information not stored: {info}")
                        return

                    for pid in ids:
                        if bid == "PR":
                            results[bid][pid] = info
                        else:
                            if pid in results[bid]:
                                results[bid][pid].append(info)
                            else:
                                results[bid][pid] = [info]
                else:
                    if bid == "SY" and item[0] != '#':
                        logging.info(f"{ec}_{bid}: generic synonyms are not stored: {item}")
                    else:
                        logging.error(f"{ec}_{bid}: could not be parsed: `{item}`")

        def parse_bid_item(line):
            tokens = line.split("\t")
            bid = tokens[0].strip()
            item = "\t".join(tokens[1:])
            return bid, item

        # parse entries from line
        lines = ec_str.split("\n")
        in_item = False

        for line in lines:
            if not in_item:
                if len(line) > 0 and not line.startswith("\t"):
                    bid, item = parse_bid_item(line)
                    if bid in BrendaParser.BRENDA_KEYS:
                        in_item = True
                    else:
                        in_item = False
                        item = None

            elif in_item:
                # entries longer than one line
                if line.startswith("\t"):
                    item += " " + line.strip()

                # write entries if next entry begins
                elif len(line) > 0 and not line.startswith("\t"):
                    # store old entry
                    store_item(bid, item)
                    in_item = False

                    # create new entry
                    bid, item = parse_bid_item(line)
                    if bid in BrendaParser.BRENDA_KEYS:
                        in_item = True
                    else:
                        logging.error(f"{ec}_{bid}: BRENDA key not supported in line: `{line}`")
                        item = None

                # write last entry
                elif len(line) == 0:
                    store_item(bid, item)
                    in_item = False

        return results

    @staticmethod
    def _get_ec_from_line(line):
        ec = line.strip().split("\t")[1].strip()
        ec = ec.split(" ")[0]
        if utils.is_ec_number(ec):
            return ec
        else:
            return None

    def get_proteins(self, ec):
        """ Parses all BRENDA proteins for given EC number.

        :param ec:
        :return: OrderedDict of BRENDA proteins
        """
        # process text data for ec if not already existing
        if ec not in self.ec_data:
            self.ec_data[ec] = BrendaParser._parse_info_dict(ec, ec_str=self.ec_text[ec])

        ec_data = self.ec_data[ec]
        proteins = {}
        for key in ec_data['PR'].keys():
            proteins[key] = BrendaProtein(ec=ec, key=key, data=ec_data)
        return proteins


class BrendaProtein(object):
    """ Stores all BRENDA information for a given EC number.

    Parsed protein information from the BRENDA database.

    For every ec number one or more (in most cases multiple) protein entries
    exist. The information for one protein entry is stored in
    a BRENDAProtein() object.

    One BRENDA entry consists of multiple protein entries.
    One protein entry is specific for one organism and
    corresponds to one information in the BRENDA database
    """
    ids = ["PR", "RE", "ST", "LO", "NSP", "SP",
           "TN", "KM", "SA", "CF", "IN", "KI", "ME", "RF"]
    names = [
        "Protein", "Reaction", "Source Tissue", "Localization",
        "Natural Substrate Product",
        "Substrate Product", "Turnover number", "Km",
        "Specific activity", "Cofactors",
        "Inhibitors", "Ki", "Metal ions", "References"
    ]

    def __init__(self, ec, key, data):
        """ Protein object is initialized with ec number 'ec',

        id (number of entry for ec in Brenda) and ec_string which contains the
        data for the protein.
        """
        self.data = OrderedDict([
            ('protein_id', key),
            ('ec', ec),
            ('organism', data['PR'][key]['data']),
        ])
        reference_ids = set(data['PR'][key]['refs'])
        for bid in [
            "AC", "AP", "CF", "CL", "CR", "EN", "EXP", "GI", "GS", "IC50",
            "ID", "IN", "KKM", "KI", "KM", "LO", "ME", "MW", "NSP", "OS",
            "OSS", "PHO", "PHR", "PHS", "PI", "PM", "PR", "PU", "RE", "RF",
            "REN", "RN", "RT", "SA", "SN", "SP", "SS", "ST", "SU", "SY", "TN",
            "TO", "TR", "TS"
        ]:
            if bid in ["ID", "PR", "RN", "RE", "RT", "SN", "RF"]:
                continue
            info = data[bid].get(key, None)
            if info:
                # print(bid, info)
                self.data[bid] = info
                for item in info:
                    reference_ids.update(item['refs'])

        # FIXME: some mentioned references are missing
        self.data['references'] = {ref_id: data['RF'].get(ref_id, None) for ref_id in reference_ids}

    @property
    def protein_id(self):
        return self.data['protein_id']

    @property
    def ec(self):
        return self.data['ec']

    @property
    def organism(self):
        return self.data['organism']

    @property
    def source_tissues(self):
        return [item['data'] for item in self.data["ST"]]

    @property
    def kms(self):
        return [item['data'] for item in self.data["KM"]]

    @property
    def kis(self):
        return [item['data'] for item in self.data["KM"]]

    @property
    def references(self):
        return self.data['references']

    def __str__(self):
        """String representation. """
        from pprint import pformat
        return pformat(self.data)
