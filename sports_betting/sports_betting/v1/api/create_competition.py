# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class CreateCompetition(Resource):

    def post(self):
        print(g.json)
        print(g.args)

        return {'name': 'something', 'id': 9573, 'is_active': False, 'matches': []}, 200, None