print('Hello, Python world')

def get_min(num1, num2):
    min = num2
    if num1 < num2:
        min = num1
    return min

def get_gcd(num1, num2):
    min = get_min(num1, num2)
    gcd = 1
    for i in range(2, min+1):
        if (num1%i == 0):
            if(num2%i == 0):
                gcd = i
    return gcd

num_str = input("正の整数を入力してください：")
num1 = int(num_str)
num_str = input("正の整数を入力してください：")
num2 = int(num_str)
gcd = get_gcd(num1, num2)

print(gcd)