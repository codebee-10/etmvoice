#!/usr/bin/env python
# encoding: utf-8

V_TOKEN = "e4b89ce696b9e8b4a2e5af8ce8afade99fb3e8bdace68da2636c69656e74"

APPID = '11131820'
APIKEY = 'w6BGPRq4HqGxIMLNYG3M3iOH'
SECRETKEY = 'Z7EHpSGFWFRnwm8bC6820sTUGrFNsPBg'

GETTOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+APIKEY+'&client_secret='+SECRETKEY

VOICTTOAUDIO_URL = 'http://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=11131820&tok='
