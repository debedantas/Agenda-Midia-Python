import customtkinter

def click_button(user, password, text_error_var, login_frame, change_to_menu):
    print(user.get())
    print(password.get())
    # Se usuario e senha forem corretos, muda a tela pra menu, se não, exibe mensagem de erro:
    if user.get() == "usuario" and password.get() == "senha123":
        change_to_menu(login_frame)
    else:
        text_error_var.set("Usuário ou senha incorreto")

def create_login(root, change_to_menu):
    # Cria tela de login:
    login_frame = customtkinter.CTkFrame(root)

    text = customtkinter.CTkLabel(login_frame, text='Fazer Login')
    text.pack(padx=10, pady=40)

    user = customtkinter.CTkEntry(login_frame, placeholder_text='Usuário')
    user.pack(padx=10, pady=5)

    password = customtkinter.CTkEntry(login_frame, placeholder_text = 'Senha', show = '*')
    password.pack(padx=10, pady=10)

    button = customtkinter.CTkButton(login_frame, text='Login', command = lambda: click_button(user, password, text_error_var, login_frame, change_to_menu), fg_color =("purple"))
    button.pack(padx=10, pady=10)


    text_error_var = customtkinter.StringVar(login_frame, "")
    text_error = customtkinter.CTkLabel(login_frame, textvariable=text_error_var)
    text_error.pack(padx=10, pady=40)

    return login_frame
