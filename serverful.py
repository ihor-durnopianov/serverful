# -*- coding: utf-8 -*-
""""""


import flask


class Server(flask.Flask):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.__class__.__dict__:
            func = getattr(self, name)
            try:
                method_or_methods, rule = func.exposed_by_serverful
            except AttributeError:
                continue
            if rule is None:
                rule = f"/{name}"
            if isinstance(method_or_methods, list):
                methods = method_or_methods
            else:
                methods = [method_or_methods]
            self.route(rule, methods=methods)(func)


def expose(method_or_methods="GET", rule=None):
    """"""
    def _decorate(func):
        # How much better would it be to inherit from function...
        func.exposed_by_serverful = method_or_methods, rule
        return func
    return _decorate
