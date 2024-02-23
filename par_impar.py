# programar para verificar si el numero es par o impar
# input
x=int (input("digite un numero: "))

# prosesing
r=x%2
if r == 0:
    rta = "par"
else:
    rta ="impar"      
# auput
print("el numero",x,"es",rta)