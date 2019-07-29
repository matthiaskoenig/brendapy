"""
    Get Information from BRENDA via SOAP and WSDL
    http://www.brenda-enzymes.info/soap/

    Especially genes associated with reactions (ec numbers) are of interest.
    Furthermore all information regarding kinetics and thermodynamics of the
    reaction.
    
    Data is used to build 
        1. kinetic network
        2. stoichiometric network
        
    Of interest are enzymatic modifieres (for example inhibitors and Activators with 
    coresponding Ki values).
    
    The genetic level is also of interest. Which genes in which organisms are present
    for the reaction. 
    
    In a first step all gentetic information is used. Filters for organsims have to be
    established.
    
    This Webinterface couldn't be used for the project. The Brenda data had to be parsed 
    from the downloaded brenda image.
    The webinterface did not support the retreival of the necessary information. 
    
    author: Matthias Koenig
    version: 0.1
    date: 06.08
"""

import files
from SOAPpy import WSDL
proxy = files.proxy
# wsdl = 'http://www.brenda-enzymes.info/soap/brenda.wsdl'
wsdl = files.BRENDAwsdl
server = WSDL.Proxy(wsdl, http_proxy=proxy)

def createServer(new_proxy):
    """ Creates server with new proxy
        needed if working in different proxy environments """
    global server, proxy
    proxy = new_proxy
    server = WSDL.Proxy(wsdl, http_proxy=new_proxy)

def testConnection():
    """ Establishes simple test connection to BRENDA database and
        retreives some data
    """
    print "Test connection to BRENDA Enzyme database "
    print "WSDL file:".ljust(15), wsdl
    print "Proxy:".ljust(15), proxy

    # connection information
    server.soapproxy.config.dumpSOAPOut = 1
    server.soapproxy.config.dumpSOAPIn = 1
    # get data
    print server.getEcNumbersFromActivatingCompound()


def getData():
    """ Simple method for getting data from the database """
    list = server.methods
    for item in list:
        print item
        
if __name__ == "__main__":
    # Test connection to BRENDA database
    testConnection()
    getData()