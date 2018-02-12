#!/usr/bin/env python
#-*-coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import urlparse
import re

def getHtmlInfo(root_url, res_data):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    rsp = urllib2.Request(root_url, headers=headers)
    content = urllib2.urlopen(rsp).read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf8')
    base_url = 'http://jiuye.www.sust.edu.cn'

    #<tr style="line-height:180%;border-bottom: 1px dotted #cccccc;font-size:10pt;">
    all_info = soup.find_all('tr', style=re.compile(r'ine-height'))
    next_info = soup.find('a', class_='Next')
    next_page = next_info['href']
    #<a href="/new.jsp?urltype=news.NewsContentUrl&amp;wbtreeid=1003&amp;wbnewsid=11042" target="_blank" title="2017年常州市赴陕西科技大学校园专场招聘会" style="">2017年常州市赴陕西科技大学校园专场招聘会</a>
    for info in all_info:
        data = {}
        url_title = info.find('a', href=re.compile(r'/new.jsp?'))
        times = info.find('td', width='20%')
        locals = info.find('td', width='30%')
        local = locals.get_text()
        new_url = url_title['href']
        new_full_url = urlparse.urljoin(base_url, new_url)
        title = url_title['title']
        time = times.get_text().strip()
        data['url'] = new_full_url
        data['title'] = title
        data['time'] = time
        data['local'] = local
        res_data.append(data)

    return next_page


def outputHtml(res_data):
    fout = open('output.html', 'w')

    fout.write("<html>")
    fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
    fout.write("<body>")
    fout.write("<body>")
    fout.write("<table>")

    # ASCII
    for data in res_data:
        fout.write("<tr>")
        #<a href="/new.jsp?urltype=news.NewsContentUrl&amp;wbtreeid=1003&amp;wbnewsid=11042" target="_blank" title="2017年常州市赴陕西科技大学校园专场招聘会" style="">2017年常州市赴陕西科技大学校园专场招聘会</a>
        fout.write("<td>")
        fout.write("<a href=%s>" % data['url'].encode('utf-8'))
        fout.write("%s</a>"  % data['title'].encode('utf-8'))
        fout.write("</td>")
        fout.write("<td>%s</td>" % data['local'].encode('utf-8'))
        fout.write("<td>%s</td>" % data['time'].encode('utf-8'))
        fout.write("</tr>")

    fout.write("</table>")
    fout.write("</body>")
    fout.write("</html>")

    fout.close()


if __name__ == '__main__':
    root_url = 'http://jiuye.www.sust.edu.cn/zph.jsp?urltype=tree.TreeTempUrl&wbtreeid=1003'
    base_url = 'http://jiuye.www.sust.edu.cn/zph.jsp'
    res_data = []
    i = 0

    while i < 3:
        root_url = getHtmlInfo(root_url, res_data)
        root_url = urlparse.urljoin(base_url, root_url)
        #root_url = new_url
        print root_url
        i += 1


    outputHtml(res_data)
        #找到前三页的网址
        #http://jiuye.www.sust.edu.cn/zph.jsp?a47862t=239&a47862p=2&a47862c=15&urltype=tree.TreeTempUrl&wbtreeid=1003
        #                                    ?a47862t=239&a47862p=2&a47862c=15&urltype=tree.TreeTempUrl&wbtreeid=1003
        #首先解析 root_url
        #得到下一页 url，当前页所有招聘公司 url、 公司名、招聘地点、时间
        #循环三次，得到前三页的信息
        #输出为 html 文件
