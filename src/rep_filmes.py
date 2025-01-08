# Acrescentar novo filme:
def create_filme(nome, diretor, tamanho):
    # Retorna false caso filme já exista:
    if read_filme_detalhes(nome) != None:
        return False

    # Abre arquivo do banco de dados com os filmes, no modo de escrever:
    bf = open("bd_filmes.txt", mode="a", encoding="utf-8")

    tamanho = tamanho + " minutos"
    visto = "Não visto"
    nota = "Null"
    comentario = "Null"
    # Escreve no banco de dados as informações dadas e pré-estabelecidas:
    bf.write(nome+";"+diretor+";"+tamanho+";"+visto+";"+nota+";"+comentario+"\n")
    return True

# Listar todos os filmes:
def read_filmes():
    # Abre arquivo do banco de dados com os filmes, no modo de ler:
    bf = open("bd_filmes.txt", mode="r", encoding="utf-8")

    # Cria uma lista vazia:
    todos_filmes = []
    # Para cada filme no banco, separa as informações e adiciona na lista todos_filmes:
    for filmes in bf:
        lista_filmes = filmes.split(sep=";")
        todos_filmes.append(lista_filmes)
    bf.close()
    return todos_filmes

# Listar todos os filmes vistos e não vistos:
def read_filmes_vistos(valor):
    # Abre arquivo do banco de dados com os filmes, no modo de ler:
    bf = open("bd_filmes.txt", mode="r", encoding="utf-8")

    # Cria uma lista vazia:
    todos_filmes_vistos = []
    # Para cada filme no banco, separa as informações e adiciona na lista todos_filmes_vistos:
    for filmes in bf:
        lista_filmes = filmes.split(sep=";")
        if lista_filmes[3] == valor:
            todos_filmes_vistos.append(lista_filmes)
    bf.close()
    return todos_filmes_vistos

# Listar detalhes de um filme específico:
def read_filme_detalhes(titulo):
    # Abre arquivo do banco de dados com os filmes, no modo de ler:
    bf = open("bd_filmes.txt", mode="r", encoding="utf-8")

    # Para cada filme no banco de dados, separa as informações, checa se o nome do filme no index[0] é igual o do titulo:
    for filmes in bf:
        lista_filmes = filmes.split(sep=";")
        if lista_filmes[0] == titulo:
            return lista_filmes
    bf.close()
    # Caso o filme não seja encontrado:
    return None

# Apagar um filme: 
def apagar_filme(titulo):
    # Abre arquivo do banco de dados com os filmes, no modo de ler:
    bf = open("bd_filmes.txt", mode="r", encoding="utf-8")

    l_gravacao = []

    # Separa as informações, checa se o nome no index[0] é diferente do titulo, se sim, escreve o filme na lista vazia:
    for filmes in bf:
        lista_filmes = filmes.split(sep=";")
        if lista_filmes[0] != titulo:
            l_gravacao.append(filmes)
    bf.close()

    # Abre arquivo do banco de dados com os filmes, no modo de escrever:
    bf = open("bd_filmes.txt", mode="w", encoding="utf-8")

    # Escreve (por cima do arquivo antigo) cada filme da lista no arquivo:
    for filme in l_gravacao:
        bf.write(filme)
    bf.close()

# Atualizar filme:
def atualizar_filme(titulo, index, valor):
    # Abre arquivo do banco de dados com os filmes, no modo de ler:
    bf = open("bd_filmes.txt", mode="r", encoding="utf-8")

    l_gravacao = []

    # Separa as informações e adiciona a lista_filmes na lista l_gravacao: 
    for filmes in bf:
        lista_filmes = filmes.split(sep=";")
        l_gravacao.append(lista_filmes)
    bf.close()

    # Checa se o nome do filme == titulo que quero atualizar, se sim, atualiza o index(visto, nota ou comentário):
    for filme in l_gravacao:
        if filme[0] == titulo:
            filme[index] = valor

    # Junta os dados dos filmes em l_gravacao com ; e coloca numa nova lista l_gravacao_novo:
    l_gravacao_novo = []
    for i in l_gravacao:
        l_gravacao_update = ';'.join(i)
        l_gravacao_novo.append(l_gravacao_update)

    # Abre arquivo do banco de dados com os filmes, no modo de escrever:
    bf = open("bd_filmes.txt", mode="w", encoding="utf-8")

    # Escreve (por cima do arquivo antigo) cada filme da lista no arquivo:
    for novo in l_gravacao_novo:
        bf.write(novo)
    bf.close()

# titulo = input("Digite o filme: ")
# read_filme_detalhes(titulo)
# atualizar_filme(titulo, 3, "Visto")
# print(read_filmes_vistos("Não visto"))
