
#exemp_08: Cashback do E-commerce (Sobrecarga de Operadores)
#Cenário: Uma loja quer gerar uma barra de progresso visual para o cashback do cliente.
#Objetivo: O cliente ganhou 10 pontos. Cada ponto vale um caractere █.

#Desafio: Crie a barra de progresso usando "multiplicação de strings" e concatene com a porcentagem final.

#Saída esperada: Progressão: [██████████] 100% (Use o + para colar os textos).

pontos = 10

ponto_progresso = "█"

porcentagem = "100%"

barra_visual = pontos*ponto_progresso + porcentagem

print ([barra_visual])