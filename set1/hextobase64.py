#!/usr/bin/python

base64dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
print "Enter a hex string: "
hex_input = raw_input().strip()

def padto(string, length, c):
    return c * (length - len(string)) + string

def hex2bytearr(hexstring):
    if len(hexstring) % 2 != 0:
        hexstring = "0"+hexstring
    return [int(hexstring[x] + hexstring[x+1], 16) for x in range(0, len(hexstring), 2)]

def bytearr2binstring(bytearr):
    return "".join([padto(bin(x)[2:], 8, '0') for x in bytearr])

temp = bytearr2binstring(hex2bytearr(hex_input))
#correct
#maps a 6 bit pattern to the respective dict
def base64map(bits):
    a = int(bits, 2)
    return base64dict[a]

#match a triplet of octets
def mapoctets3(octet3):
    temp = ""
    for x in range(4):
        temp += base64map(octet3[x*6:x*6+6])
    return temp

def map_last_octet3(octet3, padlen):
    temp = ""
    if padlen >= 12:
        iterations = 2
    elif padlen >= 6:
        iterations = 3
    else:
        iterations = 4
    for x in range(iterations):
        temp += base64map(octet3[x*6:x*6+6])

    temp += '=' * (4 - iterations)
    return temp

#pad strings at the back such that it is divisible by 24
def padstring(bitstring):
    padlen =  (24 - len(bitstring) % 24)
    bitstring = bitstring + "0"  * padlen
    return bitstring, padlen

#splits the bitstring to a list of list of 3 octets
def split3octets(bitstring):
    return [bitstring[x:x+24]  for x in range(0, len(bitstring), 24)]
base64string = ""

if len(temp) % 24 == 0:
    octets3 = split3octets(temp)
    for octet3 in octets3:
        base64string += mapoctets3(octet3)
else:
    bs, padlen = padstring(temp)
    octets3 = split3octets(bs)
    for octet3 in octets3[:-1]:
        base64string += mapoctets3(octet3)
    base64string += map_last_octet3(octets3[-1], padlen)

print base64string

