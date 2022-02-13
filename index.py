from mimetypes import init
from re import S
import bs4
import requests
from bs4 import BeautifulSoup
class GetInfo:
    def __init__(self,url):
        self.userAgent = 'ozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
        self.headers = {'User-Agent': self.userAgent}
        self.response = requests.get(url,headers=self.headers)
        self.html = self.response.content
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def FindInfos(self):
        self.Names = self.soup.find_all("div","name")
        self.imgUrls = self.soup.find_all("div","search-product-wrap-img")
        self.Grades = self.soup.find_all("div","rating")
        self.GradeCount = self.soup.find_all("div","rating-total-count")

    def ShowInfos(self):
        print(self.Names)
    # def Showinfos(self):


Bs4 = GetInfo('https://www.coupang.com/np/search?component=&q=%EB%A7%88%EC%9A%B0%EC%8A%A4&channel=user')

Bs4.FindInfos()

Bs4.ShowInfos()
