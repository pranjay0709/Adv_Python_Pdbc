import pymysql


def prac_insert3(id, name):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')

    cursor = connection.cursor()
    sql = 'insert into prac_crud values(%s,%s)'

    data = (id, name)

    cursor.execute(sql, data)


    connection.commit()
    connection.close()
    print("Record Insereted")
prac_insert3(4, "Dd")
