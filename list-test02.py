# 로또번호 생성 - 난수
mylotto = []

import random
r = random.randint(1,45)
if r not in mylotto:
    mylotto.append( r )
r = random.randint(1,45)
if r not in mylotto:
    mylotto.append( r )
r = random.randint(1,45)
if r not in mylotto:
    mylotto.append( r )
r = random.randint(1,45)
if r not in mylotto:
    mylotto.append( r )
r = random.randint(1,45)
if r not in mylotto:
    mylotto.append( r )
r = random.randint(1,45)
if r not in mylotto:
    mylotto.append( r )
print(mylotto)
# 중복되면 안 나옴 (숫자가 6개가 안 나오는 경우가 생김)