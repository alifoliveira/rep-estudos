# coding=utf-8

from tkinter import *
from tkinter import messagebox as ms
from datetime import datetime
import sqlite3

now = datetime.now()
photo2 = None
logo2 = None
cont = 0
cont2 = 2


# -=-=-=-=-=-=- Cadastro -=-=-=-=-=-=-


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
    cpf = Entry(window_cliente, width=13, font=('', 11, 'bold'))
    cpf.place(x=20, y=110)

    ltelefone = Label(window_cliente, text='Telefone:', bg='#292929', fg='white', font=('', 12, 'bold'))
    ltelefone.place(x=147, y=80)
    telefone = Entry(window_cliente, width=13, font=('', 11, 'bold'))
    telefone.place(x=147, y=110)

    lcelular = Label(window_cliente, text='Celular:', bg='#292929', fg='white', font=('', 12, 'bold'))
    lcelular.place(x=274, y=80)
    celular = Entry(window_cliente, width=13, font=('', 11, 'bold'))
    celular.place(x=274, y=110)

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

    bt_pesquisar = Button(window_cliente, width=8, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                          command=cliente2)
    bt_pesquisar.place(x=155, y=410)

    bt_cancelar = Button(window_cliente, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_cliente.destroy)
    bt_cancelar.place(x=292, y=410)

    window_cliente.geometry('400x500+200+200')


def cpf_cliente():
    global result, cpf_validate
    cpf_validate = cpf.get()
    mult = 10
    verif_1 = 0
    verif_2 = 0
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    find_cpf = 'SELECT * FROM cliente WHERE cpf = ?'
    c.execute(find_cpf, [(cpf.get())])
    result = c.fetchall()
    if result:
        cpf['bg'] = 'pink2'
    elif len(cpf_validate) != 11:
        cpf['bg'] = 'pink2'
    elif cpf_validate[0] == cpf_validate[1] and cpf_validate[1] == cpf_validate[2] and cpf_validate[2] == \
            cpf_validate[3] and cpf_validate[3] == cpf_validate[4] and \
            cpf_validate[4] == cpf_validate[5] and cpf_validate[5] == cpf_validate[6] and cpf_validate[6] == \
            cpf_validate[7] and cpf_validate[7] == cpf_validate[8] \
            and cpf_validate[8] == cpf_validate[9] and cpf_validate[9] == cpf_validate[10]:
        cpf['bg'] = 'pink2'
    elif cpf_validate[0:2] == cpf_validate[3:5] and cpf_validate[3:5] == cpf_validate[6:8]:
        cpf['bg'] = 'pink2'
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
                cpf['bg'] = 'white'
                return f'{cpf_validate}'
    db.close()


def nome_cliente():
    nome_validate = nome.get()
    if len(nome_validate) < 4:
        nome['bg'] = 'pink2'
    else:
        nome['bg'] = 'white'
        return nome.get()


def rua_cliente():
    rua_validate = rua.get()
    if len(rua_validate) < 4:
        rua['bg'] = 'pink2'
    else:
        rua['bg'] = 'white'
        return rua.get()


def numero_cliente():
    try:
        numero_test = int(numero.get())
        numero['bg'] = 'white'
        return numero.get()
    except:
        numero['bg'] = 'pink2'


def bairro_cliente():
    bairro_validade = bairro.get()
    if len(bairro_validade) < 4:
        bairro['bg'] = 'pink2'
    else:
        bairro['bg'] = 'white'
        return bairro.get()


def cidade_cliente():
    cidade_validade = cidade.get()
    if len(cidade_validade) < 4:
        cidade['bg'] = 'pink2'
    else:
        cidade['bg'] = 'white'
        return cidade.get()


def estado_cliente():
    estado_validade = estado.get()
    if len(estado_validade) < 4:
        estado['bg'] = 'pink2'
    else:
        estado['bg'] = 'white'
        return estado.get()


def nascimento_cliente():
    global dia, mes, ano
    data_validate = nascimento.get()
    try:
        nascimento_test = int(nascimento.get())
        dia = int(data_validate[:2])
        mes = int(data_validate[2:4])
        ano = int(data_validate[4:])
        if dia > 31:
            print('erro_dia')
            nascimento['bg'] = 'pink2'
        elif mes > 12:
            print('erro_mes')
            nascimento['bg'] = 'pink2'
        elif ano > 2018:
            print('erro_ano')
            nascimento['bg'] = 'pink2'
        elif len(data_validate) < 8:
            print('erro_formato')
            nascimento['bg'] = 'pink2'
        else:
            nascimento['bg'] = 'white'
            return f'{data_validate}'
    except Exception as erro:
        print(erro, '\n\n tipo, nascimento')
        pass


def telefone_cliente():
    telefone_validate = telefone.get()
    try:
        telefone_test = int(telefone.get())
        if len(telefone_validate) > 10:
            telefone['bg'] = 'white'
        else:
            telefone['bg'] = 'white'
            return f'({telefone_test})'
    except:
        return 'NULL'


def celular_cliente():
    celular_validate = celular.get()
    try:
        celular_test = int(celular.get())
        if len(celular_validate) < 11:
            celular['bg'] = 'pink2'
        else:
            celular['bg'] = 'white'
            return f'{celular_test}'
    except:
        pass


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


