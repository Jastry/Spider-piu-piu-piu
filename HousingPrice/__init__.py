#!/usr/bin/env python
#-*-coding:utf-8 -*-
import urllib2
import re
import urlparse
from bs4 import BeautifulSoup


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
        fout.write("<td>%s</td>" % data['text'].encode('utf-8'))
        fout.write("<td>%s</td>" % data['price'].encode('utf-8'))

        fout.write("</tr>")

    fout.write("</table>")
    fout.write("</body>")
    fout.write("</html>")

    fout.close()
if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    root_url = 'http://fangjia.fang.com/XIAN/'
    rsp = urllib2.Request(root_url, headers=headers)
    content = urllib2.urlopen(rsp).read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='gb18030')

    base_url = 'http://fangjia.fang.com'
    top_5 = soup.find_all('dl', class_='clearfix')
    res_data = []
    for info in top_5:
        d = {}
        data = info.find('a', href=re.compile(r'process'))
        title = data.get_text()
        d['title'] = title

        url = data['href']
        full_url = urlparse.urljoin(base_url, url)
        d['url'] = full_url

        data = info.find('span', class_=re.compile(r'pm-price'))
        if data is not None:
            price = data.get_text()
            d['price'] = price

        data = info.find('p', class_=re.compile(r'f14'))
        text = data.get_text()
        d['text'] = text
        res_data.append(d)

    outputHtml(res_data)

