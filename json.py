import ujson
temp = 52.2
pressure = 1928.3
obj = {
    'temperature': temp,
    'pressure': pressure
}
json_str = ujson.dumps(obj)
