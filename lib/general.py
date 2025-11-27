# Author : ysh
# 2025/11/17 Mon 17:37:45
from core.general import *

def ok(data = None, **ot) -> dict:
    info('OK detected, returning ' + str({
        'ok': True,
        'data': data,
        **ot
    }))
    return {
        'ok': True,
        'data': data,
        **ot
    }

def fail(error = None) -> dict:
    warning('Error detected, returning ' + str({
        'ok': False,
        'data': error,
        'error': error
    }))
    return {
        'ok': False,
        'data': error,
        'error': error
    }