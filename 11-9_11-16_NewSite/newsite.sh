#!/bin/bash
# the line above this lets us put this in our path and run it as a command

# make a new directory for the site
mkdir new_site

# enter the directory
cd new_site

# make the directories for css and js files
mkdir css
mkdir scripts
mkdir images

# make the new index.html file and fill it with the beginnigns of a website
echo "<!DOCTYPE html>
<html lang=\"en-US\"> <!-- this page is in English -->
  <head>
    <meta charset=\"UTF-8\" /> <!-- use UTF-8 encoding -->
    <title></title> <!-- put the title of your site here -->
    <link rel=\"stylesheet\" type=text/css href=\"css/styles.css\" />
    <!-- <link rel=\"icon\" href=\"images/icon.png\" /> -->
  </head>
  <body></body> <!-- put the body of your site here -->
</html>" > index.html

# go into the css folder
cd css

# make a blank template for css
echo > styles.css

# go into the scrips directory
cd ../scripts

# make a new script template file
echo > script.js
