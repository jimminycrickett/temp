# To do:
# Create at least 24 guard points (simulating Black) for LDT testing
# Create function to get current policies if a given host (inputs: hostname) (output: array of ([policy : guard_path],[policy : guard_path],[policy : guard_path]) )
# Create a function to create a guard point (inputs: Policy, Directory, hostname) (output: (success|failed: %s (error) ) )
# Create function to get corresponding key given a policy in Vormetric (inputs: policy name) (outputs: key name)
# Create function to get the policy settings of a given policy (inputs: policy name) (outputs: array of ([policy: (rules)],[policy: (rules)],[policy: (rules)] ))
# Create a function to get the list of configured hosts in Vormetric (inputs: creds?, Vormetric host/url) (outputs: array of (hosts))
# Create a function to create a key in Vormetric (inputs: expiry, name, description, key type)
# Create a function to create a policy in Vormetric (inputs: key, array of (rules), policy name )
# 
#  --  requests.get('https://api.github.com/user', auth=('user', 'pass'))
#
# def getGuardPoints(host)
#    GET /dsm/v1/domains/{domainId}/hosts/{hostId}/guardpoints
# {
# 	"total" : 2,
# 	"offset" : 0,
# 	"limit" : 25,
# 	"list" : 
# 	[ {
# 		"id" : 3,
# 		"url" : "/v1/domains/1000/hosts/1/guardpoints/3",
# 		"guardPath" : "/scala/",
# 		"guardPointType" : "AUTO_GUARD_DIRECTORY",
# 		"enabled" : true,
# 		"guardStatus" : "UP",
# 		"guardInfo" : 
# 		{
# 			"config_state" : "guarded",
# 			"POLICY_VERSION" : "0",
# 			"flags" : "0",
# 			"GUARDED" : "Guarded",
# 			"reason" : "N/A",
# 			"statuschk_tm" : "7/21/2015 15:24:13",
# 			"lock" : "1",
# 			"policy_name" : "policy2",
# 			"GUARD_TIME" : "7/21/2015 15:24:13",
# 			"TYPE" : "1"
# 		},
# 		"autoMountEnabled" : false,
# 		"hostUrl" : "/v1/domains/1000/hosts/1",
# 		"policy" : 
# 		{
# 			"id" : 1,
# 			"url" : "/v1/domains/1000/policies/1",
# 			"name" : "policy2",
# 			"description" : "policy2",
# 			"policyType" : "ONLINE",
# 			"version" : 0,
# 			"domainUrl" : "/v1/domains/1000",	
# 			"moreInfo" : true
# 		}
# 	}, 
# 	{
# 		"id" : 42,
# 		"url" : "/v1/domains/1000/hosts/1/guardpoints/42",
# 		"guardPath" : "/xyzblah/",
# 		"guardPointType" : "AUTO_GUARD_DIRECTORY",
# 		"enabled" : true,
# 		"guardStatus" : "UP",
# 		"guardInfo" : 
# 		{
# 			"config_state" : "guarded",
# 			"flags" : "0",
# 			"POLICY_VERSION" : "0",
# 			"GUARDED" : "Guarded",
# 			"reason" : "N/A",
# 			"statuschk_tm" : "7/21/2015 15:6:38",
# 			"lock" : "1",
# 			"policy_name" : "policy2",
# 			"GUARD_TIME" : "7/21/2015 15:6:38",
# 			"TYPE" : "1"
# 		},
# 		"autoMountEnabled" : false,
# 		"hostUrl" : "/v1/domains/1000/hosts/1",
# 		"policy" : 
# 		{
# 		"id" : 1,
# 		"url" : "/v1/domains/1000/policies/1",
# 		"name" : "policy2",
# 		"description" : "policy2",
# 		"policyType" : "ONLINE",
# 		"version" : 0,
# 		"domainUrl" : "/v1/domains/1000",
# 		"moreInfo" : true
# 		}
# 	} ]
# }

#     return policy_array

# def getGuardPoint_byID()
#     GET /dsm/v1/domains/{domainId}/hosts/{hostId}/guardpoints/{guardPointId}
# {
# "id" : 3,
# "url" : "/v1/domains/1000/hosts/1/guardpoints/3",
# "guardPath" : "/scala/",
# "guardPointType" : "AUTO_GUARD_DIRECTORY",
# "enabled" : true,
# "guardStatus" : "UP",
# "guardInfo" : 
# 	{
# 		"config_state" : "guarded",
# 		"POLICY_VERSION" : "0",
# 		"flags" : "0",
# 		"GUARDED" : "Guarded",
# 		"reason" : "N/A",
# 		"statuschk_tm" : "7/21/2015 15:24:13",
# 		"lock" : "1",
# 		"policy_name" : "policy2",
# 		"GUARD_TIME" : "7/21/2015 15:24:13",
# 		"TYPE" : "1"
# 	},
# "autoMountEnabled" : false,
# "hostUrl" : "/v1/domains/1000/hosts/1",
# "policy" : 
# 	{
# 		"id" : 1,
# 		"url" : "/v1/domains/1000/policies/1",
# 		"name" : "policy2",
# 		"description" : "policy2",
# 		"policyType" : "ONLINE",
# 		"version" : 0,
# 		"domainUrl" : "/v1/domains/1000",
# 		"moreInfo" : true
# 	}
# }


