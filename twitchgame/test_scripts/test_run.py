import twitch_client
twitch = twitch_client.TwitchClient()
# print(map(i.values()) for i in twitch.get_top_streamers(count=5, language='ru'))
print(twitch.get_top_streamers(count=5, language='ru'))
