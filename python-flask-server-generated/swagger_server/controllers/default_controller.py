import connexion
import six

from swagger_server.models.base_user_info import BaseUserInfo  # noqa: E501
from swagger_server.models.competition import Competition  # noqa: E501
from swagger_server.models.create_bet_body import CreateBetBody  # noqa: E501
from swagger_server.models.create_competition_body import CreateCompetitionBody  # noqa: E501
from swagger_server.models.create_match_body import CreateMatchBody  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.match import Match  # noqa: E501
from swagger_server.models.register_approve import RegisterApprove  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server.models.user_meta import UserMeta  # noqa: E501
from swagger_server import util
from swagger_server.controllers.db_manager import DataBaseManagemantSystem


def competitions_get(id):  # noqa: E501
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


def competitions_info_post(competition_id, id):  # noqa: E501
    """competitions_info_post

    Добавляет пользователя в участие в соревнование. # noqa: E501

    :param competition_id: 
    :type competition_id: str
    :param id: 
    :type id: str

    :rtype: Competition
    """
    return 'do some magic!'


def create_bet_post(id, match_id, body=None):  # noqa: E501
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
    return 'do some magic!'


def create_competition_post(id, body=None):  # noqa: E501
    """create_competition_post

    Создает новое соревнование. # noqa: E501

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: Competition
    """
    if connexion.request.is_json:
        body = CreateCompetitionBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_match_post(id, competion_id, body=None):  # noqa: E501
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


def match_info_get(match_id, id):  # noqa: E501
    """match_info_get

    Отдает информаицю о матче для этого пользовтеля. # noqa: E501

    :param match_id: 
    :type match_id: str
    :param id: 
    :type id: str

    :rtype: Match
    """
    return 'do some magic!'


def user_get(id):  # noqa: E501
    """user_get

    Выдача информации о пользователе # noqa: E501

    :param id: 
    :type id: str

    :rtype: UserInfo
    """
    return 'do some magic!'


def user_login_post(body=None):  # noqa: E501
    """user_login_post

    Залогинивает пользователя с заданными данными. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BaseUserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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
