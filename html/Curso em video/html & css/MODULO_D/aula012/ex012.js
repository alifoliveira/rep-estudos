var now = new Date()
var hours = now.getHours()
console.log(`Agora são exatamente ${hours} horas`)
if (hours < 12) {
    console.log('Bom Dia!')
} else if (hours <= 18) {
    console.log('Boa Tarde!')
} else {
    console.log('Boa Noite!')
}
