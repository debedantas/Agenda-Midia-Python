import customtkinter
from rep_filmes import create_filme

# Função chamada quando usuário clica para adicionar filme:
def adicionar_filme(name, director, duration, message_var):
    nome = name.get()
    diretor = director.get()
    duracao = duration.get()
    # Verifica se todos os campos foram preenchidos:
    if nome == "" or diretor == "" or duracao == "":
        message_var.set("Preencha todos os campos.")
    else:
        # Tenta criar filme:
        created = create_filme(nome, diretor, duracao)
        if created: 
            message_var.set("Filme adicionado!")
        else:
            message_var.set("Filme já existe!")

# Criar tela de adicionar filme:
def create_adicionar(root, change_to_menu):
    adicionar_frame = customtkinter.CTkFrame(root)

    name_label = customtkinter.CTkLabel(adicionar_frame, text='Nome do filme:')
    name_label.pack(padx=10, pady=5)

    name_input = customtkinter.CTkEntry(adicionar_frame, placeholder_text='Titanic')
    name_input.pack(padx=10, pady=0)

    director_label = customtkinter.CTkLabel(adicionar_frame, text='Nome do diretor:')
    director_label.pack(padx=10, pady=5)

    director_input = customtkinter.CTkEntry(adicionar_frame, placeholder_text='James Cameron')
    director_input.pack(padx=10, pady=0)

    duration_label = customtkinter.CTkLabel(adicionar_frame, text='Duração do filme (em min):')
    duration_label.pack(padx=10, pady=5)

    duration_input = customtkinter.CTkEntry(adicionar_frame, placeholder_text='195')
    duration_input.pack(padx=10, pady=0)

    create_button = customtkinter.CTkButton(adicionar_frame, text='Adicionar novo filme', command = lambda: adicionar_filme(name_input, director_input, duration_input, message_var), fg_color =("purple"))
    create_button.pack(padx=10, pady=20)

    message_var = customtkinter.StringVar(adicionar_frame, "")
    message = customtkinter.CTkLabel(adicionar_frame, textvariable=message_var)
    message.pack(padx=10, pady=40)

    # Botão de voltar para menu:
    back_button = customtkinter.CTkButton(adicionar_frame, text='Voltar', command = lambda: change_to_menu(adicionar_frame), fg_color =("grey"), text_color=("black"))
    back_button.pack(padx=10, pady=20)

    return adicionar_frame
