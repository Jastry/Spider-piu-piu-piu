#!/usr/bin/env python
#-*-coding=utf8-*-

import url_manager
import html_downloader
import html_parser
import html_output

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlMannager()                   #url管理器
        self.downloader = html_downloader.HtmlDownloader()      #网页下载
        self.parser = html_parser.HtmlParser()                  #解析器
        self.outputer = html_output.HtmlOutputer()              #输出结果

    #爬虫调度程序
    def craw(self, root_url):
        #记录第几个 url
        count = 1
        #初始化的 url
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            print '走到这里了'

            try:
                #从管理器中获取一个待爬 url
                new_url = self.urls.get_new_url()
                print "craw %d : %s" % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                #将新的 url 添加到 url 管理器
                self.urls.add_new_urls(new_urls)

                #输出器收集数据
                self.outputer.collect_data(new_data)

                if count == 10:
                    break

                count = count + 1
            except:
                print 'craw failed'
        #将结果输出
        self.outputer.output_html()

if __name__=="__main__":

    root_url = 'https://baike.baidu.com/item/Python/407313'
    #root_url = 'https://baike.baidu.com/item/%E6%8C%87%E9%92%88'

    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

