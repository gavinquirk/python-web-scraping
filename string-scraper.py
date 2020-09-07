from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/aphrodite"

# Open the page, returning an HTTPResponse Object
page = urlopen(url)

# The page is is returned in bytes, and must be decoded
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

# Text can be extracted by using string methods. This is generally unreliable as trailing spaces
# or unexpected characters can cause the index to be incorrect.
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
