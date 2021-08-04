import requests
from bs4 import BeautifulSoup
from texttable import Texttable
t = Texttable()

req=requests.get("https://www.cricbuzz.com/cricket-schedule/upcoming-series/international")
soup=BeautifulSoup(req.content,"html.parser")
tags = {tag.name for tag in soup.find_all()}
Tour=[]
Date=[]
Match=[]
l=[]
x=0
for tag in tags:
	for i in soup.find_all( tag ):
		if i.has_attr( "class" ):
			if len( i['class'] ) != 0:
				if(i['class']==["cb-col-33","cb-col","cb-mtchs-dy","text-bold"]):
					Tour.append(i.get_text())
				if(i['class']==["cb-ovr-flo","cb-col-60","cb-col","cb-mtchs-dy-vnu","cb-adjst-lst"]):
					Match.append(i.get_text())

t.add_row(['Tour', 'Match'])
for i in range(len(Tour)):
	t.add_row([Tour[i],Match[i]])
print(t.draw())





					
