nota1=float(input("ingrese la primera nota:"))
nota2=float(input("ingrese la segunda nota:"))
nota3=float(input("ingrese la tercera nota:"))
nota4=float(input("ingrese la cuarta nota:"))
suma =nota1+nota2+nota3+nota4
promedio=suma/4

print("el promedio es:",promedio)
if promedio == 7:
    print("usted a aprobado.")
else:
    print("usted a reprobado.")
