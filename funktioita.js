const defaultTulostin = maara => {
    let tulostus = ''
    for(let merkki = 0; merkki < maara; merkki++) {
        tulostus += '* '
    }
    console.log(tulostus)
}

const tulostaNelio = (sivu, tulostin = defaultTulostin) => {
    for(let rivi = 0; rivi < sivu; rivi++) {
        tulostin(sivu)
    }
}

const tulostaSuorakulmio = (leveys, korkeus, tulostin = defaultTulostin) => {
    for(let rivi = 0; rivi < korkeus; rivi++) {
        tulostin(leveys)
    }
}

const tulostaKolmio = (korkeus, tulostin = defaultTulostin) => {
    for(let rivi = 1; rivi <= korkeus; rivi++) {
        tulostin(rivi)
    }
}

const lukusarjanSumma = n => {
    let summa = 0
    for(let luku = 1; luku <= n; luku++) {
        summa += luku
    }
    return summa
}

const kertoma = n => {
    let tulo = 1
    for(let luku = 1; luku <= n; luku++) {
        tulo *= luku
    }
    return tulo
}

module.exports = {
    tulostaNelio,
    tulostaSuorakulmio,
    tulostaKolmio,
    lukusarjanSumma,
    kertoma
}