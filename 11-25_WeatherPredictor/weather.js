/*
Auth: Nate Koike
Date: 25 November 2019
Desc: predict future weather patterns in a city based on past data

Note: this is currently just a terminal application, but i might build an HTML
      interface later
      to run this program use "node weather [weatherKey] [geocodeKey] [city]"
*/

const request = require("request");

// the base url that we will modify for weather requests
const WEATHER = "https://api.darksky.net/forecast/";

// the base url that we will modify for location requests
const LATLNG = ""; // i am still deciding on

// get data from Dark Sky using the key supplied on the given date
function getData(weatherURL) {
  request({ url: weatherURL, json: true }, function(err, res) {
    temp = res.body.currently.temperature;
  });
}

// get the latitude and longitude of a city
function getCoords(city) {
  return;
}

// the main function that will handle all the processing
function main() {
  // get the key from the comamnd line call to the program
  var key = process.argv[2];

  // get the name of the city
  var city = process.argv[3];

  // get the coordinates of the city
  var coords = getCoords(city);
}

main();

console.log(URL);
