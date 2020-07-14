def salva_rank(nome, pontos_totais)
    conteudo = "#{nome}\n#{pontos_totais}"
    File.write("rank.txt", conteudo) # sobrescreve arquivo
end

def ler_rank
    conteudo = File.read "rank.txt"
    return conteudo.split "\n"
end