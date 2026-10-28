from college_model import CollegeModel

def test_add_college():
    params = {}
    # params['id'] = 8
    params['name'] = 'abc'
    params['state'] = 70
    params['city'] = 67
    params['phone_number'] = 79

    model = CollegeModel()
    model.add(params)


def test_update_college():
    params = {}
    params['id'] = 21
    params['roll_no'] = 108
    params['name'] = 'Arjun Singh'
    params['state'] = 70
    params['city'] = 67
    params['phone_number'] = 79

    model = CollegeModel()
    model.update(params)


def delete_college():
    model = CollegeModel()
    model.delete(8)


def get_college():
    model = CollegeModel()
    model.get(2)


def test_find_college_name():
    model = CollegeModel()
    model.find_by_name(103)


def search_college():
    params = {}
    # params['name'] = 'abc'
    # params['roll_no'] = 101
    # params['pageNo'] = 1
    # params['pageSize'] = 5
    model = CollegeModel()
    model.search(params)
# update_marksheet()

# add_marksheet()
search_college()
# get_marksheet()

# find_by_roll_no()