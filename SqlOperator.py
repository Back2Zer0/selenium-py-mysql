def table_initial(sqlcon):
    with sqlcon.cursor() as cursor:
        # 通过游标对象向数据库服务器发出SQL语句
        cursor.execute(
            #新建一个数据库(如果存在就放弃创建！)
            "CREATE TABLE IF NOT EXISTS summary ("
            "proname VARCHAR(255),"
            "price VARCHAR(255),"
            "month_sales VARCHAR(255),"
            "seller VARCHAR(255) )"
            "CHARSET=utf8;"
        )


def insert(sqlcon,tbname):
    num = int(input("添加商品的数目"))
    tnum = num
    val=[]

    while tnum !=0:
        tnum-=1
        tname = input("你要添加商品的名称")
        tprice = input("该商品的价格") #输入数字时小心格式问题！
        tmonth = input("该商品的月销量")
        tseller = input("该商品的商家名称")
        val.append([tname, tprice, tmonth, tseller])
    with sqlcon.cursor() as cursor:
            while tnum < num:
                sql="INSERT INTO %s (proname, price,month_sales,seller) VALUES ('%s', '%s','%s','%s');"%\
                    (tbname,val[tnum][0],val[tnum][1],val[tnum][2],val[tnum][3])
                cursor.execute(sql)
                tnum+=1
    print("添加完毕！")
    sqlcon.commit()


def delete(sqlcon,tbname):
    tname = input("输入要删除的商家的名称")
    with sqlcon.cursor() as cursor:
        affected_rows = cursor.execute(
            f"DELETE FROM %s WHERE seller = '%s';"%(tbname,tname)
        )
    if affected_rows == 1:  # 这里的1指 游标函数发送成功后的返回值为1
        print('删除信息成功!!!')
    else:print("信息不存在！")


def search(sqlcon,tbname):
    tname = input("输入要查找的商家的名称")
    with sqlcon.cursor() as cursor:
        sql_exe =  f"SELECT * FROM %s WHERE seller = '%s';"%(tbname,tname)
        flag = cursor.execute(sql_exe)
        if flag:
            datas = cursor.fetchall()
            print(datas)
            print("查找完毕!")
        else :
            print("不存在该商家!\n")

def showme(sqlcon,tbname):
    with sqlcon.cursor() as cursor:
        flag = cursor.execute(
            f"SELECT * FROM {tbname}"
        )
        if flag:
            datas = cursor.fetchall()
            for data in datas:
                print(data)
            print("以上为数据库内信息")
        else:
            print("该库不存在！")


def tbcreate(sqlcon,product):
    with sqlcon.cursor() as cursor:
        # 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            #新建一个数据库(如果存在就放弃创建！)
            f"CREATE TABLE IF NOT EXISTS {product} ("
            "proname VARCHAR(255),  "
            "price VARCHAR(255),"
            "month_sales VARCHAR(255),"
            "seller VARCHAR(255) ) "
            "CHARSET=utf8;"
        )


def tbshow(sqlcon):
    print("当前数据库中的表:")
    with sqlcon.cursor() as cursor:
        # 通过游标对象向数据库服务器发出SQL语句
        flag = cursor.execute(
            "show tables;"
        )
        if flag:
            datas = cursor.fetchall()
            for data in datas:
                print(data)
        else :
            print("输入有误，该库不存在！")


def tbdrop(sqlcon,tbname):
    with sqlcon.cursor() as cursor:
            cursor.execute(f"DROP TABLE IF EXISTS {tbname} ")
    print("操作完成")

def sqloperate(sqlcon,tbname):

    message="1.增加几列sql数据\n2.单独删除一列sql数据\n3.查找一列sql数据\n4.查看当前数据库数据\n"
    flag = int(input(message+"\n请输入:"))
    match flag:
        case 1:
            insert(sqlcon,tbname)
        case 2:
            delete(sqlcon,tbname)
        case 3:
            search(sqlcon,tbname)
        case 4:
            showme(sqlcon,tbname)
        case _:
            print("what are you doing???\n输入不合法。")
