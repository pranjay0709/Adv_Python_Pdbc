import pymysql
from pymysql import connect


class MarksheetModel:
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
        id = MarksheetModel.next_pk(self)
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
        data = (id, roll_no, name, physics, chemistry, maths)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')



    def update(data):
        id = data['id']
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "update marksheet set roll_no = %s, name = %s, physics = %s, chemistry = %s, maths = %s where id = %s"
        data = (roll_no, name, physics, chemistry, maths, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def delete(id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "delete from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def get(id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "rollNo", "name", "physics", "chemistry", "maths")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_roll(self,roll_no):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from college where roll_no = %s"
        data = (roll_no)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.close()


    def search(self,dicts={}):
        id = dicts.get('id', 0)
        name = dicts.get('name', '')
        roll_no = dicts.get('roll_no', 0)
        physics = dicts.get('physics', 0)
        chemistry = dicts.get('chemistry', 0)
        maths = dicts.get('maths', 0)
        page_size = dicts.get('page_size', 0)
        page_number = dicts.get('page_number', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from college where 1=1"
        if name != '':
            sql += " and name like '" + name + "%'"
        if roll_no != 0:
            sql += " and roll_no = " + str(roll_no)
        if physics != 0:
            sql += " and physics = " + str(physics)
        if chemistry != 0:
            sql += " and chemistry = " + str(chemistry)
        if maths != 0:
            sql += " and maths = " + str(maths)
        if page_number > 0:
            page_number = (page_number - 1) * page_size
            sql += ' limit ' + str(page_number) + ',' + str(page_size)
        print("Sql Query:", sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "rollNo", "name", "physics", "chemistry", "maths")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

