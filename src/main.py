from machine import Pin, PWM, I2C
import ssd1306

f1 = PWM(Pin(1), freq=2000, duty_u16=32768/2)
f2 = PWM(Pin(2), freq=5000, duty_u16=32768/2)

clkiic = I2C(0)

disiic = I2C(1, sdaPin=Pin(14), sclPin=Pin(15))
dis = ssd1306.SSD1306_I2C(128, 64, disiic)
dis.poweron()

buf = bytearray(7)
buf_old = bytearray(7)

clkiic.writeto(0x68, 7)
clkiic.readfrom(0x68, buf_old)

while True:
    clkiic.writeto(0x68, 7)
    clkiic.readfrom(0x68, buf)
    buf_t = str.from_bytes(buf, 'little')
    time = f"{str(buf_t[2]):02}:{str(buf_t[1]):02}:{str(buf_t[0]):02}"
    date = f"{str(buf_t[4]):02}/{str(buf_t[5]):02}/{str(buf_t[6]):02}"

    dis.text(time,0,0,1)
    dis.text(date,0,0,2)
    dis.show()

    if buf[1] > buf_old[1] + 5:
        f1.duty_u16(0)
        f2.duty_u16(0)
    
    
    