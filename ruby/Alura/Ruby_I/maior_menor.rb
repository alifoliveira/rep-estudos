##################################
# puts = : output
# gets = : input  
# .to_i = converte para inteiro  
# .to_s = converte para string 
##################################

def boas_vindas 
    puts "Bem vindo ao jogo da adivinhação"
    puts "Qual é o seu nome?"
    nome = gets
    puts "\n\n\n"
    puts "Começaremos o jogo para você, " + nome
end

def sortear_numero_secreto
    puts "Escolhendo um número secreto entre 0 e 200..."
    sorteado = 175
    puts "Escolhido... que tal adivinhar nosso número secreto?"
    sorteado  # isso é o return
end

def pede_numero(tentativa, limite_tentativa)
    puts "\n\n\n"
    puts "Tentativa " + tentativa.to_s + " de " + limite_tentativa.to_s
    puts "Entre com o número"
    chute = gets
    puts "Será que acertou? Você chutou " + chute
    chute
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
    false
end

boas_vindas
numero_secreto = sortear_numero_secreto

limite_tentativa = 5

for tentativa in 1..limite_tentativa
    chute = pede_numero(tentativa, limite_tentativa) # não é obrigado passsar parenteses, mas eu vou!
    break if verifica_acerto(numero_secreto, chute)
end
