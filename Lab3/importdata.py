# coding=UTF-8
import sys
import requests
import psycopg2
import urllib
import os
from bs4 import BeautifulSoup
from inspect import currentframe, getframeinfo
import urllib2

try:
        conn = psycopg2.connect("dbname='exampledb' user='dbuser' host='localhost' password='password'")
except:
        print "I am unable to connect to the database"
cur = conn.cursor()
c = 0;
inputstr = sys.argv[1];
#inputstr = "1022";
url = urllib2.urlopen("http://data.tainan.gov.tw/dataset/denguefevercases").read()
soup = BeautifulSoup(url);

for anchor in soup.findAll('a', href=True):
	s = anchor['href'];
	if("http://data.tainan.gov.tw/" in s) and (inputstr in s):
		c = c + 1;

for anchor in soup.findAll('a', href=True):
        s = anchor['href'];
	if(c > 1) and (len(s) > 139):
		if("http://data.tainan.gov.tw/" in s) and (inputstr in s) and (inputstr[0] == s [135]) and (inputstr[3] == s [138]):
#			print s;
		#	if(len(s) > 139):
		#		print s[135]+s[136]+s[137]+s[138];
			urlin = urllib2.urlopen(s).read();

	else :
		if("http://data.tainan.gov.tw/" in s) and (inputstr in s):
			urlin = urllib2.urlopen(s).read();


soup = BeautifulSoup(urlin);
tmp = soup.get_text();
str1 = "";
count = 0;
#print tmp.split('\n');
k = tmp.split('\n');
#print k[7];

try:
	for i in range(len(k) -1 ):
		count = count + 1;
		if(count - 1 == 0):
			continue;
		str1 = k[i];
		n = str1.split(',');
#		query = "INSERT INTO hotfever(Id, date, region, dist, road, latitude, longitude) VALUES (%s,%s,%s,%s,%s,%s,%s);";
		cur.execute("""INSERT INTO hotfever(Id, date, region, dist, road, latitude, longitude) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(count,n[0],n[1],n[2],n[3],n[4],n[5]));
#		cur.execute(query, data);
		conn.commit();
		str1 = "";

except: 
        print "I can't SELECT from user"

#print(soup.get_text());
conn.close();

