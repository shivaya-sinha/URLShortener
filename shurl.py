#!/usr/bin/python
 
from sys import argv
import httplib2
import simplejson as json
 
API_KEY = ENTER_YOUR_API_KEY_HERE           
 
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
	print response 
        short_url = json.loads(response)['id']
 
    except Exception, e:
        print "unexpected error %s" % e
    short_url = "ERROR"     
    return short_url
		 
if __name__ == '__main__':
    short_url = shurl(argv[1])
    print "**************************"
    print short_url
    print "**************************\n"

