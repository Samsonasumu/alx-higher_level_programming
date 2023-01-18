#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const ep = process.argv[2];
request(url + ep, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonobj = JSON.parse(body);
    console.log(jsonobj.title);
  } else {
    console.log('error ocurred or chapter not found. Status code: ' + response.statusCode);
  }
});
