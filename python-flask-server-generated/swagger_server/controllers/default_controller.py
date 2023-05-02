import connexion

from swagger_server.controllers.db_manager import DataBaseManagemantSystem, update_competition
from swagger_server.controllers.parser import parse_competition
from swagger_server.models.base_user_info import BaseUserInfo  # noqa: E501
from swagger_server.models.competition import Competition  # noqa: E501
from swagger_server.models.create_bet_body import CreateBetBody  # noqa: E501
from swagger_server.models.create_competition_body import CreateCompetitionBody  # noqa: E501
from swagger_server.models.create_match_body import CreateMatchBody  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.match import Match  # noqa: E501
from swagger_server.models.register_approve import RegisterApprove  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server.models.user_meta import UserMeta  # noqa: E501


def competitions_get(id_):  # noqa: E501
    """competitions_get

    Получает все соревнования пользователя. # noqa: E501

    :param id: 
    :type id: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def competitions_info_get(competition_id, id):  # noqa: E501
    """competitions_info_get

    Отдает информаицю о соревновании для этого пользовтеля. # noqa: E501

    :param competition_id: 
    :type competition_id: str
    :param id: 
    :type id: str

    :rtype: Competition
    """
    return 'do some magic!'


def competitions_info_post(competition_id, id_):  # noqa: E501
    """competitions_info_post

    Добавляет пользователя в участие в соревнование. # noqa: E501

    :param competition_id: 
    :type competition_id: str
    :param id: 
    :type id: str

    :rtype: Competition
    """
    try:
        db = DataBaseManagemantSystem()
        db.add_user_to_competition(id_, competition_id)
    except Exception as e:
        print(e)
        return ErrorResponse("BadRequest", "Что-то пошло не так"), 400


def create_bet_post(id_, match_id, competition_id, body=None):  # noqa: E501
    """create_bet_post

    Делает ставку. # noqa: E501

    :param id: 
    :type id: str
    :param match_id: 
    :type match_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: Match
    """
    if connexion.request.is_json:
        body = CreateBetBody.from_dict(connexion.request.get_json())  # noqa: E501
    db = DataBaseManagemantSystem()
    try:
        compet_url = db.get_competition_by_match_id(competition_id)
        if compet_url['parsing_ref'] is not None:
            update_competition(compet_url['special_id'], compet_url['parsing_ref'])
        db.check_if_match_active(match_id, compet_url['special_id'])
        db.add_bets_to_match(match_id, compet_url['special_id'], id_, connexion.request.get_json())
        return db.get_match_info(match_id, compet_url['special_id'], id_)
    except Exception as e:
        print(e)
        return ErrorResponse("BadMatch", "Неправильный матч"), 400


def create_competition_post(id_, body=None):  # noqa: E501
    """create_competition_post

    Создает новое соревнование. # noqa: E501

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: Competition
    """
    if connexion.request.is_json:
        body = CreateCompetitionBody.from_dict(connexion.request.get_json())
    try:
        if body.parsing_ref is None:
            result = {'competition_id': '0', "name": body.name if body.name else "Default", 'is_active': False,
                      'parsing_ref': None, 'ended_matches': [], 'not_ended_matches': []}
            db = DataBaseManagemantSystem()
            db.add_competition(id_, result)
            return Competition(result['name'], result['competition_id'], result['is_active'], [])
        result = parse_competition(body.parsing_ref)
        if body.name:
            result['name'] = body.name
        db = DataBaseManagemantSystem()
        special_id = db.add_competition(id_, result)
        matches = []
        for match in result['ended_matches']:
            matches.append(
                Match(match['id'], match['name'], match['team1_name'],
                      match['team2_name'], match['team1_res'],
                      match['team2_res'], match['is_active'], start_time=match['start_time'].strftime("%H:%M %B %d, %Y") if match['start_time'] is not None else None))
        for match in result['not_ended_matches']:
            matches.append(
                Match(match['id'], match['name'], match['team1_name'], match['team2_name'], match['team1_res'],
                      match['team2_res'], match['is_active'], start_time=match['start_time'].strftime("%H:%M %B %d, %Y") if match['start_time'] is not None else None))
        return Competition(result['name'], special_id, result['is_active'], matches)
    except Exception as e:
        print(e)
        return ErrorResponse("BadRequest", "Неправильная ссылка"), 400


def create_match_post(id_, competion_id, body=None):  # noqa: E501
    """create_match_post

    Создает новый матч. # noqa: E501

    :param id: 
    :type id: str
    :param competion_id: 
    :type competion_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: Match
    """
    if connexion.request.is_json:
        body = CreateMatchBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def match_info_get(match_id, id_, competition_id):  # noqa: E501
    """match_info_get

    Отдает информаицю о матче для этого пользовтеля. # noqa: E501

    :param match_id: 
    :type match_id: str
    :param id: 
    :type id: str

    :rtype: Match
    """
    db = DataBaseManagemantSystem()
    try:
        compet_url = db.get_competition_by_match_id(competition_id)
        if compet_url['parsing_ref'] is not None:
            update_competition(compet_url['special_id'], compet_url['parsing_ref'])
        return db.get_match_info(match_id, compet_url['special_id'], id_)
    except Exception as e:
        print(e)
        return ErrorResponse("BadMatch", "Неправильный матч"), 400


def user_get(id_):  # noqa: E501
    """user_get

    Выдача информации о пользователе # noqa: E501

    :param id: 
    :type id: str

    :rtype: UserInfo
    """
    db = DataBaseManagemantSystem()
    try:
        info = db.get_user_info(id_)
        return UserInfo(UserMeta(info['name'], info['surname'], info['password']), id_)
    except Exception:
        return ErrorResponse("BAD_USER", "Неправильный пользователь"), 400


def user_login_post(body=None):  # noqa: E501
    """user_login_post

    Залогинивает пользователя с заданными данными. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    db = DataBaseManagemantSystem()
    if connexion.request.is_json:
        body = BaseUserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        info = db.get_user_info(body.id)
        if info['password'] == body.password:
            token = db.get_user_token(body.id)
            return InlineResponse2001(token)
    except Exception:
        return ErrorResponse("BAD_USER", "Неправильный пользователь"), 400


def user_put(id, body=None):  # noqa: E501
    """user_put

    Изменение информации о пользователе. # noqa: E501

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: UserInfo
    """
    if connexion.request.is_json:
        body = UserMeta.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_register_approve_post(body=None):  # noqa: E501
    """user_register_approve_post

    Подтверждает регистрацию пользователя (страница с вводом слова регистрации). # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: UserInfo
    """
    db = DataBaseManagemantSystem()
    if connexion.request.is_json:
        body = RegisterApprove.from_dict(connexion.request.get_json())  # noqa: E501
    if db.check_registered(body.id):
        return ErrorResponse("REPEAT", "Вы уже зарегистрированы"), 400
    if db.check_registeration_approve(body.id, body.secret_code):
        db.update_approved_info(body.id)
        info = db.get_user_info(body.id)
        return UserInfo(id=body.id, user_meta=UserMeta(info['name'], info['surname'], info['password']))
    return ErrorResponse("BAD_CODE", "Неправильный код"), 400


def user_register_post(body=None):  # noqa: E501
    """user_register_post

    Регистрирует пользователя с заданными данными. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    db = DataBaseManagemantSystem()
    if connexion.request.is_json:
        body = UserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    if db.check_registered(body.id):
        return ErrorResponse("REPEAT", "Вы уже зарегистрированы"), 400
    db.add_new_user(body.id, body.user_meta.name, body.user_meta.surname, body.user_meta.password)
    return {}
