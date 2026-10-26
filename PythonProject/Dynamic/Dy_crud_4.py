import pymysql
def prac_insert4(data={}):
    id=data['id']
    name=data['name']
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='prac')
    cursor=connection.cursor()
    sql="insert into prac_crud values(%s,%s)"
    data=(id,name)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Method 4 Record inserted")
pr={}
pr['id']=5
pr['name']="Ee"
prac_insert4(pr)