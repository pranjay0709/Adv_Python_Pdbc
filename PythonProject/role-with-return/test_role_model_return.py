from role_return import RoleModel

def add_role():
    params = {}
    params['id'] = 15
    params['name'] = 'Cleaning'
    params['description'] = 'Maintain'
    model = RoleModel()
    model.add(params)


def update_role():
    params = {}
    params['id'] = 15
    params['name'] = 'Cleaning'
    params['description'] = 'Hygine'

    model = RoleModel()
    model.update(params)


def del_role():
    model = RoleModel()
    model.delete(8)


def get_role():
    model = RoleModel()
    model.get(2)
    # for data in list:
    #     print(data['id'], '\t', data['name'], '\t', data['description'],'\t' )


def find_by_column():
    model = RoleModel()
    model.find_by_name("IT")


def search_role():
    params = {}
    # params['name'] = 'abc'
    # params['id'] = 1
    # params['page_number'] = 1
    # params['page_size'] = 5
    model = RoleModel()
    model.search(params)


# find_by_column()
get_role()
# add_role()
# update_role()
# search_role()
