from marksheet.marksheet_model import MarsksheetModel

def add_marksheet():
    params = {}
    # params['id'] = 8
    params['roll_no'] = 108
    params['name'] = 'abc'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = MarsksheetModel()
    model.add(params)


def update_marksheet():
    params = {}
    params['id'] = 21
    params['roll_no'] = 108
    params['name'] = 'Arjun Singh'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = MarsksheetModel()
    model.update(params)


def delete_marksheet():
    model = MarsksheetModel()
    model.delete(8)


def get_marksheet():
    model = MarsksheetModel()
    model.get(2)


def find_by_roll_no():
    model = MarsksheetModel()
    model.find_by_roll(103)


def search_marksheet():
    params = {}
    # params['name'] = 'abc'
    # params['roll_no'] = 101
    # params['pageNo'] = 1
    # params['pageSize'] = 5
    model = MarsksheetModel()
    model.search(params)
# update_marksheet()

# add_marksheet()
search_marksheet()
# get_marksheet()

find_by_roll_no()