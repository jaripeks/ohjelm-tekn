const poisRouter = require('express').Router()
const poisHandler = require('../db')
const poisValidator = require('../utils/poiValidator')
const tokenValidator = require('../utils/tokenValidator')
const queryValidator = require('../utils/queryValidator')
const haversine = require('haversine-js')
const haversineOptions = {
    radius: haversine.EARTH.KM
};

poisRouter.get('/', queryValidator, (req, res) => {
    let pois = poisHandler.getPoi()

    if (req.parameters) {
        const parameters = req.parameters
        pois = pois.filter(poi => {
            const distance = haversine(
                { latitude: poi.coordinates.lat, longitude: poi.coordinates.lng },
                { latitude: parameters.lat, longitude: parameters.lng },
                haversineOptions).toFixed(3)
            console.log(distance)
            return Number(parameters.radius) >= Number(distance)
        })
    }

    res.status(200).json(pois)
})

poisRouter.get('/:id', (req, res, next) => {
    const id = req.params.id

    if (poisHandler.getPoi(id)) {
        console.log('löytyy')
        const foundPoi = poisHandler.getPoi(id)
        res.status(200).json(foundPoi)
    } else {
        const error = {
            statusCode: 404,
            message: 'Id:tä ei ole'
        }

        next(error)
    }
})

poisRouter.put('/:id', tokenValidator, poisValidator, (req, res) => {
    const id = req.params.id
    const body = req.body

    const poi = {
        name: body.name,
        description: body.description,
        city: body.city,
        coordinates: body.coordinates
    }

    if (poisHandler.getPoi(id)) {
        //poi found -> updated
        res.status(200)
    } else {
        //poi not found -> created
        res.status(201)
    }

    const updatedOrNew = poisHandler.setPoi(id, poi)

    res.json(updatedOrNew)
})

poisRouter.post('/', tokenValidator, poisValidator, (req, res) => {
    const body = req.body
    const poi = {
        name: body.name,
        description: body.description,
        city: body.city,
        coordinates: body.coordinates
    }

    const newPoi = poisHandler.createPoi(poi)
    res.status(201).json(newPoi)

})

poisRouter.delete('/:id', tokenValidator, (req, res, next) => {
    if (poisHandler.deletePoi(req.params.id)) {
        res.sendStatus(204)
    } else {
        const error = {
            statusCode: 404,
            message: 'Id:tä ei ole'
        }
        next(error)
    }
})

module.exports = poisRouter