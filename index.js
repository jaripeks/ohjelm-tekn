const express = require('express')
const app = express()
const cors = require('cors')
const PORT = 3000
const baseUrl = '/api/exercise'

app.use(cors())
app.use(express.static('public'))
app.use('/hello', express.static('hello'))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.get('/api', (req, res) => {
    return res.json({ msg: 'Hello, World!' })
})

app.get(baseUrl, (req, res) => {
    return res.status(200).json(req.query)
})

app.post(baseUrl, (req, res) => {
    const body = req.body
    res.status(200).send(`
        <h1>Hello from Express!</h1>
        <h2>POST parameters</h2>
        <p>I received these parameters: </p>
        <ul>
            ${Object.keys(body).map(key => {
                return(
                    `<li>${key}: ${body[key]}`
                )
            })}
        </ul>
    `)
})

app.post('/api/login', (req, res) => {
    const body = req.body
    if(!body.user || !body.pwd) {
        return res.status(400).end()
    } else if (body.user === 'mark' && body.pwd === 'giraffe') {
        return res.status(200).json({ user: body.user })
    }
    return res.status(403).end()
})

app.listen(PORT, () => {
    console.log(`Server running on ${PORT}`)
})