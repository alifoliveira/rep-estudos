def boas_vindas
    puts "Bem vindo ao jogo da forca!"
    puts "Qual é o seu nome?"
    nome = gets.strip
    puts "\n\n\n"
    puts "Começaremos o jogo para você, #{nome}."
    return nome
end

def escolhe_palavra_secreta
    puts "Escolhendo uma palavra secreta..."
    palavra_secreta = "programador"
    puts "Palavra secreta com #{palavra_secreta.size} letras... Boa sorte!"
    return palavra_secreta
end

def nao_quer_jogar?
    puts "Deseja jogar novamente? (S/N)"
    quero_jogar = gets.strip
    nao_quero_jogar = quero_jogar.upcase == "N"
    return nao_quero_jogar
end

def pede_um_chute(chutes, erros)
    puts "\n\n\n"
    puts "Erros até agora:  #{erros}"
    puts "Chutes até agora: #{chutes}"
    puts "Entre com uma letra ou uma palavra"
    chute = gets.strip
    puts "Será que acertou? Você chutou #{chute}"
    return chute
end

def conta(texto, letra)
    total_encontrado = 0
    for caractere in texto.chars # transforma string em um array de caracteres | percorre caracteres em texto
        if caractere == letra
            total_encontrado += 1
        end
    end
    return total_encontrado
end

def joga(nome)
    palavra_secreta = escolhe_palavra_secreta()
    
    erros = 0
    chutes = []
    pontos_ate_agora = 0

    while erros < 5
        chute = pede_um_chute(chutes, erros)
        if chutes.include? chute # verificar se está incluso na lista
            puts "Você já chutou #{chute}."
            next # inicia proxima iteração
        end
        chutes << chute
        
        # verificação
        chutou_uma_letra = chute.size == 1

        # caso chute for uma letra
        if chutou_uma_letra
            letra_procurada = chute
            total_encontrado  = palavra_secreta.count(letra_procurada) # conta quantas vezes um caractere se repete em uma string
            if total_encontrado == 0
                puts "Letra não encontrada."
                erros += 1
            else
                puts "Letra encontrada #{total_encontrado} vezes."
            end
        # caso o chute for uma palavra
        else
            acertou = chute == palavra_secreta
            if acertou
                puts "Parabéns! Acertou!"
                pontos_ate_agora += 100
                break
            else
                puts "Que pena... errou"
                pontos_ate_agora -= 30
                erros += 1
            end
        end

    end

    puts "Você ganhou #{pontos_ate_agora} pontos."
end

nome = boas_vindas()
palavra_secreta = escolhe_palavra_secreta()

loop do
    joga(nome)
    if nao_quer_jogar?
        break
    end
end
