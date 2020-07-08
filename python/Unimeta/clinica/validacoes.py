class Validar_nome():
    def __init__(self,valor):
        nome_validate = valor
        if len(nome_validate) < 4:
            print('Errado')
        else:
            print('Certo')
            return self.nome.entry.get()


'''def celular_cliente():
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


def numero_cliente():
    try:
        numero_test = int(numero.get())
        numero['bg'] = 'white'
        return numero.get()
    except:
        numero['bg'] = 'pink2'


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
                return email.get()'''


