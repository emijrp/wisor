# -*- coding: utf-8 -*-
import wx,thread,re,time
import wx.html
import Page,Historial,query

def pageParse(texto):
        html=texto
        
        html=re.sub(ur"\n", ur"<br />", html)
        html=re.sub(ur"'''(.*?)'''", ur"<b>\1</b>", html)
        html=re.sub(ur"''(.*?)''", ur"<i>\1</i>", html)
        html=re.sub(ur"^===(.*?)===", ur"<h3>\1</h3>", html)
        html=re.sub(ur"^==(.*?)==", ur"<h2>\1</h2>", html)
        html=re.sub(ur"^=(.*?)=", ur"<h1>\1</h1>", html)
                
        html=re.sub(ur"\[\[(.*?)\]\]", ur"<a href='http://es.wikipedia.org/wiki/\1'>\1</a>", html)
        return html
