#for반복문
test_list = ['one', 'two', 'three', 3, 5]
for i in test_list:
    print(i)
for i, v in enumerate(test_list):
    print('인덱스' + str(i) + '값 :' + str(v))
for i in range(len(test_list)):
    print(i)
for i in range(5):
    print(i)

    # one
    # two
    # three
    # 3
    # 5

    # 인덱스0값: one
    # 인덱스1값: two
    # 인덱스2값: three
    # 인덱스3값: 3
    # 인덱스4값: 5

    # 0
    # 1
    # 2
    # 3
    # 4

    # 0
    # 1
    # 2
    # 3
    # 4
