# -*- coding: utf-8 -*-
""""""


import flask

from serverful import (
    Server,
    expose,
)


TEST_RULE = "/"


def test_simplest_e2e():
    serverful = _Test("serverful")
    bare = flask.Flask("bare")
    bare.route(TEST_RULE)(serverful.serve)
    with serverful.test_client() as one, bare.test_client() as other:
        assert one.get(TEST_RULE).data == other.get(TEST_RULE).data


class _Test(Server):

    @expose(rule=TEST_RULE)
    def serve(self):
        """"""
        return "Hello"
