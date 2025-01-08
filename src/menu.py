import customtkinter
from list_filmes import create_list_filmes
from rep_filmes import read_filmes, read_filmes_vistos

# Sai da tela de menu para outra tela:
def change_frame(menu_frame, next_frame):
    next_frame.pack(fill="both", expand=1)
    menu_frame.pack_forget()

def todos_filmes(root, menu_frame):
    # Cria tela de todos os filmes e muda para essa tela:
    todos_filmes_frame = create_list_filmes(root, menu_frame, read_filmes)
    change_frame(menu_frame, todos_filmes_frame)

def filmes_vistos(root, menu_frame):
    # Cria tela de todos os filmes vistos e muda para essa tela:
    filmes_vistos_frame = create_list_filmes(root, menu_frame, lambda: read_filmes_vistos("Visto"))
    change_frame(menu_frame, filmes_vistos_frame)

def filmes_nao_vistos(root, menu_frame):
    # Cria tela de todos os filmes não vistos e muda para essa tela:
    filmes_nao_vistos_frame = create_list_filmes(root, menu_frame, lambda: read_filmes_vistos("Não visto"))
    change_frame(menu_frame, filmes_nao_vistos_frame)

def create_menu(root, adicionar_frame):
    # Cria tela de menu:
    menu_frame = customtkinter.CTkFrame(root)

    text = customtkinter.CTkLabel(menu_frame, text='Menu')
    text.pack(padx=10, pady=40)

    # Botão de ir para tela de adicionar filme:
    button = customtkinter.CTkButton(menu_frame, text='Adicionar novo filme', command = lambda: change_frame(menu_frame, adicionar_frame), fg_color =("purple"))
    button.pack(padx=10, pady=10)

    # Botão de ir para tela de todos os filmes:
    button2 = customtkinter.CTkButton(menu_frame, text='Todos os filmes', command = lambda: todos_filmes(root, menu_frame), fg_color =("purple"))
    button2.pack(padx=10, pady=10)

    # Botão de ir para tela de filmes vistos:
    button3 = customtkinter.CTkButton(menu_frame, text='Filmes assistidos', command = lambda: filmes_vistos(root, menu_frame), fg_color =("purple"))
    button3.pack(padx=10, pady=10)

    # Botão de ir para tela de filmes não vistos:
    button4 = customtkinter.CTkButton(menu_frame, text='Filmes não assistidos', command = lambda: filmes_nao_vistos(root, menu_frame), fg_color =("purple"))
    button4.pack(padx=10, pady=10)
    
    return menu_frame
