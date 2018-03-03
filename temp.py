from xml.dom import minidom

# # Open XML document using minidom parser
# DOMTree = xml.dom.minidom.parse("example.xml")
# collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print "Root element : %s" % collection.getAttribute("shelf")

# # Get all the movies in the collection
# movies = collection.getElementsByTagName("movie")

# # Print detail of each movie.
# for movie in movies:
#    print "*****Movie*****"
#    if movie.hasAttribute("title"):
#       print "Title: %s" % movie.getAttribute("title")

#    type = movie.getElementsByTagName('type')[0]
#    print "Type: %s" % type.childNodes[0].data
#    format = movie.getElementsByTagName('format')[0]
#    print "Format: %s" % format.childNodes[0].data
#    rating = movie.getElementsByTagName('rating')[0]
#    print "Rating: %s" % rating.childNodes[0].data
#    description = movie.getElementsByTagName('description')[0]
#    print "Description: %s" % description.childNodes[0].data


# DOMTree = xml.dom.minidom.parse("op_BO_connectdirect_visa.xml")
# collection = DOMTree.documentElement




securityRules = []
for i in doc.getElementsByTagName("SecurityRules")[0].childNodes:
      if(i.nodeType == 1):
         for n in i.childNodes:
            if(n.nodeType == 1):




from xml.dom import minidom

def f(elem, level=-1):
    if elem.nodeType == elem.ELEMENT_NODE:
        for child in elem.childNodes:
            for e, l in f(child, level + 1):
                yield e, l


def handleCharData(data): pass
def handleStartElement(self, name, attrs): pass
def handleEndElement(self, name): pass

securityRules = doc.getElementsByTagName("SecurityRules")[0]
for node in securityRules.childNodes:
   if(node.nodeType == 1):
      root = node.nodeName
   for child in node.childNodes:
      if(child.nodeType == 1):
          print "Child nodes: " + str(child.childNodes[0].data)
          print "Child names: " + str(child.nodeName)


groups = []
usersets = {}
user = {}
Users = doc.getElementsByTagName("Users")[0]
for node in Users.childNodes:
   for child in node.childNodes:
      if(child.nodeType == 1):
         for subchild in child.childNodes:
            if(subchild.nodeType == 1):
               user[str(subchild.nodeName)] = str(subchild.childNodes[0].data)
               print "Child name: " + str(subchild.nodeName)
               print "Child node: " + str(subchild.childNodes[0].data)
         groups.append(user)
   if(node.nodeType == 1):
      if(node.nodeName == 'UserSet'):
         usersets[node.getAttribute('Name')] = groups


print user
print groups

import xml.parsers.expat, sys

class MyXML:
    Parser = ""
    # Prepare for parsing
    def __init__(self, xml_filename):
        assert xml_filename != ""
        self.xml_filename = xml_filename
        self.Parser = xml.parsers.expat.ParserCreate(  )
        self.Parser.CharacterDataHandler = self.handleCharData
        self.Parser.StartElementHandler = self.handleStartElement
        self.Parser.EndElementHandler = self.handleEndElement
    # Parse the XML file
    def parse(self):
        try:
            xml_file = open(self.xml_filename, "r")
        except:
            print "ERROR: Can't open XML file %s"%self.xml_filename
            raise
        else:
            try: self.Parser.ParseFile(xml_file)
            finally: xml_file.close(  )
    # to be overridden by implementation-specific methods
    def handleCharData(self, data): pass
    def handleStartElement(self, name, attrs): pass
    def handleEndElement(self, name): pass


doc = MyXML("op_BO_connectdirect_visa.xml")
doc.parse()




list(f(doc))

xmlFile = minidom.parse( FILE_PATH )

for script in SCRIPTS:

    newScript = xmlFile.createElement("script")

    newScript.setAttribute("name"  , script.name)
    newScript.setAttribute("action", script.action)

    newScriptText = xmlFile.createTextNode( script.description )

    newScript.appendChild( newScriptText  )
    xmlFile.childNodes[0].appendChild( newScript )

print xmlFile.toprettyxml()

from xml.dom import minidom
from xml.dom.minidom import Document

class Policy(object):
    policyName = ""
    policyVersion = 0
    policyUpdateVersion = ""
    policyUniversalVersion = 110
    policyKey = ""
    policyNewKey = ""
    policySecurityRules = {}
    def __init__(self):
        self.policyName = policyName
        self.policyVersion = policyVersion
        self.policyUpdateVersion = policyUpdateVersion
        self.policyUniversalVersion = 110
        self.policyKey = policyKey
        self.policyNewKey = policyNewKey
        self.policyActions = policyActions
        self.policyEffect = policyEffect


class SecurityRule(object):
    SecurityRuleName = ""
    SecurityRuleEffect = ""
    SecurityRuleActionMatch = ""
    SecurityRuleProcessSigned = "*"
    def __init__(self):
        self.SecurityRuleName = SecurityRuleName
        self.SecurityRuleEffect = SecurityRuleEffect
        self.SecurityRuleActionMatch = SecurityRuleActionMatch
        self.SecurityRuleProcessSigned = SecurityRuleProcessSigned
    def 

def parse(xml_filename):
   doc = minidom.parse(xml_filename)
   return doc

