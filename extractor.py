#!/usr/bin/python2
list=open('00.txt','r')
for i in range(0,211):
    dat=list.readline()[:-1]
    m4a='M4A/'+dat[4:-3]+'m4a'
    datfile=open(dat,'r')
    m4afile=open(m4a,'w')
    s=datfile.read()
    a=s.find('ftyp')
    a-=4
    b=s.find(chr(0x1)+chr(0x39)+chr(0)+chr(0x10)+chr(0x27)+chr(0)+chr(0)+chr(0x70)+chr(0x17))
    m4afile.write(s[a:b])
