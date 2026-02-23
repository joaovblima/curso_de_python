peso = float(input("seu peso: "))
altura = float(input("sua altura: "))
imc = peso / (altura * altura)

print(f"seu imc é de {imc:.2f}")

if imc < 18.5:
    print("abaixo do peso")
elif imc > 25.0 and imc <=29.9:
    print("levemente acima do peso")
elif imc > 30.0 and imc <= 34.9:
    print("obesidade grau I")
elif imc > 35.0 and imc < 39.9:
    print("obesidade grau II")
elif imc >= 40:
    print("alerta vermelho, obesidade morbida")
