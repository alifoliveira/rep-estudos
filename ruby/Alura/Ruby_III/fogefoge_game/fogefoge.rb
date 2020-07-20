require_relative 'ui'

def le_mapa(numero)
    arquivo = "mapas\\mapa#{numero}.txt"
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
    end
    nil
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

def soma_vetor(vetor1, vetor2)
    [vetor1[0] + vetor2[0], vetor1[1] + vetor2[1]]
end

def posicoes_validas(mapa, novo_mapa, posicao)
    posicoes = []
    movimentos = [[+1, 0], [0, +1], [-1, 0], [0, -1]]
    movimentos.each do |movimento|
        nova_posicao = soma_vetor(movimento, posicao)
        if posicao_valida?(mapa, nova_posicao) && posicao_valida?(novo_mapa, nova_posicao)
            posicoes << nova_posicao
        end
    end
    return posicoes
end

def move_fantasma(mapa, novo_mapa, linha, coluna)
    posicoes = posicoes_validas(mapa, novo_mapa, [linha, coluna])
    return if posicoes.empty?   # retorna se estiver vazio

    aleatoria = rand(posicoes.size)
    posicao = posicoes[aleatoria]
    mapa[linha][coluna] = " "
    novo_mapa[posicao[0]][posicao[1]] = "F"
end

def move_fantasmas(mapa)
    fantasma_caractere = "F"
    novo_mapa = copia_mapa(mapa)
    mapa.each_with_index do |linha_atual, linha|
        linha_atual.chars.each_with_index do |caractere_atual, coluna|
            if eh_fantasma = caractere_atual == fantasma_caractere
                move_fantasma(mapa, novo_mapa, linha, coluna)
            end
        end
    end
    return novo_mapa
end

def copia_mapa(mapa)
    novo_mapa = mapa.join("\n").tr("F", " ").split("\n")
    return novo_mapa
end

def jogador_perdeu?(mapa)
    perdeu = !encontra_jogador(mapa)
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

        mapa = move_fantasmas(mapa)
        if jogador_perdeu?(mapa)
            game_over()
            break
        end
    end
end

def inicia_jogo
    nome = boas_vindas()
    jogo(nome)
end
