import pymysql
class RoleModel:
    def next_pk(self):
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

    def add(self, data={}):
        id = RoleModel.next_pk(self)
        name = data['name']
        description = data['description']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "insert into role values(%s, %s, %s)"
        data = (id, name, description)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Method 4 Record inserted")



    def update(self,data):
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

    def delete(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "delete from role where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')


 # READ
    def search(self, dicts={}):
        id = dicts.get('id', 0)
        name = dicts.get('name', "")
        description = dicts.get('description', "")
        page_size = dicts.get('page_size', 0)
        page_number = dicts.get('page_number', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from role where 1=1"
        if id != 0:
            sql += ' and id = ' + str(id)
        if name != '':
            sql += " and name like '" + name + "%' "
        if description != '':
            sql += " and description like '" + name + "%'"
        if page_number > 0:
            page_number = (page_number - 1) * page_size
            sql += ' limit ' + str(page_number) + ',' + str(page_size)
        print("Sql Query:", sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "name", "description")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from role where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "description")
        list = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list


    def find_by_name(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='prac')
        cursor = connection.cursor()
        sql = "select * from role where name = %s"
        data = (name)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "name", "description")
        list = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list