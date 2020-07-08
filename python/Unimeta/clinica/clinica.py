from tkinter import *
import db
import sqlite3
import pycep_correios
# from validacoes import *
from tkinter import messagebox as mb



janela = Tk()
janela.title('Veterinario')
janela.geometry('350x350+200+100')
janela.resizable(width=False, height=False)


photo2 = PhotoImage(file='logo.png')
logo2 = Label(janela, image=photo2, bg='#292929')
logo2.pack(padx=0, pady=0)
loged = Label(janela, text='Seja Bem Vindo!', font=('', 20, 'bold'), bg='#3CB371', fg='white', pady=20)
loged.pack(side=BOTTOM, fill=X)


class Interface():
    # Cria menu de Subjanelas
    def __init__(self):
        barra_menu = Menu(janela)
        menu_arquivo = Menu(barra_menu, tearoff=0)
        menu_arquivo.add_command(label='Pessoa', command=Pessoa)
        menu_arquivo.add_command(label='Animal', command=Animal)
        menu_arquivo.add_command(label='Veterinário', command=Veterinario)
        barra_menu.add_cascade(label='Cadastrar', menu=menu_arquivo)

        menu_consulta = Menu(barra_menu, tearoff=0)
        menu_consulta.add_command(label='Agendar Consulta', command=Consulta)
        barra_menu.add_cascade(label='Consulta', menu=menu_consulta)

        menu_exame = Menu(barra_menu, tearoff=0)
        menu_exame.add_command(label='Marcar Exame', command=Exame)
        barra_menu.add_cascade(label='Exame', menu=menu_exame)

        barra_menu.add_cascade(label='Sair', command=janela.destroy)
        janela.config(menu=barra_menu)


class Label_Entry():
    # Cria Label e Entrys
    def __init__(self, tela, titulo, linha, coluna, tamanho, linha1, coluna1):
        self.tela = tela
        self.titulo = titulo
        self.linha = linha
        self.coluna = coluna
        self.linha1 = linha1
        self.coluna1 = coluna1
        self.label = Label(tela, text= titulo)
        self.label.grid(row=linha, column=coluna, padx=10, pady=5, sticky=W)
        self.entry = Entry(tela, width = tamanho)
        self.entry.grid(row = linha1, column = coluna1, padx=10, pady=5)


class Botao():
    # Cria Botões
    def __init__(self, tela, titulo,comando, linha,coluna):
        self.tela = tela
        self.titulo = titulo
        self.comando = comando
        self.linha = linha
        self.column = coluna
        self.botao = Button(tela, text=titulo, width=8, command=comando)
        self.botao.place(x=linha, y=coluna)


