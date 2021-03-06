from machine import Pin, I2C
import time
import ssd1306
import bmp280
import network
import ujson
from umqtt.robust import MQTTClient

pinScl = const(22)
pinSda = const(21)
addr_oled = const(60)  # 0x3c
addr_bmp = const(118)  # 0x76
h_size = const(32)     # display heigh in pixels
w_size = const(128)    # display width in pixels

oled_conn = False
bmp_conn = False
temp = 0
pr = 0
hum = 0

oled = None
bmp = None

mqtt_server = "test.mosquitto.org"
uuid = "fb317f06-c3dc-4757-8373-e2f7e606c915"
topic = 'knowit/objectnet/hardwareguild/micropython0'


def wlan_connect():
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    if not sta.isconnected():
        print('Connecting')
        sta.connect('ssid', 'password')
        while not sta.isconnected():
            time.sleep(0.1)
            print('.', end='')
        print('Connected!')
    print('Network:', sta.ifconfig())


wlan_connect()

mqtt_client = client = MQTTClient(uuid,
                                  mqtt_server)
mqtt_client.connect()


def send_mqtt(temp, pressure):
    obj = {
        'temperature': temp,
        'pressure': pressure
    }
    json_str = ujson.dumps(obj)
    mqtt_client.publish(topic, json_str)


i2c = I2C(scl=Pin(pinScl),
          sda=Pin(pinSda))

print('Scanning i2c bus...')
devices = i2c.scan()
if len(devices) == 0:
    print("No i2c devices found.")
else:
    print('i2c devices found:', len(devices))
    for device in devices:
        if device == addr_oled:
            print('OLED at ', addr_oled)
            oled_conn = True
            oled = ssd1306.SSD1306_I2C(w_size, h_size, i2c, addr_oled)
        if device == addr_bmp:
            print('BMP at ', addr_bmp)
            bmp_conn = True
            bmp = bmp280.BMP280(i2c_bus=i2c, addr=addr_bmp)
            bmp.use_case(bmp280.BMP280_CASE_WEATHER)
            bmp.force_measure()

        print(device)

while True:
    if bmp_conn:
        print("BMP280 values:")
        temp = bmp.temperature
        pr = bmp.pressure
        print("temp:", temp)
        print("pr:", pr)
        send_mqtt(temp, pr)

    if oled_conn:
        oled.fill(0)
        if bmp_conn:
            oled.text("Temp: {}".format(temp), 0, 0)
            oled.text("Pr: {}".format(pr), 0, 10)
            oled.show()
        else:
            oled.text("BMP N/A", 0, 0)
            oled.show()
    else:
        print('No i2c display')
    time.sleep_ms(5000)
