import pymysql
class role_model:
    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select max(id) from role"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def insert_role(self, data={}):
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

    # READ
    def sel_rol(self, dicts={}):
        id = dicts.get('id', 0)
        name = dicts.get('name', " ")
        description = dicts.get('description', " ")
        page_size = dicts.get('page_size', 0)
        page_number = dicts.get('page_number', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from role where 1=1"
        if id != 0:
            sql += ' and id = ' + str(id)
        if name != ' ':
            sql += " and name like '" + name + "%'  "
        if description != ' ':
            sql += " and description like '" + name + "%'  "
        if page_number > 0:
            page_number = (page_number - 1) * page_size
            sql += ' limit ' + str(page_number) + ',' + str(page_size)
        print("Sql Query:", sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t')
        connection.commit()
        connection.close()
        print("These are the records")


    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from role where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2])
        connection.commit()
        connection.close()

    def find_by_name(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from role where name = %s"
        data = (name)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2])
        connection.commit()
        connection.close()

    def update_role(self,data):
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



    # DELETE

    def delete_role(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "delete from role where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')
