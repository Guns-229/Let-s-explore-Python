""" Compare data

this implementation don't take care of the attributes...
"""
import sys
import xml.etree.ElementTree as ET

xml1 = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"
xml2 = "<note><to>Tove</to><f1rom>Daniel</f1rom><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"

lst_same = []
lst_diff = [] # data mismatch in xml
list_xml1 = [] # present only in xml1
lst_xml2 = [] # present only in xml2

tree1 = ET.fromstring(xml1)
tree2 = ET.fromstring(xml2)

print(dir(tree1))
