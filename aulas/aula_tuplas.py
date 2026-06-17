"""
alunos = ("Alice", "Bernardo", "Carolina","Daniel", "Eduardo", "Fernanda", "Gustavo", "Heloisa", "Isabela", "João", "Karla", "Leonardo", "Mariana", "Nicolas", "Olívia", "Pedro", "Quintino", "Rafaela", "Samuel", "Tatiana", "Ulisses", "Vanessa", "William", "Xavier", "Yara", "Zoe")

Um tuplo é:
. Ordenado
. Imutável (não pode ser alterado depois de criado)
. Permite duplicados
. Indexado


Semelhante a lista? Há uma diferença crítica:
. Lista → mutável
. Tuplo → imutável
Diferente de lista, tuplo é imutável. Tuplo é mais leve que lista, por isso é mais rápido. Se não precisares de mutabilidade, tuplo é a melhor escolha.


:: Porque usar tuplos?

. Segurança de dados
Se não queres que seja alterado.

. Performance ligeiramente melhor
Tuplos são mais leves e rápidos que listas.

. Podem ser usados como chave de dicionário, enquanto que listas não podem.
Isto é muito importante. Exemplo:

d = {
    (1, 2): "ponto"
}


Tuplo é o tipo de dados a usar quando:
. Coordenadas
. Dados fixos
. Retornos múltiplos de função
. Estruturas que não devem mudar
. Chaves compostas de dicionários


:::::: Criar tuplos

Forma normal
t = (1, 2, 3)

Com um único elemento:
t = (1,)   # correto
t = (1)    # isto é int, não é tuplo
Este é um erro comum. A vírgula é o que define o tuplo. Se não tiver vírgula, é apenas um valor entre parênteses.


:::::: Acesso a valores (por índice) - igual às listas

:: ler
print(alunos[0])                        # primeiro
print(alunos[-1])                       # último
print(alunos[2])                        # terceiro


:::::: Slicing (fatiamento)

print(alunos[0:2])
print(alunos[:2])
print(alunos[1:])


:::::: Adicionar, atualizar, remover elementos


Não se pode:
. adicionar
. modificar
. remover

Tuplos são imutáveis, não se pode adicionar, atualizar ou remover elementos depois de criados. Se for necessária mutabilidade, tem de se usar uma lista em vez de tuplo.

t[0] = "Novo"  # TypeError


:::::: Métodos de tuplos

alunos.count("Alice")                # conta ocorrências
alunos.index("Alice")                # devolve posição
len(alunos)                          # devolve o nº de elementos do tuplo


:::::: Converter entre lista e tuplo - muito usado na prática

:: Tuplo para lista
tuplo = (1, 2, 3)
lista = list(tuplo)

:: Lista para tuplo
lista = [1, 2, 3]
tuplo = tuple(lista)


:::::: Desempacotamento (muito importante)

Uma das grandes vantagens. Permite atribuir os elementos de um tuplo a variáveis individuais de forma fácil e legível.

pessoa = ("Alice", 20)
nome, idade = pessoa
print(nome)
print(idade)


:::::: Desempacotamento avançado

tuplo = (1, 2, 3, 4)
a, *b = tuplo

print(a)  # 1
print(b)  # [2,3,4] transformado em lista porque tem mais de um elemento


:::::: Tuplos dentro de listas - muito comum:

pessoas = [("Alice", 20), ("Bob", 25), ("Charlie", 30)]
for nome, idade in pessoas:
    print(f"Nome: {nome} tem {idade} anos")


:::::: Equívoco comum
Tuplo pode conter lista dentro:
t1 = (1, 2, [3, 4])
Mas a lista dentro do tuplo é mutável, então podes modificar a lista mesmo que o tuplo seja imutável:
t1[2].append(5)
print(t1)  # (1, 2, [3, 4, 5])



:::::: Resumo

Tuplo é:
Uma lista que não pode ser alterada
Mais seguro
Mais leve
Ideal para estrutura fixa

Atenção:
Se precisares de mutabilidade, usa lista. Se não precisares, tuplo é a melhor escolha.
Muita gente ignora tuplos no início, mas programadores mais experientes usam muito:
. Para retornos de função
. Para iterar dados estruturados
. Como chave composta


Exemplo da utilização de tuplo para iterar dados estruturados:
pessoas = [("Alice", 20), ("Bob", 25), ("Charlie", 30)]
for nome, idade in pessoas:
    print(f"Nome: {nome} tem {idade} anos")

Saber quando usar lista vs tuplo mostra maturidade técnica.
