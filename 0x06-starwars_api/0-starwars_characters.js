#!/usr/bin/node
const process = require('process');
const request = require('request');

const fetchFilmData = (filmId) => {
    return new Promise((resolve, reject) => {
        const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

        request.get(url, (err, res, body) => {
            if (err) {
                reject(err);
            } else {
                const data = JSON.parse(body);
                const characters = data.characters;
                const characterPromises = characters.map((characterUrl) => {
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
    });
};

const main = async () => {
    const filmId = process.argv[2];
    if (!filmId) {
        console.error('Film ID is missing.');
        return;
    }

    try {
        await fetchFilmData(filmId);
    } catch (error) {
        console.error(error);
    }
};

main();
