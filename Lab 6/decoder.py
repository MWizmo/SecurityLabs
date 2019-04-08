import socket
from encoding import *


def Caesar_decoder(message, start_position):
    words = message.split(' ')
    decoded_message = list()
    shift = 0
    for i in range(0, len(words)):
        if shift == 0:
            for j in range(start_position, 27):
                decoded_word = (Caesar_encoder(words[i], j))
                if decoded_word in dictionary:
                    shift = j
                    break
        else:
            break
    for i in range(0, len(words)):
        decoded_word = (Caesar_encoder(words[i], shift))
        decoded_message.append(decoded_word)
    flag = True
    for word in decoded_message:
        if not(word in dictionary):
            flag = False
    if flag or shift == 0 or shift == 26:
        return decoded_message, 26 - shift
    else:
        return Caesar_decoder(message, shift + 1)


def Vigener_decoder(code, start_position):
    words = code.split(' ')
    used_key = ''
    for word in words:
        for j in range(start_position, len(dictionary)):
            key = dictionary[j].lower()
            if len(word) > len(key):
                key = lengthen_key(key, word)
            decoded_word = ''
            for i in range(0, len(word)):
                code_num = alphabet_lower.get(word[i])
                if code_num is None:
                    code_num = alphabet_upper.get(word[i])
                    if code_num is None:
                        decoded_word += word[i]
                        continue
                    key_num = alphabet_lower.get(key[i])
                    message_num = (code_num - key_num + 26) % 26
                    if message_num == 0:
                        message_num = 26
                    decoded_word += get_key(alphabet_upper, message_num)
                else:
                    key_num = alphabet_lower.get(key[i])
                    message_num = (code_num - key_num + 26) % 26
                    if message_num == 0:
                        message_num = 26
                    decoded_word += get_key(alphabet_lower, message_num)
            if decoded_word in dictionary:
                used_key = dictionary[j]
                break
        if used_key != '':
            break
    message = list()
    for word in words:
        key = used_key.lower()
        if len(word) > len(key):
            key = lengthen_key(key, code)
        decoded_word = ''
        for i in range(0, len(word)):
            code_num = alphabet_lower.get(word[i])
            if code_num is None:
                code_num = alphabet_upper.get(word[i])
                if code_num is None:
                    decoded_word += word[i]
                    continue
                key_num = alphabet_lower.get(key[i])
                message_num = (code_num - key_num + 26) % 26
                if message_num == 0:
                    message_num = 26
                decoded_word += get_key(alphabet_upper, message_num)
            else:
                key_num = alphabet_lower.get(key[i])
                message_num = (code_num - key_num + 26) % 26
                if message_num == 0:
                    message_num = 26
                decoded_word += get_key(alphabet_lower, message_num)
        message.append(decoded_word)
    flag = True
    for word in message:
        if not(word in dictionary):
            flag = False
    if flag:
        return ' '.join(message), used_key
    else:
        return Vigener_decoder(code, get_key(dictionary, used_key) + 1)


sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()
while True:
    code = conn.recv(1024).decode('utf-8')
    if not code:
        continue
    print('Зашифрованное выражение:', code)
    try:
        message, shift = Caesar_decoder(code, 1)
        if shift == 0 or shift == 26:
            message, key = Vigener_decoder(code, 0)
            print('При шифровании использовался шифр Видженера.\nРасшифрованное сообщение: ' + message +
                  '\nКлюч при шифровании: ' + key)
        else:
            print('При шифровании использовался шифр Цезаря.\nРасшифрованное сообщение: ' + ' '.join(message) +
                  '\nСдвиг при шифровании: ' + str(shift))
        print()
    except:
        print('Встречено слово не из словаря, расшифровка невозможна')
