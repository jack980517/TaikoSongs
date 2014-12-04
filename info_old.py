#!/usr/bin/python2
# coding:utf-8
genre=["J-POP","アニメ","バラエティ","クラシック","ナムコオリジナル","ダウンロード","ゲームミュージック","童謠•民謠"]
list=open('00.txt','r')
result=open('result.txt','w')
result.write('Filename\tGenre\tTitle\n')
for i in range(0,211):
    dat=list.readline()[:-1]
    datfile=open(dat,'r')
    s=datfile.read()
    a=s.find('ftyp')-5
    g=ord(s[4])
    result.write(dat[4:]+'\t'+genre[g]+'\t'+s[80:a]+'\n')