const express = require('express')
const app = express()
const cors = require('cors')
const morgan = require('morgan')
const errorHandler = require('./utils/error_handler')
const weatherRouter = require('./routes/weather')

app.use(cors())
app.use(morgan('dev'))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.use('/weather', weatherRouter)

app.use(errorHandler)

const PORT = 3000
app.listen(PORT, () => {
    console.log(`Server running on ${PORT}`)
})