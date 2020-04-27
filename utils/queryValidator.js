const queryValidator = (req, res, next) => {
    const query = req.query
    if (query.filter === 'radius' && query.radius && query.lat && query.lng) {
        if (Number(query.radius) && Number(query.lat) && Number(query.lng)) {
            const parameters = {
                radius: query.radius,
                lat: query.lat,
                lng: query.lng
            }
            req.parameters = parameters
        }
    }
    next()
}

module.exports = queryValidator