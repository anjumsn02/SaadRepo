
from urlparse import urljoin
from HTMLParser import HTMLParser

class Linkfinder(HTMLParser):

    def __init__(self, baseurl, pageurl):
        HTMLParser.__init__(self)
        self.all_data=[]
        self.baseurl = baseurl
        self.pageurl = pageurl
        self.links = set()

    def handle_starttag(self, tag, attrs):
       if tag == 'a':
            for(attribute, value) in attrs:
                if attribute == 'href':
                    url = urljoin(self.baseurl, value)
                    self.links.add(url)

    def page_links(self):
       return  self.links

    def error(self, message):
        pass
