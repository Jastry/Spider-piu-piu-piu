#!/usr/bin/env python
#-*-coding:utf-8 -*-
import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        rsp = urllib2.urlopen(url)

        if rsp.getcode() != 200:
            return None

        return rsp.read()
