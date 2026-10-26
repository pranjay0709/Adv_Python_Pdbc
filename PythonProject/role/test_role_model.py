from role.role_model import role_model

def add_role():
    params = {}
    params['id'] = 15
    params['name'] = 'Cleaning'
    params['description'] = 'Maintain'
    model = role_model()
    model.insert_role(params)


def update_role():
    params = {}
    params['id'] = 15
    params['name'] = 'Cleaning'
    params['description'] = 'Hygine'

    model = role_model()
    model.update_role(params)


def del_role():
    model = role_model()
    model.delete_role(8)


def get_role():
    model = role_model()
    model.get(2)


def find_by_column():
    model = role_model()
    model.find_by_name("IT")


def search_role():
    params = {}
    # params['name'] = 'abc'
    # params['id'] = 1
    # params['page_number'] = 1
    # params['page_size'] = 5
    model = role_model()
    model.sel_rol(params)


# find_by_column()
# get_role()
# add_role()
# update_role()
search_role()
