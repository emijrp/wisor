# -*- coding: utf-8 -*-
#
# Funciones hacer peticiones de red
#

#TODO: detectar 404s
#TODO: detectar Redirecciones
#TODO: función para mostrar los Special:Prefixindex
#TODO: el Special:Random


import urllib, urllib2, httplib,re

class fetchError(Exception):
    """Wikipedia error"""

def pageText(url):
    request=urllib2.Request(url)
    user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7'
    request.add_header("User-Agent", user_agent)
    request.add_header("Accept-Charset", 'utf-8')
    response=urllib2.urlopen(request)
    text=response.read()
    response.close()
    return unicode(text,'utf-8')

def trurl(userinput):
	return urllib.quote(userinput.encode('utf-8', 'replace'))

def fetch(pagina,project='es',family='wikipedia'):
	try:
		raw=pageText('http://'+project+'.'+family+'.org/w/index.php?title='+trurl(pagina)+'&action=raw')
	except urllib2.HTTPError:
		raise fetchError
	return raw

def fetchprefindex(iniciales,project='es',family='wikipedia'):
	text=pageText('http://'+project+'.'+family+'.org/w/query.php?what=allpages&aplimit=100&apnamespace=0&apfrom='+trurl(iniciales)+'&apfilterredir=nonredirects&format=xml')
	m=re.compile(ur"<title>(.*?)</title>").finditer(text)
	encontrados=[]
	for i in m:
		encontrados.append(i.group(1))
	return encontrados