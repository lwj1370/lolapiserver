from rest_framework.views import APIView
from rest_framework.response import Response

class NetflixListViewSet(APIView):
    def post(self, request, *args, **kwargs):
        print('Request Netflix List Success')
        return Response('Success')
