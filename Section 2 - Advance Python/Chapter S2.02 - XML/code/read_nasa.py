import xml.etree.ElementTree as ET


file_name = 'data/nasa.xml'

for event, elem in ET.iterparse(file_name):
    pass
	# print(event, elem)

print("..Done..")
