import random
def rand():
    return random.randint(0,2)

def janken():
    print("[ 0 = gu, 1 = tyoki, 2 = pa ]")
    num_str = input("出す手を入力してください：")
    num = int(num_str)
    rand_int = rand()

    if rand_int == num:
       print("dlow")

    elif rand_int == 0 and num == 2:
      print("you win")
    elif rand_int == 1 and num == 0:
      print("you win")
    elif rand_int == 2 and num == 1:
      print("you win")

    else:
      print("you lose")




for i in range(3):
    data = [rand() for i in range(2)]
    print(data)    
    janken()