# -*- coding: utf-8 -*-
#
# Funciones para el query.php
# 

import re, urllib, urllib2, httplib

def pageQuery(url):
    request=urllib2.Request(url)
    user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7'
    request.add_header("User-Agent", user_agent)
    request.add_header("Accept-Charset", 'utf-8')
    response=urllib2.urlopen(request)
    text=response.read()
    response.close()
    text=unicode(text,'utf-8')
    m=re.compile(ur"<title>(.*?)</title>").finditer(text)
    encontrados=[]
    for i in m:
        encontrados.append(i.group(1))
    return encontrados        

def trurlQuery(userinput):
	return urllib.quote(userinput.encode('utf-8', 'replace'))

def fetchQuery(iniciales,project='es',family='wikipedia'):
	query=[]
	query=pageQuery('http://'+project+'.'+family+'.org/w/query.php?what=allpages&aplimit=100&apnamespace=0&apfrom='+trurlQuery(iniciales)+'&apfilterredir=nonredirects&format=xml')
	return query
