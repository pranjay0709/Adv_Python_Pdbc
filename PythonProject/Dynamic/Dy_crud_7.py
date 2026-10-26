import pymysql
def testUpdate3(data={}):
    id = data['id']
    name = data['name']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "update marksheet set name = %s where id = %s"
    data = (name,id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('Data updated successfully')
py={}
py['id']=4
py['name']= 'DDd'
testUpdate3(py)