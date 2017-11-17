#!/usr/bin/python

# takes a decimal representation of a byte and returns a
# hexadecimal representation padded to 2 characters
def hex_pad(b):
    hb = hex(b)[2:]
    if len(hb) == 1:
        return "0" + hb
    return hb


def hex_to_bytes(h):
    if len(h) % 2 != 0:
        h = "0" + h
    return [int(h[x] + h[x+1], 16) for x in range(0, len(h), 2)]

def bytes_to_hex(bs):
    return "".join([hex_pad(b) for b in bs])

def fixed_xor(plain_hex, key_hex):
    plain_bytes = hex_to_bytes(plain_hex)
    key_bytes = hex_to_bytes(key_hex)
    cipher_bytes = []
    for p, k in zip(plain_bytes, key_bytes):
        cipher_bytes.append(p ^ k)
    return cipher_bytes


if __name__ == "__main__":
    print "Enter a plaintext hex:"
    p_hex = raw_input().strip()
    print "Enter a key hex"
    k_hex = raw_input().strip()
    print "Your cipher is\n", bytes_to_hex(fixed_xor(p_hex, k_hex))


