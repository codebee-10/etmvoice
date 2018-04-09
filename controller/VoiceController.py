# -*- coding: utf-8 -*-
from tornado.web import asynchronous, RequestHandler
from config import config
import pyttsx3
from pyttsx3 import drivers
from pyttsx3.drivers import sapi5
import win32com
import binascii
import json

def play_voice(voice):
    print("------------------------------------------------------------")
    print("语音生成完成")
    print("语音播报中 ...")
    print(voice)
    print("------------------------------------------------------------")
    e = pyttsx3.init()
    e.say(voice)
    e.runAndWait()
    return


def unicode_hex(data: str):
    return str(binascii.hexlify(data.encode('utf-8')), 'ascii')


class VoiceHandler(RequestHandler):
    def get(self):
        voice = self.get_argument('voice', default='')
        v_token = self.get_argument('v_token', default='')
        try:
            if voice == '' or v_token =='':
                return self.write(json.dumps("{'error':10001,'message':'args can't be null'}"))
            elif v_token != config.V_TOKEN:
                return self.write(json.dumps("{'error':10002,'message':'token error !'}"))
            else:
                print(voice)
                play_voice(voice)
        except Exception :
            play_voice(voice)

        return self.write(json.dumps("{'status':200,'message':'request success'}"))

    def post(self):
        voice = self.get_argument('voice', default='')
        v_token = self.get_argument('v_token', default='')
        if voice == '' or v_token == '':
            return self.write(json.dumps("{'error':10001,'message':'args can't be null'}"))
        elif v_token != config.V_TOKEN:
            return self.write(json.dumps("{'error':10002,'message':'token error !'}"))
        else:
            vo = binascii.a2b_hex(voice)
            voice_str = vo.decode('utf-8')
            try:
                print(voice_str)
                play_voice(voice_str)
            except Exception:
                play_voice(voice_str)

        return self.write(json.dumps("{'status':200,'message':'request success'}"))
