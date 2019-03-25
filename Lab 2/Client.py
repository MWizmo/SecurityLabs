# coding: utf-8
import xmlrpc.client
import math


class User:
    def __init__(self):
        self.opened_key_RSA = [5, 21]  # (e,n)
        self.closed_key_RSA = 5
        self.opened_key_Shnorr = [12, 18, 23]  # (g,y,p)
        self.closed_key_Shnorr = 6
        self.opened_key_FFS = [11, 35]  # (v,n)
        self.closed_key_FFS = 4
        self.proxy = xmlrpc.client.ServerProxy("http://localhost:8005/")

    def identification_RSA(self):
        self.proxy.identification_RSA(self.opened_key_RSA)

    def authentication_RSA(self):
        r = self.proxy.authentication_RSA(1, 0)
        k = math.pow(int(r), self.closed_key_RSA) % self.opened_key_RSA[1]
        verdict = self.proxy.authentication_RSA(2, k)
        print(verdict)

    def identification_Shnorr(self):
        self.proxy.identification_Shnorr(self.opened_key_Shnorr)

    def authentication_Shnorr(self):
        k = 21    # У
        r = math.pow(self.opened_key_Shnorr[0], k) % self.opened_key_Shnorr[2]
        e = self.proxy.authentication_Shnorr(1, r)
        s = (k + self.closed_key_Shnorr * e) % 11   # q=11
        verdict = self.proxy.authentication_Shnorr(2, s)
        print(verdict)

    def identification_FFS(self):
        self.proxy.identification_FFS(self.opened_key_FFS)

    def authentication_FFS(self):
        r = 9   # З
        z = (r * r) % self.opened_key_FFS[1]
        b = self.proxy.authentication_FFS(1, z)
        if b == 0:
            verdict = self.proxy.authentication_FFS(2, r)
            print(verdict)
        else:
            y = (r * self.closed_key_FFS) % self.opened_key_FFS[1]
            verdict = self.proxy.authentication_FFS(2, y)
            print(verdict)


user = User()
while True:
    inp = int(input())
    if inp == 1:
        user.identification_RSA()
        user.authentication_RSA()
    elif inp == 2:
        user.identification_Shnorr()
        user.authentication_Shnorr()
    elif inp == 3:
        user.identification_FFS()
        user.authentication_FFS()
