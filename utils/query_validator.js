const obs_types = ['temperature', 'humidity', 'wind']

const queryValidator = async (req, res, next) => {
    const query = req.query
    const keys = Object.keys(query)
    //check if not empty
    if(!(keys.length === 0 && query.constructor === Object)) {
        if(keys.includes('observation') && typeof(query.observation) === 'object') {
            //check if obs_types are correct
            for(const obs of query.observation) {
                if(!obs_types.includes(obs)) {
                    return res.status(400).send({
                        error: 'Query parameters invalid!'
                    })
                }
            }
        } else {
            return res.status(400).send({
                error: 'Query parameters invalid!'
            })
        }
    } else {
        //empty
        req.query = {'observation': ['empty']}
    }
    next()
}

module.exports = queryValidator