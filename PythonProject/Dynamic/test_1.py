import pymysql
#CREATE
def create_role():
    connection=pymysql.connect(host='localhost', port=3306,user='root', password='root', db='prac')
    cursor=connection.cursor()
    sql='create table role(id int primary key, name varchar(20), description varchar(20))'
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('Table created')
# create_role()

def insert_role(data={}):
    id = data['id']
    name = data['name']
    description = data['description']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "insert into role values(%s,%s,%s)"
    data = (id, name, description)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Method 4 Record inserted")
# rec={}
# rec['id']=1
# rec['name']='HR'
# rec['description']='Hiring'
# insert_role(rec)
#READ
def sel_rol(dicts={}):
    id=dicts.get('id',0)
    name=dicts.get('name'," ")
    description=dicts.get('description'," ")
    pagesize=dicts.get('pagesize',0)
    pagenumber=dicts.get('pagenumber',0)

    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='prac')
    cursor=connection.cursor()
    sql="select * from role where 1=1"
    if id != 0:
        sql += ' and id = ' + str(id)
    if name != ' ':
        sql += " and name like '" + name + "%'  "
    if description != ' ':
        sql += " and description like '" + name + "%'  "
    if pagenumber > 0:
        pagenumber = (pagenumber - 1) * pagesize
        sql += ' limit ' + str(pagenumber) + ',' + str(pagesize)
    print("Sql Query:", sql)
    cursor.execute(sql)
    result=cursor.fetchall()
    for data in result:
        print(data[0],'\t', data[1], '\t',data[2],'\t')
    connection.commit()
    connection.close()
    print("These are the records")
dicts={}
# dicts['pagenumber'] = 1
# dicts['pagesize'] = 5
# dicts['id'] = 1
# dicts['name'] ='a'

sel_rol(dicts)


#UPDATE
def update_role(data):
    id = data['id']
    name = data['name']
    description = data['description']

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "update role set name = %s, description = %s where id = %s"
    data = (name, description, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')
data={}
data['name']='IT'
data['description']='Devlopment'
data['id']=14

# update_role(data)


#DELETE

def delete_role(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "delete from role where id = %s"
    data = (id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data deleted successfully')

# delete_role(15)
