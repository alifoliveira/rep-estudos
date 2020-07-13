def boas_vindas 
    puts
    puts "        P  /_\\  P                              "
    puts "       /_\\_|_|_/_\\                             "
    puts "   n_n | ||. .|| | n_n         Bem vindo ao    "
    puts "   |_|_|nnnn nnnn|_|_|     Jogo de Adivinhação!"
    puts "  |' '  |  |_|  |'  ' |                        "
    puts "  |_____| ' _ ' |_____|                        " 
    puts "        \\__|_|__/                              "
    puts
    puts "Qual é o seu nome?"
    nome = gets.strip
    puts "\n\n\n"
    puts "Começaremos o jogo para você, #{nome}"
    nome
end

def pede_dificuldade
    puts "Qual o nível de dificuldade?"
    puts "(1) Muito fácil (2) Fácil (3) Normal (4) Difícil (5) Impossível"
    puts "Escolha: "
    dificuldade = gets.to_i
end

def sortear_numero_secreto(dificuldade)
    # config dificuldade
    case dificuldade
    when 1
        maximo = 30
    when 2
        maximo = 60
    when 3
        maximo = 100
    when 4
        maximo = 150
    else
        maximo = 200
    end
    # sorteia numero
    puts "\n\n\n"
    puts "Escolhendo um número secreto entre 1 e #{maximo}..."
    sorteado = rand(maximo) + 1 # rand return numero entre 0 e 1 (multiplica por n). Nesse caso, gera um numero entre 0 e 200
    puts "Escolhido... que tal adivinhar nosso número secreto?"
    sorteado                # isso é o return com "return" oculto
end

def pede_numero(chutes, tentativa, limite_tentativa)
    puts "Tentativa #{tentativa.to_s} de #{limite_tentativa.to_s}" # "texto #{var} = interpolação de string + variavel""
    puts "Chutes até agora: #{chutes.to_s}"
    puts "Entre com o número"
    chute = gets.strip
    puts "\n\n\n"
    puts "Será que acertou? Você chutou #{chute}..."
    chute.to_i
end

def acertou?(numero_secreto, chute)
    acertou = numero_secreto == chute.to_i

    if acertou
        ganhou()
        return true
    end
    
    maior = numero_secreto > chute.to_i
    if maior
        puts "O número secreto é maior!"
    else
        puts "O número secreto é menor!"
    end
    return false
end

def ganhou
    puts
    puts "             OOOOOOOOOOO               "
    puts "         OOOOOOOOOOOOOOOOOOO           "
    puts "      OOOOOO  OOOOOOOOO  OOOOOO        "
    puts "    OOOOOO      OOOOO      OOOOOO      "
    puts "  OOOOOOOO  #   OOOOO  #   OOOOOOOO    "
    puts " OOOOOOOOOO    OOOOOOO    OOOOOOOOOO   "
    puts "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  "
    puts "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  "
    puts "OOOO  OOOOOOOOOOOOOOOOOOOOOOOOO  OOOO  "
    puts " OOOO  OOOOOOOOOOOOOOOOOOOOOOO  OOOO   "
    puts "  OOOO   OOOOOOOOOOOOOOOOOOOO  OOOO    "
    puts "    OOOOO   OOOOOOOOOOOOOOO   OOOO     "
    puts "      OOOOOO   OOOOOOOOO   OOOOOO      "
    puts "         OOOOOO         OOOOOO         "
    puts "             OOOOOOOOOOOO              "
    puts
    puts "               Acertou!                "
    puts
end

def run(nome, dificuldade)
    numero_secreto = sortear_numero_secreto(dificuldade)
    pontos = 1000

    limite_tentativa = 5
    chutes = []

    for tentativa in 1..limite_tentativa
        chute = pede_numero(chutes, tentativa, limite_tentativa) # não é obrigado passsar parenteses, mas eu vou!
        chutes << chute                                          # append  
        
        # cheat
        if nome == "admin"
            ganhou()
            break
        end

        # calculo de remoção de pontos | divisão por 0.5 converte resultado para float
        pontos_a_perder = (chute - numero_secreto).abs / 0.5 
        pontos -= pontos_a_perder # pontos perdidos

        if acertou?(numero_secreto, chute)
            break
        end
    end

    puts "Você ganhou #{pontos} pontos."
end

def nao_quer_jogar? # por convenção se usar "?" na função que retorna boolean (true, false)
    puts "Dejesa jogar novamente? (S/N)"
    quero_jogar = gets.strip
    nao_quero_jogar = quero_jogar.upcase == "N"
end

# INICIAR JOGO
nome = boas_vindas()                # mensagem de boas vindas
dificuldade = pede_dificuldade()    # seleção de dificuldade

# coloca o jogo em loop
loop do
    run(nome, dificuldade)  # iniciar jogo
    if nao_quer_jogar?()    # pergunta se quer para jogo (loop)
        break
    end
end
