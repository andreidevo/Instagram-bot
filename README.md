# Instagram-bot
Instagram bot for view stories/get likers from post. 
.
.
.
.
Getting hrefs of users, who liked some post
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



if you want create some subscribe:
```
for i in users:
    api.friendships_create(i['pk'])
    sleep(2)
```

so, all documentation you can find here: https://github.com/ping/instagram_private_api/blob/master/COMPAT.md 
.
.
.
.
.
.
.
Next, lets create view stories bot:


Download chromedriver.exe and add him to the PATH (on windows)
(link https://sites.google.com/a/chromium.org/chromedriver/downloads)

next just copy and paste :)
```
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle

users_href = ['https://www.instagram.com/pink.member', 'https://www.instagram.com/pockypack_']
driver = webdriver.Chrome(
            executable_path=f'chromedriver.exe') # here is a path for chromedriver.exe, in my case locates in main folder with py file.
delay = 3  # loading delay time

```

Later, i'm working now



