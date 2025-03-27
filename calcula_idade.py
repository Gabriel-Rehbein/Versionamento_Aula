from datetime import datetime

data_nasc = input("Digite sua data de nascimento (dd/mm/yyyy): ")
nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")

hoje = datetime.today()
idade = hoje.year - nascimento.year

if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
    idade -= 1

print(f"Você tem {idade} anos.")

if idade >= 18:
    print("Você pode tirar a CNH.")
