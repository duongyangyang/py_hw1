def positive_integer_check(a, b):
    if a >= 0 and b >=0:
        if a == int(a) and b == int(b):
            return True
    else:
        return False
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


if __name__ == '__main__':
    try:
        a = float(input('输入整数 a: '))
        b = float(input('输入整数 b: '))
        if positive_integer_check(a,b):
            print(f'a 与 b 的阶乘之和为: {factorial(int(a)) + factorial(int(b))} ')
        else:
            print('输入无效')

    except ValueError:
        print('输入无效')


    