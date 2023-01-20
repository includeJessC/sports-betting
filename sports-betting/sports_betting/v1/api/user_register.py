# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource


class UserRegister(Resource):

    def post(self):
        return None, 200, None