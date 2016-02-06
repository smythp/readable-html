import urllib.request
from readability.readability import Document
import urllib
import sys

url_in = "https://torrentfreak.com/paypal-starts-banning-vpn-and-smartdns-services-160205/"

print(type(url_in))

with urllib.request.urlopen(url_in) as url:
    html = url.read()
    print(type(html))
    readable_article = Document(html).summary()
    print(type(readable_article))
#    readable_title = Document(html).short_title()
#    sys.stdout.write(readable_article)
