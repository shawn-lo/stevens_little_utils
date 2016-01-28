import urllib.request
from lxml import etree
from StringIO import StringIO

def download(url, index):
    #response = urllib2.urlopen(url)
    with urllib.request.urlopen(url) as response:
        pdf = response.read()
    with open("./chapter %s.pdf"%index, 'wb') as file:
        file.write(pdf)
    print('file %s completed.'%index)

if __name__ == '__main__':
    for i in range(1,21):
        url = 'http://www.farinhansford.com/books/pla/material/chap%s.pdf'%i
        download(url,i)
