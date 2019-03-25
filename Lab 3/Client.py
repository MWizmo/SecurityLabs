# coding: utf-8
import xmlrpc.client
import math


class User:
    def __init__(self):
        self.message = 'Hello'
        self.opened_key_RSA = [5, 21]  # (e,n)
        self.closed_key_RSA = 5
        self.opened_key_GOST_94 = [79, 3, 1, 1]  # (p,q,a,y)
        self.closed_key_GOST_94 = 2
        self.opened_key_GOST_01 = [3, 7, 7, 17, 47, 36, 20]  # (A,B,xp,yp,q,xq,yq)
        self.closed_key_GOST_01 = 10
        self.proxy = xmlrpc.client.ServerProxy("http://localhost:8005/")

    def identification_RSA(self):
        self.proxy.identification_RSA(self.opened_key_RSA)

    def sign_message_RSA(self):
        h = 12  # K
        s = math.pow(h, self.closed_key_RSA) % self.opened_key_RSA[1]
        if self.proxy.send_signed_RSA_message(self.message, s):
            print('Message delivered')
        else:
            print('No')

    def identification_GOST_94(self):
        self.proxy.identification_GOST_94(self.opened_key_GOST_94)

    def sign_message_GOST_94(self):
        h = 21  # У
        k = 2
        w = math.pow(self.opened_key_GOST_94[2], k) % self.opened_key_GOST_94[0]
        w2 = w % self.opened_key_GOST_94[1]
        s = (w2 * self.closed_key_GOST_94 + k * h) % self.opened_key_GOST_94[1]
        if self.proxy.send_signed_GOST_94_message(self.message, w2, s):
            print('Message delivered')
        else:
            print('No')

    def identification_GOST_01(self):
        self.proxy.identification_GOST_01(self.opened_key_GOST_01)

    def sign_message_GOST_01(self):
        h = 7  # З
        e = h % self.opened_key_GOST_01[4]
        k = 11
        xc = 16
        yc = 16
        r = xc % self.opened_key_GOST_01[4]
        s = (r * self.closed_key_GOST_01 + k * e) % self.opened_key_GOST_01[4]
        if self.proxy.send_signed_GOST_01_message(self.message, r, s):
            print('Message delivered')
        else:
            print('No')


user = User()
while True:
    inp = int(input())
    if inp == 1:
        user.identification_RSA()
        user.sign_message_RSA()
    elif inp == 2:
        user.identification_GOST_94()
        user.sign_message_GOST_94()
    elif inp == 3:
        user.identification_GOST_01()
        user.sign_message_GOST_01()
