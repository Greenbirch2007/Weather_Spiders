
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
from m_d import md_list
#请求

def get_first_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except :
        return None


















#存储到MySQL中

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='weather',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
        cursor.executemany('insert into yinchuan_T (day_tem,night_tem,tm_date) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except pymysql.err.IntegrityError :
        pass











if __name__ == '__main__':

    for yeay in ["2011","2012","2013","2014","2015","2016","2017","2018","2019"]:
        for md in md_list:
            full_date = yeay+md
            try :

                url = 'http://www.tianqihoubao.com/lishi/yinchuan/'+str(full_date)+'.html'
                html = get_first_page(url)
                patt = re.compile('<td style="color:.*?><b>(.*?)℃</b></td>', re.S)
                items = re.findall(patt, html)
                items.append(full_date)
                f_t = tuple(items)
                big_list = []
                big_list.append(f_t)
                insertDB(big_list)
                print(full_date)
            except:
                pass









# 字段设置了唯一性 unique
# day_tem,night_tem,tm_date
# create table yinchuan_T(
# id int not null primary key auto_increment,
# day_tem int,
# night_tem int,
# tm_date varchar(15)
# ) engine=InnoDB  charset=utf8;

# drop table yinchuan_T;

#

# 修改字段类型

# 查询ＰＭ25最严重前３０

# select tm_date,day_tem,night_tem from yinchuan_T order by day_tem  limit 25;

