""" 
Module for parsing the BRENDA ENZYME information from flat file
"""
import os
import re
from collections import OrderedDict
from brendapy import utils
from pprint import pprint


class BRENDAparser(object):
	""" Parser for BRENDA information."""

	def __init__(self, brenda_file):
		""" Initialize the parser.
		Parses the BRENDA file

		:param brenda_file: BRENDA text file
		"""
		self.brenda_file = brenda_file
		self.ec_text = BRENDAparser.parse_entry_strings(self.brenda_file)
		# self.ec_proteins = self.parse_proteins()

	@classmethod
	def parse_entry_strings(cls, filename):
		""" Reads the string entries from given BRENDA file.

		:param filename: BRENDA file
		:return: dict (ec, brenda_info)
		"""
		ec_data = OrderedDict()
		start = "ID\t"
		end = "///"
		in_entry = False
		data_lines = []

		with open(filename, 'r') as bf:
			for line in bf.readlines():
				# start of entry
				if line.startswith(start):
					in_entry = True
					ec = BRENDAparser._get_ec_from_line(line)
					data_lines = [line]
					# print(ec)
				# in entry
				if in_entry:
					data_lines.append(line)
				# end of entry
				if in_entry and line.startswith(end):
					in_entry = False
					entry = "".join(data_lines)
					entry.replace('\xef\xbf\xbd', " ")
					ec_data[ec] = entry

		return ec_data

	@property
	def keys(self):
		""" Available ec keys.
		:return:
		"""
		return self.ec_text.keys()

	@staticmethod
	def _get_ec_from_line(line):
		ec = line.strip().split("\t")[1].strip()
		ec = ec.split(" ")[0]
		if utils.is_ec_number(ec):
			return ec
		else:
			return None

	# ------------------------------
	# Parse information from entry
	# ------------------------------
	@staticmethod
	def parse_info(bid, ec_info):
		""" Get information from ec_str for given BRENDA id (bids are listed below).
		Reads 'info' from BRENDA string for ec and returns list of entries associated with
		Brenda entry identifier. 'ID' is an two character identifier in the Brenda file.
			PR: Protein
			RN: Recommended name
			SN: Systematic name
			SY: Synonyms
			CR: CAS Registry number
			RE: Reaction
			RT: Reaction Type
			ST: Source Tissue
			LO: Localization
			NSP: Natural Substrate Product
			SP: Substrate Product
			TN: Turnover number
			KM: Km value
			PHO: ph optimum
			PHR: ph range
			SA: specific activity
			TO: temperature optimum
			CF: cofactor
			IN: inhibitors
			KI: Ki values
			ME: Metal ions
			MW: Molecular weight
			SU: Subunits
			AP: application
			EN: engineering
			CL: cloned
			CR: crystallization
			PU: purification
			GS: general stability
			PHS: ph stability
			SS: storage stability
			TS: temperature stability
			RF: reference
		"""
		def starts_with_string(line, string):
			start = [string + "\t", string + " "]
			for item in start:
				if line.startswith(item):
					return True
			return False

		results = []
		lines = ec_info.split("\n")
		in_item = False
		L = len(bid)

		for line in lines:
			# read first entry
			if not in_item and starts_with_string(line, bid):
				item = line[L+1:]
				in_item = True

			elif in_item is True:
				# entries longer than one line
				if starts_with_string(line, ''):
					item += " " + line.strip()

				# write entries if next entry begins
				elif starts_with_string(line, bid):
					results.append(item)

					item = line[L+1:]
				# write last entry
				elif len(line) == 0:
					results.append(item)
					break

		return [item.replace('\t', ' ') for item in results]

	@staticmethod
	def is_id_in_entry(id, entry):
		""" Returns True if ID is in Entry, False otherwise.

		ID list always starts with '#' and ends with '#'
		Entries are separated by comma.
		Solution with regular expressions searching for
		#3# and #3,4,5,6# patterns
		"""
		pattern = r"#[\d,]+#"
		items = re.findall(pattern, entry)
		ids = []
		for item in items:
			ids.extend([id for id in item[1:-1].split(",") if id != '' and id.isdigit()])
		# Is ID in IDlist ?
		ids = [int(id) for id in ids]
		return id in ids

	@staticmethod
	def get_entry_with_id(id, entry_list):
		""" Returns an entry list of the entries in which the id is found
			Information for proteins can be collected.
			Use the filterfunction: isIDinEntry(ID)
		"""
		return [entry for entry in entry_list if BRENDAparser.is_id_in_entry(id, entry)]

	def parse_all_proteins(self):
		proteins_all = {}
		for ec in self.ec_text.keys():
			proteins_all[ec] = self.parse_proteins(ec)
		return proteins_all

	def parse_proteins(self, ec):
		ec_str = self.ec_text[ec]
		entries = self.parse_info("PR", ec_str)

		# get the protein ids from the proteins
		protein_keys = set()
		for entry in entries:
			tokens = entry.split("#")
			protein_keys.add(int(tokens[1]))

		proteins = {}
		for key in protein_keys:
			proteins[key] = BRENDAProtein(ec, key, ec_str)
		return proteins


