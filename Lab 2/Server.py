# coding: utf-8
from xmlrpc.server import SimpleXMLRPCServer
import math


def identification_RSA(key):
    global opened_key
    opened_key = key


def authentication_RSA(step, key):
    if step == 1:
        k = 12      # К
        r = math.pow(k, opened_key[0]) % opened_key[1]
        print('r = ', r)
        return r
    else:
        print("k' = ", key)
        if key == 12:
            return True
        else:
            return False


def identification_Shnorr(key):
    global opened_key
    opened_key = key


def authentication_Shnorr(step, key):
    if step == 1:
        print('r = ',key)
        global r
        r = key
        return 10
    else:
        print('s = ', key)
        print('r = ', r)
        print('key is ', opened_key)
        t = (math.pow(opened_key[0], key) * math.pow(opened_key[1], 10)) % opened_key[2]
        print('t = ', t)
        if t == r:
            return True
        else:
            return False


def identification_FFS(key):
    global opened_key
    opened_key = key


def authentication_FFS(step, key):
    if step == 1:
        global z
        z = key
        print('z = ', z)
        import random
        global b
        b = random.randint(0, 1)
        print('b = ', b)
        return b
    else:
        if b == 0:
            x = (key * key) % opened_key[1]
            print('x = ', x)
            return z == x
        else:
            x = (key * key * opened_key[0]) % opened_key[1]
            print('x = ', x)
            return z == x


server = SimpleXMLRPCServer(("localhost", 8005), allow_none=True)
print("Listening on port 8005")
server.register_function(identification_RSA, 'identification_RSA')
server.register_function(authentication_RSA, 'authentication_RSA')
server.register_function(identification_Shnorr, 'identification_Shnorr')
server.register_function(authentication_Shnorr, 'authentication_Shnorr')
server.register_function(identification_FFS, 'identification_FFS')
server.register_function(authentication_FFS, 'authentication_FFS')
try:
    server.serve_forever()
except KeyboardInterrupt:
    exit(0)
