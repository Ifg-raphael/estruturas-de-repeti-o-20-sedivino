'''
## Lista 04 - Exercício 20

Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada a massa inicial,
em gramas, fazer um algoritmo que determine o tempo necessário para que essa massa se torne menor do que
0,5 grama. Escreva a massa inicial a massa final e o tempo calculado em horas, minutos e segundos.

O programa deve assumir que a entrada e saída seja exatamente no formato dado nos exemplos a seguir.
**Não adicione outras mensagens ou mude a capitalização das letras pois se fizer isso o teste não passará!**

---

**Exemplo 01:**

Entrada:
```
1
```
Saída:
```
0h 1m 40s
```

---

**Exemplo 02:**

Entrada:
```
10
```
Saída:
```
0h 4m 10s
```

---

**Exemplo 03:**

Entrada:
```
0.6
```
Saída:
```
0h 0m 50s
```

'''
# Inicialização de variáveis
massa_final = 0.5
tempo_segundos = 0

# Entrada de dados
massa_inicial = float(input())

massa_atual = massa_inicial

# Cálculo do tempo necessário em segundos:
while massa_atual >= massa_final:
    massa_atual /= 2
    tempo_segundos += 50

# Conversão do tempo em horas, minutos e segundos
horas = tempo_segundos // 3600
minutos = (tempo_segundos % 3600) // 60
segundos = tempo_segundos % 60

# Saída de dados
print(f"{horas}h {minutos}m {segundos}s")
