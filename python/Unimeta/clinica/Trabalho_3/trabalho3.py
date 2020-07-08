#coding=utf-8

from tkinter import *
from tkinter import messagebox as ms
import sqlite3

cont = 0
cont2 = 2
cadt = None
listr = None
empr = None
loged = None
photo2 = None
logo2 = None


def verify():
    global loged
    global cont2
    global cont
    global photo2
    global logo2
    with sqlite3.connect('registro.db') as db:
        c = db.cursor()
        find_user = 'SELECT * FROM usuario WHERE login = ? AND senha = ?'
        c.execute(find_user,[(entry_user.get()), (entry_password.get())])
        result = c.fetchall()
        if result:
            label_user.destroy()
            entry_user.destroy()
            label_password.destroy()
            entry_password.destroy()
            bt_login.destroy()
            bt_leave.destroy()
            logo.destroy()
            main()
            photo2 = PhotoImage(file='logo-biblioteca-menu.png')
            logo2 = Label(root, image=photo2, bg='#292929')
            logo2.pack(padx=20, pady=20)
            loged = Label(root, text='Bem Vindo!', font=('', 20, 'bold'), bg='#292929', fg='white', pady=20)
            loged.pack(side=BOTTOM)

        else:
            ms.showerror('ERRO', f'Usuário ou Senha Inválidos. \n\nTentativas restantes: {cont2}')
            cont2 -= 1
            cont += 1
            if cont == 3:
                ms.showwarning('Aviso', 'O Sistema será finalizado por questões de segurança.')
                root.destroy()


def main():
    barra_menu = Menu(root)
    main_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Menu', menu=main_menu)
    main_menu.add_command(label='Cadastrar', command=cadastrar)
    main_menu.add_command(label='Listar', command=listar)
    main_menu.add_command(label='Empréstimo', command=emprestimo)
    main_menu.add_separator()
    main_menu.add_command(label='Sair', command=root.destroy)
    root.config(menu=barra_menu)


