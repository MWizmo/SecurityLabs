# coding: utf-8
from xmlrpc.server import SimpleXMLRPCServer
import math


def identification_RSA(key):
    global opened_key
    opened_key = key


def send_signed_RSA_message(message, s):
    h = 12
    h2 = math.pow(s, opened_key[0]) % opened_key[1]
    print("h' = ", h2)
    if h == h2:
        print('Message from A: ', message)
        return True
    else:
        return False


def identification_GOST_94(key):
    global opened_key
    opened_key = key


def send_signed_GOST_94_message(message, w, s):
    print('w = ', w)
    h = 21
    v = math.pow(h, opened_key[1] - 2) % opened_key[1]
    z1 = (s * v) % opened_key[1]
    z2 = ((opened_key[1] - w) * v) % opened_key[1]
    u = ((math.pow(opened_key[2], z1) * math.pow(opened_key[3], z2)) % opened_key[0]) % opened_key[1]
    print('u = ', u)
    if u == w:
        print('Message from A: ', message)
        return True
    else:
        return False

def identification_GOST_01(key):
    global opened_key
    opened_key = key


def send_signed_GOST_01_message(message, r, s):
    h = 7
    e = h % opened_key[4]
    e2 = 27
    v = e2 % opened_key[4]
    z1 = (s * v) % opened_key[4]
    z2 = ((opened_key[4] - r) * v) % opened_key[4]
    xc = 16
    yc = 16
    r2 = xc % opened_key[4]
    if r2 == r:
        print('Message from A: ', message)
        return True
    else:
        return False


server = SimpleXMLRPCServer(("localhost", 8005), allow_none=True)
print("Listening on port 8005")
server.register_function(identification_RSA, 'identification_RSA')
server.register_function(send_signed_RSA_message, 'send_signed_RSA_message')
server.register_function(identification_GOST_94, 'identification_GOST_94')
server.register_function(send_signed_GOST_94_message, 'send_signed_GOST_94_message')
server.register_function(identification_GOST_01, 'identification_GOST_01')
server.register_function(send_signed_GOST_01_message, 'send_signed_GOST_01_message')

try:
    server.serve_forever()
except KeyboardInterrupt:
    exit(0)
