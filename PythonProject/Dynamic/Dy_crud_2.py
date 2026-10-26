import pymysql
def prac_insert2():
    connection=pymysql.connect(host='localhost',port=3306, user='root',password='root',db='prac')
    cursor=connection.cursor()
    sql='insert into prac_crud values(%s,%s)'
    data=(3,"Cc")
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data Inserted")
prac_insert2()