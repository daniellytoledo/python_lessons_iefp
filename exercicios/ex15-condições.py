print("\n")
print(":"*50)
titulo = "CONDIÇÕES"
print(f"{titulo:-^50}")
print(":"*50)
print("\n")

# criar uma condição com any() para verificar se existe algum produto sem stock. escreve apenas a linha do if

produtos = [
    {"nome": "Teclado", "stock": 5},
    {"nome": "Rato", "stock": 0},
    {"nome": "Monitor", "stock": 3}
]

if any(p['stock'] <=0 for p in produtos):
    print("WARNING: Há produtos sem estoque.")

print("\n")
print(":"*49)
print("\n")

# usa any() para verificar se existe algum utilizador sem email preenchido.
# usa all() para verificar se todos os utilizadores tem email preenchido

utilizadores = [
    {"nome": "Pedro", "email": "pedro@email.com"},
    {"nome": "Rui", "email": ""},
    {"nome": "Ana", "email": "ana@email.com"}
]

if any(u['email'] == "" for u in utilizadores):
    print("Existe um utilizador sem preencher email.")

print("-"*49)

if all(u['email'] != "" for u in utilizadores):
    print("Todos os utilizador possuem email preenchido.")
else:
    print("Existem emails vazios.")

print("\n")
print(":"*49)
print("\n")

# usar any() para verificar se existe alguma encomenda paga mas ainda não foi enviada

encomendas = [
    {"cliente": "Pedro", "pago": True, "enviado": True},
    {"cliente": "Rui", "pago": True, "enviado": False},
    {"cliente": "Ana", "pago": False, "enviado": False}
]

if any(e['pago'] == True and e['enviado'] == False for e in encomendas):
    print("Existe encomendas pagas, mas que ainda não foram enviadas.")

# otimizado

if any(e['pago'] and not e['enviado'] for e in encomendas):
    print("Existe encomendas pagas, mas que ainda não foram enviadas.")

print("-" * 49)

if (not e['pago'] for e in encomendas):
    print("Existem encomendas não pagas.")

print("\n")
print(":"*49)
print("\n")

# usa any() para verficar se existe alguma turma onde haja pelo menos um aluno ocm nota negativa (<10).
# usar any() dentro de any()

turmas = [
    {"nome": "A", "notas": [12, 14, 9]},
    {"nome": "B", "notas": [15, 16, 17]},
    {"nome": "C", "notas": [8, 11, 10]}
]

if any(any(nota<10 for nota in turma['notas']) for turma in turmas):
    print("Existem alunos com notas menores que 10 valores.")

print("\n")
print(":"*49)
print("\n")

# Usa any() para verificar se existe alguma turma onde haja pelo menos um aluno com nota negativa (<10). Usar any() dentro de any().
# Usa all() para verificar se existe alguma turma com todas as notas positivas. Usar all() dentro de any()
# # Usa all() para verificar se todas as turmas têm todas as notas positivas. Usar all() dentro de all()

if any(any(nota < 10 for nota in t['notas']) for t in turmas):
    print("Existe pelo menos uma negativa")

print("-" * 49)

if(any(all(nota>=10 for nota in t['notas']) for t in turmas)):
    print("Existe pelo menos uma turma com todas as notas positivas")

print("-" * 49)

if(all(all(nota>=10 for nota in t['notas']) for t in turmas)):
    print("Todas as turmas têm as notas todas positivas")