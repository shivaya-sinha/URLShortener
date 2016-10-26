#!/usr/bin/python
 
from sys import argv
import httplib2
import simplejson as json
 
API_KEY = ENTER_YOUR_API_KEY_HERE  
#The API key can be obtained by visiting the Google Developers Console 

 
def shurl(longUrl):
    
    try: API_KEY
    except NameError:
        apiUrl = 'https://www.googleapis.com/urlshortener/v1/url'    
    else:
        apiUrl = 'https://www.googleapis.com/urlshortener/v1/url?key=%s' % API_KEY
    
    headers = {"Content-type": "application/json"}
    data = {"longUrl": longUrl}
    h = httplib2.Http('.cache')
    try:
        headers, response = h.request(apiUrl, "POST", json.dumps(data), headers)
        short_url = json.loads(response)['id']
 
    except Exception, e:
        print "unexpected error %s" % e
    short_url = "Not Found"
    return short_url

def expand(shortUrl) : 
    apiUrl = "https://www.googleapis.com/urlshortener/v1/url?key=%s&shortUrl=%s" % (API_KEY, shortUrl)
    headers, response = httplib2.Http().request(apiUrl);
    long_url = json.loads(response)['longUrl']
    return longUrl 


		 
if __name__ == '__main__':
    if argv[1] == '-e' :
        result = expand(argv[2])      
    else :
        result = shurl(argv[1])
        
    print "**************************"
    print result
    print "**************************\n"

