/** 
* Mockup database module. The data is volatile, it is stored only in memory and will be reset whenever the server is restarted.
* @module db 
*/

/**
 * Coordinates
 * @typedef {Object} Coords
 * @property {number} lat - latitude 
 * @property {number} lng - longitude 
 */

/**
 * A Point of Interest (POI)
 * @typedef {Object} POI
 * @property {string} name - name of POI
 * @property {string} description - description of POI 
 * @property {string} city - location of POI
 * @property {Coords} coordinates - coordinates for POI
 */

const uuid = require('uuid/v1');

let storage = [
    {
        id: '50e31360-0521-11ea-acba-e389d9b4cbaa',
        name: 'Haaga-Helia ammattikorkeakoulu',
        description: 'Haaga-Helia ammattikorkeakoulu kouluttaa liike-elämän ja palveluelinkeinojen asiantuntijoita sekä tutkii ja kehittää näihin aloihin liittyvää osaamista ja toimintaa. Koulutusalamme ovat liiketalous, tietotekniikka, hotelli-, ravintola- ja matkailuala, johdon assistenttityö, toimittajakoulutus, liikunta-ala sekä ammatillinen opettajankoulutus. Meille on tärkeää, että opiskelijoillamme on heti valmistuttuaan vahvat siteet työelämään. Panostamme toiminnassamme yrittäjyyteen, yhteistyöhön, innovatiivisuuteen ja kansainvälisyyteen.',
        city: "Helsinki",
        coordinates: {
            lat: 60.203598,
            lng: 24.934968
        }
    },
    {
        id: 'there_is_no_place_like',
        name: 'Poromagia',
        description: 'what lies in the shadows...',
        city: 'Helsinki',
        coordinates: {
            lat: 60.199207,
            lng: 24.938719
        }
    }
]

/**
 * Get one entry by id or all POIs
 * 
 * @param {string=} id - id of entry to get, if no id given all entries are returned as an array
 */
function getPoi(id) {
    return id ? storage.filter(poi => poi.id === id)[0] : storage
}

/**
 * Update or create an entry.
 * If the id exists, the contents of the entry are updated. If id does not exist, a new entry is created for key id
 * 
 * @param {string} id - id of POI to update or create
 * @param {POI} poi - new POI data
 */
function setPoi(id, poi) {
    if (storage.map(poi => poi.id).includes(id)) {
        storage = storage.map(p => p.id !== id ? p : { id, ...poi })
    } else {
        storage = storage.concat({ id, ...poi })
    }
    return getPoi(id)
}

/**
 * Create a new entry.
 * A new entry with a new unique identifier is created
 * @param {*} poi - new POI data
 */
function createPoi(poi) {
    const id = uuid();
    storage = storage.concat({ id, ...poi });
    return getPoi(id, poi);
}

/**
 * Delete an entry.
 * If the entry does not exist, returns false, otherwise true.
 * @param {string} id 
 */
function deletePoi(id) {
    if (id && getPoi(id)) {
        storage = storage.filter(p => p.id !== id)
        return true;
    } else {
        return false;
    }
}

module.exports = {
    getPoi,
    setPoi,
    createPoi,
    deletePoi
}