class Pessoa():
    # Cria subjanela Pessoa
    def __init__(self):
        self.pessoa = Toplevel()
        self.pessoa.title('Cadastrar Pessoa')
        self.pessoa.geometry('350x370+200+100')
        self.pessoa.transient(janela)
        self.pessoa.focus_force()
        self.pessoa.grab_set()
        self.pessoa.resizable(width=False, height=False)
        self.nome = Label_Entry(self.pessoa, 'Nome: ', 0, 0, 30, 0, 1)
        self.telefone = Label_Entry(self.pessoa,'Telefone: ', 1, 0, 30, 1, 1)
        self.email = Label_Entry(self.pessoa,'Email: ', 2, 0, 30, 2, 1)
        self.cep = Label_Entry(self.pessoa,'CEP: ', 3, 0, 30, 3, 1)
        self.n_casa = Label_Entry(self.pessoa,'Número da Casa: ', 4, 0, 30, 4, 1)
        self.s = Botao(self.pessoa,'Salvar',self.salvar,20,200)
        self.p = Botao(self.pessoa,'Pesquisar',self.pesquisar,100,200)
        self.a = Botao(self.pessoa,'Alterar',self.alterar,180,200)
        self.d = Botao(self.pessoa,'Deletar',self.deletar,260, 200)


    def salvar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.s = 'SELECT nome FROM cliente WHERE nome = (?)'
        self.conexao.execute(self.s, [self.nome.entry.get()])
        self.banco = self.conexao.fetchall()
        if self.banco:
            mb.showinfo('Erro', 'Pessoa já Cadastrada')
        elif validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito curto')
        elif validar_tel(self.telefone.entry.get()):
            mb.showinfo('Erro', 'Telefone incorreto')
        elif validar_email(self.email.entry.get()):
            mb.showinfo('Erro', 'E-mail incorreto')
        elif validar_cep(self.cep.entry.get()):
            mb.showinfo('Erro', 'CEP Incorreto')
        elif validar_numero(self.n_casa.entry.get()):
            mb.showinfo('Erro', 'Número da casa Inválido')
        else:
            self.conexao.execute("Insert into cliente(nome, telefone, email, cep, numero) values ('%s','%s','%s','%s','%s')"% (self.nome.entry.get(), self.telefone.entry.get(), self.email.entry.get(), self.cep.entry.get(), self.n_casa.entry.get()))
            print('Pessoa salva com sucesso')
        self.c.commit()
        self.c.close()
        self.nome.entry.delete(0, END)
        self.telefone.entry.delete(0, END)
        self.email.entry.delete(0, END)
        self.cep.entry.delete(0, END)
        self.n_casa.entry.delete(0, END)
    

    def pesquisar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.pesquisa = 'SELECT nome, telefone, email, cep, numero FROM cliente WHERE nome = (?)'
        self.conexao.execute(self.pesquisa, [self.nome.entry.get()])
        self.data = self.conexao.fetchall()
        for i in self.data:
            if self.nome.entry.get() in i:
                self.nome.entry.delete(0, 40)
                self.nome.entry.insert(END, i[0])
                self.salva = i[0]
                self.telefone.entry.insert(END, i[1])
                self.email.entry.insert(END, i[2])
                self.cep.entry.insert(END, i[3])
                self.n_casa.entry.insert(END, i[4])
        self.c.commit()
        self.c.close()
    

    def alterar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        if validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito curto')
        elif validar_tel(self.telefone.entry.get()):
            mb.showinfo('Erro', 'Telefone incorreto')
        elif validar_email(self.email.entry.get()):
            mb.showinfo('Erro', 'E-mail incorreto')
        elif validar_cep(self.cep.entry.get()):
            mb.showinfo('Erro', 'CEP Incorreto')
        elif validar_numero(self.n_casa.entry.get()):
            mb.showinfo('Erro', 'Número da casa Inválido')
        else:
            self.altera = 'UPDATE cliente set nome = (?), telefone = (?), email = (?), cep = (?), numero = (?) where nome = (?)'
            self.conexao.execute(self.altera, [self.nome.entry.get(), self.telefone.entry.get(), self.email.entry.get(), self.cep.entry.get(), self.n_casa.entry.get(), self.salva])
            self.c.commit()
            self.c.close()
            self.nome.entry.delete(0, END)
            self.telefone.entry.delete(0, END)
            self.email.entry.delete(0, END)
            self.cep.entry.delete(0, END)
            self.n_casa.entry.delete(0, END)


    def deletar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.deleta = 'Delete from cliente where nome = (?)'
        self.conexao.execute(self.deleta, [self.nome.entry.get()])
        self.c.commit()
        self.c.close()
        self.nome.entry.delete(0, END)
        self.telefone.entry.delete(0, END)
        self.email.entry.delete(0, END)
        self.cep.entry.delete(0, END)
        self.n_casa.entry.delete(0, END)


