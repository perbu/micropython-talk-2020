# Code and notes from my Micropython talk



## Installing Micropython on ESP32 and ESP8266

### Flashing the ESP32
```
esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART write_flash -z 0x1000 esp32spiram-idf4-20200405-v1.12-337-g312c69949.bin
```

### Flashing the ESP8266
```
esptool.py --port /dev/cu.Repleo-CH341-00004114 --baud 57600 write_flash --flash_size=detect 0 esp8266-20200324-v1.12-270-g38ccb4c64.bin
```


## Tools

You'll need pip or pip3 to work in order to install these.

### esptool

```pip3 install esptool```

### pyboard

```pip3 install pyboard```


### rshell

You can find rshell here: https://github.com/dhylands/rshell

