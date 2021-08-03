#!/usr/bin/env python3

## create a dictionary
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

## display parts of the dictionary
print( switch["hostname"] )
print( switch["ip"] )

# request a 'fake' key
# print( switch["lynx"] )

## request a 'fake' key with .get() method
print( "first test - .get()" )
print( switch.get("lynx") )

print( "second test - .get()")
print( switch.get("lynx", "the key is in another castle!") )

print("third test - .get()" )
print(switch.get("version") )

print("fourth test - .keys()" )
print( switch.keys() )

print("fifth test - .values()" )
print( switch.values() )

print("sixth test - .pop()" )
switch.pop("version")
print(switch.keys() )
print(switch.values() )

print("seventh test - ADD a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print(switch.values() )

print("eighth test ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print( switch.values() )

