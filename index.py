from GetInfo import GetInfo


Bs4 = GetInfo('https://www.coupang.com/np/search?component=&q=%EB%A7%88%EC%9A%B0%EC%8A%A4&channel=user')

Bs4.FindInfos()

Bs4.ShowInfos()
