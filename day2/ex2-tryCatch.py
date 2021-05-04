# 예외처리
def calc(values):
    sum = None
    try:
        sum = values[0] + values[1] + values[2]

    except IndexError as err:
        print(str(err))
    except Exception as e:
        print(str(e))
    else:
        print('에러없음')
    finally:
        print('sum')
calc([1, 2, 3, 4])
calc([1, 2])