# def getDomainID()
#    GET /dsm/v1/domains
# *****************RESPONSE********************** 
# HTTP/1.1 200 OK
# Pragma: No-cache
# Cache-Control: no-cache
# Expires: Wed, 31 Dec 1969 16:00:00 PST
# Content-Type: application/json
# Transfer-Encoding: chunked
# Date: Tue, 04 Aug 2015 18:45:55 GMT
# Server: DSM
# {
# "total" : 2,
# "offset" : 0,
# "limit" : 25,
# "list" : [ {
# "id" : 1000,
# "url" : "/v1/domains/1000",
# "name" : "domain1",
# "organization" : "Company",
# "kmipEnabled" : false,
# "moreInfo" : true
# }, {
# "id" : 1042,
# "url" : "/v1/domains/1042",
# "name" : "domain10",
# "organization" : "Company",
# "description" : "this is a company",
# "helpDeskInfo" : "Phone: 1-999-999-9999",
# "kmipEnabled" : false,
# "moreInfo" : true
# } ]
# }


# def setGuardPoint(host, gp_name, policy,guard_path)
# def getPolicyKey(policy_??)
#      GET /dsm/v1/domains/{domainId}/policies/{all}{;name1=value1;name2=value2;...}{?offsest=...&limit=...&sort=...&order={asc, desc} }

# def createKey()
# def createPolicy(key,policy_name)
# def getPolicyRules(policy)
#
#

# def getHosts()
#   by ID - 
#     GET /dsm/v1/domains/{domainId}/hosts/{all}{;name1=value1;name2=value2;...}
#         {?offsest=...&limit=...&sort=...&order={asc, desc} }
#   by name
#     GET /dsm/v1/domains/{domainId}/hosts/name/{hostName}
#
#


# def createRule(policy,rule_number?)
#

import requests

from xml.dom import minidom
xmldoc = minidom.parse('items.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.attributes['name'].value)


import xml.dom.minidom as minidom

def parseXML(xml):
	doc = minidom.parse(xml)
	node = doc.documentElement
    return doc, node

def getElementInfo(doc, node, elementName, subElementName):
	elements = doc.getElementsByTagName(elementName)

	values = []
	for element in elements:
		valueObj = element.getElementsByTagName(subElementName)[0]
		values.append(valueObj)
    
    iterations = len(values)

    for i in range(iterations):

    nodeValues = []
	for value in values:
		nodes = value.childNodes
		for node in nodes:
			if node.nodeType == node.TEXT_NODE:
				nodeValues.append(node.data)
	return values, nodeValues
 
#----------------------------------------------------------------------
def getKey(doc, node):
    """
    Print out all titles found in xml
    """

    
 
    titles = []
    for element in elements:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)
 
    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data

def getSecurityRules(doc, node):
    """
    Print out all titles found in xml
    """

    books = doc.getElementsByTagName("book")
 
    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)
 
    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data

def getUserSets(doc, node):
    """
    Print out all titles found in xml
    """

    books = doc.getElementsByTagName("book")
 
    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)
 
    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data

def getProcesses(doc, node):
    """
    Print out all titles found in xml
    """

    books = doc.getElementsByTagName("book")
 
    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)
 
    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data

def getNewKeys(doc, node):
    """
    Print out all titles found in xml
    """

    books = doc.getElementsByTagName("book")
 
    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)
 
    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data

def getLibraries(doc, node):
    """
    Print out all titles found in xml
    """

    books = doc.getElementsByTagName("book")
 
    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)
 
    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data

def getResources(doc, node):
    """
    Print out all titles found in xml
    """

    books = doc.getElementsByTagName("book")
 
    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)
 
    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data

def getActions(doc, node):
    """
    Print out all titles found in xml
    """

    books = doc.getElementsByTagName("book")
 
    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)
 
    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data

def getTimes(doc, node):
    """
    Print out all titles found in xml
    """

    books = doc.getElementsByTagName("book")
 
    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)
 
    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print node.data


if __name__ == "__main__":
    document = 'op_BO_connectdirect_visa.xml'
    getTitles(document)


