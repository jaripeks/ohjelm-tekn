const tokenExtractor = (req, res, next) => {
    const authorization = req.get('authorization')
    if (authorization && authorization.toLowerCase().startsWith('bearer ')) {
        req.token = authorization.substring(7)
    }
    next()
}

const errorHandler = (error, req, res, next) => {
    if (!error.statusCode) {
        res.status(500).send()
    } else {
        res.status(error.statusCode).json({ error: error.message })
    }
}

const unknownEndpoint = (req, res, next) => {
    const error = {
        statusCode: 404,
        message: 'uknown endpoint'
    }

    next(error)
}

module.exports = {
    tokenExtractor,
    errorHandler,
    unknownEndpoint
}