import pymysql
def refine_sel(dicts={}):
    id=dicts.get('id',0)
    name=dicts.get('name'," ")
    pagesize=dicts.get('pagesize',0)
    pagenumber=dicts.get('pagenumber',0)

    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='prac')
    cursor=connection.cursor()
    sql="select * from prac_crud where 1=1"
    if id != 0:
        sql += ' and id = ' + str(id)
    if name != ' ':
        sql += " and name like '" + name + "%'  "
    if pagenumber > 0:
        pagenumber = (pagenumber - 1) * pagesize
        sql += ' limit ' + str(pagenumber) + ',' + str(pagesize)
    print("Sql Query:", sql)
    cursor.execute(sql)
    result=cursor.fetchall()
    for data in result:
        print(data[0],'\t', data[1], '\t')
    connection.commit()
    connection.close()
    print("These are the records")

dicts={}
# dicts['pagenumber'] = 1
# dicts['pagesize'] = 2
# dicts['id'] = 1
dicts['name'] ='a'

refine_sel(dicts)

