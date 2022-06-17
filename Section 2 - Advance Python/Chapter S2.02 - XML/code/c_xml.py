import xml.etree.ElementTree as ET
import logging
import sys
# from termcolor import colored

def colored(txt, color):
    print(color, ">>", txt)

tree1 = ET.parse(sys.argv[1])
root1 = tree1.getroot()

tree2 = ET.parse(sys.argv[2])
root2 = tree2.getroot()

class Element:
    def __init__(self,e):
        self.name = e.tag
        self.subs = {}
        self.atts = {}
        for child in e:
            self.subs[child.tag] = Element(child)

        for att in e.attrib.keys():
            self.atts[att] = e.attrib[att]

        print("name: %s, len(subs) = %d, len(atts) = %d" % (self.name,
                                                            len(self.subs),
                                                            len(self.atts) ))

    def compare(self,el):
        if self.name!=el.name:
            raise RuntimeError("Two names are not the same")

        for att in self.atts.keys():
            v1 = self.atts[att]
            if att not in el.atts.keys():
                v2 = '[NA]'
                color = 'yellow'
            else:
                v2 = el.atts[att]
                if v2==v1:
                    color = 'green'
                else:
                    color = 'red'
            print(colored("first:\t%s = %s" % ( att, v1 ), color))
            print(colored("second:\t%s = %s" % ( att, v2 ), color))

        for subName in self.subs.keys():
            if subName not in el.subs.keys():
                print(colored("first:\thas got %s" % ( subName), 'purple'))
                print(colored("second:\thasn't got %s" % ( subName), 'purple'))
            else:
                self.subs[subName].compare( el.subs[subName] )

e1 = Element(root1)
e2 = Element(root2)

e1.compare(e2)
