from user_model import UserModel
import datetime

def test_add():
    data = {}
    data['id'] = 1
    data['first_name'] = 'Pj'
    data['last_name'] = 'J'
    data['login_id'] = 'pj'
    data['password'] = 'pj'
    data['dob'] = datetime.date(2003,10,31)
    data['address'] = 'Indore'

    user = UserModel()
    user.add(data)

# test_add()

def test_update():
    data = {}
    data['id'] = 2
    data['first_name'] = 'jk'
    data['last_name'] = 'k'
    data['login_id'] = 'Madhya'
    data['password'] = 'indore'
    data['dob'] = datetime.date(2003,11,5)
    data['address'] = 'bhopal'

    user = UserModel()
    user.update(data)


def test_delete():
    user = UserModel()
    user.delete(2)



def test_get():
    user = UserModel()
    list = user.get(1)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t', data['password'],
              '\t', data['dob'], '\t', data['address'], )


def test_find_by_login_id():
    user = UserModel()
    list = user.find_by_login_id(103)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t',
              data['password'], '\t', data['dob'], '\t', data['address'], )


def test_search():
    data = {}
    # data['name'] = 'abc'
    # data['roll_no'] = 101
    data['page_no'] = 1
    data['page_size'] = 0
    model = UserModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t',
              data['password'], '\t', data['dob'], '\t', data['address'], )



# test_update()
# test_read()
# test_get()
# test_add()
# test_delete()
# test_search()