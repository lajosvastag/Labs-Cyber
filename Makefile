.PHONY: test hash crypto

test:
	python3 -m unittest discover -s tests -v

hash:
	python3 labs/02-hashes/hash_lab.py --password-demo

crypto:
	python3 labs/03-criptografia/crypto_lab.py --demo
