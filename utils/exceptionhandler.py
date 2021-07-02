from rest_framework.views import exception_handler
from rest_framework import status


def custom_exception_handler(exc, context):

    handlers = {
        'Http404': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
        'NotFound': error_404_not_found,
        'NotAuthenticated': NotAuthenticated,
        'AuthenticationFailed': AuthenticationFailed,
        'ParseError': ParseError,
        'NotAcceptable': NotAcceptable,

    }

    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        if "AuthUserAPIView" in str(context['view']) and exc.status_code == 401:
            response.status_code = 200
            response.data = {
                'is_logged_in': False,
                'status_code': 200
            }
        return handlers[exception_class](exc, context, response)
    return response


def _handle_authentication_error(exc, context, response):
    response.data = ({
        "code": "HTTP_401_UNAUTHORIZED",
        'msg': 'Authentication credentials were not provided',
    })
    return response


def error_404_not_found(exc, context, response):
    response.data = ({
        "code": "HTTP_404_NOT_FOUND",
        'msg': 'ไม่พบข้อมูล',
    })
    return response


def AuthenticationFailed(exc, context, response):
    response.data = ({
        "msg": "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง",
        "code": "LOGIN_FAIL"
    })
    return response


def NotAcceptable(exc, context, response):
    response.data = ({
        "msg": "ลงทะเบียนไม่สำเร็จ มี username นี้แล้ว",
        "code": "REGISTER_FAIL",
    })
    return response


def NotAuthenticated(exc, context, response):
    response.data = ({
        "code": "HTTP_401_UNAUTHORIZED",
        "msg": "Authentication credentials were not provided.",
    })
    return response


def ParseError(exc, context, response):
    response.data = ({
        "code": "HTTP_404_NOT_FOUND",
        'msg': 'ไม่พบข้อมูล',
    })
    return response


def _handle_generic_error(exc, context, response):
    response.data = {
        'msg': 'ไม่พบข้อมูล',
        'code': 'HTTP_404_NOT_FOUND'
    }
    return response
