#!/usr/bin/env python
#-*-coding:utf-8 -*-
class HtmlOutputer(object):

    def __init__(self):
        #初始化字典
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        #将收集的数据放入 html 里
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
        fout.write("<body>")
        fout.write("<body>")
        fout.write("<table>")

        # ASCII
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()


