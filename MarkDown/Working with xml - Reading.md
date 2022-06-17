
# Chapter 2: Working with xml : reading

## 1. XML, XPath and DOM

XML stands for eXtensible Markup Language and is designed to describe data. Unlike html, XML is very flexible. Although you must have clean markup, you can invent your own tags or use those supplied by ODD, guidelines and set of tags design for collaboration and shared practices.

You've probably heard of TEI; TEI is a nice, complex, complete language for encoding texts.


![XML, source of our everyday](images/XML.PNG)

## 2\. Parsing XML with Python

As for querying the web, Python has many libraries for playing with xml. You will most likely encounter the following during your Pythonic journey :

- **lxml**, which we will use for this course. A clean, quite fast, strict library for dealing with xml resources. It's the most accepted library for this kind of request. If IBM writes [tutorials for it](http://www.ibm.com/developerworks/library/x-hiperfparse/), it should be good. It supports xpath and xslt.
- **BeautifulSoup**. Flexible, average speed. The good thing is if your xml markup is messed up, it will try to correct it. It's perfect for dealing with web scrapped data in HTML formats. For clean xml, it might be too slow.
- **xml** : the native integration in Python. Fast, clean but no good sides such as xpath and xslt.
- Read about others on the Python [official wiki](https://wiki.python.org/moin/PythonXml)


Based on my experience, lxml will meet most of your needs when dealing with clean data. Clean is the key word here : do not expect lxml to play well with bad html or bad xml. It will just throw errors at you until you give up or fix it by hand.

We can import lxml.etree the same way we imported requests earlier.


```python
from lxml import etree
```

### From file to XML object

Opening an xml file is actually quite simple : you open it and you parse it. Who would have guessed ?


```python
# We open our file
with open("data/books.xml") as file:
    # We use the etree.parse property
    parsed = etree.parse(file)
# We print the object
print(parsed)
```

    <lxml.etree._ElementTree object at 0x7feb2c2d1608>
    

As you can see, we obtained an instance of type lxml.etree.\_ElementTree. It means the xml markup has been transformed into something Python understands.

The *parse* function of *etree* does not take many arguments. One way to customize its behaviour is to give it a home configured or homemade xml parser : 


```python
# We initiate a new parser from etree, asking it to remove nodes of text which are empty
parser = etree.XMLParser(remove_blank_text=True)
# We open the file
with open("data/books.xml") as file:
    # And we parse using the new parser
    parsed = etree.parse(file, parser)
# We print the object
print(parsed)
# We open the file
```

    <lxml.etree._ElementTree object at 0x7feb171bef48>
    

From the [documentation](http://lxml.de/parsing.html#parser-options) of the XMLParser function, here are some arguments that might be useful for you :

- *attribute_defaults* : Use DTD (if available) to add the default attributes
- *dtd_validation* : Validate against DTD while parsing
- *load_dtd* : Load and parse the DTD while parsing
- *ns_clean* : Clean up redundant namespace declarations
- *recover* : Try to fix ill-formed xml
- *remove_blank_text* : Removes blank text nodes
- *resolve_entities* : Replace entities by their value (Default : on)

You can then create a new parser according to its standards or clean namespace attribute. In this context, *ns_clean* would transform


`<root xmlns:a="xmlns1" xmlns:b="xmlns2"><tag xmlns:c="xmlns3" /><tag xmlns:a="xmlns1" /><tag /></root>`

into

`<root xmlns:a="xmlns1" xmlns:b="xmlns2"><tag xmlns:c="xmlns3" /><tag/><tag /></root>`

### From string to XML object

lxml parses strings in the same way that it parses files. The syntax differs, but is quite simple :


```python
xml = '<root xmlns:a="xmlns1" xmlns:b="xmlns2"><tag xmlns:c="xmlns3" /><tag xmlns:a="xmlns1" /><tag /></root>'
parsed = etree.fromstring(xml)
print(parsed)
```

    <Element root at 0x262a25b1308>
    

**DIY**

Can you parse a xml document made of one tag "humanities" with two children "field" named "classics" and "history"? 


```python
# Put your code here
```

### Errors and understanding them

Previouly, we have said that lxml was quite strict about xml validity. Let's see an example :


```python
xml = """
<fileDesc>
    <titleStmt>
        <title>Aeneid</title>
        <title type="sub">Machine readable text</title>
        <author n="Verg.">P. Vergilius Maro</author>
        <editor role="editor" n="Greenough">J. B. Greenough</editor>
    </titleStmt>
    <extent>about 505Kb</extent>
    <!-- &Perseus.publish;-->
    <sourceDesc>
        <biblStruct>
            <monogr>
                <author>Vergil</author>
                <title>Bucolics, Aeneid, and Georgics Of Vergil</title>
                <editor role="editor">J. B. Greenough</editor>
                <imprint>
                    <pubPlace>Boston</pubPlace>
                    <publisher>Ginn &amp; Co.</publisher>
                    <date>1900</date>
                </imprint>
            </monogr>
        </biblStruct>
    </sourceDesc>
</fileDesc>"""

etree.fromstring(xml)
```




    <Element fileDesc at 0x7feb17140e08>



What error did we raise trying to parse this XML ? We got an *XMLSyntaxError*. It can happen for various reasons, including when entities cannot be parsed. Can you try to find another way to raise an XMLSyntaxError ?


```python
#Write your xml in xml variable
# invalid
xml = """
"""
# 
xml2 = """
<start></start>
"""
#
xml3 = """
<start attr="test"/>
"""
etree.fromstring(xml3)
```




    <Element start at 0x28af480e988>



As you can see, errors are detailed enough so you can correct your own XML, at least manually.

### Node properties and methods

*Quick explanation* : Methods and properties are something special in Python and other programming languages. Unlike traditional functions (`len()`) and keys of dictionaries (`a["b"]`), they are part of something bigger.

**Methods** : Ever seen something such as `a.method()` ? Yes, you did with `.split()`, `.join()`, etc. Functions following a variable with a dot are called methods because they are an extension of the variable type. *eh* `split()` and `join()` are extensions of string objects, and they use their value as argument.

**Properties or Attributes** : Such as dictionary keys, properties are indexed values of an object, but instead of using the syntax made of square brackets, you just put the name of the key after a dot : `a.property`

**Warning : namespaces** : In lxml, namespaces are expressed using the Clark notation. This mean that, if a namespace defines a node, this node will be named using the following syntax "`{namespace}tagname`. Here is an example :


```python
# With no namespace
print(etree.fromstring("<root />"))
# With namespace
print(etree.fromstring("<root xmlns='http://localhost' />"))
```

    <Element root at 0x262a25c1a88>
    <Element {http://localhost}root at 0x262a25c1a88>
    

You can do plenty of things using lxml and access properties or methods of nodes, here is an overview of reading functionalities offered by lxml :

![Cheatsheet](images/CheatsheetElement.svg)

Let's see what that means in real life :


```python
# First, we will need some xml
xml = """
<div type="Book" n="1">
    <l n="1">Arma virumque cano, Troiae qui primus ab oris</l>
    <tei:l n="2" xmlns:tei="http://www.tei-c.org/ns/1.0">Italiam, fato profugus, Laviniaque venit</tei:l>
    <l n="3">litora, multum ille et terris iactatus et alto</l>
    <l n="4">vi superum saevae memorem Iunonis ob iram;</l>
    <l n="5">multa quoque et bello passus, dum conderet urbem,</l>
    <l n="6">inferretque deos Latio, genus unde Latinum,</l>
    <l n="7">Albanique patres, atque altae moenia Romae.</l>
</div>
"""
div = etree.fromstring(xml)
print(parsed)
```

    <lxml.etree._ElementTree object at 0x7feb171bef48>
    

If we want to retrieve the attributes of our div, we can do as follow :


```python
type_div = div.get("type")
print(type_div)
# If we want a dictionary of attributes
print(div.attrib)
attributes_div = dict(div.attrib)
print(attributes_div)
# Of if we want a list
list_attributes_div = div.items()
print(list_attributes_div)
```

    Book
    {'n': '1', 'type': 'Book'}
    {'n': '1', 'type': 'Book'}
    [('type', 'Book'), ('n', '1')]
    

Great ! We accessed our first information using lxml ! Now, how about getting somewhere other than the root tag ? To do so, there are two ways :

- getchildren() will returns a list of children tags, such as div.
- list(div) will transform div in a list of children.

Both syntaxes return the same results, so it's up to you to decide which one you prefer. 


```python
children = div.getchildren()
line_1 = children[0] # Because it's a list we can access children through index
print(line_1)
```

    <Element l at 0x7feb17143488>
    

Now that we have access to our children, we can have access to their text :


```python
print(line_1.text)
```

    Arma virumque cano, Troiae qui primus ab oris
    

Ok, we are now able to get some stuff done. Remember the namespace naming ? Sometimes it's useful to retrieve namespaces and their prefix :


```python
line_2 = children[1]
print(line_2.nsmap)
print(line_2.prefix)
print(line_2.tag)
```

    {'tei': 'http://www.tei-c.org/ns/1.0'}
    tei
    {http://www.tei-c.org/ns/1.0}l
    

**What you've learned** :

- How to parse a xml file or a string representing xml through `etree.parse()` and `etree.fromstring()`
- How to configure the way xml is parsed with `etree.XMLParser()`
- What is an attribute and a method
- Properties and methods of a node
- XMLParseError handling
- Clark's notation for namespaces and tags.

----

## 3\. XPath and XSLT with lxml
---

### XPath

XPath is a powerful tool for traversing an xml tree. XML is made of nodes such as tags, comments, texts. These nodes have attributes that can be used to identify them. For example, with the following xml :

> `<div><l n="1"><p>Text</p> followed</l><l n="2">by line two</div>`

the node p will be accessible by `/div/l[@n="1"]/p`. LXML has great support for complex XPath, which makes it the best friend of Humanists dealing with xml :


```python
# We generate some xml and parse it

## TODO 
xml = """<div>
            <l n="1">
                <p>Text</p> 
                followed
            </l>
            <l n="2">
                by line two
            </l>
            <p>test</p>
            <p><l n="3"> line 3</l></p>
        </div>"""
div = etree.fromstring(xml)
print(div)
# When doing an xpath, the results will be a list
ps = div.xpath("/div/l")
for p in ps:
    print(p)
# print(ps)
# print(ps[0].values())
# print(ps[0].text == "Text")
```

    <Element div at 0x7feb17157a48>
    
                
    
                
    

As you can see, the xpath returns a list. This behaviour is intended, since an xpath can retrieve more than one item :


```python
print(div.xpath("//l"))
```

    [<Element l at 0x28af4804808>, <Element l at 0x28af4843608>, <Element l at 0x28af48434c8>]
    

You see ? The xpath `//l` returns two elements, just like python does in a list. Now, let's apply some xpath to the children and see what happens :


```python
# We assign our first line to a variable
line_1 = div.xpath("//l")[0]
#print(dir(line_1))
print(line_1.attrib['n'])

# We look for p
print(line_1.xpath("p")) # This works
print(line_1.xpath("./p")) # This works too
print(line_1.xpath(".//p")) # This still works
print(line_1.xpath("//p")) 

```

    1
    [<Element p at 0x28af484bd48>]
    [<Element p at 0x28af484bd48>]
    [<Element p at 0x28af484bd48>]
    [<Element p at 0x28af484bd48>, <Element p at 0x28af484f908>, <Element p at 0x28af484f948>]
    

As you can see, you can do xpath from any node in lxml. One important thing though : xpath `//tagname` *will return to the root* if you do not add a dot in front of it such as **`.`**`//tagname`. This is really important to remember, because most xpath resolvers do not behave this way.

**Xpath with namespaces and prefix**

As you've seen, lxml use Clark's naming convention for expressing namespaces. This is extremely important regarding xpath, because you will be able to retrieve a node using it under certain conditions :


```python
xml = """<root>
<tag xmlns="http://localhost">Text</tag>
<tei:tag xmlns:tei="http://www.tei-c.org/ns/1.0"></tei:tag>
</root>"""
root = etree.fromstring(xml)

print(root.xpath("//tag")) # Does not retrieve anything because both tags have a namespace
print(root.findall("{http://localhost}tag")) # Retrieve first tag

print(root.xpath("//{http://www.tei-c.org/ns/1.0}tag")) # Will fail
```

    []
    [<Element {http://localhost}tag at 0x262a25c9888>]
    


    ---------------------------------------------------------------------------

    XPathEvalError                            Traceback (most recent call last)

    <ipython-input-22-b3d32d8a5404> in <module>()
          8 print(root.findall("{http://localhost}tag")) # Retrieve first tag
          9 
    ---> 10 print(root.xpath("//{http://www.tei-c.org/ns/1.0}tag")) # Will fail
    

    lxml.etree.pyx in lxml.etree._Element.xpath (src\lxml\lxml.etree.c:57803)()
    

    xpath.pxi in lxml.etree.XPathElementEvaluator.__call__ (src\lxml\lxml.etree.c:166824)()
    

    xpath.pxi in lxml.etree._XPathEvaluatorBase._handle_result (src\lxml\lxml.etree.c:165783)()
    

    XPathEvalError: Invalid expression


The last line failed because Clark's notation is not accepted in xpath. To succeed, you will need to use a namespace dictionary and prefix, which you will feed to the `xpath()` method using the argument `namespaces` : 


```python
# We create a valid xml object
xml = """<root>
<tag xmlns="http://localhost">Text</tag>
<tei:tag xmlns:tei="http://www.tei-c.org/ns/1.0">Other text</tei:tag>
</root>"""
root = etree.fromstring(xml)
# We register every namespaces in a dictionary using prefix as keys :
ns = {
    "local" : "http://localhost", # Even if this namespace had no prefix, we can register one for it
    "tei" : "http://www.tei-c.org/ns/1.0"
}
tag_1 = root.xpath("//local:tag", namespaces=ns)
print(tag_1[0].text)
tag_2 = root.xpath("//tei:tag", namespaces=ns)
print(tag_2[0].text)
```

    Text
    Other text
    

Another point to kepe in mind : if you write your xpath incorrectly, Python will raise an *XPathEvalError * error


```python
root.xpath("wrong:xpath:never:works")
```


    ---------------------------------------------------------------------------

    XPathEvalError                            Traceback (most recent call last)

    <ipython-input-26-71f4dbcd4ccf> in <module>()
    ----> 1 root.xpath("wrong:xpath:never:works")
    

    lxml.etree.pyx in lxml.etree._Element.xpath (src\lxml\lxml.etree.c:57803)()
    

    xpath.pxi in lxml.etree.XPathElementEvaluator.__call__ (src\lxml\lxml.etree.c:166824)()
    

    xpath.pxi in lxml.etree._XPathEvaluatorBase._handle_result (src\lxml\lxml.etree.c:165783)()
    

    XPathEvalError: Undefined namespace prefix


**What you have learned** :

- Each node and xml document has an `.xpath()` method which takes as its first parameter xpath
- Method `xpath()` always returns a list, even for a single result
- Method `xpath()` will return to the root when you don't prefix your `//` with a dot.
- An incorrect XPath will issue a `XPathEvalError`
- Method `xpath()` accepts a `namespaces` argument : you should enter a dictionary where keys are prefixes and values namespaces
- Unlike `findall()`, `xpath()` does not accept Clark's notation

### XSLT

XSLT stands for *Extensible Stylesheet Language Transformations*. It's an xml-based language made for transforming xml documents to xml or other formats such as LaTeX and HTML. XSLT is really powerful when dealing with similarly formated data. It's far easier to transform 100 documents with the exact same structure via XSLT than in Python or any other language.

While Python is great at dealing with weird transformations of xml, the presence of XSLT in Python allows you to create production chains without leaving your favorite IDE.

To do some XSL, lxml needs two things : first, an xml document representing the xsl that will be parsed and entered into the function `etree.XSLT()`, and second, a document to transform. 


```python
# Here is an xml containing an xsl: for each text node of an xml file in the xpath /humanities/field,
#     this will return a node <name> with the text inside
xslt_root = etree.fromstring("""
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <fields><xsl:apply-templates /></fields>
    </xsl:template>
    <xsl:template match="/humanities/field">
        <name><xsl:value-of select="./text()" /></name>
    </xsl:template>
</xsl:stylesheet>""")
# We transform our document to an xsl 
xslt = etree.XSLT(xslt_root)

# We create some xml we need to change 
xml = """<humanities>
    <field>History</field>
    <field>Classics</field>
    <field>French</field>
    <field>German</field>
</humanities>"""
parsed_xml = etree.fromstring(xml)
# And now we process our xml :
transformed = xslt(parsed_xml)
print(transformed)
```

    <?xml version="1.0"?>
    <fields>
        <name>History</name>
        <name>Classics</name>
        <name>French</name>
        <name>German</name>
    </fields>
    
    

Did you see what happened ? We used `xslt(xml)`. `etree.XSLT()` transforms a xsl document into a function, which then takes one parameter (in this case an xml document). But can you figure out what this returns ? Let's ask Python :


```python
print(type(transformed))
print(type(parsed_xml))
```

    <class 'lxml.etree._XSLTResultTree'>
    <class 'lxml.etree._Element'>
    

The result is not of the same type of element we usually have, even though it does share most of its methods and attributes :


```python
print(transformed.xpath("//name"))
```

    [<Element name at 0x262a25c9688>, <Element name at 0x262a25bdfc8>, <Element name at 0x262a25bddc8>, <Element name at 0x262a25bde88>]
    

And has something more : you can change its type to string !


```python
string_result = str(transformed)
print(string_result)
```

    <?xml version="1.0"?>
    <fields>
        <name>History</name>
        <name>Classics</name>
        <name>French</name>
        <name>German</name>
    </fields>
    
    

XSLT is more complex than just inputing xml. You can do XSLT using parameters as well. In this case, your parameters will be accessibles as a named argument to the generated function. If your XSL has a `name` xsl-param, the function given back by `etree.XSLT` will have a `name` argument :


```python
# Here is an xml containing an xsl: for each text node of an xml file in the xpath /humanities/field,
#     this will return a node <name> with the text inside
xslt_root = etree.fromstring("""
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="n" />
    <xsl:template match="/humanities">
        <fields>
            <xsl:attribute name="n">
                <xsl:value-of select="$n"/>
            </xsl:attribute>
            <xsl:apply-templates select="field"/>
        </fields>
    </xsl:template>
    <xsl:template match="/humanities/field">
        <name><xsl:value-of select="./text()" /></name>
    </xsl:template>
</xsl:stylesheet>""")
# We transform our document to an xsl 
xslt = etree.XSLT(xslt_root)

# We create some xml we need to change 
xml = """<humanities>
    <category>Humanities</category>
    <field>History</field>
    <field>Classics</field>
    <field>French</field>
    <field>German</field>
</humanities>"""
parsed_xml = etree.fromstring(xml)
# And now we process our xml :
transformed = xslt(parsed_xml, n="'Humanities'") # Note that for a string, we encapsulate it within single quotes
print(transformed)

# Be aware that you can use xpath as a value for the argument, though it can be rather complex sometimes
transformed = xslt(parsed_xml, n=etree.XPath("//category/text()"))
print(transformed)
```

    <?xml version="1.0"?>
    <fields n="Humanities"><name>History</name><name>Classics</name><name>French</name><name>German</name></fields>
    
    <?xml version="1.0"?>
    <fields n="Humanities"><name>History</name><name>Classics</name><name>French</name><name>German</name></fields>
    
    

# Using ElementTree
----


```python
from xml.etree import ElementTree

with open('data/books.xml', 'rt') as f:
    tree = ElementTree.parse(f)

print(tree)
```

    <xml.etree.ElementTree.ElementTree object at 0x0000028AF484AE10>
    

## Traversing the Parsed Tree
---
To visit all of the children in order, use iter() to create a generator that iterates over the ElementTree instance.


```python
from xml.etree import ElementTree

with open('data/books.xml', 'rt') as f:
    tree = ElementTree.parse(f)

# print(dir(tree))

for node in tree.iter():
    print (node.tag, node.attrib)
    print("-----")
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_root', '_setroot', 'find', 'findall', 'findtext', 'getiterator', 'getroot', 'iter', 'iterfind', 'parse', 'write', 'write_c14n']
    catalog {}
    -----
    book {'id': 'bk101'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk102'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk103'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk104'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk105'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk106'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk107'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk108'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk109'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk110'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk111'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    book {'id': 'bk112'}
    -----
    author {}
    -----
    title {}
    -----
    genre {}
    -----
    price {}
    -----
    publish_date {}
    -----
    description {}
    -----
    


```python
### To print only the groups of names and feed URLs for the podcasts, 
# leaving out of all of the data in the header section by iterating 
# over only the outline nodes and print the text and xmlUrl attributes.

from xml.etree import ElementTree

with open('data/podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter('outline'):
    name = node.attrib.get('text')
    url = node.attrib.get('xmlUrl')
    if name and url:
        print ('\t%s :: %s' % (name, url))
    else:
        print (name)

```

    Science and Tech
    	APM: Future Tense :: http://www.publicradio.org/columns/futuretense/podcast.xml
    	Engines Of Our Ingenuity Podcast :: http://www.npr.org/rss/podcast.php?id=510030
    	Science & the City :: http://www.nyas.org/Podcasts/Atom.axd
    Books and Fiction
    	Podiobooker :: http://feeds.feedburner.com/podiobooks
    	The Drabblecast :: http://web.me.com/normsherman/Site/Podcast/rss.xml
    	tor.com / category / tordotstories :: http://www.tor.com/rss/category/TorDotStories
    Computers and Programming
    	MacBreak Weekly :: http://leo.am/podcasts/mbw
    	FLOSS Weekly :: http://leo.am/podcasts/floss
    	Core Intuition :: http://www.coreint.org/podcast.xml
    Python
    	PyCon Podcast :: http://advocacy.python.org/podcasts/pycon.rss
    	A Little Bit of Python :: http://advocacy.python.org/podcasts/littlebit.rss
    	Django Dose Everything Feed :: http://djangodose.com/everything/feed/
    Miscelaneous
    	dhellmann's CastSampler Feed :: http://www.castsampler.com/cast/feed/rss/dhellmann/
    

### Finding Nodes in a Document¶

Walking the entire tree like this searching for relevant nodes can be error prone. The example above had to look at each outline node to determine if it was a group (nodes with only a text attribute) or podcast (with both text and xmlUrl). To produce a simple list of the podcast feed URLs, without names or groups, for a podcast downloader application, the logic could be simplified using findall() to look for nodes with more descriptive search characteristics.

As a first pass at converting the above example, we can construct an XPath argument to look for all outline nodes.


```python

for node in tree.findall('.//outline'):
    url = node.attrib.get('xmlUrl')
    if url:
        print( url)
    else:
        print(node.attrib.get("text"))
```

    Science and Tech
    http://www.publicradio.org/columns/futuretense/podcast.xml
    http://www.npr.org/rss/podcast.php?id=510030
    http://www.nyas.org/Podcasts/Atom.axd
    Books and Fiction
    http://feeds.feedburner.com/podiobooks
    http://web.me.com/normsherman/Site/Podcast/rss.xml
    http://www.tor.com/rss/category/TorDotStories
    Computers and Programming
    http://leo.am/podcasts/mbw
    http://leo.am/podcasts/floss
    http://www.coreint.org/podcast.xml
    Python
    http://advocacy.python.org/podcasts/pycon.rss
    http://advocacy.python.org/podcasts/littlebit.rss
    http://djangodose.com/everything/feed/
    Miscelaneous
    http://www.castsampler.com/cast/feed/rss/dhellmann/
    


```python
print(dir(tree))
print(tree.getroot)
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_root', '_setroot', 'find', 'findall', 'findtext', 'getiterator', 'getroot', 'iter', 'iterfind', 'parse', 'write', 'write_c14n']
    <bound method ElementTree.getroot of <xml.etree.ElementTree.ElementTree object at 0x0000028AF4878320>>
    

Another version can take advantage of the fact that the outline nodes are only nested two levels deep. Changing the search path to .//outline/outline mean the loop will process only the second level of outline nodes.


```python
for node in tree.findall('.//outline/outline'):
    url = node.attrib.get('xmlUrl')
    print (url)
```

    http://www.publicradio.org/columns/futuretense/podcast.xml
    http://www.npr.org/rss/podcast.php?id=510030
    http://www.nyas.org/Podcasts/Atom.axd
    http://feeds.feedburner.com/podiobooks
    http://web.me.com/normsherman/Site/Podcast/rss.xml
    http://www.tor.com/rss/category/TorDotStories
    http://leo.am/podcasts/mbw
    http://leo.am/podcasts/floss
    http://www.coreint.org/podcast.xml
    http://advocacy.python.org/podcasts/pycon.rss
    http://advocacy.python.org/podcasts/littlebit.rss
    http://djangodose.com/everything/feed/
    http://www.castsampler.com/cast/feed/rss/dhellmann/
    

### Parsed Node Attributes

The items returned by findall() and iter() are Element objects, each representing a node in the XML parse tree. Each Element has attributes for accessing data pulled out of the XML. This can be illustrated with a somewhat more contrived example input file, data.xml:


```python
from xml.etree import ElementTree

with open('data/data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

node = tree.find('./with_attributes')
print (node.tag)
for name, value in sorted(node.attrib.items()):
    print ('  %-4s = "%s"' % (name, value))
```

    with_attributes
      foo  = "bar"
      name = "value"
    


```python
for path in [ './child', './child_with_tail' ]:
    node = tree.find(path)
    print( node.tag)
    print ('  child node text:', node.text)
    print ('  and tail text  :', node.tail)
```

    child
      child node text: This child contains text.
      and tail text  : 
      
    child_with_tail
      child node text: This child has regular text.
      and tail text  : And "tail" text.
      
    

### Parsing Strings 

To work with smaller bits of XML text, especially string literals as might be embedded in the source of a program, use XML() and the string containing the XML to be parsed as the only argument.


```python
from xml.etree.ElementTree import XML

parsed = XML('''
<root>
  <group>
    <child id="a">This is child "a".</child>
    <child id="b">This is child "b".</child>
  </group>
  <group>
    <child id="c">This is child "c".</child>
  </group>
</root>
''')

print ('parsed =', parsed)

for elem in parsed:
    print (elem.tag)
    if elem.text is not None and elem.text.strip():
        print ('  text: "%s"' % elem.text)
    if elem.tail is not None and elem.tail.strip():
        print ('  tail: "%s"' % elem.tail)
    for name, value in sorted(elem.attrib.items()):
        print('  %-4s = "%s"' % (name, value))
    print
```

    parsed = <Element 'root' at 0x00000262A2604228>
    group
    group
    


```python
from xml.etree.ElementTree import Element, tostring


top = Element('top')

children = [
    Element('child', num=str(i))
    for i in range(3)
]

top.extend(children)

print(top)
```

    <Element 'top' at 0x0000028AF48A0598>
    


```python

```
