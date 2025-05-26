#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  const printCharacter = (index) => {
    if (index === characters.length) return;

    request(characters[index], (err, res, data) => {
      if (!err) {
        const name = JSON.parse(data).name;
        console.log(name);
        printCharacter(index + 1);
      } else {
        console.error(err);
      }
    });
  };

  printCharacter(0);
});