def salvar_cliente():
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cliente(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
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
        label_teste = Label(window_cliente, text='Cliente Salvo com Sucesso!', bg='#292929', fg='white')
        label_teste.place(x=100, y=480)
    except:
        update = '''UPDATE cliente SET nome = (?), rua = (?), numero = (?), bairro = (?), cidade = (?), estado = (?),
         nascimento = (?), telefone = (?), celular = (?), email = (?) WHERE cpf = (?)'''
        c.execute(update, [nome.get(), rua.get(), numero.get(), bairro.get(), cidade.get(), estado.get(),
                           nascimento.get(), telefone.get(), celular.get(), email.get(), cpf.get()])
        db.commit()
        c.close()
        label_teste = Label(window_cliente, text='Cliente Atualizado com Sucesso!', bg='#292929', fg='white')
        label_teste.place(x=100, y=480)
    nome.delete(0, 45)
    rua.delete(0, 31)
    numero.delete(0, 10)
    bairro.delete(0, 23)
    cidade.delete(0, 23)
    estado.delete(0, 18)
    nascimento.delete(0, 18)
    telefone.delete(0, 15)
    celular.delete(0, 15)
    email.delete(0, 45)
    cpf.delete(0, 15)
    db.close()


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

    bt_pesquisar = Button(window_autor, width=8, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                          command=autor2)
    bt_pesquisar.place(x=155, y=200)

    bt_cancelar = Button(window_autor, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_autor.destroy)
    bt_cancelar.place(x=292, y=200)

    window_autor.geometry('400x300+200+200')


def salvar_autor():
    global label_autor
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS autor(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
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
        label_autor = Label(window_autor, text='Autor já Cadastrado.', font=('', 10, 'bold'), bg='#292929', fg='white')
        label_autor.pack(side=BOTTOM)
        nome_autor['bg'] = 'pink2'
    elif len(nome_autor.get()) < 5:
        try:
            label_autor.destroy()
        except NameError:
            pass
        label_autor = Label(window_autor, text='Minino de 5 Caracteres', font=('', 10, 'bold'), bg='#292929',
                            fg='white')
        label_autor.pack(side=BOTTOM)
        nome_autor['bg'] = 'pink2'
    else:
        try:
            label_autor.destroy()
        except NameError:
            pass
        label_autor = Label(window_autor, text='Autor Cadastrado com Sucesso!',
                            font=('', 10, 'bold'), bg='#292929', fg='white')
        label_autor.pack(side=BOTTOM)
        nome_autor['bg'] = 'white'
        insert = 'INSERT INTO autor(nome) VALUES(?)'
        c.execute(insert, [(nome_autor.get())])
        db.commit()
    nome_autor.delete(0, 45)
    db.close()


def mostrar_livros():
    try:
        listbox_1.delete(0, END)
        connection = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
        c = connection.cursor()

        c.execute(f'select id from cliente where cpf = "{cpf.get()}"')
        for i in c.fetchall():
            x = i[0]

        global idbook, namebook
        teste = []
        c.execute(f'select * from cliente_livro where cliente = {x}')
        print(cpf.get())
        for i in c.fetchall():
            if 'Reservado' in i:
                teste.append(i)
        print(teste)
        idbook = []
        for i in teste:
            idbook.append(i[2])
        print(idbook)
        if len(idbook) == 0:
            listbox_1.insert(END, '                           ~NENHUM LIVRO CADASTRADO~')
        else:
            listbox_1.delete(0, END)
            namebook = []
            for i in idbook:
                c.execute(f'select titulo from Livro where id = "{i}"')
                for i in c:
                    for x in i:
                        namebook.append(x)
            print(namebook)
            for i in namebook:
                listbox_1.insert(END, i)
            global test_save
            test_save = 'perform_return'
            x = Button(root, text='Atualizar', command='')
            x.place(x=85, y=350, width=100, height=25)
    except:
        ms.showerror('Aviso', 'Cliente Não Encontrado')


def atualizar_emprestimo():
    connection = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = connection.cursor()
    valor2 = listbox_2.get(0, END)
    print(valor2)
    print('oi')
    idbook = []
    for i in valor2:
        c.execute(f'select id from livro where titulo = "{i}"')
        for x in c.fetchall():
            idbook.append(x[0])
    print(idbook)
    c.execute(f'select MAX(id) from cliente_livro where livro = "{idbook[0]}"')
    for i in c:
        for x in i:
            y = x
    c.execute(f'UPDATE Cliente_Livro SET devolvido = "Disponivel", data_hora_devolucao = "{now.ctime()}" where id = "{y}"')

    connection.commit()
    connection.close()
    ms.showinfo('Aviso', 'Devoluçõe(s) efetuada(s) com sucesso!')


def r_emprestimo():
    global entry_cpf_empr, entry_titulo_empr
    window_emprestimo = Toplevel(root, bg='#292929')
    window_emprestimo.title('Realizar Empréstimo')
    window_emprestimo.geometry('400x300+200+100')
    window_emprestimo.transient(root)
    window_emprestimo.focus_force()
    window_emprestimo.grab_set()
    empr_frame = Frame(window_emprestimo, bg='#292929')
    empr_frame.pack(fill=BOTH, expand=1)

    label_cpf_empr = Label(empr_frame, text='CPF:', font=('', 11, 'bold'), bg='#292929', fg='white')
    label_cpf_empr.place(x=20, y=40)

    entry_cpf_empr = Entry(empr_frame, width=40, font=('', 11, 'bold'))
    entry_cpf_empr.place(x=20, y=70)

    label_titulo_empr = Label(empr_frame, text='Título do Livro:', font=('', 11, 'bold'), bg='#292929',
                              fg='white')
    label_titulo_empr.place(x=20, y=100)

    entry_titulo_empr = Entry(empr_frame, width=40, font=('', 11, 'bold'))
    entry_titulo_empr.place(x=20, y=130)

    bt_cadastrat_empr = Button(empr_frame, width=10, text='Salvar', font=('', 12, 'bold'), bg='#5bc30b',
                               fg='white', command=salvar_emprestimo)
    bt_cadastrat_empr.place(x=20, y=260)

    bt_procurar_empr = Button(empr_frame, width=10, text='Procurar', font=('', 12, 'bold'), bg='#5bc30b',
                              fg='white', command=pesquisar_emprestimo)
    bt_procurar_empr.place(x=150, y=260)

    bt_cancelar_empr = Button(empr_frame, width=10, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b',
                              fg='white', command=window_emprestimo.destroy)
    bt_cancelar_empr.place(x=280, y=260)


def pesquisar_emprestimo():
    global cpf, listbox_1
    window_empr = Toplevel(root, bg='#292929')
    window_empr.title('Realizar Empréstimo')
    window_empr.transient(root)
    window_empr.focus_force()
    window_empr.grab_set()

    lcpf = Label(window_empr, text='CPF', bg='#292929', fg='grey', font=('', 12, 'bold'))
    lcpf.place(x=270, y=30)
    cpf = Entry(window_empr, width=45, font=('', 11, 'bold'))
    cpf.place(x=120, y=60)

    s = Scrollbar(window_empr)
    s.place(x=250, y=200, height=308)
    listbox_1 = Listbox(window_empr, yscrollcommand=s.set, width=30, height=16,
                      bg='grey35', fg='white', font=('', 11, 'bold'))
    listbox_1.place(x=10, y=200)
    s.config(command=listbox_1.yview)

    s2 = Scrollbar(window_empr)
    s2.place(x=573, y=200, height=308)
    listbox_2 = Listbox(window_empr, yscrollcommand=s2.set, width=30, height=16,
                        bg='grey35', fg='white', font=('', 11, 'bold'))
    listbox_2.place(x=331, y=200)
    s2.config(command=listbox_2.yview)

    connection = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = connection.cursor()
    dataname = []
    datasid = []
    dataidbook = []
    c.execute('select * from cliente_livro where devolvido = "Reservado"')
    for i in c.fetchall():
        datasid.append(i[2])
    c.execute('SELECT * FROM livro ')
    for i in c.fetchall():
        dataidbook.append(i[0])
        dataname.append(i[1])
    c.execute('SELECT * FROM livro ')
    for i in datasid:
        for v in dataidbook:
            if v == i:
                dataidbook.remove(v)
    print(dataidbook)

    dataname = []
    for i in dataidbook:
        c.execute(f'select titulo from livro where id = "{i}"')
        for y in c:
            dataname.append(y[0])
    print(dataname)
    connection.close()
    x = []
    c = 0

    for i in dataname:
        listbox_2.insert(END, f'Livro: {i}')

    bt_pesquisar = Button(window_empr, width=10, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                          command= mostrar_livros)
    bt_pesquisar.place(x=245, y=550)

    bt_cancelar = Button(window_empr, width=10, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_empr.destroy)
    bt_cancelar.place(x=385, y=550)

    window_empr.geometry('600x600+200+100')


def salvar_emprestimo():
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cliente_livro(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cliente INTEGER FK,
    livro INTEGER FK,
    data_hora_emprestimo DATETIME NOT NULL,
    data_hora_devolucao DATETIME,
    devolvido INTEGER NOT NULL
    );''')
    cpfteste = []
    c.execute('SELECT * FROM cliente')
    for i in c.fetchall():
        cpfteste.append(i[11])
    print(cpfteste)
    if entry_cpf_empr.get() in cpfteste:
        print('1')
        c.execute('SELECT * FROM cliente')
        data_cpf = None
        for i in c.fetchall():
            if entry_cpf_empr.get() in i:
                data_cpf = i[0]
        c.execute('SELECT * FROM livro')
        data_title = None
        for i in c.fetchall():
            if entry_titulo_empr.get() in i:
                data_title = i[0]
        c.execute(f'SELECT devolvido FROM cliente_livro WHERE cliente = "{entry_cpf_empr.get()}"')
        cont_empr = 0
        teste = True
        for i in c.fetchall():
            print(i, 'sdfsdf')
            if 'Reservado' in i:
                cont_empr += 1
            if cont_empr >= 5:
                ms.showinfo('Erro', 'Você já reservou 5 livros')
                teste = False
                break
        print(cont_empr)
        if teste == True:
            cont_empr = 0
            id_autor = []
            c.execute('SELECT * FROM livro')
            for i in c:
                print(i)
                if entry_titulo_empr.get() in i:
                    id_autor = i[0]
                cont_empr += 1
            print(id_autor)
            print(cont_empr)
            if cont_empr == 0:
                print('Entrada 1')
                date = now.ctime()
                c.execute(f'''INSERT INTO cliente_livro(cliente, livro, data_hora_emprestimo, data_hora, devolucao, 
                devolvido) VALUES("{data_cpf}","{data_title}","{date}","Não Informado", "Reservado")''')
                db.commit()
                db.close()
                print('oiadasds')
                ms.showinfo('Erro', 'Dados Salvos com Sucesso')
            else:
                c.execute('SELECT * FROM cliente_livro')
                data = []
                for i in c.fetchall():
                    for y in i:
                        data.append(y)
                    if data_title == data[2] and data[5] == 'Reservado':
                        ms.showinfo('Aviso', 'Livro Está Reservado')
                        teste = False
                        break
                    data = []
                if teste == True:
                    c.execute('SELECT * FROM cliente')
                    data_cpf = None
                    for i in c.fetchall():
                        if entry_cpf_empr.get() in i:
                            data_cpf = i[0]
                    c.execute('SELECT * FROM livro')
                    data_title = None
                    for i in c.fetchall():
                        if entry_titulo_empr.get() in i:
                            data_title = i[0]
                    date = now.ctime()
                    c.execute(f'''INSERT INTO cliente_livro(cliente, livro, data_hora_emprestimo, devolvido) 
                    VALUES("{data_cpf}", "{data_title}", "{date}", "Reservado")''')
                    db.commit()
                    db.close()
                    ms.showinfo('Aviso', 'Dados Salvos com Sucesso')
    else:
        ms.showinfo('Erro', 'CPF não Encontrado')
    entry_titulo_empr.delete(0, END)
    entry_cpf_empr.delete(0, END)


def r_devolucao():
    global cpf, listbox_1, listbox_2
    window_devolucao = Toplevel(root, bg='#292929')
    window_devolucao.title('Realizar Devolução')
    window_devolucao.transient(root)
    window_devolucao.focus_force()
    window_devolucao.grab_set()

    ld_cpf = Label(window_devolucao, text='CPF', bg='#292929', fg='grey', font=('', 12, 'bold'))
    ld_cpf.place(x=270, y=30)
    cpf = Entry(window_devolucao, width=45, font=('', 11, 'bold'), justify=CENTER)
    cpf.place(x=120, y=60)

    s = Scrollbar(window_devolucao)
    s.place(x=250, y=200, height=308)
    listbox_1 = Listbox(window_devolucao, yscrollcommand=s.set, width=30, height=16,
                      bg='grey35', fg='white', font=('', 11, 'bold'))
    listbox_1.place(x=10, y=200)
    s.config(command=listbox_1.yview)

    s2 = Scrollbar(window_devolucao)
    s2.place(x=573, y=200, height=308)
    listbox_2 = Listbox(window_devolucao, yscrollcommand=s2.set, width=30, height=16,
                        bg='grey35', fg='white', font=('', 11, 'bold'))
    listbox_2.place(x=331, y=200)
    s2.config(command=listbox_2.yview)

    bt_seta1 = Button(window_devolucao, text='>>', font=('', 12, 'bold'), bg='grey', fg='black', width=5, height=2,
                      command=seta_1)
    bt_seta1.place(x=270, y=300)

    bt_seta2 = Button(window_devolucao, text='<<', font=('', 12, 'bold'), bg='grey', fg='black', width=5, height=2,
                      command=seta_2)
    bt_seta2.place(x=270, y=400)

    bt_salvar = Button(window_devolucao, width=10, text='Atualizar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command= salvar_devolucao)
    bt_salvar.place(x=100, y=550)

    bt_pesquisar = Button(window_devolucao, width=10, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                          command=mostrar_livros)
    bt_pesquisar.place(x=245, y=550)

    bt_cancelar = Button(window_devolucao, width=10, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_devolucao.destroy)
    bt_cancelar.place(x=385, y=550)

    window_devolucao.geometry('600x600+200+100')




def salvar_devolucao():
    connection = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = connection.cursor()
    valor2 = listbox_2.get(0, END)
    print(valor2)
    print('oi')
    idbook = []
    for i in valor2:
        c.execute(f'select id from livro where titulo = "{i}"')
        for x in c.fetchall():
            idbook.append(x[0])
    print(idbook)
    c.execute(f'select MAX(id) from cliente_livro where livro = "{idbook[0]}"')
    for i in c:
        for x in i:
            y = x
    c.execute(f'UPDATE Cliente_Livro SET devolvido = "Disponivel", data_hora_devolucao = "{now.ctime()}" where id = "{y}"')

    connection.commit()
    connection.close()
    ms.showinfo('Aviso', 'Devoluçõe(s) efetuada(s) com sucesso!')


def livro():
    global titulo, paginas, window_livro, bt_seta1, bt_seta2, listbox_1, listbox_2
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS livro_autor(
    id_livro_autor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_livro TEXT NOT NULL, 
    id_autor TEXT NOT NULL,
    FOREIGN KEY(id_livro) REFERENCES livro(id),
    FOREIGN KEY(id_autor) REFERENCES autor(id)
    );''')

    window_livro = Toplevel(root, bg='#292929')
    window_livro.title('Cadastrar Livro')
    window_livro.transient(root)
    window_livro.focus_force()
    window_livro.grab_set()

    ltitulo = Label(window_livro, text='Titulo do Livro:', bg='#292929', fg='grey', font=('', 12, 'bold'))
    ltitulo.place(x=240, y=30)
    titulo = Entry(window_livro, width=45, font=('', 11, 'bold'))
    titulo.place(x=120, y=60)

    lpaginas = Label(window_livro, text='Nº de Páginas:', bg='#292929', fg='grey', font=('', 12, 'bold'))
    lpaginas.place(x=245, y=110)
    paginas = Entry(window_livro, width=15, font=('', 11, 'bold'))
    paginas.place(x=240, y=140)

    s = Scrollbar(window_livro)
    s.place(x=250, y=200, height=308)
    listbox_1 = Listbox(window_livro, yscrollcommand=s.set, width=30, height=16,
                      bg='grey35', fg='white', font=('', 11, 'bold'))
    listbox_1.place(x=10, y=200)
    s.config(command=listbox_1.yview)

    s2 = Scrollbar(window_livro)
    s2.place(x=573, y=200, height=308)
    listbox_2 = Listbox(window_livro, yscrollcommand=s2.set, width=30, height=16,
                        bg='grey35', fg='white', font=('', 11, 'bold'))
    listbox_2.place(x=331, y=200)
    s2.config(command=listbox_2.yview)

    bt_seta1 = Button(window_livro,  text='>>', font=('', 12, 'bold'), bg='grey', fg='black', width=5, height=2,
                      command=seta_1)
    bt_seta1.place(x=270, y=300)

    bt_seta2 = Button(window_livro,  text='<<', font=('', 12, 'bold'), bg='grey', fg='black', width=5, height=2,
                      command=seta_2)
    bt_seta2.place(x=270, y=400)

    bt_salvar = Button(window_livro, width=10, text='Salvar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command=salvar_livro)
    bt_salvar.place(x=100, y=550)

    bt_pesquisar = Button(window_livro, width=10, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                          command=livro2)
    bt_pesquisar.place(x=245, y=550)

    bt_cancelar = Button(window_livro, width=10, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_livro.destroy)
    bt_cancelar.place(x=385, y=550)

    window_livro.geometry('600x600+200+100')

    c.execute('SELECT nome FROM autor')
    x = c.fetchall()
    for i in x:
        listbox_1.insert(END, i[0])
    db.close()


def seta_1():
    try:
        listbox_1.insert(listbox_1.curselection())
        listbox_2.insert(END, (listbox_1.get(listbox_1.curselection())))
        listbox_1.delete(listbox_1.curselection())
    except:
        pass


def seta_2():
    try:
        listbox_2.insert(listbox_2.curselection())
        listbox_1.insert(END, (listbox_2.get(listbox_2.curselection())))
        listbox_2.delete(listbox_2.curselection())
    except:
        pass


def salvar_livro():
    global valor, valor2,titulo
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS livro(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    paginas INTEGER NOT NULL
    );''')
    c = db.cursor()
    c.execute("SELECT titulo FROM livro WHERE titulo = '%s';" % titulo.get())
    x = c.fetchone()
    if x is None:
        print('entrou')
        inserir = '''INSERT INTO livro(titulo, paginas) VALUES(?, ?)'''
        c.execute(inserir, [titulo.get(), paginas.get()])
        db.commit()

    else:
        print(x)
        update = 'UPDATE livro SET paginas = (?) WHERE titulo = (?)'
        c.execute(update, [(paginas.get()), (titulo.get())])
        db.commit()
        titulo['bg'] = 'white'
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    dl2 = []
    valor2 = listbox_2.get(0, END)
    for i in valor2:
        c.execute(f'select * from autor where nome = "{i}"')
        x = c.fetchall()
        if x[0] in dl2:
            pass
        else:
            dl2.append(x[0])
    c.execute('select * from livro')
    valor = []
    for i in c:
        valor.append(i)
    for i in range(len(valor)):
        if i == len(valor) - 1:
            valor = valor[i]
    teste = dl2
    print(teste)
    print(valor[0])
    c.execute(f'DELETE FROM livro_autor where id_livro = "{valor[0]}"')
    for i in teste:
        c.execute(f'insert into livro_autor(id_livro, id_autor) values("{valor[0]}", "{i[0]}");')

    db.commit()
    db.close()

    ms.showinfo('Aviso', 'Dados salvos com sucesso')

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

    bt_pesquisar = Button(window_usuario, width=8, text='Pesquisar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                          command=usuario2)
    bt_pesquisar.place(x=155, y=200)

    bt_cancelar = Button(window_usuario, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=window_usuario.destroy)
    bt_cancelar.place(x=292, y=200)

    window_usuario.geometry('400x300+200+200')


def usuario2():
    global pesq_usuario, win_pesq_usuario, frame_usuario
    win_pesq_usuario = Toplevel(root, bg='#292929')
    win_pesq_usuario.title('Pesquisar Usuario')
    win_pesq_usuario.geometry('400x300+200+200')
    win_pesq_usuario.transient(window_usuario)
    win_pesq_usuario.focus_force()
    win_pesq_usuario.grab_set()

    lpesq_usuario = Label(win_pesq_usuario, text='Pesquisar Usuário:', font=('', 12), fg='gray', bg='#292929')
    lpesq_usuario.place(x=130, y=100)
    pesq_usuario = Entry(win_pesq_usuario, justify=CENTER, font=('', 11, 'bold'), width=26)
    pesq_usuario.place(x=90, y=130)

    bt_select = Button(win_pesq_usuario, width=8, text='Selecionar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command=pesquisar_usuario)
    bt_select.place(x=90, y=200)

    bt_cancelar = Button(win_pesq_usuario, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=win_pesq_usuario.destroy)
    bt_cancelar.place(x=213, y=200)


def login_usuario():
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    find_user = 'SELECT * FROM usuario WHERE login = ?'
    c.execute(find_user, [(user.get())])
    usuario_test = c.fetchall()
    if usuario_test:
        user['bg'] = 'pink2'
    elif len(user.get()) < 4:
        user['bg'] = 'pink2'
    else:
        user['bg'] = 'white'
        return user.get()
    db.close()


def senha_usuario():
    if len(senha.get()) < 4:
        senha['bg'] = 'pink2'
    else:
        senha['bg'] = 'white'
        return senha.get()


def salvar_usuario():
    salvar_login = login_usuario()
    salvar_senha = senha_usuario()
    print(salvar_login, salvar_senha)
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuario(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL,
    senha TEXT NOT NULL 
    );''')
    try:
        insert = 'INSERT INTO usuario(login, senha) VALUES(?, ?)'
        c.execute(insert, [salvar_login, salvar_senha])
        db.commit()
    except:
        update = 'UPDATE usuario SET senha = (?) WHERE login = (?)'
        c.execute(update, [(senha.get()), (user.get())])
        db.commit()
        c.close()
        user['bg'] = 'white'
    user.delete(0, 26)
    senha.delete(0, 26)
    db.close()


def pesquisar_usuario():
    user.delete(0, 26)
    senha.delete(0, 26)
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    pesquisar = 'SELECT login, senha FROM usuario WHERE login = (?)'
    c.execute(pesquisar, [pesq_usuario.get()])
    data = c.fetchall()
    for i in data:
        if pesq_usuario.get() in i:
            user.insert(END, i[0])
            senha.insert(END, i[1])
    db.commit()
    db.close()
    win_pesq_usuario.destroy()


# ----------PESQUISAR--------------


def autor2():
    global pesq_autor, win_pesq_autor
    win_pesq_autor = Toplevel(root, bg='#292929')
    win_pesq_autor.title('Pesquisar Autor')
    win_pesq_autor.geometry('400x300+200+200')
    win_pesq_autor.transient(window_autor)
    win_pesq_autor.focus_force()
    win_pesq_autor.grab_set()

    lpesq_autor = Label(win_pesq_autor, text='Pesquisar Autor:', font=('', 12), fg='gray', bg='#292929')
    lpesq_autor.place(x=130, y=100)
    pesq_autor = Entry(win_pesq_autor, justify=CENTER, font=('', 11, 'bold'), width=26)
    pesq_autor.place(x=90, y=130)

    bt_select = Button(win_pesq_autor, width=8, text='Selecionar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command=pesquisar_autor)
    bt_select.place(x=90, y=200)

    bt_cancelar = Button(win_pesq_autor, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=win_pesq_autor.destroy)
    bt_cancelar.place(x=213, y=200)

def pesquisar_autor():
    nome_autor.delete(0, 45)

    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    pesquisar = 'SELECT nome FROM autor WHERE nome = (?)'
    c.execute(pesquisar, [pesq_autor.get()])
    x = c.fetchall()
    for i in x:
        if pesq_autor.get() in i:
            nome_autor.insert(END, i[0])
    win_pesq_autor.destroy()
    db.close()


def cliente2():
    global pesq_cliente, win_pesq_cliente
    win_pesq_cliente = Toplevel(root, bg='#292929')
    win_pesq_cliente.title('Pesquisar Cliente')
    win_pesq_cliente.geometry('400x300+200+200')
    win_pesq_cliente.transient(window_cliente)
    win_pesq_cliente.focus_force()
    win_pesq_cliente.grab_set()

    lpesq_cliente = Label(win_pesq_cliente, text='Pesquisar Cliente:', font=('', 12), fg='gray', bg='#292929')
    lpesq_cliente.place(x=130, y=100)
    pesq_cliente = Entry(win_pesq_cliente, justify=CENTER, font=('', 11, 'bold'), width=26)
    pesq_cliente.place(x=90, y=130)

    bt_select = Button(win_pesq_cliente, width=8, text='Selecionar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command=pesquisar_cliente)
    bt_select.place(x=90, y=200)

    bt_cancelar = Button(win_pesq_cliente, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=win_pesq_cliente.destroy)
    bt_cancelar.place(x=213, y=200)


def pesquisar_cliente():
    nome.delete(0, END)
    rua.delete(0, END)
    numero.delete(0, END)
    bairro.delete(0, END)
    cidade.delete(0, END)
    estado.delete(0, END)
    nascimento.delete(0, END)
    telefone.delete(0, END)
    celular.delete(0, END)
    email.delete(0, END)
    cpf.delete(0, END)

    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    pesquisar = '''SELECT nome, rua, numero, bairro, cidade, estado, nascimento, telefone, celular, email, cpf
     FROM cliente WHERE cpf = (?)'''
    c.execute(pesquisar, [pesq_cliente.get()])
    x = c.fetchall()

    for i in x:
        if pesq_cliente.get() in i:
            nome.insert(END, i[0])
            rua.insert(END, i[1])
            numero.insert(END, i[2])
            bairro.insert(END, i[3])
            cidade.insert(END, i[4])
            estado.insert(END, i[5])
            nascimento.insert(END, i[6])
            celular.insert(END, i[8])
            email.insert(END, i[9])
            cpf.insert(END, i[10])
            telefone.insert(END, i[7])
    win_pesq_cliente.destroy()
    db.close()


def livro2():
    global pesq_livro, win_pesq_livro, teste_update
    win_pesq_livro = Toplevel(root, bg='#292929')
    win_pesq_livro.title('Pesquisar Livro')
    win_pesq_livro.geometry('400x300+200+200')
    win_pesq_livro.transient(window_livro)
    win_pesq_livro.focus_force()
    win_pesq_livro.grab_set()
    teste_update = 'update'

    lpesq_livro = Label(win_pesq_livro, text='Pesquisar Livro:', font=('', 12), fg='gray', bg='#292929')
    lpesq_livro.place(x=130, y=100)
    pesq_livro = Entry(win_pesq_livro, justify=CENTER, font=('', 11, 'bold'), width=26)
    pesq_livro.place(x=90, y=130)

    bt_select = Button(win_pesq_livro, width=8, text='Selecionar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                       command=pesquisar_livro)
    bt_select.place(x=90, y=200)

    bt_cancelar = Button(win_pesq_livro, width=8, text='Cancelar', font=('', 12, 'bold'), bg='#5bc30b', fg='white',
                         command=win_pesq_livro.destroy)
    bt_cancelar.place(x=213, y=200)


def pesquisar_livro():
    titulo.delete(0, 45)
    paginas.delete(0, 12)
    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    pesquisar = 'SELECT titulo, paginas FROM livro WHERE titulo = (?)'
    c.execute(pesquisar, [pesq_livro.get()])
    data = c.fetchall()
    for i in data:
        if pesq_livro.get() in i:
            titulo.insert(END, i[0])
            paginas.insert(END, i[1])
    win_pesq_livro.destroy()
    db.close()


 # -=-=-=-=-=-=- Listar =-=-=-=-=-=-=-


def listar_autor():
    window_listar_autor = Toplevel()
    window_listar_autor.title('Listar Autor')
    window_listar_autor.geometry('400x300+200+200')
    window_listar_autor.transient(root)
    window_listar_autor.focus_force()
    window_listar_autor.grab_set()

    s = Scrollbar(window_listar_autor)
    s.pack(side=RIGHT, fill=Y)

    listbox_1 = Listbox(window_listar_autor, yscrollcommand=s.set, bg='#292929', fg='white', font=('', 11, 'bold'))
    listbox_1.pack(side=LEFT, fill=BOTH, expand=1)
    s.config(command=listbox_1.yview)

    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('SELECT * FROM autor')
    x = c.fetchall()

    for i in x:
        listbox_1.insert(END, f'ID:  {i[0]}')
        listbox_1.insert(END, f'Nome do Autor:  {i[1]}')
        listbox_1.insert(END, '\n\n')
    db.close()


def listar_cliente():
    window_listar_cliente = Toplevel()
    window_listar_cliente.title('Listar Cliente')
    window_listar_cliente.geometry('400x300+200+200')
    window_listar_cliente.transient(root)
    window_listar_cliente.focus_force()
    window_listar_cliente.grab_set()

    s = Scrollbar(window_listar_cliente)
    s.pack(side=RIGHT, fill=Y)

    listbox_1 = Listbox(window_listar_cliente, yscrollcommand=s.set, bg='#292929', fg='white', font=('', 11, 'bold'))
    listbox_1.pack(side=LEFT, fill=BOTH, expand=1)
    s.config(command=listbox_1.yview)

    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('SELECT * FROM cliente')
    x = c.fetchall()
    for i in x:
        listbox_1.insert(END, f'ID:  {i[0]}')
        listbox_1.insert(END, f'Nome:  {i[1]}')
        listbox_1.insert(END, f'Rua:  {i[2]}')
        listbox_1.insert(END, f'Número da Casa:  {i[3]}')
        listbox_1.insert(END, f'Bairro:  {i[4]}')
        listbox_1.insert(END, f'Cidade:  {i[5]}')
        listbox_1.insert(END, f'Estado:  {i[6]}')
        listbox_1.insert(END, f'Data de Nascimento:  {i[7]}')
        listbox_1.insert(END, f'Telefone:  {i[8]}')
        listbox_1.insert(END, f'Celular:  {i[9]}')
        listbox_1.insert(END, f'E-mail:  {i[10]}')
        listbox_1.insert(END, f'CPF:  {i[11]}')
        listbox_1.insert(END, '\n\n')
    db.close()


def listar_livro():
    window_listar_livro = Toplevel()
    window_listar_livro.title('Listar Livro')
    window_listar_livro.geometry('400x300+200+200')
    window_listar_livro.transient(root)
    window_listar_livro.focus_force()
    window_listar_livro.grab_set()

    s = Scrollbar(window_listar_livro)
    s.pack(side=RIGHT, fill=Y)

    listbox_1 = Listbox(window_listar_livro, yscrollcommand=s.set, bg='#292929', fg='white', font=('', 11, 'bold'))
    listbox_1.pack(side=LEFT, fill=BOTH, expand=1)
    s.config(command=listbox_1.yview)

    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('SELECT * FROM livro')
    x = c.fetchall()
    for i in x:
        listbox_1.insert(END, f'ID:  {i[0]}')
        listbox_1.insert(END, f'Título do Livro:  {i[1]}')
        listbox_1.insert(END, f'Número de Páginas:  {i[2]}')
        listbox_1.insert(END, '\n\n')
    db.close()


def listar_usuario():
    window_listar_usuario = Toplevel()
    window_listar_usuario.title('Listar Usuários')
    window_listar_usuario.geometry('400x300+200+200')
    window_listar_usuario.transient(root)
    window_listar_usuario.focus_force()
    window_listar_usuario.grab_set()

    s = Scrollbar(window_listar_usuario)
    s.pack(side=RIGHT, fill=Y)

    listbox_1 = Listbox(window_listar_usuario, yscrollcommand=s.set, bg='#292929', fg='white', font=('', 11, 'bold'))
    listbox_1.pack(side=LEFT, fill=BOTH, expand=1)
    s.config(command=listbox_1.yview)

    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('SELECT * FROM usuario')
    x = c.fetchall()
    for i in x:
        listbox_1.insert(END, f'ID:  {i[0]}')
        listbox_1.insert(END, f'Login:  {i[1]}')
        listbox_1.insert(END, f'Senha:  {i[2]}')
        listbox_1.insert(END, '\n\n')
    db.close()


def listar_emprestimos():
    window_listar_emprestimos = Toplevel(root)
    window_listar_emprestimos.title('Listar Empréstimos')
    window_listar_emprestimos.geometry('400x300+200+200')
    window_listar_emprestimos.transient(root)
    window_listar_emprestimos.focus_force()
    window_listar_emprestimos.grab_set()

    s = Scrollbar(window_listar_emprestimos)
    s.pack(side=RIGHT, fill=Y)

    listbox_1 = Listbox(window_listar_emprestimos, yscrollcommand=s.set, bg='#292929', fg='white', font=('', 11, 'bold'))
    listbox_1.pack(side=LEFT, fill=BOTH, expand=1)
    s.config(command=listbox_1.yview)

    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('SELECT cliente, livro, data_hora_emprestimo FROM cliente_livro')
    for i in c:
        listbox_1.insert(END, f'Cliente: {i[0]}')
        listbox_1.insert(END, f'Livro: {i[1]}')
        listbox_1.insert(END, f'Data de Empréstimo: {i[2]}')
        listbox_1.insert(END, '\n\n')
    db.close()


def listar_devolucoes():
    window_listar_devolucoes = Toplevel(root)
    window_listar_devolucoes.title('Listar Devoluções')
    window_listar_devolucoes.geometry('400x300+200+200')
    window_listar_devolucoes.transient(root)
    window_listar_devolucoes.focus_force()
    window_listar_devolucoes.grab_set()

    s = Scrollbar(window_listar_devolucoes)
    s.pack(side=RIGHT, fill=Y)

    listbox_1 = Listbox(window_listar_devolucoes, yscrollcommand=s.set, bg='#292929', fg='white', font=('', 11, 'bold'))
    listbox_1.pack(side=LEFT, fill=BOTH, expand=1)
    s.config(command=listbox_1.yview)

    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('SELECT cliente, livro, data_hora_devolucao, devolvido FROM cliente_livro')
    for i in c:
        listbox_1.insert(END, f'Cliente: {i[0]}')
        listbox_1.insert(END, f'Livro: {i[1]}')
        listbox_1.insert(END, f'Data da Devolução: {i[2]}')
        listbox_1.insert(END, f'Situação: {i[3]}')
        listbox_1.insert(END, '\n\n')
    db.close()


def listar_emprestimo():
    window_listar_emprestimo = Toplevel(root)
    window_listar_emprestimo.title('Listar Empréstimos')
    window_listar_emprestimo.geometry('400x300+200+200')
    window_listar_emprestimo.transient(root)
    window_listar_emprestimo.focus_force()
    window_listar_emprestimo.grab_set()

    s = Scrollbar(window_listar_emprestimo)
    s.pack(side=RIGHT, fill=Y)

    listbox_1 = Listbox(window_listar_emprestimo, yscrollcommand=s.set, bg='#292929', fg='white', font=('', 11, 'bold'))
    listbox_1.pack(side=LEFT, fill=BOTH, expand=1)
    s.config(command=listbox_1.yview)

    db = sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db')
    c = db.cursor()
    c.execute('SELECT livro FROM cliente_livro WHERE devolvido = "Reservado"')
    for i in c:
        listbox_1.insert(END, f'Livro Emprestado: {i[0]}')
    db.close()

# -=-=-=-=-=-=- Login -=-=-=-=-=-=-


def menu_bar():
    barra_menu = Menu(root)
    main_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Cadastrar', menu=main_menu)
    main_menu.add_command(label='Autor', command=autor)
    main_menu.add_command(label='Cliente', command=cliente)
    main_menu.add_command(label='Livro', command=livro)
    main_menu.add_command(label='Usuário', command=usuario)

    main_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Listar', menu=main_menu)
    main_menu.add_command(label='Autores', command=listar_autor)
    main_menu.add_command(label='Clientes', command=listar_cliente)
    main_menu.add_command(label='Livros', command=listar_livro)
    main_menu.add_command(label='Usuários', command=listar_usuario)
    main_menu.add_command(label='Empréstimos', command=listar_emprestimos)
    main_menu.add_command(label='Devoluções', command=listar_devolucoes)
    main_menu.add_command(label='Livros em situação de empréstimo', command=listar_emprestimo)

    main_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Empréstimo', menu=main_menu)
    main_menu.add_command(label='Realizar Empréstimo', command=r_emprestimo)
    main_menu.add_command(label='Realizar Devolução', command=r_devolucao)

    main_menu = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Sair', menu=main_menu)
    main_menu.add_command(label='Sair', command=root.destroy)
    root.config(menu=barra_menu)


def verify():
    global cont, cont2, photo2, logo2, label_error, frame_logado
    frame_logado = Frame(root, bg='#292929')
    with sqlite3.connect('2_Periodo/Trabalho_3/BibliotecaMeta/data/Registro.db') as db:
        c = db.cursor()
        find_user = 'SELECT * FROM usuario WHERE login = ? AND senha = ?'
        c.execute(find_user, [(entry_user.get()), (entry_password.get())])
        login_test = c.fetchall()
        if login_test:
            frame_login.destroy()
            frame_logado.pack(fill=BOTH, expand=1)
            photo2 = PhotoImage(file='2_Periodo/Trabalho_3/BibliotecaMeta/data/logo-biblioteca-menu.png')
            logo2 = Label(frame_logado, image=photo2, bg='#292929')
            logo2.pack(padx=25, pady=50)
            label_login = Label(frame_logado, text='[Logado]', font=('', 16, 'bold'), bg='#292929', fg='white')
            label_login.pack(side=BOTTOM)
            menu_bar()
        else:
            label_error = Label(frame_login, text=f'Usuário ou Senha Inválidos ({cont2})', bg='#292929', fg='white')
            label_error.place(x=130, y=280)
            entry_user['bg'] = 'pink2'
            entry_password['bg'] = 'pink2'
            cont2 -= 1
            cont += 1

            if cont == 3:
                ms.showwarning('Aviso', 'O Sistema será finalizado por questões de segurança.')
                root.destroy()


def master():
    global entry_user, entry_password, photo, frame_login
    frame_login = Frame(root, bg='#292929')
    frame_login.pack(fill=BOTH, expand=1)
    photo = PhotoImage(file='2_Periodo/Trabalho_3/BibliotecaMeta/data/logo-biblioteca.png')
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


root = Tk()

master()

root.title('Login')
root['bg'] = '#292929'
root.geometry('400x300+600+300')
root.resizable(0, 0)
root.mainloop()
