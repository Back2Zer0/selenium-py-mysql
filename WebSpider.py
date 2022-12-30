from SqlConnect import *
from selenium import webdriver
from SqlOperator import *
import time


def scan():#用户输入函数(input)
    temp = 0 #计数器
    products = ["白菜", "茄子", "番茄", "卷心菜", "土豆", "辣椒", "萝卜", "西兰花"]
    for product in products:
        print(temp,end=". ")
        print(product)
        temp+=1
    print(temp,". 我要输入其他农产品")
    print("请输入：")
    temp = int(input())
    if temp<=7:
        product = products[temp]
    else:
        product = str(input("请输入农产品名称："))
    return product


def spider(product):#数据爬取函数(selenium)
    web = webdriver.Chrome()
    web.get('http://uland.taobao.com/sem/tbsearch?keyword=' + product)  # 启动浏览器，打开对应网页

    lists = web.find_elements(by='xpath', value='//*[@class="pc-search-items-list"]/li')
    #爬取前创建好表
    tbcreate(sqlconnect(), product)
    for li in lists:
        name = li.find_element(by='xpath', value='.//*[@class="title-text"]').text
        price = li.find_element(by="xpath", value='.//*[@class="coupon-price-afterCoupon"]').text
        month_sales = li.find_element(by='xpath', value='.//*[@class="sell-info"]').text
        seller = li.find_element(by='xpath', value='.//*[@class="seller-name"]').text

        time.sleep(5) #防止页面关闭太快，还没有爬完程序就关掉了
        result = [name,price,month_sales.split(" ")[1],seller[1:]]
        #收集完数据，建立连接！
        sqlcon = sqlconnect()
        sqlspider(sqlcon,product,result)
    print(f"{product}的产品数据输入完毕")






