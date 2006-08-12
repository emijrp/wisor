# -*- coding: utf-8 -*-
#
# Funciones hacer peticiones de red
#
import urllib, urllib2, httplib

def pageText(url):
    request=urllib2.Request(url)
    user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7'
    #print url
    request.add_header("User-Agent", user_agent)
    response=urllib2.urlopen(request)
    text=response.read()
    response.close()
    return text

def trurl(userinput):
	return urllib.quote(userinput.encode('utf-8', 'replace'))

def fetch(pagina,project='es',family='wikipedia'):
	raw=pageText('http://'+project+'.'+family+'.org/w/index.php?title='+pagina+'&action=raw')
	return raw