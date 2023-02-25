# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class UserRegisterApprove(Resource):

    def post(self):
        print(g.json)

        return {'user_meta': {}, 'id': 'something'}, 200, None