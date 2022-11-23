from django.http import HttpResponse

# Middleware 설정 정보 documentation
# https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse
class CustomHttpMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code != 200:
            response = self.process_response(request, response)
        
        return response
    
    def process_response(self, request, response):
        
        response_data = {
            'code': response.status_code, # 실패 코드
            'message': response.reason_phrase # 실패 이유
        }

        res = HttpResponse()
        res.write(response_data) # Data field 작성
        res.headers['Content-Type'] = 'application/json' # 헤더 정보 입력
        return res

        # HttpResponse 바로 생성해서 전달 방법
        # return HttpResponse(str(response_data), headers={
        #     'Content-Type': 'application/json',
        # })
