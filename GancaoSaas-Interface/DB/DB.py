import pymysql


def exe_sql(sql):
    db = pymysql.connect(host="rm-bp14dy1c89k64zb7cpo.mysql.rds.aliyuncs.com",
                         port=3306,
                         user="gancaocn",
                         password="gancaocn2020#@!",
                         database="gd_default",
                         charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount != 0:
            print("查询到符合条件的数据")
        else:
            print("没有找到符合条件的数据")
    except:
        print("Error: unable to fecth data")
    db.close()


def del_sql(sql):
    db = pymysql.connect(host="rm-bp14dy1c89k64zb7cpo.mysql.rds.aliyuncs.com",
                         port=3306,
                         user="gancaocn",
                         password="gancaocn2020#@!",
                         database="gd_default",
                         charset='utf8')
    cursor = db.cursor()
    try:
        print(sql)
        cursor.execute(sql)
        db.commit()
        print("删除数据成功")
    except:
        # 发生错误时回滚
        db.rollback()
        print("删除数据失败")
    finally:
        cursor.close()

