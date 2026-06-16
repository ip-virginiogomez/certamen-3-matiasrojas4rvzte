Edad = int(input("Ingrese su edad"))
Tarjeta = input("¿cuenta con tarjeta de socio? Si/No")
monto = int(input("Ingrese el total de su compra"))
Descuento = monto*1,15
True==Si
False==No
if Edad>=60 and Tarjeta==True :
        print(f"Descuento Aplicado, su total es de {Descuento}")
elif Edad>=60 and Tarjeta==False or Edad<=60 and Tarjeta==False :
        print(f"Descuento no aplicado por falta de tarjeta su total es de{monto}")
