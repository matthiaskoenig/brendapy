""" 
Module for parsing the BRENDA ENZYME information from flat file
"""
import os
from brendapy import protein, gene


class BRENDAparser(object):
	""" Parser for BRENDA information."""

	def __init__(self, brenda_file):
		""" Initialize the parser.
		Parses the BRENDA file

		:param brenda_file: BRENDA text file
		"""
		self.brenda_file = brenda_file
		self.ec_str = BRENDAparser.parse_entry_strings(self.brenda_file)
		# for ec, str_data in self.ec_str.items():


	@classmethod
	def parse_entry_strings(cls, filename):
		""" Reads the string entries from given BRENDA file.

		:param filename: BRENDA file
		:return: dict (ec, brenda_info)
		"""
		ec_data = {}
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

	@staticmethod
	def _get_ec_from_line(line):
		ec = line.strip().split("\t")[1].strip()
		ec = ec.split(" ")[0]
		if BRENDAparser._is_ec_number(ec):
			return ec
		else:
			return None

	@staticmethod
	def _is_ec_number(ec):
		"""Tests if given string 'ec' is EC number.

		:param ec: ec string
		:return: True if EC number, False otherwise
		"""
		ec = ec.strip().split(".")
		for number in ec:
			if not number.isdigit():
				return False
		return True

	# ------------------------------
	# Parse information from entry
	# ------------------------------
	@staticmethod
	def parse_info_for_bid(self, bid, ec_info):
		""" readEntryFromString(entry, string)

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
			if in_item == False and starts_with_string(line, bid):
				item = line[L+1:]
				in_item = True

			elif in_item is True:
				# entries longer than one line
				if starts_with_string(line, ''):
					item += " " + line.replace("\t", "").strip()
				# write entries if next entry begins
				elif starts_with_string(line, bid):
					results.append(item)
					item = line[L+1:]
				# write last entry
				elif len(line) == 0:
					results.append(item)
					break
		return [item.replace('\t', ' ') for item in results]


if __name__ == "__main__":
	# parse all the ec data
	base_path = os.path.dirname(os.path.realpath(__file__))
	filename = os.path.join(base_path, "..", 'data', 'brenda_download.txt')
	brenda = BRENDAparser(filename)
	print(brenda.ec_data["1.1.1.1"])
