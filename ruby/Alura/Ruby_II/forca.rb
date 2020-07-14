require_relative 'ui' # requere lib relativa ao diretório desse arquivo, com prefixo ui
require_relative 'rank' # requere lib relativa ao diretório desse arquivo, com prefixo ui

def escolhe_palavra_secreta
    avisa_escolhendo_palavra()
    texto = File.read('dicionario.txt')
    todas_as_palavras = texto.split "\n"
    numero_escolhido = rand(todas_as_palavras.size)
    palavra_secreta = todas_as_palavras[numero_escolhido].downcase
    avisa_palavra_escolhida(palavra_secreta)
end

def escolhe_palavra_secreta_2
    avisa_escolhendo_palavra()
    arquivo = File.new("dicionario.txt")
    quantidade_de_palavras = arquivo.gets.to_i # Lê a primeira linha do arquivo e transforma em inteiro
    numero_escolhido = rand(quantidade_de_palavras)
    for linha in 1..(numero_escolhido-1)
        arquivo.gets
    end
    palavra_secreta = arquivo.gets.strip.downcase
    arquivo.close
    avisa_palavra_escolhida(palavra_secreta)
end

def palavra_mascarada(chutes, palavra_secreta)
    mascara = ""
    for letra in palavra_secreta.chars
        if chutes.include? letra
            mascara << letra
        else
            mascara << "_"
        end
    end
    return mascara
end

def pede_chute_valido(chutes, erros, mascara)
    cabecalho_tentativa(chutes, erros, mascara)
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

    avisa_campeao_atual(ler_rank)

    while erros < 5
        mascara = palavra_mascarada(chutes, palavra_secreta)
        chute = pede_chute_valido(chutes, erros, mascara)
        chutes << chute
        
        # Verificação
        chutou_uma_letra = chute.size == 1

        # Caso chute for uma letra
        if chutou_uma_letra
            letra_procurada = chute
            total_encontrado  = palavra_secreta.count(letra_procurada) # conta quantas vezes um caractere se repete em uma string
            # Errou
            if total_encontrado == 0
                erros += 1
                avisa_nao_encontrada()
            # Acertou
            else
                avisa_letra_encontrada(total_encontrado)
            end
        # Caso o chute for uma palavra
        else
            acertou = chute == palavra_secreta
            # Acertou
            if acertou
                pontos_ate_agora += 100
                avisa_acertou_palavra()                
                break
            # Errou
            else
                erros += 1
                pontos_ate_agora -= 30
                avisa_errou_palavra()
            end
        end

    end

    avisa_pontos(pontos_ate_agora)
    return pontos_ate_agora
end

def jogo_da_forca   
    nome = boas_vindas()
    pontos_totais = 0

    avisa_campeao_atual(ler_rank)

    loop do
        pontos_totais += joga(nome)
        avisa_pontos_totais(pontos_totais)

        if ler_rank[1].to_i < pontos_totais
            salva_rank(nome, pontos_totais)
        end
        if nao_quer_jogar?
            break
        end
    end
end


