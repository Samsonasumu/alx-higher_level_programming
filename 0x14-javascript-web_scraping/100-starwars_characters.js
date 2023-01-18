#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const ep = process.argv[2];
request(url + ep, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsobj = JSON.parse(body);
    console.log(jsobj.characters);
    for (const index in jsobj.characters) {
      const charusr = jsobj.characters[index];
      request(charusr, function (err, response, body) {
        if (err) {
          console.log(err);
        } else if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.log('error ocurred, Status code:' + response.statusCode);
        }
      });
    }
  } else {
    console.log('error ocurred, Status code: ' + response.statusCode);
  }
});
