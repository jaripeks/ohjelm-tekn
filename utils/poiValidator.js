const poiValidator = (req, res, next) => {
    const body = req.body
    const newError = {
        statusCode: 400,
        message: 'POI-tiedot virheelliset'
    }
    //just checks whether the parameters are given
    if (!body.name || !body.description || !body.city || !body.coordinates) {
        next(newError)
    } else {
        const coordinates = body.coordinates
        // checks whether the coordinates are given or not and if the types are correct
        if (!coordinates.lat || !coordinates.lng) {
            next(newError)
        } else if (typeof (coordinates.lat) !== 'number' || typeof (coordinates.lng) !== 'number') {
            next(newError)
        } else {
            next()
        }
    }
}

module.exports = poiValidator