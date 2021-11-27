# Декоратор для реализации маршрутизации
class AppRoute:
    def __init__(self, routes, url,method):
        """
        Сохраняем значение переданного параметра
        """
        self.routes = routes
        self.url = url
        self.method = method

    def __call__(self, cls):
        """
        Сам декоратор
        """
        self.routes[self.url] = cls()