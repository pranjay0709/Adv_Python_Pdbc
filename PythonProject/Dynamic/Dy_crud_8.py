import pymysql
def testDelete3(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "delete from prac_crud where id = %s"
    data = (id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data deleted successfully')
testDelete3(5)