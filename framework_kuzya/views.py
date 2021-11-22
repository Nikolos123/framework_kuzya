"""Модуль, содержащий контроллеры веб-приложения"""
from framework_kuzya.templator import render
from components.models import Engine
from components.decorators import AppRoute

site = Engine()
routes = {}

# Класс-контроллер - Страница "главная страница"
@AppRoute(routes=routes, url='/')
class Index:
    def __call__(self,request):
        return '200 OK', render('schedule.html')

# Класс-контроллер - Страница "о компании"
@AppRoute(routes=routes, url='/about/')
class About:
    def __call__(self,request):
        return '200 OK', render('about.html')

# Класс-контроллер - Страница "обратная связь"
@AppRoute(routes=routes, url='/feedback/')
class Feedback:
    def __call__(self,request):
        return '200 OK', render('feedback.html')


# Класс-контроллер - Страница "Список категорий"
@AppRoute(routes=routes, url='/category-list/')
class CategoryList:

    def __call__(self, request):

        return '200 OK', render('category.html',
                                objects_list=site.categories)


# Класс-контроллер - Страница "Создать категорию"
@AppRoute(routes=routes, url='/create-category/')
class CreateCategory:

    def __call__(self, request):

        if request['method'] == 'POST':
            data = request['data']
            name = site.decode_value(data['name'])
            category_id = data.get('category_id')
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))
                category['name'] = name
                category['category'] = category
            new_category = site.create_category(name, category)
            site.categories.append(new_category)

        #     return '200 OK', render('category.html',
        #                             objects_list=site.categories)
        # else:
        #     categories = site.categories
        return '200 OK', render('category.html',
                                    categories=site.categories)