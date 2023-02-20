# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import re

page = 1
listPerPage = 50

# html = requests.get("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=10050146&search.media=0&search.searchdate=all&search.exact=&search.include=&userDisplay="+str(listPerPage)+"&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=0&search.searchBlockYn=0&search.includeAll=&search.query=%B8%C6%BA%CF%C7%C1%B7%CE&search.viewtype=title&search.page="+str(page))

html = requests.get("https://cafe.naver.com/joonggonara?iframe_url=/ArticleSearchList.nhn?search.clubid=10050146&search.media=0&search.searchdate=all&search.exact=&search.include=&userDisplay="+str(listPerPage)+"&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=0&search.searchBlockYn=0&search.includeAll=&search.query=%B8%C6%BA%CF%C7%C1%B7%CE&search.viewtype=title&search.page="+str(page))
soup = BeautifulSoup(html.content.decode("euc-kr", "replace"), "html.parser")

junggo = soup.find("div", id="content-area").find_all("div", id="main-area")[0].find_all("div", class_="article-board")[1]
junggo = junggo.find("tbody").find_all("tr")

for item in junggo :
        title = item.find("td", class_="td_article")

        if title != None :

                str = tite.find("div", class_="board-list").find("a", class_="articlle")
                
                if str.find(text=re.compile("2020")) :
                        print(" ".join(str.stripped_strings))