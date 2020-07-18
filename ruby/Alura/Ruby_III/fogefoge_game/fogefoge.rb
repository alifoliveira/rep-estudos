require_relative 'ui'

def le_mapa(numero)
    arquivo = "fogefoge_game\\mapa#{numero}.txt"
    texto = File.read(arquivo)
    mapa = texto.split("\n")
end

def encontra_jogador(mapa)
    heroi_caractere = "H"
    mapa.each_with_index do |linha_atual, linha| # para cada item do mapa 'linha_atual' recebe o elemento e 'linha' recebe o index
        coluna_do_heroi = linha_atual.index(heroi_caractere)
        if coluna_do_heroi
            # Achei linha e coluna!
            return [linha, coluna_do_heroi]
        end
        # não achei
    end
end

def calcula_nova_posicao(heroi, direcao)
    heroi = heroi.dup # Clona o objeto para não interferir com a utilização do objeto dentro do jogo
    case direcao
        when "W"
            heroi[0] -= 1
        when "S"
            heroi[0] += 1
        when "A"
            heroi[1] -= 1
        when "D"
            heroi[1] += 1
    end
    return heroi
end

def posicao_valida?(mapa, posicao)
    linhas = mapa.size
    colunas = mapa[0].size
    estorou_linhas = posicao[0] < 0 || posicao[0] >= linhas
    estorou_colunas = posicao[1] < 0 || posicao[1] >= colunas
    # Colisão Bordas do Mapa
    if estorou_linhas || estorou_colunas
        return false
    end
    # Colisão Paredes do Mapa
    if mapa[posicao[0]][posicao[1]] == "X"
        return false
    end
    return true
end

def jogo(nome)
    mapa = le_mapa(1)
    while true
        desenha(mapa)
        direcao = pede_movimento
        heroi = encontra_jogador(mapa)
        nova_posicao = calcula_nova_posicao(heroi, direcao)
        if !posicao_valida?(mapa, nova_posicao)
            next
        end
        mapa[heroi[0]][heroi[1]] = " "
        mapa[nova_posicao[0]][nova_posicao[1]] = "H"
    end
end

def inicia_jogo
    nome = boas_vindas()
    jogo(nome)
end
