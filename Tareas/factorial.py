num  = int(input("Digite su numero "))
fact = 1
while num >= 1:
    fact = num * fact 
    num -= 1
print("El factorial: ", fact)