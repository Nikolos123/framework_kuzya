import json


def add_test_data_type_course(site):
    type_data = ['Онлайн','Офлайн','Онлайн-Офлайн',]
    for i in type_data:
        name = site.decode_value(i)
        new_type = site.type_course(name)
        site.type_courses.append(new_type)


def add_test_data_course(site):
    online = "Онлайн"
    off_online = "Офлайн"

    dict_course = {
        'Python': [online, off_online],
        'Java': [online, ],
        'JavaScript': [off_online],
        'C': [online, ]
    }

    list_course = ['Python','Java','JavaScript','C']

    for i in list_course:
        type_course = dict_course.get(i)
        new_course = site.create_course(i,type_course)
        site.courses.append(new_course)



