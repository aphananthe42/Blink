import machine
import ssd1306
import time

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0,sda=sda, scl=scl, freq=400000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    oled.text("So long, and", 0, 5)
    oled.show()
    time.sleep(2)
    oled.text("thanks for", 0, 15)
    oled.show()
    time.sleep(2)
    oled.text("all the fish.", 0, 25)
    oled.show()
    time.sleep(2)
    oled.text("-- Douglas Adams", 0, 45)
    oled.show()
    time.sleep(2)
    oled.fill(0)
