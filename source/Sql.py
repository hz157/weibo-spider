import pymysql


def connect():
    conn = pymysql.connect(
        host='gis.test.cn',
        user='gis',
        passwd='123456',
        db='gis',
        port=3306,
        charset="utf8")
    return conn


def insertData(data, keyword):
    con = connect()
    sql = f"INSERT INTO data (mid, user, verified,verifiedType, verifiedReason, createTime, content, keyword) VALUES ({data[0]}, '{data[1]}', {data[2]}, {data[3]}, '{data[4]}', '{data[5]}', '{data[6]}','{keyword}')"
    cursor = con.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()
    con.close()
    print(cursor.rowcount, "record inserted.")


def insertPic(mid, picPath):
    con = connect()
    cursor = con.cursor()
    sql = f"INSERT INTO pic (mid, path) VALUES ({mid}, '{picPath}')"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()
    con.close()
    print(cursor.rowcount, "record inserted.")


def writeData(data,keyword):
    # for i in data:
    for i in data[7]:
        path = data[8] + "/" + i
        insertPic(data[0], path)
    insertData(data, keyword)

def verifMid(mid):
    con = connect()
    sql = f"SELECT * FROM data WHERE mid={mid}"
    cursor = con.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        results = cursor.fetchall()
        con.close()
        if results != ():
            return True
        else:
            return False
    except:
        # Rollback in case there is any error
        con.close()
        return False
