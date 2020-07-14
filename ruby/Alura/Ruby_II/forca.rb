require_relative 'ui' # requere lib relativa ao diretório desse arquivo, com prefixo ui

def pede_chute_valido(chutes, erros)
    cabecalho_tentativa(chutes, erros)
    loop do
        chute = pede_um_chute()
        if chutes.include? chute # verificar se está incluso na lista
            avisa_chute(chute)
        else
            return chute
        end
    end
end

def joga(nome)
    palavra_secreta = escolhe_palavra_secreta()
    
    erros = 0
    chutes = []
    pontos_ate_agora = 0

    while erros < 5
        chute = pede_chute_valido(chutes, erros)
        chutes << chute
        
        # Verificação
        chutou_uma_letra = chute.size == 1

        # Caso chute for uma letra
        if chutou_uma_letra
            letra_procurada = chute
            total_encontrado  = palavra_secreta.count(letra_procurada) # conta quantas vezes um caractere se repete em uma string
            # Errou
            if total_encontrado == 0
                avisa_letra_nao_encontrada()
                erros += 1
            # Acertou
            else
                avisa_letra_encontrada(total_encontrado)
            end
        # Caso o chute for uma palavra
        else
            acertou = chute == palavra_secreta
            # Acertou
            if acertou
                avisa_acertou_palavra()                
                pontos_ate_agora += 100
                break
            # Errou
            else
                avisa_errou_palavra()
                pontos_ate_agora -= 30
                erros += 1
            end
        end

    end

    avisa_pontos(pontos_ate_agora)
end

def jogo_da_forca   
    nome = boas_vindas()

    loop do
        joga(nome)
        if nao_quer_jogar?
            break
        end
    end
end


