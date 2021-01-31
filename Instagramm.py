from instagram_private_api import Client, ClientCompatPatch

user_name = 'log'
password = 'pass'


api = Client(user_name, password)
results = api.feed_timeline()

stra = api.oembed("https://www.instagram.com/p/CKq8pgypcc1/")['media_id']
print(stra)


users = api.media_likers(str(stra))['users'][:100]
print(users)

users_href = ['https://www.instagram.com/' + str(i['username']) for i in users]
print(users_href)


#api.friendships_create(7199352842)

# for i in users:
#     # ' - ' + str(i['pk'])
#     print('https: // www.instagram.com /' + str(i['username']))
#
#     #api.friendships_create(i['pk'])
#     #sleep(2)


#media_id
#print(api.replay_broadcast_likes())


#7199352842

