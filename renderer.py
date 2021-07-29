from rest_framework import renderers
import pdb
import json


class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, render_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dump('error', data)
        else:
            response = json.dump('data', data)
        return response
