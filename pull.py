import requests
from readability.readability import Document

url_in = "" # put url here

r = requests.get(url_in)
# print(r.status_code)

html = r.text

with open('out.html','w') as out_file:
    readable_article = Document(html).summary()
    readable_article = readable_article.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c","\"").replace(u"\u201d", "\"")
    out_file.write("<!DOCTYPE html>\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\" /></head>")
    out_file.write(readable_article[6:])
