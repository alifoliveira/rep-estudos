function carregar() {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    var minuto = data.getMinutes()
    msg.innerHTML = `Agora são ${hora}:${minuto} horas`
    if (hora >= 0 && hora < 12) {
        // Bom dia
        img.src = 'manha.png'
        document.body.style.background = '#9BC7D6'
    } else if (hora >= 12 && hora < 18) {
        // Boa tarde
        img.src = 'tarde.png'
        document.body.style.background = '#D8D29B'
    } else {
        // Boa noite
        img.src = 'noite.png'
        document.body.style.background = '#4D82A3'
    }
}
