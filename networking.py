import time
import network

def wlan_connect():
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    if not sta.isconnected():
        print('Connecting', end='')
        sta.connect('ssid', 'password')
        while not sta.isconnected():
            time.sleep(0.1)
            print('.', end='')
        print('Connected!')
    print('Network:', sta.ifconfig())

wlan_connect()
