# coding: utf-8

RESOURCE_MAPPING = {
    'users_search': {
        'resource': 'users/search.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/users/search'
    },
    'users_lookup': {
        'resource': 'users/lookup.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/users/lookup'
    },
    'statuses_mentions_timeline': {
        'resource': 'statuses/mentions_timeline.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline'
    },
    'statuses_user_timeline': {
        'resource': 'statuses/user_timeline.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/statuses/user_timeline'
    },
    'statuses_home_timeline': {
        'resource': 'statuses/home_timeline.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/statuses/home_timeline'
    },
    'statuses_retweets_of_me': {
        'resource': 'statuses/retweets_of_me.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/statuses/retweets_of_me'
    },
    'statuses_retweets_of_id': {
        'resource': 'statuses/retweets/{id}.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/statuses/retweets/%3Aid'
    },
    'statuses_show': {
        'resource': 'statuses/show.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/statuses/show/%3Aid'
    },
    'statuses_destroy_from_id': {
        'resource': 'statuses/destroy/{id}.json',
        'docs': 'https://dev.twitter.com/rest/reference/post/statuses/destroy/%3Aid'
    },
    'statuses_update': {
        'resource': 'statuses/update.json',
        'docs': 'https://dev.twitter.com/rest/reference/post/statuses/update'
    },
    'statuses_retweet_id': {
        'resource': 'statuses/retweet/{id}.json',
        'docs': 'https://dev.twitter.com/rest/reference/post/statuses/retweet/%3Aid'
    },
    'statuses_oembed': {
        'resource': 'statuses/oembed.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/statuses/oembed'
    },
    'retweeters_of_id': {
        'resource': 'retweeters/ids.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/statuses/retweeters/ids'
    },
    'statuses_lookup': {
        'resource': 'statuses/lookup.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/statuses/lookup'
    },
    'media_upload': {
        'resource': 'media/upload.json',
        'docs': 'https://dev.twitter.com/rest/reference/post/media/upload'
    },
    'direct_messages_sent': {
        'resource': 'direct_messages/sent.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/direct_messages/sent'
    },
    'direct_messages_show': {
        'resource': 'direct_messages/show.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/direct_messages/show'
    },
    'search_tweets': {
        'resource': 'search/tweets.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/search/tweets'
    },
    'direct_messages': {
        'resource': 'direct_messages.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/direct_messages'
    },
    'direct_messages_destroy': {
        'resource': 'direct_messages/destroy.json',
        'docs': 'https://dev.twitter.com/rest/reference/post/direct_messages/destroy'
    },
    'direct_messages_new': {
        'resource': 'direct_messages/new.json',
        'docs': 'https://dev.twitter.com/rest/reference/post/direct_messages/new'
    },
    'friendships_no_retweets_ids': {
        'resource': 'friendships/no_retweets/ids.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/friendships/no_retweets/ids'
    },
    'friends_ids': {
        'resource': 'friends/ids.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/friends/ids'
    },
    'friends_list': {
        'resource': 'friends/list.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/friends/list'
    },
    'followers_ids': {
        'resource': 'followers/ids.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/followers/ids'
    },
    'followers_list': {
        'resource': 'followers/list.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/followers/list'
    },
    'friendships_incoming': {
        'resource': 'friendships/incoming.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/friendships/incoming'
    },
    'friendships_outgoing': {
        'resource': 'friendships/outgoing.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/friendships/outgoing'
    },
    'friendships_create': {
        'resource': 'friendships/create.json',
        'docs': 'https://dev.twitter.com/rest/reference/post/friendships/create'
    },
    'friendships_destroy': {
        'resource': 'friendships/destroy.json',
        'docs': 'https://dev.twitter.com/rest/reference/post/friendships/destroy'
    },
    'friendships_update': {
        'resource': 'friendships/update.json',
        'docs': 'https://dev.twitter.com/rest/reference/post/friendships/update'
    },
    'friendships_show': {
        'resource': 'friendships/show.json',
        'docs': 'https://dev.twitter.com/rest/reference/get/friendships/show'
    },
}
