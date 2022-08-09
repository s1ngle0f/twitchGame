import requests
from twitchAPI.twitch import Twitch
class TwitchClient:
    def __init__(self):
        self.client_id = 'unqn1ywwwblsl0d7xrd4m1k83r1ixj'
        self.secret_key = 'e83aj23g2gvu5nh70u9n2zy13khnef'
        self.twitch = Twitch(self.client_id, self.secret_key)
    def get_top_streamers(self, count, language):
        none_sort = self.twitch.get_streams(first=count, language=language)
        return [{'user_name':    stream['user_name'],
                 'viewer_count': stream['viewer_count']}
                for stream in none_sort['data']]
        # return none_sort
