#!/usr/bin/env python3
import argparse


def caesar(text: str, shift: int) -> str:
    out = []
    for char in text:
        base = ord('A') if char.isupper() else ord('a')
        if char.isalpha(): out.append(chr((ord(char)-base+shift)%26+base))
        else: out.append(char)
    return ''.join(out)


def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes(value ^ key[i % len(key)] for i, value in enumerate(data))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--caesar'); parser.add_argument('--shift', type=int, default=3)
    parser.add_argument('--demo', action='store_true')
    args = parser.parse_args()
    if args.caesar is not None: print(caesar(args.caesar, args.shift))
    if args.demo:
        message, key = b'estudo local', b'lab'
        encoded = xor_bytes(message, key)
        print('César:', caesar('Segurança', 3))
        print('XOR (hex):', encoded.hex())
        print('XOR revertido:', xor_bytes(encoded, key).decode())

if __name__ == '__main__': main()
