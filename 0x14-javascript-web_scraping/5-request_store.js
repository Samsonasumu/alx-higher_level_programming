#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filepath, body, 'utf-8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
