def calcular_imc():

    nome = input('Qual o seu nome? ')
    peso = float(input('Qual o seu peso? '))
    altura = float(input('Qual a sua altura? '))

    imc = peso / (altura * altura) 

    print(f'\n{nome}, seu IMC é: {imc:.2f}')

    if imc < 18.5:
        print ('Você está abaixo do peso')
    elif imc < 25:
        print ('Você está com peso normal')
    elif imc < 30:
        print ('Você está com sobrepeso')
    else:
        print('Você está com obesidade')



# Chama a função para executar
calcular_imc()