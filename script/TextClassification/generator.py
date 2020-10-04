import pandas as pd
from html.parser import HTMLParser
import re
from urllib import parse
import numpy as np
import os
import numpy as np
from sklearn.model_selection import train_test_split
def DecodeQuery1(fileName):
    data = [x.strip() for x in open(fileName, "r").readlines()]
    query_list = []
    for item in data:
        item = item.lower()
        if len(item) > 50 or len(item) < 5:
           continue
        h = HTMLParser()
        item = h.unescape(item) #将&gt或者&nbsp这种转义字符转回去
        item = parse.unquote(item)#解码,就是把字符串转成gbk编码，然后把\x替换成%。如果
        item, number = re.subn(r'\d+', "8", item) #正则表达式替换
        item, number = re.subn(r'(http|https)://[a-zA-Z0-9\.@&/#!#\?:]+', "http://u", item)
        query_list.append(item)
    return query_list

def DecodeQuery2(fileName1,fileName2):
    data1 = [x.strip() for x in open(fileName1, "r").readlines()]
    data2 = [x.strip() for x in open(fileName2, "r").readlines()]
    query_list = []
    time_list = []
    for item1,item2 in zip(data1,data2):
        item1 = item1.lower()
        if len(item1) > 50 or len(item1) < 5:
           continue        
        h = HTMLParser()
        item1 = h.unescape(item1) #将&gt或者&nbsp这种转义字符转回去
        item1 = parse.unquote(item1)#解码,就是把字符串转成gbk编码，然后把\x替换成%。如果
        item1, number = re.subn(r'\d+', "8", item1) #正则表达式替换
        item1, number = re.subn(r'(http|https)://[a-zA-Z0-9\.@&/#!#\?:]+', "http://u", item1)
        query_list.append(item1)
        time_list.append(item2)
    return query_list,time_list

def readFile():
    #读取训练集数据
    bX1_d = DecodeQuery1('./data/网络攻击.csv')
    bX2_d = DecodeQuery1('./data/恶意软件.csv')
    gX_d = DecodeQuery1('./data/业务流量.csv')
    X=np.array(bX1_d+bX2_d+gX_d).reshape(-1,1)
    Y=np.array([1]*len(bX1_d)+[2]*len(bX2_d)+[0]*len(gX_d)).reshape(-1,1) #正常请求标签为0  网络攻击流量标签为1 恶意软件流量标签为2
    comXY=np.concatenate((X,Y),axis=1)
    np.random.shuffle(comXY)
    X=np.squeeze(comXY[:,:-1],axis=1)
    Y=comXY[:,-1]
    comXY = pd.DataFrame({'label':Y,'url':X}) 
    comXY.to_csv('data/data.csv',index=False,sep=',',encoding="utf-8")
if __name__=="__main__":
    readFile()
