# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import requests, json
from time import sleep
from random import randint

if len(sys.argv) != 3:
    print("python3 test.py [directory name] [url]")
    print("example: python3 test.py exp1 http://wlxyzlw.iptime.org:8088/")
    exit(1)

path = sys.argv[1]
link = sys.argv[2]
print("1. Upload input data")
print("...track") 
with open(path+"/track.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        l=line.split("\n")[0].split(" ")
        l[2] = True if l[2]=="Y" else False
        data = {"id":l[0],"name":l[1],"is_title":l[2]} 
        res = requests.post(link+"track/", data)
        print(str(res.status_code))
print("...tag")
with open(path+"/tag.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        l=line.split("\n")[0].split(" ")
        data = {"id":l[0],"name":l[1],"score":l[2]}
        res = requests.post(link+"tag/", data)
        print(str(res.status_code))
print("...mtm")
with open(path+"/mtm.txt", 'r') as f:
    while True:
          line = f.readline()
          if not line:
              break
          l=line.split("\n")[0].split(" ")
          data = {"track":l[0],"tag":l[1],"harmony":l[2]}
          res=requests.post(link+"mtm/", data)
          print(str(res.status_code))
print("...address")
with open(path+"/address.txt", 'r') as f:
    while True:
          line = f.readline()
          if not line:
              break
          l=line.split("\n")[0]
          data = {"address":line}
          res=requests.post(link+"address/", data)
          print(str(res.status_code))
print("...play")
with open(path+"/play.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        l=line.split("\n")[0].split(" ")
        data = {"date":l[0],"track":l[1],"address":l[2]} 
        res=requests.post(link+"play/", data=data)
        print(str(res.status_code))
print("2. Proposal results")
with open(path+"/output.txt", 'w') as out:
    with open(path+"/address.txt", 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            data=requests.get(link+"address/"+line.split("\n")[0]+"/proposal")
            out.write(data.text+"\n")
