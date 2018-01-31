#!/usr/bin/env python
#-*-coding:utf-8 -*-

import urllib2

import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, url):
        html_cont = self.downloader.download(url)
        weather_data = self.parser.parse(url, html_cont)
        self.outputer.collect_data(weather_data)
        self.outputer.output_html()

if __name__=='__main__':
    #root_url = 'http://www.nmc.gov.cn/publish/forecast/ASN/xi-an.html'
    root_url = 'https://weather.com/zh-CN/weather/today/l/CHXX0141:1:CH'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
