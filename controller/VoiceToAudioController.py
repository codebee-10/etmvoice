# -*- coding: utf-8 -*-
from tornado.web import asynchronous, RequestHandler
from config import config
import requests
import binascii
import json
import re

global b_token


def get_token():
    token = requests.get(config.GETTOKEN_URL)
    r_data = json.loads(str(token.text))
    global b_token
    b_token = r_data['access_token']


def voice_to_audio(voice):
    print("------------------------------------------------------------")
    print("语音播报中 ...")
    print(voice)
    print("------------------------------------------------------------")
    global b_token
    try:
        print(b_token)
    except:
        get_token()


def countWords(s):
    n = 0
    for c in s:
        if ord(c) > 127:
            n += 1
    n2 = len(s)
    return n, n2


def unicode_hex(data: str):
    return str(binascii.hexlify(data.encode('utf-8')), 'ascii')


class VoiceToAudioHandler(RequestHandler):
    def get(self):
        voice = self.get_argument('voice', default='')
        v_token = self.get_argument('v_token', default='')
        try:
            if voice == '' or v_token =='':
                return self.write(json.dumps("{'error':10001,'message':'args can't be null'}"))
            elif v_token != config.V_TOKEN:
                return self.write(json.dumps("{'error':10002,'message':'token error !'}"))
            else:
                voice_to_audio(voice)
                r_data = requests.get(config.VOICTTOAUDIO_URL + b_token + '&vol=9&per=0&spd=5&pit=5&tex=haody,Roan')
                try:
                    json.loads(r_data.text)
                    print("token 失效, 重新获取 ... ")
                    voice_to_audio(voice)
                except:
                    print("token 有效, 语言合成中  ... ")

                #print("汉字数量：")
                ch_num, all_num = countWords(voice)
                #print(ch_num, all_num)
                voices = list()
                list_v = list(voice)
                si = 0
                if ch_num > 600 and all_num > 800:
                    si = all_num / 800
                    di = 0
                    while di < int(si+1):
                        voices.append(list_v[di*800:(di+1)*800])
                        di += 1

                # 输出 h5 audio
                data_html = ""
                vv = 1
                if int(si) == 0:
                    data_html = '<div style="display:black;margin-bottom:30px;">' \
                                 '<div style="padding:20px;border:1px solid #ccc;font-size:22px;color:#fff;background:#4684C3;' \
                                 'border-radius:5px;">' \
                                 '语言播报 ' + str(vv) + '</div>' \
                                 '<div style="position:relative;top:-30px;"><video controls=""  autoplay="" name="media" style="height:100px"><source src="' + config.VOICTTOAUDIO_URL \
                                 + b_token + '&vol=9&per=0&spd=5&pit=5&tex=' + voice + '" type="audio/mp3"></video></div>' \
                                 '<div style="padding:18px;border:1px solid #ccc;font-size:20px;color:#fff;background:#21B384;' \
                                 'border-radius:5px;line-height:40px">' + voice + '</div></div>'
                else:
                    for v in voices:
                        vo = "".join(v)
                        data_html += '<div style="display:black;margin-bottom:30px;">' \
                                '<div style="padding:20px;border:1px solid #ccc;font-size:22px;color:#fff;background:#4684C3;' \
                                'border-radius:5px;">' \
                                '语言播报 '+str(vv)+'</div>' \
                                '<div style="position:relative;top:-30px;"><video controls=""  name="media" style="height:100px"><source src="' + config.VOICTTOAUDIO_URL \
                                 + b_token + '&vol=9&per=0&spd=5&pit=5&tex=' + vo + '" type="audio/mp3"></video></div>' \
                                '<div style="padding:18px;border:1px solid #ccc;font-size:20px;color:#fff;background:#21B384;' \
                                'border-radius:5px;line-height:40px">'+vo+'</div></div>'
                        vv += 1

                return self.write(data_html)
        except Exception :
            voice_to_audio(voice)

        return self.write(json.dumps("{'status':500,'message':'request failed'}"))

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
                voice_to_audio(voice_str)
            except Exception:
                voice_to_audio(voice_str)

        return self.write(json.dumps("{'status':200,'message':'request success'}"))
