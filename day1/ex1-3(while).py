#조건문 while
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print('나무를 %d 번 찍었습니다.' %treeHit)
    print('나무를 ' + treeHit + '번 찍었습니다.')
    if treeHit == 10:
        print('나무가 넘어갑니다')
