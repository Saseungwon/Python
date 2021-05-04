def fn_sum_mul(choice, *args):
    if choice == 'sum':
        result =0
        for i in args:
            result +=i
    elif choice == 'mul':
        result = 1
        for i in args:
            result += i
    return result

print(fn_sum_mul('sum', 1, 2, 3))
print(fn_sum_mul('sum', 1, 2, 3))
print(fn_sum_mul('sum', 1, 2, 3))