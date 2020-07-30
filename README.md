# bitcoinTicker

A bitcoin price ticker I made using JSON and Python. It is displayed on a 8x32 dotmatrix display.

## requirements: 

* luma.led_matrix
* rm-hull/bitcoin-bar was helpful in this creation

## Display: 
<p>
  <a name="top" href="https://github.com/nolimitcarter/bitcoinTicker">
    <img height="200px" width="200px" src="pics/dotmatrix.jpg">
  </a>
</p>

## Usage: 

Intro to webscraping. It's a pretty simple program. All it does is create the device, makes a request to the website which is in json format, loads in the data, and picks what to show on the dotmatrix. You could also redirect it to a file.
