/*
Auth: Nate Koike
Date: 25 November 2019
Desc: predict future weather patterns in a city based on past data. this is
      similar to a Farmer's Almanac, but for (almost) anywhere in the world

Note: this is currently just a terminal application, but i might build an HTML
      interface later
      to run this program use "node weather [weatherKey] [geocodeKey] [city]"
*/

const request = require("request");

// the base url that we will modify for weather requests
const WEATHER = "https://api.darksky.net/forecast/";

var weatherKey; // this will be the key to access the weather api

// the base url that we will modify for location requests
const LATLNG = "http://www.mapquestapi.com/geocoding/v1/address?key=";

var geocodeKey; // this will be the key to access the geocoding api

var COORDS;
var PREDICTED;
var DATA = [];

// get data from Dark Sky on the given date
function getWeather(weatherURL) {
  request({ url: weatherURL, json: true }, function(err, res) {
    stats = res.body.daily.data[0];
    DATA.push(stats);
    // console.log(weatherURL); // this is for debugging purposes
  });
}

// convert the date into the stem of the correct format
// return [MM]-[DD]T00:00:00
function getDate(date) {
  // get the base format for the corrected date, 1 second into the day
  var correct = "T00:00:01";

  // split the date into a usable format
  var splitDate = date.split("/");

  // add add the values so it reads -[MM]-[DD]correct
  for (let i = splitDate.length - 1; i >= 0; i--) {
    // add a leading zero to the term if necessary
    correct =
      splitDate[i].length < 2
        ? "0" + splitDate[i] + correct
        : splitDate[i] + correct;

    // add the delimiter
    correct = "-" + correct;
  }

  return correct;
}

// make a prediction about future weather based on past data
function makePrediction(key, date) {
  // add the key to the url to prepare for data requests
  var URL = WEATHER + key + "/" + COORDS.lat + "," + COORDS.lng + ",";

  // first, make the date into the correct format
  var dateString = getDate(date);

  // get the current year
  var currentYear = new Date().getFullYear();

  // loop through the five years prior to the current one
  for (let i = 1; i < 6; i++) {
    let fetchDate = currentYear - i + dateString;
    getWeather(URL + fetchDate);
  }
}

// get the latitude and longitude of a city using the MapQuest API
function getCoords(city, key) {
  var URL =
    LATLNG +
    key +
    // take JSON in, return JSON
    '&inFormat=json&outFormat=json&json={"location":{"street":"' +
    city + // add the city name to the query
    // disable the map and limit the number of responses to one
    '"},"options":{"thumbMaps":false,"maxResults":"1"}}';

  var latLng;

  request({ url: URL, json: true }, function(err, res) {
    // parse the result to get just the JSON object containing the lat and long
    // coordinates for the city
    COORDS = res.body.results[0].locations[0].displayLatLng;
  });
}

// the main function that will handle all the processing
function main() {
  // get the weather api key from the comamnd line call to the program
  weatherKey = process.argv[2];

  // get the geocoding api key from the comamnd line call to the program
  geocodeKey = process.argv[3];

  // get the name of the city
  const city = process.argv[4];

  // get the date that the user would like from the command line
  const date = process.argv[5];

  // get the coordinates of the city as a JSON object witt lat and lng
  getCoords(city, geocodeKey);

  // delay the running of code so that we get our coords
  // (which are returned asynchronously)
  setTimeout(function() {
    // get the data for the given date
    makePrediction(weatherKey, date);

    // push this even further back in the queue
    setTimeout(function() {
      // the average high temperature
      var high = 0;

      // the average low temperature
      var low = 0;

      // sum all of the daily highs and lows
      for (let i = 0; i < DATA.length; i++) {
        // console.log("high:", parseFloat(DATA[i].temperatureHigh)); // debugging code
        // console.log("low:", parseFloat(DATA[i].temperatureLow)); // debugging code
        high += parseFloat(DATA[i].temperatureHigh);
        low += parseFloat(DATA[i].temperatureLow);
      }

      // calculate an average for the highs and lows
      high /= DATA.length;
      low /= DATA.length;

      // calculate precipitation chance
      // precipitation chance
      var precip = 0;

      // sum all of the daily highs and lows
      for (let i = 0; i < DATA.length; i++) {
        precip += parseFloat(DATA[i].precipProbability);
      }

      // calculate an average for the highs and lows
      precip /= DATA.length;

      // return the results
      PREDICTED = [high, low, precip];
      // deal with asynchronicity
      setTimeout(function() {
        console.log("\nThe predicted high is:", PREDICTED[0]);
        console.log("The predicted low is:", PREDICTED[1]);
        console.log("The predicted precipitation chance is:", PREDICTED[2]);
        console.log();
      }, 0);
    }, 500);
  }, 500);
}

main();
