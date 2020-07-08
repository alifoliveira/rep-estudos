function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.querySelector('input#txtano')
    var res = document.querySelector('div#res')
    if (fano.value.length == 0 || fano.value > ano || fano.value <= 0) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - fano.value
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 10) {
                // criança M
                img.setAttribute('src', 'crianca-m.png')
            } else if (idade < 28) {
                // jovem M
                img.setAttribute('src', 'jovem-m.png')
            } else if (idade < 50) {
                // adulto
                img.setAttribute('src', 'adulto.png')
            } else {
                // idoso
                img.setAttribute('src', 'idoso.png')
            }
        } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 10) {
                // criança F
                img.setAttribute('src', 'crianca-f.png')
            } else if (idade < 28) {
                // jovem F
                img.setAttribute('src', 'jovem-f.png')
            } else if (idade < 50) {
                // adulta
                img.setAttribute('src', 'adulta.png')
            } else {
                // idosa
                img.setAttribute('src', 'idosa.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        res.appendChild(img)
    }
}
