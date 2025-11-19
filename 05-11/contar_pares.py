par = 0
impar = 0
while True:
    num = int(input("Digite el numero "))
    if num == 0:
        break
    elif num % 2 == 0:
        print("Es par")
        par += 1
    elif num % 2 == 1:
        print("Es impar")
        impar += 1
print(f"Impar: {impar}")
print(f"Par: {par}")