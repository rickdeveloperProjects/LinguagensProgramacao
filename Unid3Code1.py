from datetime import date 
atual = date.today().year

nascAno = int(input("Digite o ano do nascimento:  "))
nascMes = int(input("Digite o mes do nascimento:  "))
nascDia = int(input("Digite o dia do nascimento:  "))

idade = atual - nascAno

print ('essa pessoa tem {} anos de idade'.format(idade))
print ('Nasceu no dia {} do mes {} do ano {} '.format(nascDia,nascMes,nascAno))

