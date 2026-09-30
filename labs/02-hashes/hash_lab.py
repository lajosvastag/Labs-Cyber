#!/usr/bin/env python3
"""Demonstrações locais de integridade e armazenamento de senhas."""
import argparse, hashlib, hmac, secrets


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def derive_password(password: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 240_000)
    return salt, digest


def verify_password(password: str, salt: bytes, expected: bytes) -> bool:
    _, candidate = derive_password(password, salt)
    return hmac.compare_digest(candidate, expected)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text")
    parser.add_argument("--password-demo", action="store_true")
    args = parser.parse_args()
    if args.text is not None:
        print(sha256(args.text))
    if args.password_demo:
        salt, digest = derive_password("senha-ficticia")
        print("salt:", salt.hex())
        print("verificador:", digest.hex())
        print("senha correta:", verify_password("senha-ficticia", salt, digest))
        print("senha incorreta:", verify_password("outra", salt, digest))
    if args.text is None and not args.password_demo:
        parser.error("use --text ou --password-demo")

if __name__ == "__main__":
    main()
