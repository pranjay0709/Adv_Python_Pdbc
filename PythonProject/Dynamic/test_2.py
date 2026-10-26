import pymysql
#CREATE
def create_college():
    connection=pymysql.connect(host='localhost', port=3306,user='root', password='root', db='prac')
    cursor=connection.cursor()
    sql='create table college(id int primary key, name varchar(20), address varchar(20), state varchar(20), city varchar(20), phone_number varchar(20))'
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('Table created')
# create_college()

def add_college(data={}):
    id = data['id']
    name = data['name']
    address = data['address']
    state = data['state']
    city = data['city']
    phone_number = data['phone_number']

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "insert into college values(%s,%s,%s,%s,%s,%s)"
    data = (id, name, address,state,city, phone_number)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Method 4 Record inserted")
# rec={}
# rec['id']=21
# rec['name']='Abc'
# rec['address']='Jaora Compound'
# rec['state']='Madhya Pradesh'
# rec['city']='Indore'
# rec['phone_number']='9856956321'
# add_college(rec)
#READ
def read_college(dicts={}):
    id=dicts.get('id',0)
    name=dicts.get('name'," ")
    address = dicts.get('address'," ")
    state = dicts.get('state'," ")
    city = dicts.get('city'," ")
    phone_number = dicts.get('phone_number'," ")
    pagesize=dicts.get('pagesize',0)
    pagenumber=dicts.get('pagenumber',0)

    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='prac')
    cursor=connection.cursor()
    sql="select * from college where 1=1"
    if id != 0:
        sql += ' and id = ' + str(id)
    if name != ' ':
        sql += " and name like '" + name + "%'  "
    if address != ' ':
        sql += " and address like '" + name + "%'  "
    if state != ' ':
        sql += " and state like '" + name + "%'  "
    if city != ' ':
        sql += " and city like '" + name + "%'  "
    if phone_number != ' ':
        sql += " and Phone_Number like '" + name + "%'  "
    if pagenumber > 0:
        pagenumber = (pagenumber - 1) * pagesize
        sql += ' limit ' + str(pagenumber) + ',' + str(pagesize)
    print("Sql Query:", sql)
    cursor.execute(sql)
    result=cursor.fetchall()
    for data in result:
        print(data[0],'\t', data[1], '\t',data[2],'\t',data[3],'\t', data[4], '\t',data[5], '\t')
    connection.commit()
    connection.close()
    print("These are the records")

def findByphone_number(phone_number):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from college where phone_number = %s"
        data = (phone_number)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()


def get(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "select * from college where id = %s"
    data = (id)
    cursor.execute(sql, data)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()
get(4)
# findByphone_number(9876543222)

dicts={}
dicts['pagenumber'] = 1
dicts['pagesize'] = 5
# dicts['id'] = 1
# dicts['name'] ='a'
# read_college(dicts)



#UPDATE
def update_college(data):
    id = data['id']
    name = data['name']
    address = data['address']
    state = data['state']
    city = data['city']
    phone_number = data['ph_number']

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "update college set name = %s, address = %s, state = %s, city = %s, phone_number = %s where id = %s"
    data = (name, address, state, city , phone_number, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')
data={}
data['name']='Abhay'
# data['description']='Devlopment'
data['id']=21

# update_college(data)


#DELETE

def delete_college(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
    cursor = connection.cursor()
    sql = "delete from college where id = %s"
    data = (id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data deleted successfully')

# delete_college(21)