class BRENDAProtein(object):
	""" Stores all BRENDA information for a given EC number.

	Parsed protein information from the BRENDA database.

	For every ec number one or more (in most cases multiple) protein entries
	exist. The information for one protein entry is stored in
	a BRENDAProtein() object.

	One BRENDA entry consists of multiple protein entries.
	One protein entry is specific for one organism and
	corresponds to one information in the BRENDA database
	"""
	ids = ["PR", "RE", "ST", "LO", "NSP", "SP", "TN", "KM", "SA", "CF", "IN", "KI", "ME", "RF"]
	names = [
		"Protein", "Reaction", "Source Tissue", "Localization", "Natural Substrate Product",
		"Substrate Product", "Turnover number", "Km", "Specific activity", "Cofactors",
		"Inhibitors", "Ki", "Metal ions", "References"
	]

	def __init__(self, ec, id, ec_string):
		""" Protein object is initialized with ec number 'ec',

		id (number of entry for ec in Brenda) and ec_string which contains the
		data for the protein.
		"""
		self.ec = ec
		self.id = id
		self.ec_string = ec_string
		self.organism = self.get_organism()
		self.gene = self.get_swissprot_gene()
		self.references = self.get_references()
		self.reaction = self.get_reaction()
		self.source_tissue = self.get_source_tissue()
		self.localisation = self.get_localication()
		self.natural_substrate_product = self.get_natural_substrate_product()
		self.substrate_product = self.get_substrate_product()
		self.turnover_number = self.get_turnover_number()
		self.km = self.getKm()
		self.specific_activity = self.getSpecificActivity()
		self.cofactors = self.getCofactors()
		self.inhibitors = self.getInhibitors()
		self.ki = self.getKi()
		self.metal_ions = self.getMetalIons()
		self.pubmed = self.getPubMedReferences()

	def get_organism(self):
		""" Sets organism information from protein """
		pr_entries = BRENDAparser.parse_info("PR", self.ec_string)

		# Get Entries for id
		#print(f"*** id={self.id} ***")
		# print(pr_entries)
		entry = BRENDAparser.get_entry_with_id(self.id, pr_entries)
		items = entry[0].split(" ")
		if len(items[2]) > 0 and items[2][0] != "Q":
			organism = items[1] + " " + items[2]
		else:
			organism = items[1]
		return organism

	def get_swissprot_gene(self):
		""" Sets gene information for protein """
		pr_entries = BRENDAparser.parse_info("PR", self.ec_string)
		# Get Entries for id
		entry = BRENDAparser.get_entry_with_id(self.id, pr_entries)
		items = entry[0].split(" ")
		gene = [items[-3], items[-2]]
		return gene

	def get_references(self):
		""" Sets references for protein """
		pr_entries = BRENDAparser.parse_info("PR", self.ec_string)
		# Get Entries for id
		entry = BRENDAparser.get_entry_with_id(self.id, pr_entries)
		items = entry[0].split(" ")
		references = items[-1].replace("<", "").replace(">", "").split(",")
		return references

	def get_reaction(self):
		""" Sets reaction for protein

		FIXME: What is this ? Still necessary ?
		"""
		pass

	def get_source_tissue(self):
		""" Sets source tissue for protein """
		st_entries = BRENDAparser.parse_info("ST", self.ec_string)

		entries = BRENDAparser.get_entry_with_id(self.id, st_entries)
		tissues = []

		def get_tissue(entry):
			pattern = r"#.*?# .*? \("
			tmp = re.findall(pattern, entry)
			print(tmp)
			if not tmp:
				pattern = r"#.*# .* <"
				tmp = re.findall(pattern, entry)
			tmp = tmp[0].split("#")
			tissue = tmp[-1][:-1].strip()
			return tissue

		for entry in entries:
			print(entry)
			tissues.append(get_tissue(entry))
		return tissues

	def get_localication(self):
		""" Sets localisation for protein """
		lo_entries = BRENDAparser.parse_info("LO", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, lo_entries)
		localisation = []

		def get_loc(entry):
			pattern = r"^#.*# .* <"
			tmp = re.findall(pattern, entry)
			if not tmp:
				pattern = r"^#.*# .* ("
				tmp = re.findall(pattern, entry)
			tmp = tmp[0].split("#")
			loc = tmp[2][:-1].strip()
			return loc

		for entry in entries:
			localisation.append(get_loc(entry))
		return localisation

	def get_natural_substrate_product(self):
		""" Sets natural substrate, product for protein """
		nsp_entries = BRENDAparser.parse_info("NSP", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, nsp_entries)
		nsp = []

		def get_reaction(entry):
			""" Gets the natural reaction equation """
			pattern = r"#.*# .* \("
			tmp = re.findall(pattern, entry)
			if not tmp:
				pattern = r"#.*# .* <"
				tmp = re.findall(pattern, entry)
			if not tmp:
				tmp = re.findall(r"#.*# .*", entry)
			tmp = tmp[0].split("#")
			reaction = tmp[-1][:-1].strip()
			return reaction

		def get_info(entry):
			""" Gets additional information """
			pattern = r"\(.*\)"
			tmp = re.findall(pattern, entry)
			if tmp:
				info = tmp[0][1:-1]
			else:
				info = ''
			if not BRENDAparser.is_id_in_entry(self.id, info):
				info = ''
			return info

		for entry in entries:
			nsp.append(
				[get_reaction(entry), get_info(entry)]
			)
		return nsp

	def get_substrate_product(self):
		""" Sets substrate, product for protein

		Additional substrate, product information
		TODO: not implemented (information not very important)
		"""
		sp_entries = BRENDAparser.parse_info("SP", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, sp_entries)

		return []

	def get_turnover_number(self):
		""" Sets the turnover numbers for the proteins """
		tn_entries = BRENDAparser.parse_info("TN", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, tn_entries)
		tn = []

		def getTN(entry):
			""" gets the turnover value """
			pattern = r"#.*# \d*.\d*.* {"
			tmp = re.findall(pattern, entry)
			tmp = tmp[0].split("#")
			tn = tmp[-1][:-1].strip()
			return tn

		def getSubstrate(entry):
			""" gets the coresponding value """
			pattern = r"{.*}"
			tmp = re.findall(pattern, entry)
			substrate = tmp[0][1:-1]
			return substrate

		def getAddInfo(entry):
			""" gets addtional information for the tn value """
			info = ''
			pattern = r"\(.*\)"
			tmp = re.findall(pattern, entry)
			if tmp:
				info = tmp[0][1:-1].replace("\xb0", "")
			if not BRENDAparser.is_id_in_entry(self.id, info):
				info = ''
			else:
				info = re.sub("#.*#", "", info).strip()
			return info

		# Get the information from the entries
		for entry in entries:
			tn.append([getTN(entry), getSubstrate(entry), getAddInfo(entry)])
		return tn

	def getKm(self):
		""" Sets the Km values of the proteins """
		km_entries = BRENDAparser.parse_info("KM", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, km_entries)
		# print entries
		km = []

		def getKM(entry):
			""" gets the turnover value """
			pattern = r"#.*# \d*.\d*.* {"
			tmp = re.findall(pattern, entry)
			tmp = tmp[0].split("#")
			km = tmp[-1][:-1].strip()
			return km

		def getSubstrate(entry):
			""" gets the coresponding value """
			pattern = r"{.*}"
			tmp = re.findall(pattern, entry)
			substrate = tmp[0][1:-1]
			return substrate

		def getAddInfo(entry):
			""" gets addtional information for the tn value """
			info = ''
			pattern = r"\(.*\)"
			tmp = re.findall(pattern, entry)
			if tmp:
				info = tmp[0][1:-1].replace("\xb0", "")
			if not BRENDAparser.is_id_in_entry(self.id, info):
				info = ''
			else:
				info = re.sub("#.*#", "", info).strip()
			return info

		for entry in entries:
			km.append([getKM(entry), getSubstrate(entry), getAddInfo(entry)])
		# print km[-1]
		return km

	def getSpecificActivity(self):
		""" Sets the specific activity of the proteins """
		km_entries = BRENDAparser.parse_info("SA", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, km_entries)
		# print entries
		sa = []

		def getSA(entry):
			""" gets value of specific activity """
			pattern = r"#.*# \d*.\d*.* \("
			tmp = re.findall(pattern, entry)
			if not tmp:
				tmp = re.findall(r"#.*# \d*.\d*.* <", entry)
			if not tmp:
				tmp = re.findall(r"#.*# -\d*.\d*.* \(", entry)
			if not tmp:
				tmp = re.findall(r"#.*# -\d*.\d*.* <", entry)
			tmp = tmp[0].split("#")
			sa = tmp[-1][:-1].strip()
			return sa

		def getAddInfo(entry):
			""" gets additional information for the sa value """
			info = ''
			pattern = r"\(.*\)"
			tmp = re.findall(pattern, entry)
			if tmp:
				info = tmp[0][1:-1]
			if not BRENDAparser.is_id_in_entry(self.id, info):
				info = ''
			else:
				info = re.sub("#.*#", "", info).strip()
			return info

		for entry in entries:
			sa.append([getSA(entry), getAddInfo(entry)])
		# print sa[-1]
		return sa

	def getCofactors(self):
		""" Sets the cofactors of the proteins """
		co_entries = BRENDAparser.parse_info("CF", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, co_entries)
		# print entries
		co = []

		def getCF(entry):
			""" Gets the cofactor from entry. """
			pattern = r"#.*# .* \("
			tmp = re.findall(pattern, entry)
			if not tmp:
				pattern = r"#.*# .* <"
				tmp = re.findall(pattern, entry)
			tmp = tmp[0].split("#")
			cf = tmp[-1][:-1].strip()
			return cf

		def getAddInfo(entry):
			""" Gets additional information for the cofactor """
			info = ''
			pattern = r"\(.*\)"
			tmp = re.findall(pattern, entry)
			if tmp:
				info = tmp[0][1:-1]
				info = [item for item in info.split(';') if BRENDAparser.is_id_in_entry(self.id, item)]
				info = [re.sub(r"#.*#", "", item).strip() for item in info]
			return "; ".join(info)

		for entry in entries:
			co.append([getCF(entry), getAddInfo(entry)])
		# print co[-1]
		return co

	def getInhibitors(self):
		""" Sets the inhinitors of the proteins """
		in_entries = BRENDAparser.parse_info("IN", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, in_entries)
		# print entries
		inhibitors = []

		def getIN(entry):
			""" Gets the inhibitor from entry. """
			pattern = r"#.*# .* \("
			tmp = re.findall(pattern, entry)
			if not tmp:
				pattern = r"#.*# .* <"
				tmp = re.findall(pattern, entry)
			tmp = tmp[0].split("#")
			inhibitor = tmp[-1][:-1].strip()
			return inhibitor

		def getAddInfo(entry):
			""" Gets additional information for the inhibitor """
			info = ''
			pattern = r"\(.*\)"
			tmp = re.findall(pattern, entry)
			if tmp:
				info = tmp[0][1:-1]
				info = [item for item in info.split(';') if BRENDAparser.is_id_in_entry(self.id, item)]
				info = [re.sub(r"#.*#", "", item).strip() for item in info]
			return "; ".join(info)

		for entry in entries:
			inhibitors.append([getIN(entry), getAddInfo(entry)])
		# print inhibitors[-1]
		return inhibitors

	def getKi(self):
		""" Sets the Ki values of the proteins """
		ki_entries = BRENDAparser.parse_info("KI", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, ki_entries)
		# print entries
		ki = []

		def getKI(entry):
			""" gets the turnover value """
			pattern = r"#.*# \d*.\d*.* {"
			tmp = re.findall(pattern, entry)
			# print entry
			tmp = tmp[0].split("#")
			ki = tmp[-1][:-1].strip()
			return ki

		def getSubstrate(entry):
			""" gets the coresponding value """
			pattern = r"{.*}"
			tmp = re.findall(pattern, entry)
			substrate = tmp[0][1:-1]
			return substrate

		def getAddInfo(entry):
			""" gets addtional information for the tn value """
			info = ''
			pattern = r"\(.*\)"
			tmp = re.findall(pattern, entry)
			if tmp:
				info = tmp[0][1:-1].replace("\xb0", "")
			if not BRENDAparser.is_id_in_entry(self.id, info):
				info = ''
			else:
				info = re.sub("#.*#", "", info).strip()
			return info

		for entry in entries:
			ki.append([getKI(entry), getSubstrate(entry), getAddInfo(entry)])
		# print ki[-1]
		return ki

	def getMetalIons(self):
		""" Sets the metal ions of the proteins """
		me_entries = BRENDAparser.parse_info("ME", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, me_entries)
		# print entries
		me = []

		def getME(entry):
			""" Gets the metal ions from entry. """
			pattern = r"#.*# .* \("
			tmp = re.findall(pattern, entry)
			if not tmp:
				pattern = r"#.*# .* <"
				tmp = re.findall(pattern, entry)
			tmp = tmp[0].split("#")
			me_ion = tmp[-1][:-1].strip()
			return me_ion

		def getAddInfo(entry):
			""" Gets additional information for the cofactor """
			info = ''
			pattern = r"\(.*\)"
			tmp = re.findall(pattern, entry)
			if tmp:
				info = tmp[0][1:-1]
				info = [item for item in info.split(';') if BRENDAparser.is_id_in_entry(self.id, item)]
				info = [re.sub(r"#.*#", "", item).strip() for item in info]
			return "; ".join(info)

		for entry in entries:
			me.append([getME(entry), getAddInfo(entry)])
		# print me[-1]
		return me

	def getPubMedReferences(self):
		""" Gets information about the cited references. So the given data in the
            protein objects can be validated
            TODO: Parse the given references (can be down in the output of the protein
                  information
        """
		rf_entries = BRENDAparser.parse_info("RF", self.ec_string)
		entries = BRENDAparser.get_entry_with_id(self.id, rf_entries)
		# print entries
		rf = []

		return rf

	def __str__(self):
		""" creates InformationString for object"""
		lines = []
		data = OrderedDict([
			("ec", self.ec),
			("id", self.id),
			("Organism", self.organism),
			("Source Tissue", self.source_tissue),
			("Localisation", self.localisation),
			("NSP", self.natural_substrate_product),
			("Turnover Number", self.turnover_number),
			("Km", self.km),
			("Specific Activity", self.specific_activity),
			("Cofactors", self.cofactors),
			("Inhibitors", self.inhibitors),
			("Ki", self.ki),
			("Metal Ions", self.metal_ions),
			("Pubmed", self.pubmed),
		])
		for (field, info) in data.items():
			lines.append(field.ljust(20) + str(info) + "\n")
		return "".join(lines)


if __name__ == "__main__":
	# parse all the ec data
	base_path = os.path.dirname(os.path.realpath(__file__))
	filename = os.path.join(base_path, "..", 'data', 'brenda_download.txt')
	brenda = BRENDAparser(filename)
	# print(brenda.ec_text["1.1.1.1"])

	ec_str = brenda.ec_text["1.1.1.1"]
	for k in range(1, 168):
		protein = BRENDAProtein(ec="1.1.1.1", id=k, ec_string=ec_str)
		print(protein)

	for ec in brenda.keys():
		print(ec)
		proteins = brenda.parse_proteins(ec)


