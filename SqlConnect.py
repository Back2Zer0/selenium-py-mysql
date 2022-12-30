import pymysql

def sqlconnect(): #sql连接函数
    # 1.建立连接
    sqlcon = pymysql.connect(host='127.0.0.1', port=3306,
                           user='guest', password='Guest.618',
                           database='dbtest11', charset='utf8mb4',
                           autocommit=True)
    return sqlcon

def sqlspider(sqlcon,product,res): #sql配合爬虫的函数
    try:
        # 1. 获取游标对象（Cursor）
        with sqlcon.cursor() as cursor:
            # 2. 通过游标对象向数据库服务器发出SQL语句
            cursor.execute(
                f'INSERT INTO {product}(proname,price,month_sales,seller) VALUES("%s","%s","%s","%s");'%(res[0], res[1], res[2],res[3])
            )
            # summary是汇总表，方便下载数据
            cursor.execute(
                'INSERT INTO summary(proname,price,month_sales,seller) VALUES("%s","%s","%s","%s");'% (res[0], res[1], res[2], res[3])
            )
        # 3. 提交事务
        sqlcon.commit()
    except pymysql.MySQLError as err : #一旦爬出来的数据，在加入到数据库时出错，立即回滚到原正常状态
        # 4. 回滚事务(如果提交出错出错)
        sqlcon.rollback()
        print(type(err), err)
    finally:
        sqlcon.close()