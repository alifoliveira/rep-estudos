# puts 175 != 174
# puts 175 != 175

# puts 175 > 174
# puts 175 >= 175
# puts 175 < 176
# puts 175 <= 176

# for dedos in 1..3
#     puts "Contando " + dedos.to_s
# end

chutes = []                  # array
chute = 176                  # substitui
chutes << chute              # append

chute = 100
tentativa = 2
chutes << chute              

chute = 130
chutes << chute

puts chutes.size
for chute in chutes
    puts chute
end