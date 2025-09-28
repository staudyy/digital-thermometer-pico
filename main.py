import asyncio
from machine import Pin, I2C

import ssd1306
from mpy_basic_components import TemperatureSensor, RgbLed, Button

HUE_RANGE = (240, 360)
TEMP_RANGE = (25, 28)
OLED_WIDTH = 128
OLED_HEIGHT = 64
UPDATE_SPEED = 1/25

sensor = TemperatureSensor(26)
led = RgbLed(11, 10, 9)
toggle_btn = Button(12)
toggle_fh_btn = Button(13)
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
oled = ssd1306.OLED_SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
toggled = True
toggled_fh = False

async def toggle():
    global toggled
    toggled = not toggled
    if not toggled:
        await asyncio.sleep(UPDATE_SPEED)
        led.off()
        oled.clear_display()
        oled.display()

def toggle_fh():
    global toggled_fh
    toggled_fh = not toggled_fh

def led_logic(led, temp):
    if temp <= TEMP_RANGE[0]:
        led.set_color_hsv(HUE_RANGE[0] / 360, 1.0, 1.0)
    elif temp >= TEMP_RANGE[1]:
        led.set_color_hsv(HUE_RANGE[1] / 360, 1.0, 1.0)
    else:
        hue_range_size = HUE_RANGE[1] - HUE_RANGE[0]
        temp_range_size = TEMP_RANGE[1] - TEMP_RANGE[0]
        hue = (((temp - TEMP_RANGE[0]) / temp_range_size) * hue_range_size) + HUE_RANGE[0]
        led.set_color_hsv(hue / 360, 1.0, 1.0)

def display_logic(oled, temp, is_fh=False):
    oled.clear_display()
    if is_fh:
        temp_str = f"{str(temp)}\x7FF"
    else:
        temp_str = f"{str(temp)}\x7FC"

    # Get the text bounds (width and height) of the string
    x1, y1, width, height = oled.get_text_bounds(temp_str, 0, 0)

    # Set cursor to the calculated centered position
    cursor_x = (oled.WIDTH - width) // 2
    cursor_y = (oled.HEIGHT - height) // 2
    oled.set_cursor(cursor_x, cursor_y)
    # Print the text on the display
    oled.write(temp_str)

    # Refresh the display to show the text
    oled.display()

async def main():
    sensor.start_measuring(0.01, 50)
    toggle_btn.on_click_async(toggle)
    toggle_fh_btn.on_click(toggle_fh)
    oled.set_text_size(3)

    while True:
        temp = sensor.get_stable_temperature(3)
        if toggled:
            led_logic(led, temp)

            if toggled_fh:
                temp = sensor.get_stable_temperature_fahrenheit(3)
            else:
                temp = sensor.get_stable_temperature(3)
            display_logic(oled, round(temp, 1), toggled_fh)

        await asyncio.sleep(UPDATE_SPEED)

asyncio.run(main())