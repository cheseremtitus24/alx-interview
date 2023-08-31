#!/usr/bin/node

const request = require('request');
const args = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + args, (error, response, body) => {
    if (error) throw error;
    else {
        const characters = JSON.parse(body).characters;
        order(characters, 0);
    }
});

request.get(url, (err, res, body) => {
    if (err) {
        reject(err);
    } else {
        const data = JSON.parse(body);
        const characters = data.characters;
        const characterPromises = characters.map((characterUrl) => {
            console.log(characterUrl);
            return new Promise((resolve, reject) => {
                request.get(characterUrl, (err, res, body) => {
                    if (err) {
                        reject(err);
                    } else {
                        const characterData = JSON.parse(body);
                        console.log(characterData.name);
                        resolve();
                    }
                });
            });
        });

        Promise.all(characterPromises)
            .then(resolve)
            .catch(reject);
    }
});


