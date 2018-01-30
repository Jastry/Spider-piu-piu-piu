#!/usr/bin/env python
#-*-coding:utf-8 -*-
class UrlMannager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            print '添加成功'
            self.new_urls.add(url)

    #添加新的 url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            print url
            self.add_new_url(url)

    #判断管理器中是否有这个 url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #获取一个新的 url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

