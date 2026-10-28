import pymysql
from pymysql import connect


class CollegeModel:
    def next_pk(self):
        pk=0
        connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='prac')
        cursor=connection.cursor()
        sql='select max(id) from college'
        cursor.execute(sql)
        result=cursor.fetchall
        for data in result:
            if data[0] is not None:
                pk= data[0]
        connection.close()
        return pk + 1

    def add(self, data={}):
        id = CollegeModel.next_pk(self)
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_number = data['phone_number']

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "insert into college values(%s,%s,%s,%s,%s,%s)"
        data = (id, name, address, state, city, phone_number)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()



    def update(self,data):
        id = data['id']
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_number = data['ph_number']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "update college set name = %s, address = %s, state = %s, city = %s, phone_number = %s where id = %s"
        data = (name, address, state, city, phone_number, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')


    def delete(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "delete from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def get(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "address", "state", "city", "phone_number")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_name(self,name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from college where name = %s"
        data = (name)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "address", "state", "city", "phone_number")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list


    def search(self,dicts={}):
        id = dicts.get('id', 0)
        name = dicts.get('name', "")
        address = dicts.get('address', "")
        state = dicts.get('state', "")
        city = dicts.get('city', "")
        phone_number = dicts.get('phone_number', "")
        page_size = dicts.get('page_size', 0)
        page_number = dicts.get('page_number', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from college where 1=1"
        if id != 0:
            sql += ' and id = ' + str(id)
        if name != '':
            sql += " and name like '" + name + "%'"
        if address != '':
            sql += " and address like '" + name + "%'"
        if state != '':
            sql += " and state like '" + name + "%'"
        if city != '':
            sql += " and city like '" + name + "%'"
        if phone_number != '':
            sql += " and phone_number like '" + name + "%'"
        if page_number > 0:
            page_number = (page_number - 1) * page_size
            sql += ' limit ' + str(page_number) + ',' + str(page_size)
        print("Sql Query:", sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        # for data in result:
        #     print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5], '\t')
        connection.close()
        print("These are the records")

