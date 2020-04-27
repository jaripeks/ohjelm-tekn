const validator = require('../tokens').verify

const tokenValidator = (req, res, next) => {
    const payload = validator(req.token)
    if (!payload) {
        const error = {
            statusCode: 401,
            message: 'Verification failed'
        }
        next(error)
    } else {
        next()
    }
}

module.exports = tokenValidator