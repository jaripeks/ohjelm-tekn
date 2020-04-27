const express = require('express')
const app = express()
const cors = require('cors')
const morgan = require('morgan')
const baseURL = '/api/v1'
const poisRouter = require('./routes/pois')
const loginRouter = require('./routes/login')
const middleware = require('./utils/middleware')

app.use(cors())
app.use(morgan('dev'))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(middleware.tokenExtractor)

app.use(`${baseURL}/pois`, poisRouter)
app.use(`${baseURL}/auth`, loginRouter)

app.use(middleware.unknownEndpoint)
app.use(middleware.errorHandler)

const PORT = 3000
app.listen(PORT, () => {
    console.log(`Server running on ${PORT}`)
})