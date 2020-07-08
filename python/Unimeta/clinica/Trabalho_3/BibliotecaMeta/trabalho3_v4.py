# coding=utf-8

from tkinter import *
from tkinter import messagebox as ms
import sqlite3

cadt = None
listr = None
empr = None
loged = None
photo2 = None
logo2 = None


def main():
    barra_menu = Menu(root)
    main_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Cadastrar', menu=main_menu)
    main_menu.add_command(label='Autor', command=autor)
    main_menu.add_command(label='Cliente', command=cliente)
    main_menu.add_command(label='Livro', command=livro)
    main_menu.add_command(label='Usuário', command=usuario)

    main_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Listar', menu=main_menu)
    main_menu.add_command(label='Autores')
    main_menu.add_command(label='Clientes')
    main_menu.add_command(label='Livros')
    main_menu.add_command(label='Usuários')
    main_menu.add_command(label='Empréstimos')
    main_menu.add_command(label='Devoluções')
    main_menu.add_command(label='Livros em situação de empréstimo')

    main_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Empréstimo', menu=main_menu)
    main_menu.add_command(label='Realizar Empréstimo')
    main_menu.add_command(label='Realizar Devolução')

    main_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Sair', menu=main_menu)
    main_menu.add_command(label='Sair', command=root.destroy)
    root.config(menu=barra_menu)


def master():
    global entry_user, entry_password, photo, frame_login
    frame_login = Frame(root, bg='#292929')
    frame_login.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file='data\logo-biblioteca.png')
    logo = Label(frame_login, image=photo, bg='#292929')
    logo.pack(pady=20)

    label_user = Label(frame_login, text='Usuário:', font=('', 12), fg='gray', bg='#292929')
    label_user.place(x=30, y=120)
    entry_user = Entry(frame_login, justify=CENTER, font=('', 11, 'bold'), width=26)
    entry_user.place(x=100, y=120)

    label_password = Label(frame_login, text='Senha:', font=('', 12), fg='gray', bg='#292929')
    label_password.place(x=40, y=150)
    entry_password = Entry(frame_login, justify=CENTER, font=('', 11, 'bold'), show='*', width=26)
    entry_password.place(x=100, y=150)

    bt_login = Button(frame_login, width=8, text='LOGIN', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                      command=verify)
    bt_login.place(x=100, y=200)
    bt_leave = Button(frame_login, width=8, text='SAIR', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                      command=root.quit)
    bt_leave.place(x=223, y=200)


def verify():
    global loged, cont, cont2, photo2, logo2, label_error, frame_logado
    cont = 0
    cont2 = 2
    frame_logado = Frame(root, bg='#292929')
    with sqlite3.connect('data\Registro.db') as db:
        c = db.cursor()
        find_user = 'SELECT * FROM usuario WHERE login = ? AND senha = ?'
        c.execute(find_user, [(entry_user.get()), (entry_password.get())])
        login_test = c.fetchall()
        if login_test:
            frame_login.destroy()
            frame_logado.pack(fill=BOTH, expand=1)
            photo2 = PhotoImage(file='data\logo-biblioteca-menu.png')
            logo2 = Label(frame_logado, image=photo2, bg='#292929')
            logo2.pack(padx=25, pady=50)
            label_login = Label(frame_logado, text='[Logado]', font=('', 16, 'bold'), bg='#292929', fg='white')
            label_login.pack(side=BOTTOM)
            main()
        else:
            label_error = Label(frame_login, text=f'Usuário ou Senha Inválidos ({cont2})', bg='#292929', fg='white')
            label_error.pack(side=BOTTOM)
            cont2 -= 1
            cont += 1
            if cont == 3:
                ms.showwarning('Aviso', 'O Sistema será finalizado por questões de segurança.')
                root.destroy()


# -=-=-=-=-=-=- Cadastro -=-=-=-=-=-=-


