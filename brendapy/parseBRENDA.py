""" 
	Module for parsing the BRENDA ENZYME information for the reactions. 
	The soap Interface in soapBRENDA is of no use. Not all data could be 
	retreived easily.
	Therefore the data has to be parsed from file.
	
	TODO: remove BRENDAInformation object and return list of proteins
	
	author: Matthias Koenig
	version: 0.1
	date: 06.08
	
"""

import files
import proteinBRENDA
import tools.equationTools as equationTools


def getBrendaProteinsFromEC(ec, ec_string=None):
	""" getBrendaProteinsFromEC(ec, ec_string)
		Creates list of all BRENDA Protein entries for given ec number 'ec' and 
		'ec_data'. 'ec_data' is part of brenda information file for the given ec
		number.
		Returns protein list. 
	"""
	if not ec_string:
		filename = files.install_dir + "/data/output/brenda_ecs/" + ec
		# print filename
		input = open(filename, "r")
		ec_string = input.read()
		input.close()
	
	proteins = []
	# number of proteins in entry
	protein_count = numberOfProteins(ec_string)		
	# create list of Protein entries
	for id in range(1, protein_count+1):
		proteins.append(proteinBRENDA.BRENDAProtein(ec, id, ec_string))
	return proteins

def getStringFromEC(ec):
		""" Returns the full information string for a given ec number. 
			String consists of lines from
			ID	6.6.1.2 (first line) till /// (last line).
		"""
		if not equationTools.isECnumber(ec):
			return None
		result = []
		input = open(files.BRENDAfile, 'r')
		start = "ID\t" + ec + "\n"
		start1 = "ID\t" + ec + " "
		end = "///"
		
		in_entry = False      # marker if in entry
		for line in input:
			if in_entry == False and (line.startswith(start) or line.startswith(start1)):
				in_entry = True
			if in_entry == True and not line.startswith(end):
				result.append(line)
			if in_entry == True and line.startswith(end):
				result.append(line)
				break
		input.close()
		result = "".join(result)
		result = result.replace('\xef\xbf\xbd', " ")
		return result

def createAllECStringFiles():
	"""
		Creates files for all ec entries in Brenda.
		Returns list of available ec_numbers
	"""
	def getECFromLine(line):
		ec = line.strip().split("\t")[1].strip()
		ec = ec.split(" ")[0]
		if equationTools.isECnumber(ec):
			return ec
		else:
			return None
	# Read Data from file to ec entries
	input = open(files.BRENDAfile, 'r')
	output = files.install_dir + "/data/output/brenda_ecs/"
	ecs = []	
	start = "ID\t"
	end = "///"
	in_entry = False
	data_lines = []
	for line in input:
		# Start of entry	
		if line.startswith(start):
			data_lines = []
			ec = getECFromLine(line)
			if ec:
				in_entry = True
				ecs.append(getECFromLine(line))
			print line[:-1]
		# In entry
		if in_entry:
			data_lines.append(line)
		# End of entry
		if in_entry and line.startswith(end):
			in_entry = False
			entry = "".join(data_lines)
			entry.replace('\xef\xbf\xbd', " ")
			out = open(output + ec, "w")
			out.write(entry)
			out.close()
	input.close()
	return ecs

def getAllECStrings():
	""" getAllECStrings()
		Takes the BRENDA file and returns list of all entry strings and list of
		corresponding EC numbers.
		One entry string contains all the information for a given ec number.
		Theoretical good idea- but not enough heap memory.
	"""
	ecs = []	
	ecs_data = []
	def getECFromLine(line):
		ec = line.strip().split("\t")[1].strip()
		return ec
	# Read Data from file to ec entries
	input = open(files.BRENDAfile, 'r')
	start = "ID\t"
	end = "///"
	in_entry = False
	data_lines = []
	for line in input:
		# Start of entry	
		if line.startswith(start):
			in_entry = True
			ecs.append(getECFromLine(line))
			print line[:-1]
		# In entry
		if in_entry:
			data_lines.append(line)
		# End of entry
		if in_entry and line.startswith(end):
			in_entry = False
			entry = "".join(data_lines)
			entry.replace('\xef\xbf\xbd', " ")
			ecs_data.append(entry)
	input.close()
	return ecs, ecs_data
	
def getEntryFromString(ID, ec_string):
	""" readEntryFromString(entry, string)
	    Reads 'entry' from 'string' and returns list of entries associated with
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
	def startsWithString(line, string):
		start = [string + "\t", string + " "]
		for item in start:
			if line.startswith(item):
				return True
		return False
	
	results = []
	lines = ec_string.split("\n")	
	in_item = False	
	L = len(ID)
	
	#print "Begin search for ID:\t %s" % ID
	for line in lines:
		# read first entry
		if in_item == False and startsWithString(line, ID):
			item = line[L+1:]
			in_item = True

		elif in_item == True:
			# entries longer than one line
			if startsWithString(line, ''):
				item += " " + line.replace("\t", "").strip()
			# write entries if next entry begins
			elif startsWithString(line, ID):
				results.append(item)
				item = line[L+1:]
			# write last entry
			elif len(line) == 0:
				results.append(item)
				break
	return [item.replace('\t', ' ') for item in results]

def getEntryWithID(ID, entry_list):
	""" Returns an entry list of the entries in which the id is found 
		Information for proteins can be collected.
		Use the filterfunction: isIDinEntry(ID)
	"""
	result = []
	for entry in entry_list:
		if isIDinEntry(ID, entry):
			result.append(entry)
	return result

def isIDinEntry(ID, entry):
	""" Returns True if ID is in Entry, False otherwise. 
		ID list always starts with '#' and ends with '#'
		Entries are separeted by comma.
		Solution with regular expressions searching for
		#3# and #3,4,5,6# patterns
	"""
	import re
	pattern = r"#[\d,]+#"
	items = re.findall(pattern, entry)
	ids = []
	for item in items:
		ids.extend([id for id in item[1:-1].split(",") if id!='' and id.isdigit()])
	# Is ID in IDlist ?
	ids = [int(id) for id in ids]
	if ID in ids:
		return True
	else:
		return False

def numberOfProteins(ec_string):
	""" Get the number of protein entries in the BRENDA database for
	    ec number."""
	return len(getEntryFromString("PR", ec_string))

def test():
	def basicTest():
		print "Parsing BRENDA data"
		ec = "1.1.1.10"
		print ec
		# Get the enzyme data from the BRENDA file for ec number
		ec_string = getStringFromEC(ec)
		nsp = getEntryFromString("RF", ec_string)
		print nsp
	
		# Create Brenda information object
		ec = "4.1.2.13"
		BI = BRENDAInformation(ec)
		BI.printInformationString()
	
	def readAllEntries():
		# Read all BRENDA entries from file
		#ecs, ecs_data = getAllECStrings()
		ecs = createAllECStringFiles()
		print ecs
	
	if 0:
		basicTest()
	if 1:
		readAllEntries()
	
if __name__ == "__main__":
	test()