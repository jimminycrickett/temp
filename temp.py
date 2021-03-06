from xml.dom import minidom

# # Open XML document using minidom parser
# DOMTree = xml.dom.minidom.parse("example.xml")
# collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print "Root element : %s" % collection.getAttribute("shelf")

# DOMTree = xml.dom.minidom.parse("op_BO_connectdirect_visa.xml")
# collection = DOMTree.documentElement




securityRules = []
for i in doc.getElementsByTagName("SecurityRules")[0].childNodes:
      if(i.nodeType == 1):
         for n in i.childNodes:
            if(n.nodeType == 1):

class Rule(object):
    RuleActionMatch = "all_ops"
    RuleProcessSigned = "*"
    def __init__(self, RuleActionMatch, RuleProcessSigned):
        self.RuleActionMatch = RuleActionMatch
        self.RuleProcessSigned = RuleProcessSigned

def getSecurityRuleSets(doc):
    # initialize default domain name and username, check for them on exit
    RuleActionMatch = "all_ops"
    RuleProcessSigned = "*"
    rules = []
    rules_sets = {}
    rules_tuple = ()
    SecurityRules_list = doc.getElementsByTagName("SecurityRules")[0]
    for node in SecurityRules_list.childNodes:
        if(node.nodeType == 1):
            actions = []
            actions.append(str(node.getAttribute("PartialMatch")))
            actions.append(str(node.getAttribute("Effect")))
        for child in node.childNodes:
            if(child.nodeType == 1):
                rule = None # zero-out the rule object in case there's no preexisting usermatch or processmatch...
                group = []
                rule = Rule(RuleActionMatch,RuleProcessSigned)
                if(child.nodeName == "UserMatch"):
                    rule.UserMatch = str(child.childNodes[0].data)
                elif(child.nodeName == "ProcessMatch"):
                    rule.ProcessMatch == str(child.childNodes[0].data)
                if(child.nodeName == "ActionMatch"):
                    actionMatch = str(child.childNodes[0].data)
                    rule.RuleActionMatch = actionMatch
                elif(child.nodeName == "ProcessSigned"):
                    RuleProcessSigned = str(child.childNodes[0].data)
                    rule.RuleProcessSigned = RuleProcessSigned
                if(hasattr(rule.UserMatch)):
                    group.append(rule.UserMatch)
                elif(hasattr(rule.ProcessMatch)):
                    group.append(rule.ProcessMatch
                else:
                    group.append("None")
                group.append(rule.RuleActionMatch)
                group.append(rule.RuleProcessSigned)
                rules_tuple = (group, actions)
            else: continue
        rules.append(rules_tuple)
        rules_sets[str(node.getAttribute('Name'))] = rules
    return rules_sets


def handleCharData(data): pass
def handleStartElement(self, name, attrs): pass
def handleEndElement(self, name): pass


def createSecurityRuleSets(SecurityRuleSetDict):
    # returns the resultant xml node of a provided UserSet dictionary
    #self.SecurityRuleSetDict = SecurityRuleSetDict
    keys = SecurityRuleSetDict.keys()
    doc = Document()
    root = doc.createElement("SecurityRules")
    root.setAttribute("PartialMatch", 1)
    root.setAttribute("NeverDeny", 1)
    root.setAttribute("PermitCombiningAlg", "first_applicable")
    for key in keys:
        values = SecurityRuleSetDict[key][0]
        subroot = doc.createElement("SecurityRule")
        subroot.setAttribute("PartialMatch", 1)
        subroot.setAttribute("Effect", )
        for val in values:
            if(values[val] == "UserMatch"):
                userMatchNode = doc.createElement("UserMatch")
                userMatchNode_text = doc.createTextNode(val)
                userMatchNode.appendChild(userMatchNode_text)
                subroot.appendChild(userMatchNode)
            elif(values[val] == "ProcessMatch"):
                processMatchNode = doc.createElement("ProcessMatch")
                processMatchNode_text = doc.createTextNode(val)
            actionMatchNode = doc.createElement("ActionMatch") 
            processSigned = doc.createElement("ProcessSigned")
            processSigned_text = doc.createTextNode(val)
            subroot.appendChild(usernode)
    root.appendChild(subroot)
    return root

def createProcessSets(ProcessSetDict):
    # returns the resultant xml node of a provided UserSet dictionary
    #self.UserSetDict = UserSetDict
    keys = ProcessSetDict.keys()
    doc = Document()
    root = doc.createElement("Processes")
    root.setAttribute("Name", "Process")
    for key in keys:
        values = ProcessSetDict[key][0]
        subroot = doc.createElement("ProcessSet")
        subroot.setAttribute("Name", key)
        for val in values:
            # set up process node structure------------
            objNode = doc.createElement("Object")
            objNode.setAttribute("Type", "process")
            attrNode = doc.createElement("Attr")
            attrNode.setAttribute("Type", "location")
            #------------------------------------------
            dirnode = doc.createElement("Dir")
            basenode = doc.createElement("BaseName")
            dir_text = doc.createTextNode(val)
            base_text = doc.createTextNode(values[val])
            # input process values (dir and basename)
            dirnode.appendChild(dir_text)
            basenode.appendChild(base_text)
            #------------------------------------------
            attrNode.appendChild(dirnode)
            attrNode.appendChild(basenode)
            objNode.appendChild(attrNode)
            subroot.appendChild(objNode)
    root.appendChild(subroot)
    return root


# for script in SCRIPTS:

#     newScript = xmlFile.createElement("script")

#     newScript.setAttribute("name"  , script.name)
#     newScript.setAttribute("action", script.action)

#     newScriptText = xmlFile.createTextNode( script.description )

#     newScript.appendChild( newScriptText  )
#     xmlFile.childNodes[0].appendChild( newScript )

# print xmlFile.toprettyxml()

from xml.dom import minidom
from xml.dom.minidom import Document

#-----------Classes--------------------------------------------------------
class User(object):
    UserName = "baduser"
    UserDomain = "TFD1"
    def __init__(self,UserName, UserDomain):
        self.UserName = UserName
        self.UserDomain = UserDomain

class Process(object):
    ProcessName = "badprocess"
    ProcessDirectory = "baddirectory"
    def __init__(self,ProcessName, ProcessDirectory):
        self.ProcessName = ProcessName
        self.ProcessDirectory = ProcessDirectory


class Policy(object):
    policyName = "Place Holder Policy Name"
    policyVersion = 0
    policyUpdateVersion = 0
    policyUniversalVersion = 110
    policyType = "LDT"
    # We're going to be creating LDT policies, so it's a good default.
    policyKey = "Place Holder Current Key Name"
    policyNewKey = "Place Holder New Key Name"
    policySecurityRules = {}
    def __init__(self,policyName):
        self.policyName = policyName

    def getPolicyVersion(self, doc):
        policyInfo = doc.getElementsByTagName("Policy")[0]
        self.policyVersion = policyInfo.getAttribute("Version")
        return self.policyVersion

    def getCurrentKeys(self, doc):
        self.currentKeys = doc.getElementsByTagName("KeyRules")[0].childNodes[0].childNodes[0].data
        return self.currentKeys

    def getNewKeys(self, doc):
        self.newKeys = doc.getElementsByTagName("NewKeyRules")[0].childNodes[0].childNodes[0].data
        return self.newKeys

    def getPolicyUpdateVersion(self, doc):
        self.policyUpdateVersion = doc.getElementsByTagName("PolicyUpdateVersion")[0].childNodes[0].data
        return self.policyUpdateVersion

    def getUniversalVersion(self, doc):
        self.UniversalVersion = doc.getElementsByTagName("UniversalVersion")[0].childNodes[0].data
        return self.UniversalVersion

    def getpolicyType(self, doc):
        self.policyType = doc.getElementsByTagName("PolicyType")[0].childNodes[0].data
        return self.policyType

    def getUserSets(self,doc):
        # initialize default domain name and username, check for them on exit
        domain = 'TFD1'
        username= 'baduser'
        groups = []
        self.usersets = {}
        user_dict = {}
        User_list = doc.getElementsByTagName("Users")[0]
        for node in User_list.childNodes:
            for child in node.childNodes:
                if(child.nodeType == 1):
                    for subchild in child.childNodes:
                        if(subchild.nodeType == 1):
                            user = User(username,domain)
                            if(subchild.nodeName == "Uname"):
                                username = str(subchild.childNodes[0].data)
                                user.UserName = username
                            elif(subchild.nodeName == "OSDomain"):
                                domain = str(subchild.childNodes[0].data)
                                user.Domain = domain
#                            print "Child name: " + user.UserName
#                            print "Child node: " + user.UserDomain
                            if(user.UserName != 'baduser'):
                                user_dict[user.UserName] = user.UserDomain
                            else: continue
            if(node.nodeType == 1):
                if(node.nodeName == 'UserSet'):
                    groups.append(user_dict)
                    self.usersets[str(node.getAttribute('Name'))] = groups
        return self.usersets


    def createUserSets(self,UserSetDict):
        # returns the resultant xml node of a provided UserSet dictionary
        self.UserSetDict = UserSetDict
        keys = self.UserSetDict.keys()
        doc = Document()
        root = doc.createElement("Users")
        root.setAttribute("Name", "Contact")
        for key in keys:
            values = UserSetDict[key][0]
            subroot = doc.createElement("UserSet")
            subroot.setAttribute("Name", key)
            for val in values:
                usernode = doc.createElement("User")
                user = doc.createElement("Uname")
                user_text = doc.createTextNode(val)
                user.appendChild(user_text)
                domain_node = doc.createElement("OSDomain")
                domain_text = doc.createTextNode(values[val])
                domain_node.appendChild(domain_text)
                usernode.appendChild(user)
                usernode.appendChild(domain_node)
                subroot.appendChild(usernode)
        root.appendChild(subroot)
        self.user_root = root
        return self.user_root

    def getProcessSets(self,doc):
        # initialize default directory name and process name, check for them on exit
        processname= 'mimikatz.exe'
        directory = '\\somestrangehost\somedirectory'
        groups = []
        self.processSets = {}
        process_dict = {}
        process_list = doc.getElementsByTagName("Processes")[0]
        for node in process_list.childNodes:
            # ProcessSet
            if(node.nodeType == 1):
                for child in node.childNodes:
                    # Object
                    if(child.nodeType == 1):
                        for subchild in child.childNodes:
                            # Attr
                            if(subchild.nodeType == 1):
                                for underchild in subchild.childNodes:
                                    # pay dirt...
                                    process = Process(processname,directory)
                                    if(underchild.nodeName == "Dir"):
                                        directory = str(underchild.childNodes[0].data)
                                        process.ProcessDirectory = directory
                                    elif(underchild.nodeName == "BaseName"):
                                        processname = str(underchild.childNodes[0].data)
                                        process.ProcessName = processname
                                    if(process.ProcessName != 'mimikatz.exe'):
                                        process_dict[process.ProcessDirectory] = process.ProcessName
                                    else: continue
                if(node.nodeType == 1):
                    if(node.nodeName == 'ProcessSet'):
                        groups.append(process_dict)
                        self.processSets[str(node.getAttribute('Name'))] = groups
        return self.processSets

    def createProcessSets(self, ProcessSetDict):
        # returns the resultant xml node of a provided UserSet dictionary
        #self.UserSetDict = UserSetDict
        keys = ProcessSetDict.keys()
        doc = Document()
        self.root = doc.createElement("Processes")
        self.root.setAttribute("Name", "Process")
        for key in keys:
            values = ProcessSetDict[key][0]
            subroot = doc.createElement("ProcessSet")
            subroot.setAttribute("Name", key)
            for val in values:
                # set up process node structure------------
                objNode = doc.createElement("Object")
                objNode.setAttribute("Type", "process")
                attrNode = doc.createElement("Attr")
                attrNode.setAttribute("Type", "location")
                #------------------------------------------
                dirnode = doc.createElement("Dir")
                basenode = doc.createElement("BaseName")
                dir_text = doc.createTextNode(val)
                base_text = doc.createTextNode(values[val])
                # input process values (dir and basename)
                dirnode.appendChild(dir_text)
                basenode.appendChild(base_text)
                #------------------------------------------
                attrNode.appendChild(dirnode)
                attrNode.appendChild(basenode)
                objNode.appendChild(attrNode)
                subroot.appendChild(objNode)
        self.root.appendChild(subroot)
        return self.root


class SecurityRule(object):
    SecurityRuleEffect = "audit enc permit" # here, have some sensible defaults...
    SecurityRuleActionMatch = "all_ops" # here, have some crappy defaults...
    SecurityRuleProcessSigned = "*"
    def __init__(self):
        self.SecurityRuleEffect = SecurityRuleEffect
        self.SecurityRuleActionMatch = SecurityRuleActionMatch
        self.SecurityRuleProcessSigned = SecurityRuleProcessSigned
    def ifUserMatch(self):
        self.SecurityRuleUserMatch = SecurityRuleUserMatch
    def ifProcessMatch(self):
        self.SecurityRuleProcessMatch = SecurityRuleProcessMatch

#-----------Classes--------------------------------------------------------

from os.path import basename
from sys import platform
from xml.dom.minidom import parse, Document

def get_policy(xml):
    doc = parse(xml)
    policy = Policy()
    if(platform == "linux" or platform == "linux2"):
        policy.PolicyName = os.path.realpath(xml).split("/")[-1].split(".")[0]
    elif(platform == "win32" or platform == "cygwin"):
        policy.PolicyName = os.path.realpath(xml).split("\\")[-1].split(".")[0]
    policy.policyVersion = getPolicyVersion(doc)
    policy.policyType = getpolicyType(doc)
    policy.policyKey = getPolicyKey(doc)
    policy.policyUpdateVersion = getPolicyUpdateVersion(doc)
    policy.policyUserSets = getUserSets(doc)
    policy.policyProcesses = getProcesses(doc)
    polciy.policySecurityRules = getSecurityRules(doc)
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

