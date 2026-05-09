# 02. Fintech: Um banco digital quer premiar clientes. Receba três depósitos: d1 =
# 0.1, d2 = 0.1 e d3 = 0.1.
# ● Cálculo: Faça a soma total. Se a soma for exatamente 0.3, exiba "Bônus
# Ativado".
# ● Se não for, exiba "Erro de cálculo, ".
# ● OBS: No final, seu algoritmo deve testar (e provar) se a soma dá
# exatamente 0.3 dentro do print. Deve sair algo como: “Soma correta: True”

from decimal import Decimal

deposito_1 = Decimal("0.1")
deposito_2 = Decimal("0.1")
deposito_3 = Decimal("0.1")

Soma_total = {deposito_1 + deposito_2 + deposito_3}

if "Soma_total" == "0.3":
    print("Bônus ativado")
    
    
#falta o print do resultado
    