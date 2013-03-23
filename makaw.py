#!/usr/bin/env python
import sys
import os
import tweepy

consumerKey = 'myaYupXCSINvlAuwScIa3w'
consumerSecret = '97idfD3sWNbpowOVs3ZiHp83bFT5vZbdHNxItMUu4'

accessToken = '163395512-MLcrxHBjYwBK3oYBa4SDFYLIabJyEWkB1LZMCRy2'
accessSecret = 'y5ZLf5cqAldsKSeDR037KnC0MQ8MpoifDce83X3oHI'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth)

os.system("touch hello.md")
#api.update_status(sys.argv[1])
