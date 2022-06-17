
# Web scraping with Python

This is an introduction to web scraping using Python, where our task is to extract information from web pages.

Prerequisites (knowledge):

 * basic Python (its data structures, string manipulation)
 * basic HTML
 * basic HTTP (know what a GET request is: this will be reviewed)
 * bonus: knowledge of how to use XPath

Prerequisites (software):

 * the `lxml` package

Rather than using Scrapy or another Python web scraping framework, we'll go the barebones route.

## HTTP basics

HTTP is a protocol for transferring data across the internet. Every communication looks like this: a **client** (such as a browser) sends a request to a **web server**, and the server sends a response back to the client.

There's a few types of **requests** that the client can send, such as the `GET` and `POST` request types.

* The `GET` request is the most common type. Semantically, it is used for requesting data from the web server. 
* `POST` requests are usually used when we're sending data to the server that's large or changes some kind of state on the server, such as if it causes a database to be updated.

The request and **response** each follow a simple text-based format: the first line is specific to requests and responses, then several lines of headers are specified in a `Header-Name: value` format, then a blank line follows the headers and precedes the body. The body contains the main payload, and a header tells the client/server how large the body is.

An example request (from Wikipedia):

    GET /index.html HTTP/1.1
    Host: www.example.com

And a corresponding response, showing us a status code (everyone's seen 404 Not Found) among other things:

    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: "3f80f-1b6-3e1cb03b"
    Content-Type: text/html; charset=UTF-8
    Content-Length: 131
    Connection: close
    
    <html>
    <head>
      <title>An Example Page</title>
    </head>
    <body>
      Hello World, this is a very simple HTML document.
    </body>
    </html>

The body doesn't necessarily have to be plain text as in this example: it could be a sequence of non-text bytes whose length is specified by `Content-Length`.

Let's try simulating that same request.


```
import urllib2
response = urllib2.urlopen("http://example.com")
print response.read()
```

    <!doctype html>
    <html>
    <head>
        <title>Example Domain</title>
    
        <meta charset="utf-8" />
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
        body {
            background-color: #f0f0f2;
            margin: 0;
            padding: 0;
            font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
            
        }
        div {
            width: 600px;
            margin: 5em auto;
            padding: 50px;
            background-color: #fff;
            border-radius: 1em;
        }
        a:link, a:visited {
            color: #38488f;
            text-decoration: none;
        }
        @media (max-width: 700px) {
            body {
                background-color: #fff;
            }
            div {
                width: auto;
                margin: 0 auto;
                border-radius: 0;
                padding: 1em;
            }
        }
        </style>    
    </head>
    
    <body>
    <div>
        <h1>Example Domain</h1>
        <p>This domain is established to be used for illustrative examples in documents. You may use this
        domain in examples without prior coordination or asking for permission.</p>
        <p><a href="http://www.iana.org/domains/example">More information...</a></p>
    </div>
    </body>
    </html>
    
    

Python's `urlopen` function in the `urllib2` module returns a file-like object, so we can call `read()` to read all its contents.

We can access the response's headers, too, using the `.info()` method of the response object. It returns a `mimetools.Message` instance that we can use like a `dict`:


```
print response.info()
print "The content type is '%s'." % response.info()['content-type']
```

    Accept-Ranges: bytes
    Content-Type: text/html; charset=UTF-8
    Date: Tue, 02 Jul 2013 05:54:23 GMT
    ETag: "780602-4f6-4db31b2978ec0"
    Last-Modified: Thu, 25 Apr 2013 16:13:23 GMT
    Server: ECS (sea/1C15)
    X-Cache: HIT
    Content-Length: 1270
    Connection: close
    
    The content type is 'text/html; charset=UTF-8'.
    

This was a simple `GET` request. We can also send `POST` requests using the `data` keyword argument of the `urlopen()` function.

## Massaging out information

For those familiar with regular expressions (affectionately referred to as regex's), regexes look like something we could use here to extract information from HTML. That's partially correct.

Let's try extracting the page title of a website.


```
import re

source = urllib2.urlopen("http://ncix.com").read()
print re.search(r'<title>(.*?)</title>', source).group(1)
```

    NCIX.com - Canada's Premier Computer Store - Online PC Discount Store, Buy Computer Accessories
    

We can handle simple stuff with regexes, but HTML tags are simply too complicated for all but the simplest of cases.
A tag with attributes can span multiple lines, there can be arbitrary whitespace in a tag, etc.
However, regexes will still prove useful to process text that's inside an HTML page, and might be useful for extracting text from some Javascript source in a page.

What can we do instead? HTML, like XML, has a recursive containment structure, so lends itself well to a recursive (nested) data structure with classes representing each tag. There's parsers for HTML source that nicely handle constructing these representations of HTML. For Python, we've got

* BeautifulSoup
* html5lib
* lxml (a wrapper for the C++ libxml library)

We'll stick with the last one, but the other two are good too.

Let's try using it to read all the `<a>` tags (hyperlinks) from the NCIX homepage.


```
import lxml.html
html = lxml.html.fromstring(source)
print html.xpath('//a')[:10]  # just print out the first 10
```

    [<Element a at 0x1bd7170>, <Element a at 0x1bd7050>, <Element a at 0x1bd7110>, <Element a at 0x1bd70b0>, <Element a at 0x1bd71d0>, <Element a at 0x1bd7230>, <Element a at 0x1bd7290>, <Element a at 0x1bd72f0>, <Element a at 0x1bd7350>, <Element a at 0x1bd73b0>]
    

So, we've got a bunch of `<a>` tags. The `xpath()` method performs an **XPath query**. XPath is a query language for XML that searches the hierarchical structure that XML or HTML has (called the DOM or Document Object Model).

Our query was `//a`. An XPath query consists of slash-delimited parts. Here, the double slash `//` means "any number of parents", followed by an `<a>` tag.

Using an HTML inspector like the one built into Google Chrome (press F12 to activate it on a page), we can determine what the structure of a certain node in the DOM is. For example, if we open up the NCIX page and inspect the "Popular Categories" on the side, we find that each category link is inside a certain `div` tag:

    <div id="sublinks"> ...

and each link looks like:

    <a href="http://www.ncix.com/products/?minorcatid=1263" class="sub_link">Blu-Ray Drives<span class="qtycount"> (6)</span></a>

Let's grab all of these links using an Xpath query. In XPath, an at-sign `@` before an identifier means "attribute":


```
html.xpath('//div[@id="sublinks"]/a[@class="sub_link"]/@href')
```




    ['http://ncix.com/products/?minorcatid=1263',
     'http://ncix.com/products/?minorcatid=1265',
     'http://ncix.com/products/?minorcatid=1084',
     'http://ncix.com/products/?minorcatid=1015',
     'http://ncix.com/products/?minorcatid=104',
     'http://ncix.com/products/?minorcatid=1228',
     'http://ncix.com/products/?minorcatid=1303',
     'http://ncix.com/products/?minorcatid=1020',
     'http://ncix.com/products/?minorcatid=1272',
     'http://ncix.com/products/?minorcatid=109',
     'http://ncix.com/products/?minorcatid=1031',
     'http://ncix.com/products/?minorcatid=1051',
     'http://ncix.com/products/?minorcatid=101',
     'http://ncix.com/products/?minorcatid=1032',
     'http://ncix.com/products/?minorcatid=1003',
     'http://ncix.com/products/?minorcatid=1331',
     'http://ncix.com/products/?minorcatid=102',
     'http://ncix.com/products/?minorcatid=1216',
     'http://ncix.com/products/?minorcatid=107',
     'http://ncix.com/products/?minorcatid=1045',
     'http://ncix.com/products/?minorcatid=1004',
     'http://ncix.com/products/?minorcatid=1191',
     'http://ncix.com/products/?minorcatid=1005',
     'http://ncix.com/products/?minorcatid=1055',
     'http://ncix.com/products/?minorcatid=1066',
     'http://ncix.com/products/?minorcatid=106',
     'http://ncix.com/products/?minorcatid=1012',
     'http://ncix.com/products/?minorcatid=1019',
     'http://ncix.com/products/?minorcatid=1275',
     'http://ncix.com/products/?minorcatid=103',
     'http://ncix.com/products/?minorcatid=1036',
     'http://ncix.com/products/?minorcatid=108']



Here strings got returned directly because we requested the `href` attributes. But instead, we could've gotten a bunch of `Element` instances and manipulated these. This is useful when you want to do some more complex manipulation, or if you want to extensively query the children of a specific element.
