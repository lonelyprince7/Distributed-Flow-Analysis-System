#!/usr/bin/env python
#encoding=utf-8
import scapy.all as scapy
import os, sys, stat
import re
import pymysql
import string
import random
import time
from stat import *

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="zhanghongyu", db='EP2', port=3306, autocommit=True)  # ����ָ�����ݿ�
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
cursor.execute("""use EP2;""")
cursor.execute("""set sql_mode="";""")

#while True:
#url_path = '/var/lib/mysql-files/'
#salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
#url_filename = url_path + salt + '.txt'
url_filename = '/var/lib/mysql-files/url.txt'  # �洢url��txt�ļ���·��
url_file = open(url_filename,mode='w+')    # �Զ�д����ģʽ��txt�ļ�
print( filemode(os.stat(url_filename).st_mode) )  # �鿴�ļ�Ȩ��
#os.chmod(url_filename, stat.S_IRWXO|stat.S_IRWXG|stat.S_IRWXU)
#print( filemode(os.stat(url_filename).st_mode) )
pattern = re.compile(r'GET /(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # ���url������ƥ��ģʽ
  
path = "/root/pcap"   # pcap�ļ�����·��

counter = 0
for file in os.listdir(path):       # ����pcap�ļ�����·���ҵ���·����ÿһ��pcap�ļ�
	counter += 1
	if counter > 10:
		break

	file_path = path + "/" + file   
	print(file_path)
	packets = scapy.rdpcap(file_path)  

	for p in packets:
		for f in p.payload.payload.payload.fields_desc:
			fvalue = p.payload.payload.getfieldval(f.name)
			reprval = f.i2repr(p.payload.payload, fvalue)
			if 'HTTP' in reprval:  # ��ȡÿ��pcap����http����
				lst = str(reprval).split(r'\r\n')
				for l in lst:
					#print(l)
					url = re.findall(pattern, l) # ��������ƥ���ȡhttp�����е�url�ֶ�
					url = "".join(url)
					if url != "":
						print(url)
						#url_file.seek(0)
						url_file.write(url + '\n')   # ��url�ֶ�д��txt�ļ���
					else:
						continue
			else:
				break
	# print(file_path)
	os.remove(file_path)  



#sql = """load data infile '%s' into table url FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'  LINES TERMINATED BY '\n'"""%(url_filename)
#print(sql)
#cursor.execute(sql)
url_file.seek(0)
cursor.execute("""load data infile '/var/lib/mysql-files/url.txt' into table url FIELDS TERMINATED BY ','  OPTIONALLY
 ENCLOSED BY '"'  LINES TERMINATED BY '\n';""")  # ���洢url��txt�ļ��е��������ݱ��������ݿ��е�url���е�url�ֶ���
cursor.execute("""update url set time = "0000-0-0 00:00:00";""") 
cursor.execute("""update url set time=concat('2013-3-29 ', floor(10+rand()*10),':',floor(10+rand()*49),':',floor(10+rand()*49))  where time="0000-0-0 00:00:00"
;""") 
cursor.execute("""update url set url='url',time='time' limit 1;""") 