def make_policy_object(policyName, policyVersion, policyKey, policyUpdateVersion, policyNewKey, policyActions):
    policy = Policy()
    policy.policyName = policyName
    policy.policyVersion = policyVersion
    policy.policyUpdateVersion = policyUpdateVersion
    policy.policyUniversalVersion = 110
    policy.policyKey = policyKey
    policy.policyNewKey = policyNewKey
    policy.policySecurityRules = policySecurityRules
    policy.policyLibs = policyLibs
    policy.policyResources = policyResources
    policy.policyActions = policyActions
    policy.policyTimes = policyTimes
    policy.policyEffect = policyEffect
    return policy


def get_policy(xml):
    doc = parse(xml)

    securityRules = doc.getElementsByTagName("SecurityRules")[0]
    userSets = doc.getElementsByTagName("UserSet")[0]
    currentKeys = doc.getElementsByTagName("KeyRules")[0].childNodes[0].childNodes[0].data
    newKeys = doc.getElementsByTagName("NewKeyRules")[0].childNodes[0].childNodes[0].data
    policyInfo = doc.getElementsByTagName("Policy")[0]
    policyVersion = policyInfo.getAttribute("Version")
    policyUpdateVersion = doc.getElementsByTagName("PolicyUpdateVersion")[0].childNodes[0].data
    universalVersion = doc.getElementsByTagName("UniversalVersion")[0].childNodes[0].data
    policyType = doc.getElementsByTagName("PolicyType")[0].childNodes[0].data
    return policy


def generate_policy(policy):

    currentKey = policy.currentKey
    policyName = policy.policyName
    policyType = policy.policyType
    policyVersion = policy.policyVersion
    policyUpdateVersion = policy.policyUpdateVersion
    policyUniversalVersion = policy.policyUniversalVersion
    policyKey = policy.policyKey
    policyNewKey = policy.policyNewKey
    policySecurityRules = policy.policySecurityRules
    policyLibs = policy.policyLibs
    policyResources = policy.policyResources
    policyActions = policy.policyActions
    policyTimes = policy.policyTimes
    policyEffect = policy.policyEffect

    doc = Document()
    node_0 = doc.createElement('Policy')
    node_0.setAttribute('Version', policyVersion)

    node_1_text = doc.createTextNode(policyType)
    node_1 = doc.createElement('PolicyType')
    node_1.appendChild(node_1_text)

    node_2_text = doc.createTextNode(policyUpdateVersion)
    node_2 = doc.createElement('PolicyUpdateVersion')
    node_2.appendChild(node_2_text)

    node_3_text = doc.createTextNode(policyUniversalVersion)
    node_3 = doc.createElement('UniversalVersion')
    node_3.appendChild(node_3_text)
    
    node_4_text = doc.createTextNode("")
    node_4 = doc.createElement('Description')
    node_4.appendChild(node_4_text)

    node_5 = doc.createElement('KeyRules')
    node_5.setAttribute('KeyCombiningAlg', "first_applicable")

    node_6 = doc.createElement('KeyRule')

    node_7_text = doc.createTextNode(currentKey)
    node_7 = doc.createElement('Key')
    node_7.appendChild(node_7_text) 

    node_8_text = doc.createTextNode(policyNewKey)
    node_8 = doc.createElement('NewKeyRules')
    node_8.appendChild(node_8_text) 

    node_9 = doc.createElement('KeyRule')

    node_10_text = doc.createTextNode(currentKey)
    node_10 = doc.createElement('Key')
    node_10.appendChild(node_10_text) 

    node_11 = doc.createElement('SecurityRules')
    node_11.setAttribute('PermitCombiningAlg','first_applicable')
# We set "NeverDeny" to '1' so it defaults to Learning Mode. The current policies
# don't restrict access anyway, so we aren't losing anything by learning exactly 
# what actions are occuring.
    node_11.setAttribute('NeverDeny','1')
    node_11.setAttribute('PartialMatch','1')

# Node list:
#  node_0 - policy
#  node_1 - policyupdateversion
#  node_2 - universalversion
#  node_3 - description
#  node_4 - keyrules
#  node_5 - keyrule
#  node_6 - key
#  node_7 - newkeyrules
#  node_8 - newkey (key node for new key)
#  node_9 - SecurityRules
#   ********** gotta be a better way to do this part *********
#  node_10 - SecurityRule
#  node_11 - UserMatch
#  node_12 - ActionMatch
#  node_13 - ProcessSigned
# *************************************************************

#  node_14 - Target
#  node_15 - Users
#  node_16 - UserSet

#   ********** gotta be a better way to do this part *********
#  node_17 - User
#  node_18 - Uname
#  node_19 - Gname
#  node_20 - OSDomain
# *************************************************************
#  node_21 - Processes
#   ********** gotta be a better way to do this part **********
#  node_22 - ProcessSet
#  ************************************************************
#  node_23 - Object
#  node_24 - Attr
#  node_25 - Dir
#  node_26 - BaseName
#  node_27 - Libs
#  node_28 - Actions
#  node_29 - Times


    doc.appendChild(node_0)
    node_0.appendChild(node_1)
    node_0.appendChild(node_2)
    node_0.appendChild(node_3)
    node_0.appendChild(node_4)
    node_0.appendChild(node_5)
    node_5.appendChild(node_6)
    node_6.appendChild(node_7)
    node_6.appendChild(node_8)
    node_0.appendChild(node_9)
    node_9.appendChild(node_10)
    node_10.appendChild(node_)

    node_

    return doc

