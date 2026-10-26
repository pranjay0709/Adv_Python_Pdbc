from marksheet.marksheet_module.marksheet_model import marksheet_model

def add_marksheet():
    params = {}
    # params['id'] = 8
    params['roll_no'] = 108
    params['name'] = 'abc'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = marksheet_model()
    model.add(params)


def update_marksheet():
    params = {}
    params['id'] = 8
    params['roll_no'] = 108
    params['name'] = 'ooo'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = marksheet_model()
    model.update(params)


def delete_marksheet():
    model = marksheet_model()
    model.delete(8)


def get_marksheet():
    model = marksheet_model()
    model.get(2)


def find_by_roll_no():
    model = marksheet_model()
    model.find_by_roll_no(103)


def search_marksheet():
    params = {}
    # params['name'] = 'abc'
    # params['roll_no'] = 101
    params['pageNo'] = 1
    params['pageSize'] = 5
    model = marksheet_model()
    model.search(params)


search_marksheet()
# get_marksheet()
