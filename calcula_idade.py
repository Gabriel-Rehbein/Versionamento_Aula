from datetime import datetime

data_nasc = input("Digite sua data de nsciemnto (dd/mm/yyyy):")
nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")

hoje = datetime.today()
idade = hoje.year - nascimento.year
idade = idade.year -nascimento.year
print(f"Você tem {idade} anos.")