import sys

import framebuf
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

ID = 0
SCL_PIN = 17
SDA_PIN = 16

DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64


def init_i2c(id_, scl_pin, sda_pin):
    # Initialize I2C device
    i2c = I2C(id_, scl=Pin(scl_pin), sda=Pin(sda_pin))
    i2c_addr = [hex(ii) for ii in i2c.scan()]

    if not i2c_addr:
        print("No I2C Display Found")
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c))

    return i2c


def load_img_data():
    with open("./lenna.dat", "rb") as f:
        return f.read(), 128, 64


def display_logo(oled):
    data, width, height = load_img_data()

    buffer = bytearray(data)
    fb = framebuf.FrameBuffer(buffer, width, height, framebuf.MONO_HLSB)

    oled.fill(0)
    oled.blit(fb, 0, 0)
    oled.show()


def main():
    i2c = init_i2c(id_=ID, scl_pin=SCL_PIN, sda_pin=SDA_PIN)
    oled = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)
    display_logo(oled)


if __name__ == "__main__":
    main()