def autor():
    global nome_autor, window_autor
    window_autor = Toplevel(root, bg='#292929')
    window_autor.title('Cadastrar Autor')
    window_autor.transient(root)
    window_autor.focus_force()
    window_autor.grab_set()

    lnome_autor = Label(window_autor, text='Nome:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lnome_autor.place(x=20, y=50)
    nome_autor = Entry(window_autor, width=45, font=('', 11, 'bold'))
    nome_autor.place(x=20, y=80)

    bt_salvar = Button(window_autor, width=8, text='Salvar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command=salvar_autor)
    bt_salvar.place(x=20, y=200)

    bt_pesquisar = Button(window_autor, width=8, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white')
    bt_pesquisar.place(x=155, y=200)

    bt_cancelar = Button(window_autor, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_autor.destroy)
    bt_cancelar.place(x=292, y=200)

    window_autor.geometry('400x300+200+200')


def salvar_autor():
    global label_autor
    db = sqlite3.connect('data\Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS autor(
        id INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL 
        );''')
    find_autor = '''SELECT * FROM autor WHERE nome = ?'''
    c.execute(find_autor, [(nome_autor.get())])
    autor_test = c.fetchall()
    if autor_test:
        try:
            label_autor.destroy()
        except NameError:
            pass
        nome_autor['bg'] = 'pink2'
        label_autor = Label(window_autor, text='Autor já Cadastrado.', font=('', 10, 'bold'), bg='#292929', fg='white')
        label_autor.pack(side=BOTTOM)
    elif len(nome_autor.get()) < 5:
        try:
            label_autor.destroy()
        except NameError:
            pass
        nome_autor['bg'] = 'pink2'
        label_autor = Label(window_autor, text='Minino de 5 Caracteres', font=('', 10, 'bold'), bg='#292929',
                            fg='white')
        label_autor.pack(side=BOTTOM)
    else:
        try:
            label_autor.destroy()
        except NameError:
            pass
        nome_autor['bg'] = 'white'
        label_autor = Label(window_autor, text='Autor Cadastrado com Sucesso!',
                            font=('', 10, 'bold'), bg='#292929', fg='white')
        label_autor.pack(side=BOTTOM)
        insert = 'INSERT INTO autor(nome) VALUES(?)'
        c.execute(insert, [(nome_autor.get())])
        db.commit()
    nome_autor.delete(0, 45)
    db.close()


def cliente():
    global window_cliente, nome, rua, nascimento, numero, bairro, cidade, estado, telefone, celular, email, cpf
    window_cliente = Toplevel(root, bg='#292929')
    window_cliente.title('Cadastrar Cliente')
    window_cliente.transient(root)
    window_cliente.focus_force()
    window_cliente.grab_set()

    lnome = Label(window_cliente, text='Nome:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lnome.place(x=20, y=20)
    nome = Entry(window_cliente, width=45, font=('', 11, 'bold'))
    nome.place(x=20, y=50)

    lcpf = Label(window_cliente, text='CPF:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lcpf.place(x=20, y=80)
    cpf = Entry(window_cliente, width=12, font=('', 11, 'bold'))
    cpf.place(x=20, y=110)

    ltelefone = Label(window_cliente, text='Telefone:', bg='#292929', fg='white', font=('', 12, 'bold'))
    ltelefone.place(x=150, y=80)
    telefone = Entry(window_cliente, width=12, font=('', 11, 'bold'))
    telefone.place(x=150, y=110)

    lcelular = Label(window_cliente, text='Celular:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lcelular.place(x=283, y=80)
    celular = Entry(window_cliente, width=12, font=('', 11, 'bold'))
    celular.place(x=283, y=110)

    lemail = Label(window_cliente, text='E-mail:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lemail.place(x=20, y=140)
    email = Entry(window_cliente, width=45, font=('', 11, 'bold'))
    email.place(x=20, y=170)

    lrua = Label(window_cliente, text='Rua:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lrua.place(x=20, y=200)
    rua = Entry(window_cliente, width=31, font=('', 11, 'bold'))
    rua.place(x=20, y=230)

    lnascimento = Label(window_cliente, text='Data/Nascimento:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lnascimento.place(x=235, y=260)
    nascimento = Entry(window_cliente, width=18, font=('', 11, 'bold'))
    nascimento.place(x=235, y=290)

    lnumero = Label(window_cliente, text='Número:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lnumero.place(x=300, y=200)
    numero = Entry(window_cliente, width=10, font=('', 11, 'bold'))
    numero.place(x=300, y=230)

    lbairro = Label(window_cliente, text='Bairro:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lbairro.place(x=20, y=260)
    bairro = Entry(window_cliente, width=23, font=('', 11, 'bold'))
    bairro.place(x=20, y=290)

    lcidade = Label(window_cliente, text='Cidade:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lcidade.place(x=20, y=320)
    cidade = Entry(window_cliente, width=23, font=('', 11, 'bold'))
    cidade.place(x=20, y=350)

    lestado = Label(window_cliente, text='Estado:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lestado.place(x=235, y=320)
    estado = Entry(window_cliente, width=18, font=('', 11, 'bold'))
    estado.place(x=235, y=350)

    bt_salvar = Button(window_cliente, width=8, text='Salvar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command=salvar_cliente)
    bt_salvar.place(x=20, y=410)

    bt_pesquisar = Button(window_cliente, width=8, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white')
    bt_pesquisar.place(x=155, y=410)

    bt_cancelar = Button(window_cliente, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_cliente.destroy)
    bt_cancelar.place(x=292, y=410)

    window_cliente.geometry('400x500+200+200')


# Salvar Cliente

def salvar_cliente():
    db = sqlite3.connect('data\Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cliente(
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    rua TEXT NOT NULL,
    numero INTEGER NOT NULL,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    nascimento DATE NOT NULL,
    telefone TEXT,
    celular TEXT NOT NULL,
    email TEXT NOT NULL,
    cpf TEXT NOT NULL
    );''')
    salvar_nome = nome_cliente()
    salvar_rua = rua_cliente()
    salvar_numero = numero_cliente()
    salvar_bairro = bairro_cliente()
    salvar_cidade = cidade_cliente()
    salvar_estado = estado_cliente()
    salvar_nascimento = nascimento_cliente()
    salvar_telefone = telefone_cliente()
    salvar_celular = celular_cliente()
    salvar_email = email_cliente()
    salvar_cpf = cpf_cliente()
    try:
        insert = '''INSERT INTO cliente(nome, rua, numero, bairro, cidade, estado, nascimento, telefone, 
        celular, email, cpf) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        c.execute(insert, [salvar_nome, salvar_rua, salvar_numero, salvar_bairro, salvar_cidade, salvar_estado,
                           salvar_nascimento, salvar_telefone, salvar_celular, salvar_email, salvar_cpf])
        db.commit()
    except Exception as erro:
        print(erro)
    nome.delete(0, 45)
    rua.delete(0, 31)
    numero.delete(0, 10)
    bairro.delete(0, 23)
    cidade.delete(0, 23)
    estado.delete(0, 18)
    nascimento.delete(0, 18)
    telefone.delete(0, 12)
    celular.delete(0, 12)
    email.delete(0, 45)
    cpf.delete(0, 12)
    db.close()


def cpf_cliente():
    global label_cliente, result, cpf_validate
    cpf_validate = cpf.get()
    mult = 10
    verif_1 = 0
    verif_2 = 0
    db = sqlite3.connect('data\Registro.db')
    c = db.cursor()
    find_cpf = 'SELECT * FROM cliente WHERE cpf = ?'
    c.execute(find_cpf, [(cpf.get())])
    result = c.fetchall()
    if result:
        try:
            label_cliente.destroy()
        except NameError:
            pass
        label_cliente = Label(window_cliente, text='CPF já Cadastrado', font=('', 10, 'bold'), bg='#292929',
                              fg='white')
        label_cliente.pack(side=BOTTOM)
    elif len(cpf_validate) != 11:
        try:
            label_cliente.destroy()
        except NameError:
            pass
        label_cliente = Label(window_cliente, text='CPF Inválido', font=('', 10, 'bold'), bg='#292929',
                              fg='white')
        label_cliente.pack(side=BOTTOM)
    elif cpf_validate[0] == cpf_validate[1] and cpf_validate[1] == cpf_validate[2] and cpf_validate[2] == \
            cpf_validate[3] and cpf_validate[3] == cpf_validate[4] and \
            cpf_validate[4] == cpf_validate[5] and cpf_validate[5] == cpf_validate[6] and cpf_validate[6] == \
            cpf_validate[7] and cpf_validate[7] == cpf_validate[8] \
            and cpf_validate[8] == cpf_validate[9] and cpf_validate[9] == cpf_validate[10]:
        print("CPF Inválido")
    elif cpf_validate[0:2] == cpf_validate[3:5] and cpf_validate[3:5] == cpf_validate[6:8]:
        try:
            label_cliente.destroy()
        except NameError:
            pass
        label_cliente = Label(window_cliente, text='CPF Inválido', font=('', 10, 'bold'), bg='#292929',
                              fg='white')
        label_cliente.pack(side=BOTTOM)
    else:
        for i in cpf_validate[0:9]:
            i = int(i)
            verif_1 = verif_1 + (i * mult)
            if mult != 1:
                mult = mult - 1
            else:
                mult = 11
        verif_1 = verif_1 % 11
        if verif_1 == 0 or verif_1 == 1:
            verif_1 = 0
        else:
            verif_1 = 11 - verif_1
        mult = 11
        for i in cpf_validate[0:10]:
            i = int(i)
            verif_2 = verif_2 + (i * mult)
            if mult != 1:
                mult = mult - 1
            else:
                mult = 11
        verif_2 = verif_2 % 11
        if verif_2 == 0 or verif_2 == 1:
            verif_2 = 0
        else:
            verif_2 = 11 - verif_2
        verif_1 = str(verif_1)
        verif_2 = str(verif_2)
        if cpf_validate[9] == verif_1:
            if cpf_validate[10] == verif_2:
                try:
                    label_cliente.destroy()
                except NameError:
                    pass
                label_cliente = Label(window_cliente, text='CPF Cadastrado com Sucesso!', font=('', 10, 'bold'),
                                      bg='#292929', fg='white')
                label_cliente.pack(side=BOTTOM)
                cpf_p1 = cpf_validate[:3]
                cpf_p2 = cpf_validate[3:6]
                cpf_p3 = cpf_validate[6:9]
                verify_cpf = cpf_validate[9:]
                return f'{cpf_p1}.{cpf_p2}.{cpf_p3}-{verify_cpf}'
    db.close()


def nome_cliente():
    global label_cliente
    nome_validate = nome.get()
    if len(nome_validate) < 4:
        try:
            label_cliente.destroy()
        except NameError:
            pass
        label_cliente = Label(window_cliente, text='Minimo de 4 Caracteres', font=('', 10, 'bold'),
                              bg='#292929', fg='white')
        label_cliente.pack(side=BOTTOM)
    else:
        return nome.get()


def rua_cliente():
    global label_cliente
    rua_validate = rua.get()
    if len(rua_validate) < 4:
        try:
            label_cliente.destroy()
        except:
            pass
        label_cliente = Label(window_cliente, text='Minimo de 4 Caracteres', font=('', 10, 'bold'),
                              bg='#292929', fg='white')
        label_cliente.pack(side=BOTTOM)
    else:
        return rua.get()


def numero_cliente():
    try:
        numero_test = int(numero.get())
        return numero.get()
    except:
        pass


def bairro_cliente():
    bairro_validade = bairro.get()
    if len(bairro_validade) < 4:
        print('Minimo de 4 caracteres')
    else:
        return bairro.get()


def cidade_cliente():
    cidade_validade = cidade.get()
    if len(cidade_validade) < 4:
        print('Minimo de 4 caracteres')
    else:
        return cidade.get()


def estado_cliente():
    estado_validade = estado.get()
    if len(estado_validade) < 4:
        print('Minimo de 4 caracteres')
    else:
        return estado.get()


def nascimento_cliente():
    data_validate = nascimento.get()
    try:
        nascimento_test = int(nascimento.get())
        dia = data_validate[:2]
        mes = data_validate[2:4]
        ano = data_validate[4:]
        if len(data_validate) != 8:
            print('data errada')
        else:
            return f'{dia}/{mes}/{ano}'
    except:
        print('nascimento errado')


def telefone_cliente():
    telefone_validate = telefone.get()
    try:
        telefone_test = int(telefone.get())
        ddd = telefone_validate[:2]
        parte1 = telefone_validate[2:6]
        parte2 = telefone_validate[6:]
        if len(telefone_validate) < 10:
            telefone['bg'] = 'pink2'
        else:
            telefone['bg'] = 'white'
            return f'({ddd}){parte1}-{parte2}'
    except:
        telefone['bg'] = 'pink2'


def celular_cliente():
    celular_validate = celular.get()
    try:
        celular_test = int(celular.get())
        ddd = celular_validate[:2]
        parte1 = celular_validate[2:7]
        parte2 = celular_validate[7:]
        if len(celular_validate) < 11:
            celular['bg'] = 'pink2'
        else:
            celular['bg'] = 'white'
            return f'({ddd}){parte1}-{parte2}'
    except:
        celular['bg'] = 'pink2'


def email_cliente():
    email_validate = email.get()
    if len(email_validate) < 9:
        email['bg'] = 'pink2'
    elif ' ' in email_validate:
        email['bg'] = 'pink2'
    else:
        x = email_validate.split('@')
        if len(x) != 2 or len(x[0]) == 0:
            email['bg'] = 'pink2'
        else:
            x = x[1].split('.')
            if len(x) < 2 or len(x) > 3 or len(x[0]) == 0:
                email['bg'] = 'pink2'
            elif len(x[1]) == 0:
                email['bg'] = 'pink2'
            else:
                email['bg'] = 'white'
                return email.get()


def livro():
    global titulo
    global paginas
    global window_livro
    window_livro = Toplevel(root, bg='#292929')
    window_livro.title('Cadastrar Livro')
    window_livro.transient(root)
    window_livro.focus_force()
    window_livro.grab_set()

    ltitulo = Label(window_livro, text='Titulo do Livro:', bg='#292929', fg='white', font=('', 12, 'bold'))
    ltitulo.place(x=20, y=30)
    titulo = Entry(window_livro, width=45, font=('', 11, 'bold'))
    titulo.place(x=20, y=60)

    lpaginas = Label(window_livro, text='Nº de Páginas:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lpaginas.place(x=20, y=110)
    paginas = Entry(window_livro, width=12, font=('', 11, 'bold'))
    paginas.place(x=20, y=140)

    bt_salvar = Button(window_livro, width=8, text='Salvar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command=salvar_livro)
    bt_salvar.place(x=20, y=200)

    bt_pesquisar = Button(window_livro, width=8, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white')
    bt_pesquisar.place(x=155, y=200)

    bt_cancelar = Button(window_livro, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_livro.destroy)
    bt_cancelar.place(x=292, y=200)

    window_livro.geometry('400x300+200+200')


def salvar_livro():
    db = sqlite3.connect('data\Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS livro(
    id INTEGER PRIMARY KEY NOT NULL,
    titulo TEXT NOT NULL,
    paginas INTEGER NOT NULL
    );''')
    salvar_titulo = titulo_livro()
    salvar_paginas = paginas_livro()
    try:
        insert = '''INSERT INTO livro(titulo, paginas) VALUES(?, ?)'''
        c.execute(insert, [salvar_titulo, salvar_paginas])
        db.commit()
    except Exception as erro:
        print(erro)
    titulo.delete(0, 45)
    paginas.delete(0, 12)
    db.close()


def titulo_livro():
    global label_livro
    db = sqlite3.connect('data\Registro.db')
    c = db.cursor()
    find_livro = 'SELECT * FROM livro WHERE titulo = ?'
    c.execute(find_livro, [(titulo.get())])
    titulo_test = c.fetchall()
    if titulo_test:
        titulo['bg'] = 'pink2'
    elif len(titulo.get()) < 2:
        titulo['bg'] = 'pink2'
    else:
        try:
            label_livro.destroy()
        except NameError:
            pass
        titulo['bg'] = 'white'
        return titulo.get()
    db.close()


def paginas_livro():
    global label_livro
    paginas_validate = paginas.get()
    try:
        paginas_test = int(paginas.get())
        if len(paginas_validate) < 1:
            paginas['bg'] = 'pink2'
        else:
            label_livro.destroy()
            paginas['bg'] = 'white'
            return paginas.get()
    except:
        paginas['bg'] = 'pink2'


def usuario():
    global window_usuario, user, senha
    window_usuario = Toplevel(root, bg='#292929')
    window_usuario.title('Cadastrar Usuário')
    window_usuario.transient(root)
    window_usuario.focus_force()
    window_usuario.grab_set()

    lusuario = Label(window_usuario, text='Usuário:', font=('', 12), fg='gray', bg='#292929')
    lusuario.place(x=30, y=60)
    user = Entry(window_usuario, justify=CENTER, font=('', 11, 'bold'), width=26)
    user.place(x=100, y=60)

    lsenha = Label(window_usuario, text='Senha:', font=('', 12), fg='gray', bg='#292929')
    lsenha.place(x=40, y=100)
    senha = Entry(window_usuario, justify=CENTER, font=('', 11, 'bold'), show='*', width=26)
    senha.place(x=100, y=100)

    bt_salvar = Button(window_usuario, width=8, text='Salvar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command=salvar_usuario)
    bt_salvar.place(x=20, y=200)

    bt_pesquisar = Button(window_usuario, width=8, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white')
    bt_pesquisar.place(x=155, y=200)

    bt_cancelar = Button(window_usuario, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_usuario.destroy)
    bt_cancelar.place(x=292, y=200)

    window_usuario.geometry('400x300+200+200')


def salvar_usuario():
    salvar_login = login_usuario()
    salvar_senha = senha_usuario()
    db = sqlite3.connect('data\Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuario(
    id INTEGER PRIMARY KEY NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NOT NULL 
    );''')
    try:
        insert = 'INSERT INTO usuario(login, senha) VALUES(?, ?)'
        c.execute(insert, [salvar_login, salvar_senha])
        db.commit()
    except Exception as erro:
        print(erro)
    user.delete(0, 26)
    senha.delete(0, 26)
    db.close()


def login_usuario():
    global label_usuario
    db = sqlite3.connect('data\Registro.db')
    c = db.cursor()
    find_user = 'SELECT * FROM usuario WHERE login = ?'
    c.execute(find_user, [(user.get())])
    usuario_test = c.fetchall()
    if usuario_test:
        try:
            label_usuario.destroy()
        except NameError:
            pass
        label_usuario = Label(window_usuario, text='Usuário já Cadastrado', font=('', 10, 'bold'),
                              bg='#292929', fg='white')
        label_usuario.pack(side=BOTTOM)
        user['bg'] = 'pink2'
    elif len(user.get()) < 4:
        try:
            label_usuario.destroy()
        except NameError:
            pass
        label_usuario = Label(window_usuario, text='Login no Minimo 4 Caracteres', font=('', 10, 'bold'),
                              bg='#292929', fg='white')
        label_usuario.pack(side=BOTTOM)
        user['bg'] = 'pink2'
    else:
        label_usuario.destroy()
        user['bg'] = 'white'
        return user.get()
    db.close()


def senha_usuario():
    global label_usuario
    if len(senha.get()) < 4:
        label_usuario = Label(window_usuario, text='Senha no Minimo 4 Caracteres', font=('', 10, 'bold'),
                              bg='#292929', fg='white')
        label_usuario.pack(side=BOTTOM)
        senha['bg'] = 'pink2'
    else:
        label_usuario.destroy()
        senha['bg'] = 'white'
        return senha.get()


# =-=-=-=-=-=- Listar =-=-=-=-=-=-


root = Tk()

master()

root.title('Login')
root['bg'] = '#292929'
root.geometry('400x300+600+300')
root.resizable(0, 0)
root.mainloop()
