# https://www.geeksforgeeks.org/python-urllib-module/
# https://www.journaldev.com/20795/python-urllib-python-3-urllib
# https://christophergs.github.io/python/2016/12/03/python-urllib-parse/

# ______________________________________________________________________


# urllib.request

import urllib.request 

# This module helps to define functions and classes to open URLs (mostly HTTP). 
# One of the most simple ways to open such URLs is :
# urllib.request.urlopen(url)



request_url = urllib.request.urlopen('https://github.com/')

# print(request_url.read())   # or you can do:

with open('./file/test_site_01.html', 'w') as file:
    file.write(str(request_url.read()))


# ______________________________________________________________________

# urllib.parse

# This module helps to define functions to manipulate URLs and their components 
# parts, to build or break them. It usually focuses on splitting a URL into small 
# components; or joining different URL components into URL string.

# _____________________________

# urlparse 

from urllib.parse import urlparse 

parse_url = urlparse('https://www.facebook.com')
print(parse_url,'\n')

parse_url = urlparse('https://www.facebook.com/joellemt')
print(parse_url,'\n')

parse_url = urlparse('https://www.facebook.com/joellemt/about?lst=100001388624544%3A1086104530%3A1575451430')
print(parse_url,'\n') 

# _____________________________

# urlsplit
# Very similar to urlparse except that it does not split the params from the URL, 
# meaning that it returns 5 components  instead of 6.

from urllib.parse import urlsplit

split_url = urlsplit('https://www.facebook.com/joellemt/about?lst=100001388624544%3A1086104530%3A1575451430')
print(split_url,'\n') 

# _____________________________

# urljoin
# Construct a complete/new URL from a base and an additional string. 
# Note that when working with URLs, you want to use this method and not 
# os.path.join as the latter will not give the desired effect on Windows

from urllib.parse import urljoin

base_url = 'https://docs.python.org'
addition = '3/library/urllib.parse.html#module-urllib.parse'
url = urljoin(base_url, addition)
print('',base_url,'\n',url,'\n')

# _____________________________