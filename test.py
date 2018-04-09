import binascii
import json

def unicode_hex(data: str):
    return str(binascii.hexlify(data.encode('utf-8')), 'ascii')

def hex():
    v1 = unicode_hex('你好东方财富')
    print(v1)
    v2 = binascii.a2b_hex(v1)
    print(v2.decode('utf-8'))
    return json.dumps("{'error':10001,'message':'入参不能为空'}")

if __name__ == "__main__":
    print(hex())