import urllib2
response = urllib2.urlopen("https://money.cnn.com")
print (response.read())
print (re.search(r'<ul class="module-body wsod currencies">(.*?)</ul>', source).group(1))

