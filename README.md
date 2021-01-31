# Instagram-bot
Instagram bot for view stories/get likers from post. 


# Getting hrefs of users, who liked some post

```
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
```
