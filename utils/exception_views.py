from django.http import JsonResponse

def error_404(request,exception):
    messages = ('The Endpoint is not found')
    response = JsonResponse(data={'message':message,'status_code':404})
    response.status_code=404
    return response

def error_401(request,exception):
    messages = ('Refetch Token ไม่ถูกต้อง')
    response = JsonResponse(data={'message':message,'status_code':'REFETCH_TOKEN_FAIL'})
    response.status_code=401
    return response

def error_500(request):
    message = ('An error occured, It is on us')
    response = JsonResponse(data={'message':message,'status_code':500})
    response.status_code=500
    return response