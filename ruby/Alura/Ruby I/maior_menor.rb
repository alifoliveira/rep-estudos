# puts = : output
# gets = : input
# == : igual
# .to_i : converte para inteiro

puts "Bem vindo ao jogo da adivinhação"

puts "Qual é o seu nome?"
nome = gets
puts "\n\n\n"

puts "Começaremos o jogo para você, " + nome
puts "Escolhendo um número secreto entre 0 e 200..."
numero_secreto = 175
puts

puts "Escolhido... que tal adivinhar hoje nosso número secreto?"

puts "Tentativa 1"
puts "Entre com o número"
chute = gets
puts

puts "Será que acertou? Você chutou " + chute
puts chute.to_i == numero_secreto # converte para inteiro e compara
