import requests
from bs4 import BeautifulSoup
from texttable import Texttable

reply=input("Do you want to get the list of next 10 upcoming cricket matches(yes/no):")
if(reply=='yes'):
	t = Texttable()
	req=requests.get("https://www.cricbuzz.com/cricket-schedule/upcoming-series/international")
	soup=BeautifulSoup(req.content,"html.parser")
	tags = {tag.name for tag in soup.find_all()}
	Tour=[]
	Date=[]
	Match=[]
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
reply=input("Do you want to get the list of ICC test team rankings(yes/no):")
if(reply=='yes'):
	t=Texttable()
	req=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/test")
	soup=BeautifulSoup(req.content,"html.parser")
	tags={tag.name for tag in soup.find_all()}
	Country=[]
	for tag in tags:
		for i in soup.find_all(tag):
			if i.has_attr("class"):
				if len(i['class']) != 0:
					if(i['class']==["u-hide-phablet"]):
						Country.append(i.get_text())

	print("ICC TEST RANKINGS")
	t.add_row(["Ranking","Team"])
	for i in range(len(Country)):
		t.add_row([i+1,Country[i]])
	print(t.draw())

reply=input("Do you want to get the list of ICC ODI team rankings(yes/no):")
if(reply=='yes'):
	t=Texttable()
	req=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
	soup=BeautifulSoup(req.content,"html.parser")
	tags={tag.name for tag in soup.find_all()}
	Country=[]
	for tag in tags:
		for i in soup.find_all(tag):
			if i.has_attr("class"):
				if len(i['class']) != 0:
					if(i['class']==["u-hide-phablet"]):
						Country.append(i.get_text())

	print("ICC TEST RANKINGS")
	t.add_row(["Ranking","Team"])
	for i in range(len(Country)):
		t.add_row([i+1,Country[i]])
	print(t.draw())

reply=input("Do you want to get the list of ICC T20 team rankings(yes/no):")
if(reply=='yes'):
	t=Texttable()
	req=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/t20i")
	soup=BeautifulSoup(req.content,"html.parser")
	tags={tag.name for tag in soup.find_all()}
	Country=[]
	for tag in tags:
		for i in soup.find_all(tag):
			if i.has_attr("class"):
				if len(i['class']) != 0:
					if(i['class']==["u-hide-phablet"]):
						Country.append(i.get_text())

	print("ICC TEST RANKINGS")
	t.add_row(["Ranking","Team"])
	for i in range(len(Country)):
		t.add_row([i+1,Country[i]])
	print(t.draw())








					
