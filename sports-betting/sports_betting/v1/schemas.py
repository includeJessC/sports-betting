# -*- coding: utf-8 -*-

import six
from jsonschema import RefResolver
# TODO: datetime support

class RefNode(object):

    def __init__(self, data, ref):
        self.ref = ref
        self._data = data

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, value):
        return self._data.__setitem__(key, value)

    def __getattr__(self, key):
        return self._data.__getattribute__(key)

    def __iter__(self):
        return self._data.__iter__()

    def __repr__(self):
        return repr({'$ref': self.ref})

    def __eq__(self, other):
        if isinstance(other, RefNode):
            return self._data == other._data and self.ref == other.ref
        elif six.PY2:
            return object.__eq__(other)
        elif six.PY3:
            return object.__eq__(self, other)
        else:
            return False

    def __deepcopy__(self, memo):
        return RefNode(copy.deepcopy(self._data), self.ref)

    def copy(self):
        return RefNode(self._data, self.ref)

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'

definitions = {'definitions': {'UserMeta': {'type': 'object', 'required': ['password'], 'properties': {'name': {'type': 'string'}, 'surname': {'type': 'string'}, 'password': {'type': 'string'}}}, 'UserInfo': {'type': 'object', 'required': ['user_meta', 'id'], 'properties': {'user_meta': {'$ref': '#/definitions/UserMeta'}, 'id': {'type': 'string'}}}, 'BaseUserInfo': {'type': 'object', 'required': ['id', 'password'], 'properties': {'id': {'type': 'string'}, 'password': {'type': 'string'}}}, 'RegisterApprove': {'type': 'object', 'required': ['secret_code', 'id'], 'properties': {'id': {'type': 'string'}, 'secret_code': {'type': 'string'}}}, 'ErrorResponse': {'type': 'object', 'required': ['code', 'text'], 'properties': {'code': {'type': 'string'}, 'text': {'type': 'string'}}}, 'Match': {'type': 'object', 'required': ['id', 'name', 'first_team_result', 'second_team_result', 'first_team_name', 'second_team_name'], 'properties': {'id': {'type': 'integer'}, 'name': {'type': 'string'}, 'first_team_name': {'type': 'string'}, 'second_team_name': {'type': 'string'}, 'first_team_result': {'type': 'integer'}, 'second_team_result': {'type': 'integer'}, 'bets_result': {'type': 'double'}, 'user_bets': {'type': 'array', 'items': {'$ref': '#/definitions/Bets'}}}}, 'Competition': {'type': 'object', 'required': ['name', 'id', 'is_active', 'matches'], 'properties': {'name': {'type': 'string'}, 'id': {'type': 'integer'}, 'is_active': {'type': 'boolean'}, 'matches': {'type': 'array', 'items': {'$ref': '#/definitions/Match'}}, 'leader_board': {'type': 'array', 'items': {'$ref': '#/definitions/BetsResult'}}}}, 'Bets': {'type': 'object', 'required': ['name', 'bet'], 'properties': {'name': {'type': 'string'}, 'bet': {'type': 'integer'}, 'bet_profit': {'type': 'double'}}}, 'BetsResult': {'type': 'object', 'required': ['user_id', 'result'], 'properties': {'user_id': {'type': 'string'}, 'result': {'type': 'double'}, 'bets': {'type': 'array', 'items': {'$ref': '#/definitions/Bets'}}}}}, 'parameters': {}}

validators = {
    ('user_register', 'POST'): {'json': {'$ref': '#/definitions/UserInfo'}},
    ('user_login', 'POST'): {'json': {'$ref': '#/definitions/BaseUserInfo'}},
    ('user_register_approve', 'POST'): {'json': {'$ref': '#/definitions/RegisterApprove'}},
    ('user', 'PUT'): {'json': {'$ref': '#/definitions/UserMeta'}, 'args': {'required': ['id'], 'properties': {'id': {}}}},
    ('user', 'GET'): {'args': {'required': ['id'], 'properties': {'id': {}}}},
    ('competitions', 'GET'): {'args': {'required': ['id'], 'properties': {'id': {'schema': {'type': 'string'}}}}},
    ('competitions_info', 'POST'): {'args': {'required': ['competition_id', 'id'], 'properties': {'competition_id': {'schema': {'type': 'string'}}, 'id': {'schema': {'type': 'string'}}}}},
    ('competitions_info', 'GET'): {'args': {'required': ['competition_id', 'id'], 'properties': {'competition_id': {'schema': {'type': 'string'}}, 'id': {'schema': {'type': 'string'}}}}},
    ('match_info', 'GET'): {'args': {'required': ['match_id', 'id'], 'properties': {'match_id': {'schema': {'type': 'string'}}, 'id': {'schema': {'type': 'string'}}}}},
    ('create_competition', 'POST'): {'json': {'type': 'object', 'properties': {'parsing_ref': {'type': 'string'}}, 'required': ['parsing_ref']}, 'args': {'required': ['id'], 'properties': {'id': {'schema': {'type': 'string'}}}}},
    ('create_match', 'POST'): {'json': {'type': 'string'}, 'args': {'required': ['id', 'competion_id'], 'properties': {'id': {'schema': {'type': 'string'}}, 'competion_id': {'schema': {'type': 'string'}}}}},
    ('create_bet', 'POST'): {'json': {'type': 'object', 'properties': {'bets': {'type': 'array', 'items': {'$ref': '#/definitions/Bets'}}}, 'required': ['bets']}, 'args': {'required': ['id', 'match_id'], 'properties': {'id': {'schema': {'type': 'string'}}, 'match_id': {'schema': {'type': 'string'}}}}},
}

filters = {
    ('user_register', 'POST'): {200: {'headers': None, 'schema': None}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('user_login', 'POST'): {200: {'headers': None, 'schema': None}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('user_register_approve', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/UserInfo'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('user', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/UserInfo'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('user', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/UserInfo'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('competitions', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'required': ['competitions'], 'properties': {'competitions': {'type': 'array', 'items': {'$ref': '#/definitions/Competition'}}}}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('competitions_info', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Competition'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('competitions_info', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Competition'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('match_info', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Match'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('create_competition', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Competition'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('create_match', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Match'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
    ('create_bet', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Match'}}, 400: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}, 404: {'headers': None, 'schema': {'$ref': '#/definitions/ErrorResponse'}}},
}

scopes = {
}

resolver = RefResolver.from_schema(definitions)

class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True, resolver=None):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults, resolver=resolver)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None, resolver=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key or '$ref' in _schema:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, (dict, RefNode)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize_ref(schema, data):
        if resolver == None:
            raise TypeError("resolver must be provided")
        ref = schema.get(u"$ref")
        scope, resolved = resolver.resolve(ref)
        if resolved.get('nullable', False) and not data:
            return {}
        return _normalize(resolved, data)

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
            'ref': _normalize_ref
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'
        if schema.get(u'$ref', None):
            type_ = 'ref'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors
