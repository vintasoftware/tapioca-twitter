# coding: utf-8

import arrow

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)
from tapioca.serializers import SimpleSerializer
from requests_oauthlib import OAuth1

from .resource_mapping import RESOURCE_MAPPING


class TwitterSerializer(SimpleSerializer):

    def to_datetime(self, data):
        return arrow.get(data, 'ddd MMM DD HH:mm:ss Z YYYY').datetime

    def serialize_datetime(self, data):
        return arrow.get(data).format('ddd MMM DD HH:mm:ss Z YYYY')


class TwitterClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.twitter.com/1.1/'
    resource_mapping = RESOURCE_MAPPING
    serializer_class = TwitterSerializer

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(TwitterClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params['auth'] = OAuth1(api_params.get('api_key'),
                client_secret=api_params.get('api_secret'),
                resource_owner_key=api_params.get('access_token', ''),
                resource_owner_secret=api_params.get('access_token_secret', ''))

        return params

    def get_iterator_list(self, response_data):
        if isinstance(response_data, list):
            return response_data

        if isinstance(response_data, dict) and 'statuses' in response_data:
            return response_data['statuses']

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data, response):
        iterator_list = self.get_iterator_list(response_data)
        last_item = iterator_list[-1]
        if 'id' in last_item:
            if not 'params' in iterator_request_kwargs:
                iterator_request_kwargs['params'] = {}
            iterator_request_kwargs['params']['max_id'] = last_item['id']

            return iterator_request_kwargs


Twitter = generate_wrapper_from_adapter(TwitterClientAdapter)
