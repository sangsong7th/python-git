import requests
import re
from bs4 import BeautifulSoup
import os
import sys
def progress_bar(N,i,name) :
	print("\n现在正在下载的是",name)
	print("这只需要几分钟")
	for j in range(i+1):
			sys.stdout.write("|")

	for j in range(N-i-1):
			sys.stdout.write("_")
	
def bigimg(url,name):
		try :
			ds=requests.get(url).text
		except :
			print("网络连接断开，或网址访问失败")
		r1=re.compile(r'<a class="highres-show" href="(.{20,300}.jpg)">View larger version</a>')
		ri=r1.findall(str(ds))
		for img in ri :
			try :
				ds1=requests.get(img)
			except :
				print("网络连接断开，或网址访问失败")
			f=open(name,'wb')
			f.write(ds1.content)
			f.close()
def time():
	url="https://yande.re/post"
	try:
		ds=requests.get(url)
	except :
		print("网络连接断开，或网址访问失败")
	r=re.compile(r'<span class="plid">#pl https://yande.re/post/show/(.{0,11}.)</span></a></div><a class="directlink largeimg"')
	new=r.findall(ds.text)
	update=new[0]
	print("最新的图片号",update)
	N=int(input("图片张数:" ))
	star=int(input("开始图片号:"))
	ur="https://yande.re/post/show/"
	os.system('cls')

	for l in range(N) :	
		i=l
		l=str(star+int(l))
		url=ur+l
		name=l+".png"	
		progress_bar(N,i,name)
		bigimg(url,name)
		os.system('cls')
def artists():
	print("input artist's name who you like")
	url="https://yande.re/wiki/show?title="
	u2="https://yande.re"
	Aname=input()
	url=str(url+Aname)
	print(url)
	r=re.compile(r'<div class="inner" style="width: 150px; height: 150px;"><a class="thumb" href="(.{2,30}.)" ><img src=')
	try:
		ds=requests.get(url)
	except :
		print("网络连接断开，或网址访问失败")
	u1=r.findall(ds.text)
	print(u1)
	os.system('cls')
	u=0
	N=len(u1)
	a=0
	for i in u1 :
		url=str(u2+i)
		u=u+1
		name=str(Aname+str(u)+".png")
		a=a+1
		progress_bar(N,a,name)
		bigimg(url,name)
		os.system('cls')

def pools() :
	url="https://yande.re/pool"
	ug="https://yande.re"
	pageurl="https://yande.re/pool?page="
	Pname=input()
	print(Pname)
	# print(url)
	r=re.compile(r'<td><a href="(.{2,20}.)">')
	r2=re.compile(r'">(.{2,200}.)</a></td>')
	i=1
	page=1
	while i==1 :
		try :
			ds=requests.get(url)
		except :
			print("网络连接断开，或网址访问失败")
		u1=r.findall(ds.text)
		u2=r2.findall(ds.text)
		d={}
		for i in range(len(u1)) :
			d[u2[i]]=u1[i]
		print(d)
		try :
			ug2=d[Pname]
			i=0
		except KeyError:
			print("此页没有 正在搜索下一页")
			page=page+1
			pages=str(page)
			url=str(pageurl+pages)
			i=1

	print(ug2)
	ug=ug+ug2
	print(ug)
	try :
		ds=requests.get(ug).text
	except :
		print("网络连接断开，或网址访问失败")
	soup=BeautifulSoup(ds,"lxml")
	r3=re.compile(r'<span class="plid">#pl (.{2,200}.)</span></a></div></li>')
	url=r3.findall(str(soup))
	print(url)
	for i in range(len(url)) :
		u=url[i]
		name=str(Pname+str(i)+".png")
		progress_bar(len(url),i,name)
		bigimg(u,name)
		os.system('cls')
def tages() :
	url1="https://yande.re/post?page=19&tags="
	url2="https://yande.re/post?page="
	url3="&tags="
	r=re.compile(r'<span class="plid">#pl (.{2,200}.)</span></a></div><a class=')
	tagesname=input("the artists who you like :")
	main=url1+str(tagesname)
	i=1
	k=19

	while i==1 :
		k=k+1
		try :
			ds=requests.get(main).text
		except :
			print("not work")
			i=0

		if i==1 :
			url=r.findall(ds)
			print(url)
			b=len(url)

			a=1
			j=1
			for a in url :
				name=tagesname+str(j)+"_"+str(k-1)+".jpg"
				N=len(url)
				progress_bar(N,j,name)
				bigimg(a,name)
				os.system('cls')
				j=j+1
		if b==0 :
			i=0
		print("download the next")
		main=url2+str(k)+url3+tagesname
		print(main)








		


u=1
while u==1:
	i=1
	while i==1 :
		print("how masion you want \n1.time\n2.artist\n3.pools\n4.tages")
		a=int(input('input:'))
		mainurlone="https://yande.re/"
		if a==1 :
			print('你选择了时间模式')
			time()
			i=0
		elif a==2 :
			print("你选择了艺术家模式")
			artists()
			i=0
		elif a==3 :
			
			print("你选择了风格模式")
			pools()
			i=0
		elif a==4 :
			title="Tages"
			print(title)
			tages()
			i=0
		else :
			i=1


	print("\n程序运行结束 \ninput 1 to contiue")
	u=int(input())