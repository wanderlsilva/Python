print("=== Diagnóstico de Gripe Comum ===")

febre = input("Possui febre moderada? (sim/nao): ")
nariz = input("Possui nariz entupido ou escorrendo? (sim/nao): ")
garganta = input("Possui dor de garganta? (sim/nao): ")
tosse = input("Possui tosse? (sim/nao): ")

dias = int(input("Há quantos dias os sintomas começaram? "))

if febre == "sim" and nariz == "sim" and garganta == "sim" and tosse == "sim" and dias < 7:
    print("Diagnóstico: Provável Gripe Comum")

elif dias >= 7:
    print("Diagnóstico: Sintomas atípicos, investigar outras condições")

else:
    print("Diagnóstico: Sintomas atípicos, investigar outras condições")