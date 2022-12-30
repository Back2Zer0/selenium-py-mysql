import csv

def write(sqlcon): #csv 文件写入函数
    with open("TaobaoSale.csv",mode= "w+",encoding="utf8",newline="") as file:
        csvw = csv.writer(file)
        csvw.writerow(["商家名", "价格", "月销量", "卖家"])
        with sqlcon.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM summary"
            )
        # 将sql语句查询到的内容全都保存到data变量中
        datas = cursor.fetchall()
        for data in datas:
            line = list(data)
            csvw.writerow(line)
    print("csv写入完毕")