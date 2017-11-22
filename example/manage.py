#!/usr/bin/python
# -*- coding: utf-8 -*-

from runserver import app
from sanic_script import Manager

manager = Manager(app)


@manager.command
def hello():
    print("hello")


if __name__ == "__main__":
    manager.run()