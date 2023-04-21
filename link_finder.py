from html.parser import HTMLParser
from urllib import parse
from general import *


class LinkFinder(HTMLParser):

    def __init__(self,base_url,page_url,project_name):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.links=set()
        self.is_it_paragraph=0
        self.content_file=project_name+'/content.txt'
        
    def handle_starttag(self,tag,attrs):
        if tag=='p':
            self.is_it_paragraph=1
        else:
            self.is_it_paragraph=0
            
        if tag=='a':
            for (attribute,value) in attrs:
                if attribute=='href':
                    url=parse.urljoin(self.base_url,value)
                    self.links.add(url)
    
    def handle_data(self, data):
        if self.is_it_paragraph==1:
           append_to_file(self.content_file,data)
        
    def page_links(self):
        return self.links

    def error(self,message):
        pass


#finder=LinkFinder('smartportal','/asd')
#finder.feed('<html><head><title>asd</title></head><body><h1>Parse me! </h1></body></html>')
