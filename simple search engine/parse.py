from html.parser import HTMLParser
from html.entities import name2codepoint

class parse(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []
#    def handle_starttag(self, tag, attrs):
#        print('<%s>' % tag)

#    def handle_endtag(self, tag):
#        print('</%s>' % tag)

#    def handle_startendtag(self, tag, attrs):
#        print('<%s/>' % tag)

    def handle_data(self, data):
        self.data.append(data)

#    def handle_comment(self, data):
#        print('<!--', data, '-->')

#    def handle_entityref(self, name):
#        print('&%s;' % name)

#    def handle_charref(self, name):
#        print('&#%s;' % name)



