from rest_framework import pagination
import sys
class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'
    invalid_page_message = 'ไม่พบข้อมูล'
    def list(self, request, *args, **kwargs):
        response_data = super(CustomPagination,
                              self).list(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        if not response_data.data:
            self.response_format = ErrorInfo().response
        return Response(self.response_format)
