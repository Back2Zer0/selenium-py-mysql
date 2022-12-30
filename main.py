from WebSpider import *
from SqlOperator import *
from CsvWrite import *

if __name__ == "__main__":
    table_initial(sqlconnect())  # 在数据库中初始化一个汇总表
    while 1:
        print("1.爬取农产品信息")
        print("2.对已有数据库信息操作")
        print("3.将数据库信息写入到CSV文件中")
        print("4.数据库中删除一类产品的表信息")
        print("5.退出")
        num = int(input("您要进行的操作："))
        match num:
            case 1:
                product = scan()
                spider(product)
            case 2:
                sqlcon = sqlconnect()
                tbshow(sqlcon)
                tbname = input("要操作的已有表的名称：")
                sqloperate(sqlcon, tbname)
            case 3:
                write(sqlconnect())
            case 4:
                sqlcon = sqlconnect()
                tbshow(sqlcon)
                tbname = input("要操作的已有表的名称：")
                tbdrop(sqlcon,tbname)
            case _:
                print("Bye! :)")
                break
