from rest_framework.views import APIView
from rest_framework.response import Response

import requests
from bs4 import BeautifulSoup 

class NetflixListViewSet(APIView):
    def post(self, request, *args, **kwargs):
        url = 'https://www.rottentomatoes.com/browse/tv_series_browse/affiliates:netflix~audience:upright~critics:fresh~sort:popular?page=1'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.find_all('span', 'p--small')
        
        for item in list_items:
            if item.parent.parent.parent.parent.parent.parent.name == 'div':
                # score-pairs 태그 정보 item.previous_sibling.previous_sibling
                audiencescore = item.previous_sibling.previous_sibling.get('audiencescore')
                audiencesentiment = item.previous_sibling.previous_sibling.get('audiencesentiment')
                criticsscore = item.previous_sibling.previous_sibling.get('criticsscore')
                criticssentiment = item.previous_sibling.previous_sibling.get('criticssentiment')
                posterSrc = item.parent.previous_sibling.previous_sibling.get('src')
                lastUpdate = item.next_sibling == None if '' else item.next_sibling.get_text().strip()
                
                print(f'title - {item.get_text().strip()}')
                print(f'last update - {lastUpdate}')
                print(f'audiencescore : {audiencescore}, audiencesentiment : {audiencesentiment}, criticsscore : {criticsscore}, criticssentiment : {criticssentiment}')
                print(f'img - {posterSrc}')
                print('-'*20)
        
        return Response('Success')
