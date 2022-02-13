from GetInfo import GetInfo
import json

def CreateJson(Bs4):
    data = []
    for i in range(Bs4.GetLenght()):
        data.append(
            {
            'Name' : Bs4.Names[i].text,
            'imgUrl' : Bs4.imgUrls[i]['src'],
            'Grade' :Bs4.Grades[i].text,
            'GradeCount' : Bs4.GradeCount[i].text,
            }
        )
    with open('./datas.json', 'w',encoding='UTF-8-sig') as file:
        file.write(json.dumps(data, ensure_ascii=False,indent=4,))
def CreateHTML(Bs4):
    Items = ""
    for i in range(Bs4.GetLenght()):
        Name= Bs4.Names[i].text
        imgUrl= Bs4.imgUrls[i]['src']
        Grade=Bs4.Grades[i].text
        GradeCount= Bs4.GradeCount[i].text

        Article = f"""    
        <div style="text-align:center; border-bottom: 2px solid black;">
                <h3>{Name}/h3>
            <img 
              src="{imgUrl}"
              alt=""
            />
            <div style="text-align: center;">
                <h4>평점 : {Grade}</h4>
                <h4> 건수 :({GradeCount})</h4>
            </div>
            </div>"""
        Items = Items + Article
        template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Document</title>
        </head>
        <body>
            {Items}
        </body>
        </html>

    """
    with open('./html_file.html', 'w') as html_file:
        html_file.write(template)


Bs4 = GetInfo('https://www.coupang.com/np/search?q=%EC%A0%9C%EB%A1%9C%EC%82%AC%EC%9D%B4%EB%8B%A4&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=5&backgroundColor=')

Bs4.FindInfos()

CreateJson(Bs4)
CreateHTML(Bs4)