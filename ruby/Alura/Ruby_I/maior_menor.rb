##################################
# puts = : output
# gets = : input  
# .to_i = converte para inteiro  
# .to_s = converte para string 
##################################

def boas_vindas 
    puts "Bem vindo ao jogo da adivinhação"
    puts "Qual é o seu nome?"
    nome = gets.strip
    puts "\n\n\n"
    puts "Começaremos o jogo para você, #{nome}"
end

def sortear_numero_secreto
    puts "Escolhendo um número secreto entre 0 e 200..."
    sorteado = 175
    puts "Escolhido... que tal adivinhar nosso número secreto?"
    sorteado  # isso é o return
end

def pede_numero(chutes, tentativa, limite_tentativa)
    puts "\n\n\n"
    puts "Tentativa #{tentativa.to_s} de #{limite_tentativa.to_s}" # "texto #{var} = interpolação de string + variavel""
    puts "Chutes até agora:" + chutes.to_s
    puts "Entre com o número"
    chute = gets.strip
    puts "Será que acertou? Você chutou " + chute
    chute.to_i
end

def verifica_acerto(numero_secreto, chute)
    acertou = numero_secreto == chute.to_i

    if acertou
        puts "Acertou!"
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

boas_vindas
numero_secreto = sortear_numero_secreto
pontos = 1000

limite_tentativa = 5
chutes = []

for tentativa in 1..limite_tentativa
    chute = pede_numero(chutes, tentativa, limite_tentativa) # não é obrigado passsar parenteses, mas eu vou!
    chutes << chute                                          # append

    pontos_a_perder = (chute - numero_secreto).abs / 2.0     # calculo de remoção de pontos | divisão por 0.5 converte resultado para float   
    pontos -= pontos_a_perder                                # pontos perdidos

    break if verifica_acerto(numero_secreto, chute)
end

puts "Você ganhou #{pontos} pontos."
