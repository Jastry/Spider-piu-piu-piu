#!/usr/bin/env python
#-*-coding:utf-8 -*-
import urllib2

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        rsp = urllib2.Request(url)
        rsp.add_header('User-Agent', ' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')
        #Referer: http://www.nmc.gov.cn/publish/forecast/ASN/xi-an.html
        rsp.add_header('Referer', 'http://www.nmc.gov.cn/publish/forecast/ASN/xi-an.html')
        rsp = urllib2.urlopen(url)
        if rsp.getcode() != 200:
            return None
        return rsp.read()
