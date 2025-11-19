cant = int(input("Ingrese la cantidad de numeros "))
num = 1
for num in range(1, cant+1):
    print(num, " ",
          num * num, " ",
          num + num * num )