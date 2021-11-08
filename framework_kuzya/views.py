"""Модуль, содержащий контроллеры веб-приложения"""
from framework_kuzya.templator import render
from components.decorators import AppRoute
routes = {}

@AppRoute(routes=routes, url='/')
class Index:
    def __call__(self,request):
        return '200 OK', render('schedule.html')

@AppRoute(routes=routes, url='/about/')
class About:
    def __call__(self,request):
        return '200 OK', render('about.html')
