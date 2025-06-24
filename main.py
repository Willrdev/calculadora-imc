peso = float(input('Qual o seu peso? '))
altura = float(input('Qual o sua altura? '))

imc = peso / (altura * altura) 

if imc < 18.5:
    print ('Você está abaixo do peso')
elif imc < 25:
    print ('Você está com peso normal')
elif imc < 30:
    print ('Você está com sobrepeso')
else:
    print('Você está com obesidade')