class Animal():
    # Cria subjanela Animal
    def __init__(self):
        self.animal = Toplevel()
        self.animal.title('Cadastrar Animal')
        self.animal.geometry('350x370+200+100')
        self.animal.transient(janela)
        self.animal.focus_force()
        self.animal.grab_set()
        self.animal.resizable(width=False, height=False)
        self.nome = Label_Entry(self.animal, 'Nome: ', 0, 0, 30, 0, 1)
        self.raca = Label_Entry(self.animal, 'Raça: ', 1, 0, 30, 1, 1)
        self.peso = Label_Entry(self.animal, 'Peso: ', 2, 0, 30, 2, 1)
        self.b = Botao(self.animal, 'Salvar',self.salvar,20,200)
        self.p = Botao(self.animal,'Pesquisar',self.pesquisar,100,200)
        self.a = Botao(self.animal,'Alterar',self.alterar,180,200)
        self.d = Botao(self.animal,'Deletar',self.deletar,260, 200)


    def salvar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        if validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito Curto')
        elif validar_nome(self.raca.entry.get()):
            mb.showinfo('Erro', 'Nome de raça muito Curto')
        elif validar_peso(self.peso.entry.get()):
            mb.showinfo('Erro', 'Peso Incorreto')
        else:
            self.conexao.execute("Insert into animal(nome, raca, peso) values ('%s','%s','%s')"% (self.nome.entry.get(), self.raca.entry.get(), self.peso.entry.get()))
            self.c.commit()
            self.c.close()
            self.nome.entry.delete(0, END)
            self.raca.entry.delete(0, END)
            self.peso.entry.delete(0, END)
    
    
    def pesquisar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.pesquisa = 'SELECT nome, raca, peso FROM animal WHERE nome = (?)'
        self.conexao.execute(self.pesquisa, [self.nome.entry.get()])
        self.data = self.conexao.fetchall()
        for i in self.data:
            if self.nome.entry.get() in i:
                self.nome.entry.delete(0, 40)
                self.nome.entry.insert(END, i[0])
                self.salva = i[0]
                self.raca.entry.insert(END, i[1])
                self.peso.entry.insert(END, i[2])
        self.c.commit()
        self.c.close()
    

    def alterar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        if validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito Curto')
        elif validar_nome(self.raca.entry.get()):
            mb.showinfo('Erro', 'Nome de raça muito Curto')
        elif validar_peso(self.peso.entry.get()):
            mb.showinfo('Erro', 'Peso Incorreto')
        else:
            self.altera = 'UPDATE animal set nome = (?), raca = (?), peso = (?) where nome = (?)'
            self.conexao.execute(self.altera, [self.nome.entry.get(), self.raca.entry.get(), self.peso.entry.get(), self.salva])
            self.c.commit()
            self.c.close()
            self.nome.entry.delete(0, END)
            self.raca.entry.delete(0, END)
            self.peso.entry.delete(0, END)


    def deletar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.deleta = 'Delete from animal where nome = (?)'
        self.conexao.execute(self.deleta, [self.nome.entry.get()])
        self.c.commit()
        self.c.close()
        self.nome.entry.delete(0, END)
        self.raca.entry.delete(0, END)
        self.peso.entry.delete(0, END)


