import nltk
from urllib.request import urlopen

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
print(html)
