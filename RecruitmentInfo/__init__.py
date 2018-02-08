#!/usr/bin/env python
#-*-coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import urlparse
import re


def getNextUrl(soup, current_url):
    if current_url is None:
        return None
    next_page = soup.find('a', class_='Next')
    return next_page


def getCurrentInfo(res_data, soup):
    if soup is None:
        return None
    link_base = 'http://jiuye.www.sust.edu.cn'
    links = soup.find_all('a', href=re.compile(r"/new.jsp?"))
    for link in links:
        new_url = link['href']
        new_full_url = urlparse.urljoin(link_base, new_url)
        res_data['url'] = new_full_url
        res_data['title'] = link['title']
        #print new_full_url
        #print link['title']

    times = soup.find_all('td', width='20%')
    for time in times:
        res_data.add(times)
        #print time.get_text()

    locals = soup.find_all('td', width='30%')
    for local in locals:
        res_data['local'] = local.get_text()
        #print local.get_text()


def getNextSoup(next_page):
    if next_page is None:
        return None
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    rsp = urllib2.Request(next_page, headers=headers)
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf8')
    return soup


def outputHtml(res_data):
    if res_data is None:
        return None
    fout = open('output.html', 'w')

    fout.write("<html>")
    fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
    fout.write("<body>")
    fout.write("<body>")
    fout.write("<table>")

    # ASCII
    for data in res_data:
        fout.write("<tr>")
        fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
        fout.write("<td>%s</td>" % data['local'].encode('utf-8'))
        fout.write("<td>%s</td>" % data['time'].encode('utf-8'))
        fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
        fout.write("</tr>")

    fout.write("</table>")
    fout.write("</body>")
    fout.write("</html>")

    fout.close()

if __name__ == '__main__':
    root_url = 'http://jiuye.www.sust.edu.cn/zph.jsp?urltype=tree.TreeTempUrl&wbtreeid=1003'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    rsp = urllib2.Request(root_url, headers=headers)
    content = urllib2.urlopen(rsp).read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf8')

    res_data = {}
    next_page_base = 'http://jiuye.www.sust.edu.cn/zph.jsp'
    current_url = root_url
    i = 0
    while i < 3:
        getCurrentInfo(res_data, soup)
        print res_data['title']
        print res_data['time']
        print res_data['local']

        next_page = getNextUrl(soup, current_url)
        print next_page['href']
        i+=3

    #outputHtml(res_data)
    #找到前三页的网址
    #top_three = list
    #http://jiuye.www.sust.edu.cn/zph.jsp?a47862t=239&a47862p=2&a47862c=15&urltype=tree.TreeTempUrl&wbtreeid=1003
    #                                    ?a47862t=239&a47862p=2&a47862c=15&urltype=tree.TreeTempUrl&wbtreeid=1003
    #首先解析 root_url
    #得到下一页 url，当前页所有招聘公司 url、 公司名、招聘地点、时间
    #循环三次，得到前三页的信息
    #输出为 html 文件
