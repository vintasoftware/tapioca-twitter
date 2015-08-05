
from decouple import config

from tapioca_twitter import Twitter
from tapioca.exceptions import TapiocaException


api = Twitter(api_key=config('API_KEY'),
    api_secret=config('API_SECRET'),
    access_token=config('ACCESS_TOKEN'),
    access_token_secret=config('ACCESS_TOKEN_SECRET'),)

try:
    r = api.statuses_user_timeline().get(params={'screen_name': 'xima', 'count': 2})
except TapiocaException as e:
    print e.client().data()
    print e.client().response().status_code

