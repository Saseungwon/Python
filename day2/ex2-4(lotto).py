# -*- coding: utf-8 -*-
import random
# 로또
hid = []
for i in range(6):
    hid.append(random.randint(1, 45))
print(hid)

# 로또 번호 6자리 생성(중복 안 됨)

lotto = set(hid)
print(lotto)