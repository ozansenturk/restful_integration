import requests
import functools
import time
from flask import current_app, session
from . import bp
from flask import abort

def cache(_func=None, *, expiration_time):

    def decorator_name(func):
        """Keep a cache of previous function calls"""
        @functools.wraps(func)
        def wrapper_cache(*args, **kwargs):
            cache_key = "TOKEN"
            if time.time() > wrapper_cache.expiration_time:
                wrapper_cache.cache[cache_key] = func(*args, **kwargs)
                current_app.logger.debug("token expired and refreshed again ")
                wrapper_cache.expiration_time = time.time() + expiration_time
            else:
                if cache_key not in wrapper_cache.cache:
                    wrapper_cache.cache[cache_key] = func(*args, **kwargs)
                    current_app.logger.debug("token retrieved from API ")
                else:
                    current_app.logger.debug("token retrieved from cache ")

            return wrapper_cache.cache[cache_key]

        wrapper_cache.expiration_time = time.time() + expiration_time
        wrapper_cache.cache = dict()

        return wrapper_cache

    if _func is None:
        return decorator_name
    else:
        return decorator_name(_func)


@bp.before_app_request
@cache(expiration_time=500)
def get_token():
    """
    gets the token

    :param host:
    :param email:
    :param password:
    :return:
    """

    token_body = {"email": current_app.config['EMAIL'], "password": current_app.config['PASSWORD']}

    response = requests.post(current_app.config['HOST']+current_app.config['LOGIN_URL'], json=token_body)
    current_app.logger.debug("get_token service executed ")

    session['token']=response.json()
    # return response.json()


def build_header(token):
    """
    creates Authorization header with the value of token
    :param token:
    :return:
    """

    headers = {}
    headers["Authorization"] = token

    return headers


def post_query(url, data, params=None):

    token_json = session['token']

    status = token_json['status']
    token  = token_json['token']

    if token_json['status'] != 'APPROVED':
        current_app.logger.debug("status is {}".format(status))
        abort(500)

    headers = build_header(token)

    response = requests.post(current_app.config['HOST']+url, data=data, headers=headers, params=params)

    current_app.logger.debug("Response: {} ".format(response.json()))

    return response.json()


