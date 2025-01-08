import customtkinter
from CTkMessagebox import CTkMessagebox
from rep_filmes import read_filme_detalhes, apagar_filme, atualizar_filme


### Começo da tela de lista de filmes:
# Cria tela de detalhe do filme guardando a informação das telas anteriores e sai da tela de lista:
def go_to_filme_detalhes(root, list_filmes_frame, filmes_to_show, name, menu_frame):
    filme_detalhes_frame = create_filme_detalhes(root, name, filmes_to_show, menu_frame)
    filme_detalhes_frame.pack(fill="both", expand=1)
    list_filmes_frame.pack_forget()
    list_filmes_frame.destroy()

# Função de renderizar lista de filmes(todos, vistos, não vistos):
def list_filmes(root, list_filmes_frame, filmes_to_show, menu_frame):
    filmes = filmes_to_show() # Roda a função que retorna os filmes que eu quero
    for index in range(len(filmes)):
        l = customtkinter.CTkButton(list_filmes_frame, text=filmes[index][0], command=lambda i=index: go_to_filme_detalhes(root, list_filmes_frame, filmes_to_show, filmes[i][0], menu_frame), fg_color =("purple"))
        l.pack(padx=10, pady=10)

# Função de voltar para o menu:
def change_to_menu(menu_frame, filmes_frame):
    menu_frame.pack(fill="both", expand=1)
    filmes_frame.pack_forget()
    filmes_frame.destroy()

def create_list_filmes(root, menu_frame, filmes):
    # Cria tela de lista de filmes:
    list_filmes_frame = customtkinter.CTkScrollableFrame(root)
    
    # Botão que volta pro menu:
    back_button = customtkinter.CTkButton(list_filmes_frame, text='Voltar', command = lambda: change_to_menu(menu_frame, list_filmes_frame), fg_color =("grey"), text_color=("black"))
    back_button.pack(padx=10, pady=20)
    
    # Chamar função de renderizar lista de filmes:
    list_filmes(root, list_filmes_frame, filmes, menu_frame)

    return list_filmes_frame
### Final da tela de lista de filmes!


### Começo da tela de detalhes:
def create_filme_detalhes(root, name_filme, filmes_to_show, menu_frame):
    # Cria tela de detalhes:
    filme_detalhes_frame = customtkinter.CTkFrame(root)

    # Função de voltar:
    go_back = lambda: go_to_list(root, filmes_to_show, menu_frame, filme_detalhes_frame)

    filme = read_filme_detalhes(name_filme)

    # Começo das informações exibidas na tela:
    name = customtkinter.CTkLabel(filme_detalhes_frame, text=filme[0])
    name.pack(padx=10, pady=(40, 5))

    director = customtkinter.CTkLabel(filme_detalhes_frame, text=filme[1])
    director.pack(padx=10, pady=5)

    duration = customtkinter.CTkLabel(filme_detalhes_frame, text=filme[2])
    duration.pack(padx=10, pady=5)

    visto = customtkinter.CTkLabel(filme_detalhes_frame, text=filme[3])
    visto.pack(padx=10, pady=5)

    if filme[4] == "Null":
        nota = customtkinter.CTkLabel(filme_detalhes_frame, text="Sem Nota")
    else:
        nota = customtkinter.CTkLabel(filme_detalhes_frame, text=filme[4])
    nota.pack(padx=10, pady=5)

    if filme[5] == "Null\n":
        comentario = customtkinter.CTkLabel(filme_detalhes_frame, text="Sem Comentário")
    else:
        comentario = customtkinter.CTkLabel(filme_detalhes_frame, text=filme[5])
    comentario.pack(padx=10, pady=5)
    # Final das informações exibidas na tela!

    atualizar_button = customtkinter.CTkButton(filme_detalhes_frame, text='Atualizar Filme', command = lambda: go_to_atualizar_filme(root, name_filme, filmes_to_show, menu_frame, filme_detalhes_frame))
    atualizar_button.pack(padx=10, pady=20)

    delete_button = customtkinter.CTkButton(filme_detalhes_frame, text='Deletar Filme', command = lambda: delete_filme(name_filme, go_back), fg_color =("red"))
    delete_button.pack(padx=10, pady=20)

    back_button = customtkinter.CTkButton(filme_detalhes_frame, text='Voltar', command = go_back, fg_color =("grey"), text_color=("black"))
    back_button.pack(padx=10, pady=20)

    return filme_detalhes_frame

def go_to_list(root, filmes_to_show, menu_frame, filme_detalhes_frame):
    # Recria a tela de lista de filmes (para atualizar os dados):
    list_frame = create_list_filmes(root, menu_frame, filmes_to_show)
    list_frame.pack(fill="both", expand=1)
    filme_detalhes_frame.pack_forget()
    filme_detalhes_frame.destroy()

