import random
import string

CHAR_DICT={
    'a':['A','a','4'],
    'b':['B','b','8'],
    'c':['C','c'],
    'd':['D','d'],
    'e':['E','e','3'],
    'f':['F','f'],
    'g':['G','g','6','9'],
    'h':['H','h'],
    'i':['I','i','1'],
    'j':['J','j'],
    'k':['K','k'],
    'l':['L','l'],
    'm':['M','m'],
    'n':['N','n'],
    'o':['O','o','0'],
    'p':['P','p'],
    'q':['Q','q'],
    'r':['R','r','12'],
    's':['S','s','5'],
    't':['T','t','7'],
    'u':['U','u'],
    'v':['V','v'],
    'w':['W','w'],
    'x':['X','x'],
    'y':['Y','y'],
    'z':['Z','z'],
    }
class Generator(object):
    def __init__(self, fmt, append=True):
        self.fmt=fmt
        self.append=append
    def append_random_char(self, mode, length):
        if mode =="HEX":
            return "".join([random.choice(string.ascii_lowercase[:6]+string.digits) for _ in range(length)])
    def generate(self,text,mode="HEX",length=8):
        flag=[]
        final_flag=""
        for word in str(text).lower().split():
            w=""
            for char in word:
                if char in CHAR_DICT.keys():
                    w+=str(random.choice(CHAR_DICT[char]))
                else:
                    w+=char
            flag.append(w)
        flag.append(self.append_random_char(mode,length)) if self.append==True else flag
        final_flag="_".join(flag)

        return self.fmt+'{'+final_flag+'}'
    def flags_generate(self, filepath, len_append=8):
        flags = open(filepath, 'r').readlines()
        return [self.generate(flag, length=len_append) for flag in flags]