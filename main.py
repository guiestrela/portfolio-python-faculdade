print("***********************************")
print("***********Calculo IMC*************")
print("***********************************")

altura = float(input("Qual a sua altura? "))
peso = float(input("Qual o seu peso? "))

print("Será feito o calculo agora...")

imc = (peso / (altura * altura))

print(f"Seu IMC é {imc:.2f}")

if imc < 16:
    print("Magreza Grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
elif imc > 40:
    print("Obesidade Grau III (mórbida)")