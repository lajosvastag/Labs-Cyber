# 02 — Hashes

`hash_lab.py` demonstra SHA-256 para integridade, comparação com `hmac.compare_digest` e PBKDF2-HMAC-SHA256 para derivar um verificador de senha com salt aleatório.

```bash
python3 hash_lab.py --text "mensagem de estudo"
python3 hash_lab.py --password-demo
```

Hash não é criptografia reversível. Para aplicações reais, prefira Argon2id, scrypt ou bcrypt por meio de bibliotecas mantidas; o exemplo usa a biblioteca padrão apenas para fins didáticos.
