#Unidade3Code3

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num1 < num2 and num1 < num3:
    print ('O menor numero e: {}'.format(num1))

elif num2 < num1 and num2 < num3:
    print ('O menor numero e: {}'.format(num2))

else:
    print ('O menor numero e: {}'.format((num3)))


