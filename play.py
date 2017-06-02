#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import sys
import requests
start=True
link="http://wlxyzlw.iptime.org:8008/"
sf = open('play.txt','r')
cursor=0
for i in range(int(sys.argv[1])):
    if start:
        start=False
        try:
            x = open('playlog.txt','r')
            s=x.readline()
            x.close()
            cursor=int(s)
        except:
            cursor=0
        sf.seek(cursor)
    s=sf.readline()
    if not s:
        break
    s=s.split('\t')
    try: # 되나
        s[2]=s[2][:-1]
        res1 = requests.post(link+"address/",{"address":s[2]})
        ss=datetime.strptime(s[0],'%d/%b/%Y:%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        res2 = requests.post(link+"play/",{"date":ss,"track":s[1],"address":s[2]})
        assert res2.status_code==201
    except: # 안된다
        # 길이는
        if len(s)==3:
            try: #서버는
                res1 = requests.get(link+"track/"+s[1]+"/")
                res2 = requests.get(link+"address/"+s[2]+"/")
            except: #죽었음
                print("server dead")
                exit(1)
            try: #데이터는
                datetime.strptime(s[0],"%d/%b/%Y:%H:%M:%S")
                assert res1.status_code==200
                assert res2.status_code==200
                print("too normal")
                exit(1)
            except:
                pass
        # 다음(스킵)
    cursor=str(sf.tell())
    x = open('playlog.txt','w')
    x.write(cursor)
    x.close()
