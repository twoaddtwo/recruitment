import pymysql



def exe_sql(sql):
    db = pymysql.connect(host="rm-bp14dy1c89k64zb7cpo.mysql.rds.aliyuncs.com", port=3306, user="gancaocn",
                         password="gancaocn2020#@!", database="gd_default", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount != 0:
            print("新增数据成功")
        else:
            print("新增数据失败")


    except:
        print("Error: unable to fecth data")
    db.close()