class Veterinario():
    # Cria subjanela Veterinário
    def __init__(self):
        self.veterinario = Toplevel()
        self.veterinario.title('Cadastrar Veterinário')
        self.veterinario.geometry('350x370+200+100')
        self.veterinario.transient(janela)
        self.veterinario.focus_force()
        self.veterinario.grab_set()
        self.veterinario.resizable(width=False, height=False)
        self.nome = Label_Entry(self.veterinario, 'Nome: ', 0, 0, 30, 0, 1)
        self.telefone = Label_Entry(self.veterinario, 'Telefone: ', 1, 0, 30, 1, 1)
        self.email = Label_Entry(self.veterinario, 'Email: ', 2, 0, 30, 2, 1)
        self.b = Botao(self.veterinario, 'Salvar',self.salvar,20,200)
        self.p = Botao(self.veterinario, 'Pesquisar',self.pesquisar,100,200)
        self.a = Botao(self.veterinario,'Alterar',self.alterar,180,200)
        self.d = Botao(self.veterinario,'Deletar',self.deletar,260, 200)


    def salvar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        if validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito curto')
        elif validar_tel(self.telefone.entry.get()):
            mb.showinfo('Erro', 'Telefone incorreto')
        elif validar_email(self.email.entry.get()):
            mb.showinfo('Erro', 'E-mail incorreto')
        else:
            self.conexao.execute("Insert into veterinarios(nome, telefone, email) values ('%s','%s','%s')"% (self.nome.entry.get(), self.telefone.entry.get(), self.email.entry.get()))
            self.c.commit()
            self.c.close()
            self.nome.entry.delete(0, END)
            self.telefone.entry.delete(0, END)
            self.email.entry.delete(0, END)
    
    
    def pesquisar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.pesquisa = 'SELECT nome, telefone, email FROM veterinarios WHERE nome = (?)'
        self.conexao.execute(self.pesquisa, [self.nome.entry.get()])
        self.data = self.conexao.fetchall()
        for i in self.data:
            if self.nome.entry.get() in i:
                self.nome.entry.delete(0, 40)
                self.nome.entry.insert(END, i[0])
                self.salva = i[0]
                self.telefone.entry.insert(END, i[1])
                self.email.entry.insert(END, i[2])
        self.c.commit()
        self.c.close()
    

    def alterar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        if validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito curto')
        elif validar_tel(self.telefone.entry.get()):
            mb.showinfo('Erro', 'Telefone incorreto')
        elif validar_email(self.email.entry.get()):
            mb.showinfo('Erro', 'E-mail incorreto')
        else:
            self.altera = 'UPDATE veterinarios set nome = (?), telefone = (?), email = (?) where nome = (?)'
            self.conexao.execute(self.altera, [self.nome.entry.get(), self.telefone.entry.get(), self.email.entry.get(), self.salva])
            self.c.commit()
            self.c.close()
            self.nome.entry.delete(0, END)
            self.telefone.entry.delete(0, END)
            self.email.entry.delete(0, END)


    def deletar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.deleta = 'Delete from veterinarios where nome = (?)'
        self.conexao.execute(self.deleta, [self.nome.entry.get()])
        self.c.commit()
        self.c.close()
        self.nome.entry.delete(0, END)
        self.telefone.entry.delete(0, END)
        self.email.entry.delete(0, END)

