import encoding
import random
import config
import socket


def get_code(inp, type):
    if type == 0:
        shift = random.randint(1, 25)
        return encoding.Caesar_encoder(inp, shift)
    else:
        index = random.randint(0, len(config.dictionary) - 1)
        return encoding.Vigener_encoder(inp, config.dictionary[index])


sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    print('Введите выражение')
    inp = input()
    code = get_code(inp, random.randint(0, 1))
    sock.send(code.encode('utf-8'))
