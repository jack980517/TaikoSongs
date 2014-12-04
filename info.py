#!/usr/bin/python2
# coding:utf-8
genre=["J-POP","アニメ","バラエティ","クラシック","ナムコオリジナル","ボーカロイド曲","ゲームミュージック","どうよう"]
list=open('00.txt','r')
result=open('result.txt','w')
result.write('Filename\tGenre\tTitle\n')
for i in range(0,211):
    dat=list.readline()[:-1]
    datfile=open(dat,'r')
    s=datfile.read()
    a=s.find('ftyp')-5
    g=ord(s[4])
    if g==2 and s[3]=='\x00':g=5
    b=s[:a].rfind('\x00')+1
    result.write(dat[4:]+'\t'+genre[g]+'\t'+s[b:a]+'\n')
