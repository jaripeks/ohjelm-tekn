const menuRouter = require('express').Router()
const validator = require('../utils/query_validator')
const baseURL = 'https://www.ilmatieteenlaitos.fi/observation-data?station=101004'
const fetch = require('node-fetch')


menuRouter.get('/',validator, async (req, res, next) => {
    console.log(req.query.observation)
    const rawData = await makeRequest(baseURL)
    let data = {}
    for(const obs of req.query.observation) {
        switch(obs) {
            case 'temperature':
                // en oo ihan varma, oliko lämpötila t2m:n alla, mutta en minuutin googlailulla löytänyt apin kuvausta, joten oletin
                data = {...data, 'temperature': rawData.t2m[0][1]}
                break
            case 'humidity':
                data = {...data, 'humidity': rawData.Humidity[0][1]}
                break
            case 'wind':
                data = {...data, 'wind': rawData.WindSpeedMS[0][1]}
                break
            default:
                data = rawData
        }
    }
    res.status(200).json(data)
})

const makeRequest = async url => {
    try {
        const response = await fetch(url)
        const data = await response.json()
        return(data)
    } catch (error) {
        console.log(error)
    }
}

module.exports = menuRouter