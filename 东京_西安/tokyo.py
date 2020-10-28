
from requests.exceptions import RequestException
import pymysql
import requests
from lxml import etree
import re

import pymysql

import time
from selenium import webdriver
from lxml import etree
import datetime

import sys
sys.path.append("../") #


def get_first_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except :
        return None






def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        ff_str = f_str +"00"
        f_l.append(ff_str)

    return f_l

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num
def remove_block(items):
    new_items = []
    for it in items:
        if it != '\r\n                                            ':

            f = "".join(it.split())
            new_items.append(f)
        else:
            pass
    return new_items


def parse_html(html):
    big_list =[]

    element = etree.HTML(html)

    date_ = element.xpath('//td[1]/text()')
    f_date = remove_block(date_)
    temp_ = element.xpath('//td[3]/text()')
    f_temp = remove_block(temp_)
    top_t =[]
    bottom_t=[]
    for item in f_temp:
        f_t = get_twoTemp(item)


        top_t.append(f_t[0])
        bottom_t.append(f_t[1])

    for i1,i2,i3 in zip(bottom_t,top_t,f_date):
        f_i = i1,i2,i3
        for item in f_i:
            if item ==[]:
                f_i


            big_list.append((i1,i2,i3))
    return big_list







def get_twoTemp(*item):
    f_s=[]
    for it in item:
        f_str = it.split("/")
        for it in f_str:

            if it == '':
                f_str[f_str.index(it)]="0℃"
            else:
                pass
        for it in f_str:

            f = re.compile("(\d+)℃").findall(it)
            f_s.append(f[0])


    return f_s








#存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='weather',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into tokyo_T (day_tem,night_tem,tm_date) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except pymysql.err.IntegrityError :
        pass






if __name__ == '__main__':
    short_url =["(/guoji/367/2013-11.html)",
"(/guoji/367/2013-12.html)",
"(/guoji/367/2014-1.html)",
"(/guoji/367/2014-2.html)",
"(/guoji/367/2014-3.html)",
"(/guoji/367/2014-4.html)",
"(/guoji/367/2014-5.html)",
"(/guoji/367/2014-6.html)",
"(/guoji/367/2014-7.html)",
"(/guoji/367/2014-8.html)",
"(/guoji/367/2014-9.html)",
"(/guoji/367/2014-10.html)",
"(/guoji/367/2014-11.html)",
"(/guoji/367/2014-12.html)",
"(/guoji/367/2015-1.html)",
"(/guoji/367/2015-2.html)",
"(/guoji/367/2015-3.html)",
"(/guoji/367/2015-4.html)",
"(/guoji/367/2015-5.html)",
"(/guoji/367/2015-6.html)",
"(/guoji/367/2015-7.html)",
"(/guoji/367/2015-8.html)",
"(/guoji/367/2015-9.html)",
"(/guoji/367/2015-10.html)",
"(/guoji/367/2015-11.html)",
"(/guoji/367/2015-12.html)",
"(/guoji/367/2016-1.html)",
"(/guoji/367/2016-2.html)",
"(/guoji/367/2016-3.html)",
"(/guoji/367/2016-4.html)",
"(/guoji/367/2016-5.html)",
"(/guoji/367/2016-6.html)",
"(/guoji/367/2016-7.html)",
"(/guoji/367/2016-8.html)",
"(/guoji/367/2016-9.html)",
"(/guoji/367/2016-10.html)",
"(/guoji/367/2016-11.html)",
"(/guoji/367/2016-12.html)",
"(/guoji/367/2017-1.html)",
"(/guoji/367/2017-2.html)",
"(/guoji/367/2017-3.html)",
"(/guoji/367/2017-4.html)",
"(/guoji/367/2017-5.html)",
"(/guoji/367/2017-6.html)",
"(/guoji/367/2017-7.html)",
"(/guoji/367/2017-8.html)",
"(/guoji/367/2017-9.html)",
"(/guoji/367/2017-10.html)",
"(/guoji/367/2017-11.html)",
"(/guoji/367/2017-12.html)",
"(/guoji/367/2018-1.html)",
"(/guoji/367/2018-2.html)",
"(/guoji/367/2018-3.html)",
"(/guoji/367/2018-4.html)",
"(/guoji/367/2018-5.html)"]


    for item1 in short_url:
        url = 'http://www.tianqihoubao.com'+item1
        f_url ="".join(url.split("("))[:-1]

        html = get_first_page(f_url)
        content  = parse_html(html)
        insertDB(content)
        print(url)















# 字段设置了唯一性 unique
# day_tem,night_tem,tm_date
# create table tokyo_T(
# id int not null primary key auto_increment,
# day_tem int,
# night_tem int,
# tm_date varchar(15)
# ) engine=InnoDB  charset=utf8;

# drop table tokyo_T;

#

# 修改字段类型

# 查询ＰＭ25最严重前３０

# select tm_date,day_tem,night_tem from yinchuan_T order by day_tem  limit 25;

