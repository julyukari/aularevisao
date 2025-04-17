repetir="s"
while repetir == "s":
   peso=float(input("informe seu peso: "))
   altura=float(input("informe sua altura: "))
   imc= peso/(altura*altura)
   if imc < 18.5:
    print("abaixo do peso")
   elif imc >= 18.6 and imc <=24.9:
    print("peso ideal (PARABÉNS)")
   elif imc >= 25.0 and imc <=29.9:
    print("levemente a cima do peso")
   elif imc >=30.0 and imc <=34.9:
    print("obesidade grau I")
   elif imc >=35.0 and imc <=39.9:
    print("obesidade grau II (SEVERA)")
   else:
    print("obesidade grau III (MÓRBIDA)")
   repetir = input("deseja verificar um novo imc ?")



