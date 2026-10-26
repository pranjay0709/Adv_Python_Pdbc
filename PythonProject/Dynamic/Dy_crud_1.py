import pymysql
def prac_insert1():
    connection=pymysql.connect(host='localhost', port=3306,user='root', password='root', db='prac')
    cursor=connection.cursor()
    sql='insert into prac_crud values(2,"Bb")'
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('Data inserted')
prac_insert1()
