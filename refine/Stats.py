from lxml import etree as ET

class Stats(object):
    def __init__(self):
        #create new tree
        #self.tree = ET.ElementTree(ET.Element('Paths'))
        #load pit file
        self.pitTree = ET.parse('refine/pitClient.xml')
