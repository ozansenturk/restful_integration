import requests
import functools
import time
from flask import current_app

def cache(_func=None, *, expiration_time):

    def decorator_name(func):
        """Keep a cache of previous function calls"""
        @functools.wraps(func)
        def wrapper_cache(*args, **kwargs):
            cache_key = "TOKEN"
            if time.time() > wrapper_cache.expiration_time:
                wrapper_cache.cache[cache_key] = func(*args, **kwargs)
                wrapper_cache.expiration_time = time.time() + expiration_time
            else:
                if cache_key not in wrapper_cache.cache:
                    wrapper_cache.cache[cache_key] = func(*args, **kwargs)

            return wrapper_cache.cache[cache_key]

        wrapper_cache.expiration_time = time.time() + expiration_time
        wrapper_cache.cache = dict()

        return wrapper_cache

    if _func is None:
        return decorator_name
    else:
        return decorator_name(_func)


@cache(expiration_time=30)
def get_token(login_url, email, password):
    """
    gets the token

    :param host:
    :param email:
    :param password:
    :return:
    """

    token_body = {"email": email, "password": password}

    response = requests.post(current_app.config['HOST']+login_url, json=token_body)

    return response.json()


def build_header(token):
    """
    creates Authorization header with the value of token
    :param token:
    :return:
    """

    headers = {}
    headers["Authorization"] = token

    return headers


def post_query(url, one_token, data):

    headers = build_header(one_token)

    response = requests.post(current_app.config['HOST']+url, data=data, headers=headers)

    print("response: {}".format(response.json()))

    return response.json()


