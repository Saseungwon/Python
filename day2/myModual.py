# -*- coding: utf-8 -*-
import random

def fn_lotto_user():
    userSet = set()
        while True:
            userSet.add(random.randint(1, 45))
            if len(userSet) == 6:
                break

        return userSet

if __name__ == '__main__':
    print('직접 실행')
else:
    print('다른곳에서 실행')