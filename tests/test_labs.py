import sys, unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.extend([str(ROOT / 'labs/02-hashes'), str(ROOT / 'labs/03-criptografia')])
import hash_lab, crypto_lab

class LabTests(unittest.TestCase):
    def test_sha256_known_value(self):
        self.assertEqual(hash_lab.sha256('abc'), 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')
    def test_password_verification(self):
        salt, digest = hash_lab.derive_password('segredo')
        self.assertTrue(hash_lab.verify_password('segredo', salt, digest))
        self.assertFalse(hash_lab.verify_password('errado', salt, digest))
    def test_caesar_round_trip(self):
        encoded = crypto_lab.caesar('Abc XYZ!', 3)
        self.assertEqual(crypto_lab.caesar(encoded, -3), 'Abc XYZ!')
    def test_xor_round_trip(self):
        self.assertEqual(crypto_lab.xor_bytes(crypto_lab.xor_bytes(b'abc', b'k'), b'k'), b'abc')

if __name__ == '__main__': unittest.main()
