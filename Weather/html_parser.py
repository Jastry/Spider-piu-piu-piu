#!/usr/bin/env python
#-*-coding:utf-8 -*-

from bs4 import BeautifulSoup

class HtmlParser(object):

    def _get_weather_data(self, soup):
        res_data = {}

        #<span class="styles-xz0ANuUJ__locationName__1t7rO">西安, 中国</span>
        location_node = soup.find('span', class_="styles-xz0ANuUJ__locationName__1t7rO")
        res_data['location'] = location_node.get_text()
        #print res_data['location']

        #<div class="today_nowcard-temp"><span class="">-4<sup>°</sup></span></div>
        temp_node = soup.find('div', class_='today_nowcard-temp')
        res_data['temp'] = temp_node.get_text()
        #print res_data['temp']

        #<div class="today_nowcard-phrase">晴朗</div>
        wea_node = soup.find('div', class_='today_nowcard-phrase')
        res_data['wea'] = wea_node.get_text()
        #print res_data['wea']
        return res_data

    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return None

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        weather_data = self._get_weather_data(soup)
        return weather_data
