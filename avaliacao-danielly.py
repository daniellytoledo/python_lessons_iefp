# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
print(":"*70)
titulo = "AVALIAÇÃO"
print(f"{titulo:-^70}")
print(":"*70)
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# .1
# Objetivo
# A - Remover duplicados
# B - Contar quantas vezes cada nome aparece

print("\n")
print("1. a) Removendo duplicado.")
print("b) Quantas vezes aparece na lista.")
print("\n")

nomes = ["Ana", "Bruno", "Ana", "Carlos", "Bruno", "Diana"]

nomes_sem_duplicados = []

for nome in nomes:
    if nome not in nomes_sem_duplicados:
        nomes_sem_duplicados.append(nome)
        print(f"{nome} aparece {nomes.count(nome)} vez(es) na lista original.")

print("\n")
print("A lista sem duplicados é: ", nomes_sem_duplicados)
print("\n")
print("-"*70)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# .2
# Objetivos
# A - Criar um set com todos os cursos existentes.
# B - Criar um dicionário que agrupe alunos por curso.


print("\n")
print("2. a) Set com todos os cursos existentes.")
print("b) Um dicionário que agrupe alunos por curso.")
print("\n")


alunos = [
    {"id": 1, "nome": "Ana", "curso": "Python"},
    {"id": 2, "nome": "Bruno", "curso": "Java"},
    {"id": 3, "nome": "Carlos", "curso": "Python"},
    {"id": 4, "nome": "Diana", "curso": "C++"},
]

cursos = set()
agrupados = {}

for aluno in alunos:
    cursos.add(aluno["curso"])
    curso = aluno["curso"]
    if curso not in agrupados:
        agrupados[curso] = []

    agrupados[curso].append({
        "nome": aluno["nome"],
        "id": aluno["id"]
    })

print("Os cursos existentes são: ", cursos)
print("\n")
print("Alunos por curso: ", agrupados)

print("\n")
print("-"*70)
print("\n")

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# 3
# Objetivos
# A - Descobrir quem tem permissão "editor".
# B - Criar um set com todas as permissões existentes no sistema.
# C - Verificar quem tem mais permissões.

print("\n")
print("3. a) descobrir quem tem permissão de editor.")
print("b) criar um set com todas as permissões existentes no sistema.")
print("c) verificar quem tem mais permissões.")
print("\n")

utilizadores = {
    "ana": {"admin", "editor"},
    "bruno": {"editor"},
    "carla": {"viewer"},
}



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# 4
# Objetivos
# A - Criar um set com todos os produtos vendidos.
# B - Criar um dicionário que mostre que produtos cada cliente comprou.
# C - Mostrar que cliente comprou mais produtos.

compras = [
    {"cliente": "Ana", "produto": "Livro"},
    {"cliente": "Bruno", "produto": "Caneta"},
    {"cliente": "Ana", "produto": "Caderno"},
    {"cliente": "Carlos", "produto": "Livro"},
]

