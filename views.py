import json

from flask import Flask
from flask_cors import CORS
from flask import request
from flask import render_template


class StaticUpdate:
    def __init__(self):
        self.data = ''
        return


class Response:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204

    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404


static_data = StaticUpdate()


def json2dict(data):
    return json.loads(data, strict=False) if data else dict()


def index():
    return render_template('index.html')


def update():
    data = json2dict(request.data)
    new_data = ''
    for k, v in data.items():
        new_data += '{}: {}\n'.format(k, v)
    static_data.data = new_data
    return static_data.data, Response.OK


def view_update():
    return static_data.data, Response.OK


def reset():
    static_data.data = ''
    return static_data.data, Response.OK