def cadastrar():
    global cadt
    try:
        loged.destroy()
        logo2.destroy()
        cadt.destroy()
        listr.destroy()
        empr.destroy()
    except:
        pass
    cadt = Frame(root, bg='#292929', width=400, height=300)
    cadt.pack(fill=BOTH, expand=1)
    bt_autor = Button(cadt, width=10, text='Autor', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_autor.place(x=140, y=60)
    bt_cliente = Button(cadt, width=10, text='Cliente', font=('', 12, 'bold'), fg='white', bg='#5bc30b', command=cliente)
    bt_cliente.place(x=140, y=100)
    bt_livro = Button(cadt, width=10, text='Livro', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_livro.place(x=140, y=140)
    bt_usuario = Button(cadt, width=10, text='Usuário', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_usuario.place(x=140, y=180)


def listar():
    global listr
    try:
        loged.destroy()
        logo2.destroy()
        listr.destroy()
        empr.destroy()
        cadt.destroy()
    except:
        pass
    listr = Frame(root, bg='#292929', width=400, height=300)
    listr.pack(fill=BOTH, expand=1)
    bt_autor = Button(listr, width=10, text='Autor', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_autor.place(x=140, y=60)
    bt_cliente = Button(listr, width=10, text='Cliente', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_cliente.place(x=140, y=100)
    bt_livro = Button(listr, width=10, text='Livro', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_livro.place(x=140, y=140)
    bt_usuario = Button(listr, width=10, text='Usuário', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_usuario.place(x=140, y=180)
    bt_emprestimo = Button(listr, width=10, text='Empréstimos', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_emprestimo.place(x=140, y=220)


def emprestimo():
    global empr
    try:
        loged.destroy()
        logo2.destroy()
        empr.destroy()
        cadt.destroy()
        listr.destroy()
    except:
        pass
    empr = Frame(root, bg='#292929', width=400, height=300)
    empr.pack(fill=BOTH, expand=1)
    bt_emprestimo = Button(empr, width=18, text='Realizar Empréstimo', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_emprestimo.place(x=110, y=80)
    bt_devolucao = Button(empr, width=18, text='Realizar Devolução', font=('', 12, 'bold'), fg='white', bg='#5bc30b')
    bt_devolucao.place(x=110, y=120)


def cliente():
    db = sqlite3.connect('registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cliente(
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    rua TEXT NOT NULL,
    numero INTEGER NOT NULL,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    data_de_nascimento DATE NOT NULL,
    telefone_residencial TEXT,
    telefone_celular TEXT NOT NULL,
    email TEXT NOT NULL,
    cpf TEXT NOT NULL
    );''')
    window_cliente = Toplevel(root, bg='#292929')
    window_cliente.title('Cadastrar Cliente')

    lnome = Label(window_cliente, text='Nome', bg='#292929', fg='white', font=('', 12, 'bold'))
    lnome.place(x=20, y=20)
    nome = Entry(window_cliente, width=45, font=('', 11, 'bold'))
    nome.place(x=20, y=50)

    lcpf = Label(window_cliente, text='CPF', bg='#292929', fg='white', font=('', 12, 'bold'))
    lcpf.place(x=20, y=80)
    cpf = Entry(window_cliente, width=12, font=('', 11, 'bold'))
    cpf.place(x=20, y=110)

    ltelefone = Label(window_cliente, text='Telefone', bg='#292929', fg='white', font=('', 12, 'bold'))
    ltelefone.place(x=150, y=80)
    telefone = Entry(window_cliente, width=12, font=('', 11, 'bold'))
    telefone.place(x=150, y=110)

    lcelular = Label(window_cliente, text='Celular', bg='#292929', fg='white', font=('', 12, 'bold'))
    lcelular.place(x=283, y=80)
    celular = Entry(window_cliente, width=12, font=('', 11, 'bold'))
    celular.place(x=283, y=110)

    lemail = Label(window_cliente, text='E-mail', bg='#292929', fg='white', font=('', 12, 'bold'))
    lemail.place(x=20, y=140)
    email = Entry(window_cliente, width=45, font=('', 11, 'bold'))
    email.place(x=20, y=170)

    lrua = Label(window_cliente, text='Rua', bg='#292929', fg='white', font=('', 12, 'bold'))
    lrua.place(x=20, y=200)
    rua = Entry(window_cliente, width=45, font=('', 11, 'bold'))
    rua.place(x=20, y=230)

    lnumero = Label(window_cliente, text='Número', bg='#292929', fg='white', font=('', 12, 'bold'))
    lnumero.place(x=300, y=260)
    numero = Entry(window_cliente, width=10, font=('', 11, 'bold'))
    numero.place(x=300, y=290)

    lbairro = Label(window_cliente, text='Bairro', bg='#292929', fg='white', font=('', 12, 'bold'))
    lbairro.place(x=20, y=260)
    bairro = Entry(window_cliente, width=31, font=('', 11, 'bold'))
    bairro.place(x=20, y=290)

    lcidade = Label(window_cliente, text='Cidade', bg='#292929', fg='white', font=('', 12, 'bold'))
    lcidade.place(x=20, y=320)
    cidade = Entry(window_cliente, width=23, font=('', 11, 'bold'))
    cidade.place(x=20, y=350)

    lestado = Label(window_cliente, text='Estado', bg='#292929', fg='white', font=('', 12, 'bold'))
    lestado.place(x=235, y=320)
    estado = Entry(window_cliente, width=18, font=('', 11, 'bold'))
    estado.place(x=235, y=350)

    window_cliente.geometry('400x550+200+200')
    db.commit()
    db.close()


root = Tk()

photo = PhotoImage(file='logo-biblioteca.png')
logo = Label(root, image=photo, bg='#292929')
logo.pack(pady=20)

label_user = Label(root, text='Usuário:', font=('', 12), fg='gray', bg='#292929')
label_user.place(x=30, y=120)
entry_user = Entry(root, justify=CENTER, font=('', 11, 'bold'), width=26)
entry_user.place(x=100, y=120)

label_password = Label(root, text='Senha:', font=('', 12), fg='gray', bg='#292929')
label_password.place(x=40, y=150)
entry_password = Entry(root, justify=CENTER, font=('', 11, 'bold'), show='*', width=26)
entry_password.place(x=100, y=150)

bt_login = Button(root, width=8, text='LOGIN', font=('', 12, 'bold'), bg='#5bc30b', fg='white', command=verify)
bt_login.place(x=100, y=200)
bt_leave = Button(root, width=8, text='SAIR', font=('', 12, 'bold'), bg='#5bc30b', fg='white', command=root.quit)
bt_leave.place(x=223, y=200)

root.title('Login')
root['bg'] = '#292929'
root.geometry('400x300+600+300')
root.resizable(0, 0)
root.mainloop()