class Consulta():
    def __init__(self):
        self.consulta = Toplevel()
        self.consulta.title('Agendar Consultar')
        self.consulta.geometry('350x350+200+100')
        self.consulta.transient(janela)
        self.consulta.focus_force()
        self.consulta.grab_set()
        self.consulta.resizable(width=False, height=False)

        self.nome = Label_Entry(self.consulta, 'Nome: ', 0, 0, 30, 0, 1)
        self.dia = Label_Entry(self.consulta, 'Data: ', 1, 0, 30, 1, 1)
        self.horario = Label_Entry(self.consulta, 'Horario: ', 2, 0, 30, 2, 1)

        self.b = Botao(self.consulta, 'Salvar',self.salvar,20,200)
        self.p = Botao(self.consulta, 'Pesquisar',self.pesquisar,100,200)
        self.a = Botao(self.consulta,'Alterar',self.alterar,180,200)
        self.d = Botao(self.consulta,'Deletar',self.deletar,260, 200)

    
    def salvar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        if validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito Curto')
        elif validar_data(self.dia.entry.get()):
            mb.showinfo('Erro', 'Data Incorreta')
        elif validar_hora(self.horario.entry.get()):
            mb.showinfo('Erro', 'Horario Incorreto')
        else:
            self.conexao.execute("Insert into consulta(nome, dia, horario) values ('%s','%s','%s')"% (self.nome.entry.get(), self.dia.entry.get(), self.horario.entry.get()))
            self.c.commit()
            self.c.close()
            self.nome.entry.delete(0, END)
            self.dia.entry.delete(0, END)
            self.horario.entry.delete(0, END)


    def pesquisar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.pesquisa = 'SELECT nome, dia, horario FROM consulta WHERE nome = (?)'
        self.conexao.execute(self.pesquisa, [self.nome.entry.get()])
        self.data = self.conexao.fetchall()
        for i in self.data:
            if self.nome.entry.get() in i:
                self.nome.entry.delete(0, 40)
                self.nome.entry.insert(END, i[0])
                self.salva = i[0]
                self.dia.entry.insert(END, i[1])
                self.horario.entry.insert(END, i[2])
        self.c.commit()
        self.c.close()
    

    def alterar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        if validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito Curto')
        elif validar_data(self.dia.entry.get()):
            mb.showinfo('Erro', 'Data Incorreta')
        elif validar_hora(self.horario.entry.get()):
            mb.showinfo('Erro', 'Horario Incorreto')
        else:
            self.altera = 'UPDATE consulta set nome = (?), dia = (?), horario = (?) where nome = (?)'
            self.conexao.execute(self.altera, [self.nome.entry.get(), self.dia.entry.get(), self.horario.entry.get(), self.salva])
            self.c.commit()
            self.c.close()
            self.nome.entry.delete(0, END)
            self.dia.entry.delete(0, END)
            self.horario.entry.delete(0, END)


    def deletar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.deleta = 'Delete from consulta where nome = (?)'
        self.conexao.execute(self.deleta, [self.nome.entry.get()])
        self.c.commit()
        self.c.close()
        self.nome.entry.delete(0, END)
        self.dia.entry.delete(0, END)
        self.horario.entry.delete(0, END)


class Exame():
    def __init__(self):
        self.exame = Toplevel()
        self.exame.title('Marcar Exame')
        self.exame.geometry('350x350+200+100')
        self.exame.transient(janela)
        self.exame.focus_force()
        self.exame.grab_set()
        self.exame.resizable(width=False, height=False)
        self.nome = Label_Entry(self.exame, 'Nome: ', 0, 0, 30, 0, 1)
        self.tipo = Label_Entry(self.exame, 'Tipo: ', 1, 0, 30, 1, 1)
        self.dia = Label_Entry(self.exame, 'Dia: ', 2, 0, 30, 2, 1)
        self.horario = Label_Entry(self.exame, 'Horario:',3,0,30,3,1)

        self.b = Botao(self.exame, 'Salvar',self.salvar,20,200)
        self.p = Botao(self.exame, 'Pesquisar',self.pesquisar,100,200)
        self.a = Botao(self.exame,'Alterar',self.alterar,180,200)
        self.d = Botao(self.exame,'Deletar',self.deletar,260, 200)

    def salvar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        if validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito Curto')
        elif validar_nome(self.tipo.entry.get()):
            mb.showinfo('Erro', 'Tipo não definido')
        elif validar_data(self.dia.entry.get()):
            mb.showinfo('Erro', 'Data Incorreta')
        elif validar_hora(self.horario.entry.get()):
            mb.showinfo('Erro', 'Horario Incorreto')
        else:
            self.conexao.execute("Insert into exames(nome, tipo, dia, horario) values ('%s','%s','%s','%s')"% (self.nome.entry.get(), self.tipo.entry.get(), self.dia.entry.get(),self.horario.entry.get()))
            self.c.commit()
            self.c.close()
            self.nome.entry.delete(0, END)
            self.tipo.entry.delete(0, END)
            self.dia.entry.delete(0, END)
            self.horario.entry.delete(0, END)
    
     
    def pesquisar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.pesquisa = 'SELECT nome, tipo, dia, horario FROM exames WHERE nome = (?)'
        self.conexao.execute(self.pesquisa,[self.nome.entry.get()])
        self.data = self.conexao.fetchall()
        for i in self.data:
            if self.nome.entry.get() in i:
                self.nome.entry.delete(0, 40)
                self.nome.entry.insert(END, i[0])
                self.salva = i[0]
                self.tipo.entry.insert(END, i[1])
                self.dia.entry.insert(END, i[2])
                self.horario.entry.insert(END, i[3])
        self.c.commit()
        self.c.close()
    
    
    def alterar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        if validar_nome(self.nome.entry.get()):
            mb.showinfo('Erro', 'Nome muito Curto')
        elif validar_nome(self.tipo.entry.get()):
            mb.showinfo('Erro', 'Tipo não definido')
        elif validar_data(self.dia.entry.get()):
            mb.showinfo('Erro', 'Data Incorreta')
        elif validar_hora(self.horario.entry.get()):
            mb.showinfo('Erro', 'Horario Incorreto')
        else:
            self.altera = 'UPDATE exames set nome = (?), tipo = (?), dia = (?), horario = (?) where nome = (?)'
            self.conexao.execute(self.altera, [self.nome.entry.get(), self.tipo.entry.get(), self.dia.entry.get(),self.horario.entry.get(),self.salva])
            self.c.commit()
            self.c.close()
            self.nome.entry.delete(0, END)
            self.tipo.entry.delete(0, END)
            self.dia.entry.delete(0, END)
            self.horario.entry.delete(0, END)
    
    def deletar(self):
        self.c = sqlite3.connect('clinica.db')
        self.conexao = self.c.cursor()
        self.deleta = 'Delete from exames where nome = (?)'
        self.conexao.execute(self.deleta, [self.nome.entry.get()])
        self.c.commit()
        self.c.close()
        self.nome.entry.delete(0, END)
        self.tipo.entry.delete(0, END)
        self.dia.entry.delete(0, END)
        self.horario.entry.delete(0, END)


