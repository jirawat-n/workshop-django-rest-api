from rest_framework.response import Response
from rest_framework import status

class ResponseInfo(object):
    def __init__(self, user=None, **args):
        self.response = {
            "message": args.get('message', 'ดึงข้อมูลสำเร็จ'),
            "data": args.get('data', []),
        }


class ErrorInfo(object):
    def __init__(self, user=None, **args):
        self.response = {
            "error": args.get('error',status.HTTP_404_NOT_FOUND),
            "message": args.get('message', 'ไม่พบข้อมูล'),
            "data": args.get('data', []),
        }
