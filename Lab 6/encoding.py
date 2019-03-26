from config import *


def Caesar_encoder(message, shift):
    words = message.split(' ')
    for i in range(0, len(words)):
        new_word = ''
        for letter in words[i]:
            num = alphabet_lower.get(letter)
            if num is None:
                num = alphabet_upper.get(letter)
                shifted_num = (num + shift) % 26
                if shifted_num == 0:
                    shifted_num = 26
                new_word += get_key(alphabet_upper, shifted_num)
            else:
                shifted_num = (num + shift) % 26
                if shifted_num == 0:
                    shifted_num = 26
                new_word += get_key(alphabet_lower, shifted_num)
        words[i] = new_word
    return ' '.join(words)


def lengthen_key(key, message):
    j = 0
    for i in range(len(key), len(message)):
        key += key[j]
        j += 1
        if j == len(key):
            j = 0
    return key


def Vigener_encoder(message, key):
    coded_message = list()
    key = key.lower()
    words = message.split(' ')
    for word in words:
        if len(word) > len(key):
            key = lengthen_key(key, word)
        code = ''
        for i in range(0, len(word)):
            message_num = alphabet_lower.get(word[i])
            if message_num is None:
                message_num = alphabet_upper.get(word[i])
                key_num = alphabet_lower.get(key[i])
                coded_num = (message_num + key_num) % 26
                if coded_num == 0:
                    coded_num = 26
                code += get_key(alphabet_upper, coded_num)
            else:
                key_num = alphabet_lower.get(key[i])
                coded_num = (message_num + key_num) % 26
                if coded_num == 0:
                    coded_num = 26
                code += get_key(alphabet_lower, coded_num)
        coded_message.append(code)
    return ' '.join(coded_message)