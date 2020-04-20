const errorHandler = (error, req, res, next) => {
    if(!error.statusCode) {
        res.status(500).send()
    }
    res.status(error.statusCode).send()
}

module.exports = errorHandler