

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
        self.imgUrls = self.soup.find_all("img","search-product-wrap-img")
        self.Grades = self.soup.find_all("em","rating")
        self.GradeCount = self.soup.find_all("span","rating-total-count")

    def ShowInfos(self):
        print(self.Names[1].text)
        print(self.imgUrls[1]['src'])
        print(self.Grades[1].text)
        print(self.GradeCount[1].text)

    def GetLenght(self):
        self.arr = [];
        self.arr.append(len(self.Names))
        self.arr.append(len(self.imgUrls))
        self.arr.append(len(self.GradeCount))
        self.arr.append(len(self.Grades))
        return min(self.arr)
