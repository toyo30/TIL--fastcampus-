from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://shopping.naver.com/outlet/stores/100424753/products/5490350874?NaPm=ct%3Dkocnsyvn%7Cci%3Dshoppingwindow%7Ctr%3Dswl%7Chk%3Dafdf66bebcf58999afd77c42a45f0d8deacf43a1%7Ctrx%3D")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

# 요일별 웹툰영역 추출
data1_list=soup.findAll('p',{'class':'NmydhT0lMt'})

print(data1_list)
# 전체 웹툰 리스트
week_title_list = []

for data1 in data1_list:
    # 제목 영역 추출
    data2=data1.findAll('span',{'class':'_2Xe0HVhCew'})

    # 제목 텍스트 추출
    title_list = [t.text for t in data2]
    ## 1차원으로 저장하려면 extend
    week_title_list.extend(title_list)
    ## 요일별로 2차원 리스트로 저장하려면 append
    # week_title_list.append(ti tle_list) 

print(week_title_list)