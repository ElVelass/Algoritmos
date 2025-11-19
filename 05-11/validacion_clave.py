cont = 0
while cont < 3:
    contra = input("Ingrese su contraseña ")
    contrasi = "contraseña"
    if contra == contrasi:
        print("Correcto")
        break
    else:
        print("Incorrecto")
    cont += 1 
if cont == 3:
    print("Bloqueado")