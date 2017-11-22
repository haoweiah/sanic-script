#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sanic import Sanic

app = Sanic(__name__)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
