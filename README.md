# QR-Generator
This project is a python based QR generator for my portfolio.

## Features

- Generates a QR code with a specified URL.
- Customizable colors for foreground and background of the QR code.
- Saves the generated QR code as a PNG file ("newgr.png")


## Installation

To use this QR code generation, we need to have Python 3.x installed on our machine.

## How it works?

The script constructs a URL to the QRServer API with the URL we want to encode as data. Then the API request include the color parameters for customizing the QR code.
The script then downloads the generated QR code image and saves it as a PNG file.

## Customization

We can change the URL that the QR code encodes by modifying the data variable in the generator_qr function.  
Additionally, we can customize the foreground and background colors by changing the foreground_color and background_color variables (in hexadecimal format).

Color Values I used in my code:
- Pink: FF69B4
- White: FFFFFF

## Result
The QR code:



![image](https://github.com/user-attachments/assets/963218f5-a22e-4cb2-8f2a-19028cc0df56)


