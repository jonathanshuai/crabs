import requests

API_KEY = '045e323fa13d495a82532ed57a97c6ac'


def call():
    print("called")


class CrabCaller():
    def call_crabs(self, n):
        return self.call_api(n, 'crabs')

    def call_friends(self, n, friend='penguin'):
        return self.call_api(n, friend)

    def call_api(self, n, query):
        base = 'https://newsapi.org/v2/everything?apiKey={}'.format(API_KEY)
        query_url = 'q={}'.format(query)

        request_url = '&'.join([base, query_url])
        r = requests.get(request_url)
        response_json = r.json()

        image_urls = []
        if response_json['status'] == 'ok':
            articles = response_json['articles']
            i = 0
            while i < len(articles) and len(image_urls) < n:
                if 'urlToImage' in articles[i]:
                    image_urls.append(articles[i]['urlToImage'])
                i += 1

        return image_urls
