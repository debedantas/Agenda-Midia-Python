import customtkinter
from login import create_login
from menu import create_menu
from adicionar import create_adicionar

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('dark-blue')

# Muda para menu e esquece a tela anterior:
def change_to_menu(current_frame):
    menu_frame.pack(fill="both", expand=1)
    current_frame.pack_forget()

# Cria janela:
root = customtkinter.CTk()
root.geometry("300x500")

# Cria telas de login, adicionar filme e menu:
login_frame = create_login(root, change_to_menu)
adicionar_frame = create_adicionar(root, change_to_menu)
menu_frame = create_menu(root, adicionar_frame)

# Coloca login na janela:
login_frame.pack(fill="both", expand=1)

# Pra rodar o programa:
root.mainloop()
