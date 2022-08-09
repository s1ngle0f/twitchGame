from django.shortcuts import render
from twitchgame.entries import twitch_service

twitch_client = twitch_service.TwitchClient()

def index(request):
    print(twitch_client.get_top_streamers(count=5, language='ru'))
    return render(request, 'main/index.html')