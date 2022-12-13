from rest_framework.views import APIView
from rest_framework.response import Response

import requests
from bs4 import BeautifulSoup 

def seasonInfo(link):   
    # link = 'https://www.rottentomatoes.com/tv/wednesday'
    response = requests.get(link)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    seasonSection = soup.find('section', {'id':'seasonList'})
    seasonItems = seasonSection.find_all('a')

    seasons = []
    
    for item in seasonItems:
        season = {}
        seassonItem = item.find('season-list-item')
        if seassonItem != None:
            season['href'] = 'https://www.rottentomatoes.com' + item.get('href')

            info = {}
            infos = seassonItem.get('info').split(', ')
            info['year'] = infos[0]
            info['ott'] = infos[1]
            info['episodes'] = infos[2].split(' ')[0]
            
            season['info'] = info
            season['posterurl'] = seassonItem.get('posterurl')
            season['tomatometerscore'] = seassonItem.get('tomatometerscore')
            season['tomatometerstate'] = seassonItem.get('tomatometerstate')

            seasons.append(season)

    return seasons
        

class NetflixListViewSet(APIView):

    def post(self, request, *args, **kwargs):
        url = 'https://www.rottentomatoes.com/browse/tv_series_browse/affiliates:netflix~audience:upright~critics:fresh~sort:popular?page=1'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.find_all('span', 'p--small')

        result = {}
        result['programs'] = []

        for item in list_items:
            if item.parent.parent.parent.parent.parent.parent.name == 'div':
                dicItem = {}

                # score-pairs 태그 정보 item.previous_sibling.previous_sibling
                dicItem['link'] = 'https://www.rottentomatoes.com' + item.parent.parent.parent.get('href')
                dicItem['title'] = item.get_text().strip()
                dicItem['audiencescore'] = item.previous_sibling.previous_sibling.get('audiencescore')
                dicItem['audiencesentiment'] = item.previous_sibling.previous_sibling.get('audiencesentiment')
                dicItem['criticsscore'] = item.previous_sibling.previous_sibling.get('criticsscore')
                dicItem['criticssentiment'] = item.previous_sibling.previous_sibling.get('criticssentiment')

                posterSrc = item.parent.previous_sibling.previous_sibling.get('src')
                if posterSrc == None:
                    posterSrc = item.parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.get('src')

                dicItem['posterSrc'] = posterSrc
                dicItem['lastUpdate'] = item.next_sibling == None if '' else item.next_sibling.get_text().strip()

                dicItem['seasons'] = seasonInfo(dicItem['link'])

                result['programs'].append(dicItem)

                # print(f'title - {dicItem}')
                # print('-' * 20)
        
        return Response(result)

    
