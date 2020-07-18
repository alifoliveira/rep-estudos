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
    # Mapeamento dos Inputs
    movimentos = { # Criando dicionario
    "W" => [-1, 0],
    "S" => [+1, 0],
    "A" => [0, -1],
    "D" => [0, +1]
    }
    movimento = movimentos[direcao]
    heroi[0] += movimento[0]
    heroi[1] += movimento[1]
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
    valor_atual = mapa[posicao[0]][posicao[1]]
    if valor_atual == "X" || valor_atual == "F"
        return false
    end
    return true
end

def move_fantasma(mapa, linha, coluna)
    posicao = [linha, coluna + 1]
    if posicao_valida?(mapa, posicao)
        mapa[linha][coluna] = " "
        mapa[posicao[0]][posicao[1]] = "F"
    end
end

def move_fantasmas(mapa)
    fantasma_caractere = "F"
    mapa.each_with_index do |linha_atual, linha|
        linha_atual.chars.each_with_index do |caractere_atual, coluna|
            if eh_fantasma = caractere_atual == fantasma_caractere
                move_fantasma(mapa, linha, coluna)
            end
        end
    end 
end

def jogo(nome)
    mapa = le_mapa(2)
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
        move_fantasmas(mapa)
    end
end

def inicia_jogo
    nome = boas_vindas()
    jogo(nome)
end
