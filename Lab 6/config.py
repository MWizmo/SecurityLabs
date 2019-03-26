dictionary = ['cat', 'dog', 'and', 'the', 'man', 'people', 'one', 'two', 'three', 'four', 'beautiful', 'sky', 'Earth',
              'go', 'walk', 'walked', 'went', 'have', 'has', 'bird', 'birds', 'wonderful', 'tree', 'trees', 'by',
              'on', 'word', 'words', 'goes', 'day', 'morning', 'children', 'night', 'summer', 'spring', 'winter',
              'love', 'Harry', 'Potter', 'boy', 'who', 'lived', 'girl', 'boys', 'girls', 'pretty', 'funny', 'amazing',
              'magic', 'it', 'is', 'was', 'he', 'she', 'i', 'you', 'they', 'we', 'was', 'were', 'are', 'am', 'food',
              'hello', 'hi', 'everyone', 'every', 'everybody', 'nobody', 'never', 'where', 'what', 'which',
              'all', 'world']

alphabet_lower = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                  'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                  't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
alphabet_upper = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                  'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                  'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def get_key(dict, value):
    for k, v in dict.items():
        if v == value:
            return k
