const loginRouter = require('express').Router()
const tokenHandler = require('../tokens')

loginRouter.post('/', (req, res, next) => {
    const body = req.body
    if (body.username === 'mark' && body.password === 'giraffe') {
        const token = tokenHandler.create(body.username)
        res.status(200).json({ token })
    } else {
        const error = {
            statusCode: 400,
            message: 'Invalid credentials'
        }
        next(error)
    }
    next()
})

module.exports = loginRouter