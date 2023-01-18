#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const filmidx in films) {
      const filmname = films[filmidx].characters;
      for (const idx in filmname) {
        if (filmname[idx].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('error ocurred or character not found, Status code:' + response.statusCode);
  }
});
