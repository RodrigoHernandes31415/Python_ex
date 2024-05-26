import random

x = int(input("Numero: "))
y = random.randint(1, 50)

while True:
    if x == y:
        print('Parabens!')
    elif x < y:
        print('Tente um numero maior')
    else:
        print('Tente um numero menor')
    
    x = int(input("Tente de novo: "))

    if x == 0:
        print("Você saiu do jogo")
        break