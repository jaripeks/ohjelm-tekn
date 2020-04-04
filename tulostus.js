const tulostaTahtia = maara => {
    let tahdet = ''
     for(let iteration = 0; iteration < maara; iteration++) {
        tahdet += '* '
     }
     console.log(tahdet)
}

const tulostaViivoja = maara => {
    let viivat = ''
    for(let iteration = 0; iteration < maara; iteration++) {
        viivat += '-'
     }
     console.log(viivat)
}

const tulostaTulos = tulos => {
    const tulosString = `${tulos}`
    tulostaViivoja(tulosString.length)
    console.log(tulosString)
    tulostaViivoja(tulosString.length)
}

module.exports = { tulostaTahtia, tulostaTulos }