# Função de deletar filme:
def delete_filme(name_filme, go_back):
    msg = CTkMessagebox(title="Deletar?", message="Tem certeza que quer deletar o filme?",
                        icon="question", option_1="Deletar", option_2="Cancelar")

    if msg.get() == "Deletar":
        apagar_filme(name_filme)
        go_back()

# Cria tela de atualizar o filme guardando a informação das telas anteriores e sai da tela de detalhes:
def go_to_atualizar_filme(root, name_filme, filmes_to_show, menu_frame, filme_detalhes_frame):
    atualizar_filme_frame = create_atualizar_filme(root, name_filme, filmes_to_show, menu_frame)
    atualizar_filme_frame.pack(fill="both", expand=1)
    filme_detalhes_frame.pack_forget()
    filme_detalhes_frame.destroy()
### Final da tela de detalhes!

### Começo da tela de atualizar filme:
def create_atualizar_filme(root, name_filme, filmes_to_show, menu_frame):
    atualizar_filme_frame = customtkinter.CTkFrame(root)

    go_back = lambda: go_to_detalhes(root, name_filme, filmes_to_show, menu_frame, atualizar_filme_frame)

    filme = read_filme_detalhes(name_filme)

    # Começo informação da tela:
    name = customtkinter.CTkLabel(atualizar_filme_frame, text=filme[0])
    name.pack(padx=10, pady=(40, 5))
    
    visto_label = customtkinter.CTkLabel(atualizar_filme_frame, text="Visto:")
    visto_label.pack(padx=10, pady=5)
    if filme[3] == "Visto":
        visto_button = customtkinter.CTkButton(atualizar_filme_frame, text="Mudar Para Não visto", command = lambda: atualizar_visto(name_filme, "Não visto", message_var))
    else:
        visto_button = customtkinter.CTkButton(atualizar_filme_frame, text="Mudar Para Visto", command = lambda: atualizar_visto(name_filme, "Visto", message_var))
    visto_button.pack(padx=10, pady=2)

    nota_label = customtkinter.CTkLabel(atualizar_filme_frame, text="Nota:")
    nota_label.pack(padx=10, pady=5)
    nota_input = customtkinter.CTkEntry(atualizar_filme_frame, placeholder_text="7.0")
    nota_input.pack(padx=10, pady=2)
    nota_button = customtkinter.CTkButton(atualizar_filme_frame, text="Atualizar Nota", command = lambda: atualizar_nota(name_filme, nota_input.get(), message_var))
    nota_button.pack(padx=10, pady=2)

    comentario_label = customtkinter.CTkLabel(atualizar_filme_frame, text="Comentário:")
    comentario_label.pack(padx=10, pady=5)
    comentario_input = customtkinter.CTkEntry(atualizar_filme_frame, placeholder_text="Comentario...")
    comentario_input.pack(padx=10, pady=2)
    comentario_button = customtkinter.CTkButton(atualizar_filme_frame, text="Atualizar Comentario", command = lambda: atualizar_comentario(name_filme, comentario_input.get(), message_var))
    comentario_button.pack(padx=10, pady=2)

    message_var = customtkinter.StringVar(atualizar_filme_frame, "")
    message = customtkinter.CTkLabel(atualizar_filme_frame, textvariable=message_var)
    message.pack(padx=10, pady=20)
    # Final informação da tela!

    back_button = customtkinter.CTkButton(atualizar_filme_frame, text='Voltar', command = go_back, fg_color =("grey"), text_color=("black"))
    back_button.pack(padx=10, pady=(0, 20))

    return atualizar_filme_frame

def go_to_detalhes(root, name_filme, filmes_to_show, menu_frame, atualizar_frame):
    detalhes_frame = create_filme_detalhes(root, name_filme, filmes_to_show, menu_frame)
    detalhes_frame.pack(fill="both", expand=1)
    atualizar_frame.pack_forget()
    atualizar_frame.destroy()

def atualizar_visto(name_filme, valor, message_var):
    atualizar_filme(name_filme, 3, valor)
    message_var.set("Visto atualizado!")

def atualizar_nota(name_filme, nota, message_var):
    if nota != "":
        atualizar_filme(name_filme, 4, nota)
        message_var.set("Nota atualizada!")
    else:
        message_var.set("Preencha nota antes de atualizar!")


def atualizar_comentario(name_filme, comentario, message_var):
    if comentario != "":
        atualizar_filme(name_filme, 5, comentario+"\n")
        message_var.set("Comentário atualizado!")
    else:
        message_var.set("Preencha comentário antes de atualizar!")
