# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class MatchInfo(Resource):

    def get(self):
        print(g.args)

        return {'id': 9573, 'name': 'something', 'first_team_name': 'something', 'second_team_name': 'something', 'first_team_result': 9573, 'second_team_result': 9573}, 200, None