# import requests
# from bs4 import BeautifulSoup
# from urllib import parse


# url = "https://cafe.naver.com/joonggonara?iframe_url_utf8=%2FArticleRead.nhn%253FreferrerAllArticles%3Dtrue%2526page%3D9%2526searchBy%3D0%2526query%3D%25EB%25A7%25A5%25EB%25B6%2581%25EC%2597%2590%25EC%2596%25B4%2520m1%2526exclude%3D%25EB%25A7%25A4%25EC%259E%2585%2526include%3D%2526exact%3D%2526searchdate%3Dall%2526media%3D0%2526sortBy%3Ddate%2526clubid%3D10050146%2526articleid%3D967126701"
# url_decoded = parse.unquote(url, encoding="utf-8")
# html = requests.get(url_decoded)
# soup = BeautifulSoup(html.content.decode("euc-kr", "replace"), "html.parser")
# for i in soup:
#     print(i)
# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import re

page = 1
listPerPage = 50

# html = requests.get("https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=10050146&search.media=0&search.searchdate=all&search.exact=&search.include=&userDisplay="+str(listPerPage)+"&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=0&search.searchBlockYn=0&search.includeAll=&search.query=%B8%C6%BA%CF%C7%C1%B7%CE&search.viewtype=title&search.page="+str(page))

html = requests.get("https://cafe.naver.com/joonggonara?iframe_url=/ArticleSearchList.nhn?search.clubid=10050146&search.media=0&search.searchdate=all&search.exact=&search.include=&userDisplay="+str(listPerPage)+"&search.exclude=&search.option=0&search.sortBy=date&search.searchBy=0&search.searchBlockYn=0&search.includeAll=&search.query=%B8%C6%BA%CF%C7%C1%B7%CE&search.viewtype=title&search.page="+str(page))
soup = BeautifulSoup(html.content.decode("euc-kr", "replace"), "html.parser")

junggo = soup.find("div", id="content-area").find("div", id="main-area").find("div", class_="article-board")
for i in junggo:
    print(i)
    #main-area > div.article-board.result-board.m-tcol