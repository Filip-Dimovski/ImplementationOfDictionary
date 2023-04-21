
from urllib.parse import urlparse

#get domain name(example.com)
def get_domain_name(url):
    try:
        results=get_sub_domain_name(url).split('.')
        if results[-2]=='com':
            return results[-3]+'.'+results[-2]+'.'+results[-1]
        
        return results[-2]+'.' + results[-1]
    except:
        return
    
# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


#print(get_domain_name('http://www.femina.mk'))
#print(get_domain_name('http://www.femina.mk/asdas/wqea'))
#print(get_domain_name('http://www.mail.example.com.mk/asd/dsa/as.html'))
    
