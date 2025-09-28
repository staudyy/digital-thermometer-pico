# Digital Thermometer Pico
A Raspberry Pi Pico powered temperature reader that displays current temperature on a 128x64 OLED display. You can switch between °C and °F with a click of a button. It also visualizes how warm it is with an RGB LED that transitions between blue and red light according to the temperature (24°C - 28°C, easily customizable).

This project is a showcase of a Micropython library I made. I coded classes for controlling (and reading) LEDs, RGB LEDs, Buttons and Thermistors with ease. A class for controlling the OLED Display is not done yet but I am planning to code that as well in the future.

**Check out the [mpy-basic-components](https://github.com/staudyy/mpy-basic-components) library as it is a significant part of this project!**

**[Showcase Video](https://hc-cdn.hel1.your-objectstorage.com/s/v3/199cc552995a48e2e026c271703f9ede09466dc0_pxl_20250928_141131784.mp4)**  
*The display does not really blink it's just a video recording issue.*

## Dependencies
- [mpy-basic-components](https://github.com/staudyy/mpy-basic-components)
- [ssd1306 Library](https://github.com/DIYables/DIYables_MicroPython_OLED)

## Instalation Guide
1. Download ```main.py``` from this repo, ```mpy-basic-components.py```, and the ssd1306 library python file. Rename it to ```ssd1306.py```.
2. Upload all the files to your Raspberry Pi Pico (It has to be running MicroPython firmware.)
3. Check ```main.py``` for correct GPIO Pin connections, or modify them to your liking. You can also watch the [Showcase Video](https://hc-cdn.hel1.your-objectstorage.com/s/v3/199cc552995a48e2e026c271703f9ede09466dc0_pxl_20250928_141131784.mp4) for inspiration.
