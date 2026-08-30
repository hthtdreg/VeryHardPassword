import random
spisok = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    password = []
    while True:
        lenpas = input("Введите длину желаемого пароля: ")
        try:
            lenpas = int(lenpas)
            break
        except:
            print("Введите число.")
    for i in range(lenpas):
        password.append(spisok[random.randint(0, len(spisok)-1)])
    print("".join(password))
