

def add_test_data(site):
    type_data = ['Онлайн','Офлайн','Онлайн-Офлайн',]
    for i in type_data:
        name = site.decode_value(i)
        new_type = site.create_type_course(name)
        site.type_courses.append(new_type)
