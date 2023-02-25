# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.user_register import UserRegister
from .api.user_login import UserLogin
from .api.user_register_approve import UserRegisterApprove
from .api.user import User
from .api.competitions import Competitions
from .api.competitions_info import CompetitionsInfo
from .api.match_info import MatchInfo
from .api.create_competition import CreateCompetition
from .api.create_match import CreateMatch
from .api.create_bet import CreateBet


routes = [
    dict(resource=UserRegister, urls=['/user_register'], endpoint='user_register'),
    dict(resource=UserLogin, urls=['/user_login'], endpoint='user_login'),
    dict(resource=UserRegisterApprove, urls=['/user_register_approve'], endpoint='user_register_approve'),
    dict(resource=User, urls=['/user'], endpoint='user'),
    dict(resource=Competitions, urls=['/competitions'], endpoint='competitions'),
    dict(resource=CompetitionsInfo, urls=['/competitions_info'], endpoint='competitions_info'),
    dict(resource=MatchInfo, urls=['/match_info'], endpoint='match_info'),
    dict(resource=CreateCompetition, urls=['/create/competition'], endpoint='create_competition'),
    dict(resource=CreateMatch, urls=['/create/match'], endpoint='create_match'),
    dict(resource=CreateBet, urls=['/create/bet'], endpoint='create_bet'),
]