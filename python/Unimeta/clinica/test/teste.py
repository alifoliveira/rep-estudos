def validar(a):
    if type(a) != int or a <= 0:
        return True
    else:
        return False


dado = 0

if validar(dado):
    print('Não é inteiro')
else:
    print('É inteiro')