def validar_nome(dado):
    nome_validate = dado
    if len(nome_validate) < 4:
        return True
    else:
        return False

def validar_tel(dado):
    try:
        valor = int(dado)
        ddd = dado[:2]
        parte_1 = dado[3:7]
        parte_2 = dado[7:]
        if len(ddd) != 2 and len(parte_1) != 4 and len(parte_2) != 4:
            return True
        else:
            return False
    except ValueError:
        return True

def validar_email(dado):
    email_validate = dado
    if len(email_validate) < 9 or ' ' in email_validate:
        return True
    else:
        x = email_validate.split('@')
        if len(x) != 2 or len(x[0]) == 0:
            return True
        else:
            x = x[1].split('.')
            if len(x) < 2 or len(x) > 3 or len(x[0]) == 0:
                return True
            elif len(x[1]) == 0:
                return True
            else:
                return False  

def validar_cep(dado):
    try:
        endereco = pycep_correios.consultar_cep(f'{dado}')
        return False
    except:
        return True

def validar_numero(dado):
    try:
        valor = int(dado)
        return False
    except ValueError:
        return True

def validar_peso(dado):
    try:
        valor = float(dado)
        return False
    except ValueError:
        return True

def validar_data(dado):
    try:
        dia = int(dado[:2])
        mes = int(dado[2:4])
        ano = int(dado[4:])
        if mes != 2:
            if dia > 31 or mes <= 0 or mes > 12 or ano < 2019:
                return True
        else:
            if dia > 28 or mes <= 0 or mes > 12 or ano < 2019:
                return True
    except ValueError:
        print("Formato errado")
    return False

def validar_hora(dado):
    try:
        hora = int(dado[:2])
        minuto = int(dado[2:])
        if hora > 23 or hora < 0 or minuto > 59 or minuto < 0:
            return True
        else:
            return False
    except ValueError:
        return True

Interface() # Instancia o Menu de Subjanelas

janela.mainloop()