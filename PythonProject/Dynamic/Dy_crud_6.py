import pymysql
def testUpdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "update prac_crud set name = %s where id = %s"
    data = ('CCc',3)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')
testUpdate2()
