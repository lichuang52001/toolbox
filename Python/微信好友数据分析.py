# 微信好友数据分析
"""
Created on Wed Aug 14 20:45:41 2019
@author: Edward
E-mail: lichuang52001@gmail.com
"""

import itchat
import matplotlib.pyplot as plt
import csv
from collections import Counter

itchat.auto_login(hotReload = True)
friends = itchat.get_friends(update = True)

#%% sex
def analyseSex(friends):
    sexs = list(map(lambda x:x['Sex'],friends[1:]))
    counts = list(map(lambda x:x[1],Counter(sexs).items()))
    labels = ['Unknow','Male','Female']
    colors = ['red','yellowgreen','lightskyblue']
    plt.figure(figsize=(8,5), dpi=200)
    plt.axes(aspect=1) 
    plt.pie(counts, #性别统计结果
            labels=labels, #性别展示标签
            colors=colors, #饼图区域配色
            labeldistance = 1.1, #标签距离圆点距离
            autopct = '%3.1f%%', #饼图区域文本格式
            shadow = False, #饼图是否显示阴影
            startangle = 90, #饼图起始角度
            pctdistance = 0.6 #饼图区域文本距离圆点距离
    )
    plt.legend(loc='upper right',)
    plt.title(u'Sex distribution of %s' % friends[0]['NickName'])
    plt.show()

#%% location, after get the csv file, analysis using BDP
def analyseLocation(friends):
    headers = ['NickName','Province','City']
    with open('location.csv','w',encoding='utf-8',newline='',) as csvFile:
        writer = csv.DictWriter(csvFile, headers)
        writer.writeheader()
        for friend in friends[1:]:
           row = {}
           row['NickName'] = friend['NickName']
           row['Province'] = friend['Province']
           row['City'] = friend['City']
           writer.writerow(row)

analyseSex(friends)

analyseLocation(friends)