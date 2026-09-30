# 05 — Autenticação

Servidor HTTP local com uma conta fictícia (`aluno` / `laboratorio-123`). A senha é armazenada como derivação `scrypt`, a comparação usa `hmac.compare_digest` e o cookie de sessão é aleatório.

```bash
python3 auth_lab.py
# abra http://127.0.0.1:8080
```

O exemplo é propositalmente mínimo e não deve ser colocado em produção. Exercícios: adicionar expiração da sessão, limite de tentativas e CSRF token. Nunca substitua provedores de identidade ou bibliotecas mantidas em sistemas reais.
