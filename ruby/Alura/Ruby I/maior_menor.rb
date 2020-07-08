# puts = : output
# gets = : input
# == : igual
# .to_i : converte para inteiro

nova_linha = "\n"

puts "Bem vindo ao jogo da adivinhação" + nova_linha

puts "Qual é o seu nome?" + nova_linha
nome = gets
puts

puts "Começaremos o jogo para você, " + nome + nova_linha
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts

puts "Escolhido... que tal adivinhar hoje nosso número secreto?" + nova_linha

puts "Tentativa 1"
puts "Entre com o número"
chute = gets
puts

puts "Será que acertou? Você chutou " + chute + nova_linha
puts chute.to_i == numero_secreto # converte para inteiro e compara
