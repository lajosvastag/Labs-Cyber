# Laboratório de Cibersegurança

**Autoria:** Luís Brito

Pequenos ambientes locais para estudar fundamentos de segurança da informação com responsabilidade. O projeto foi desenhado para servir como laboratório de estudos e portfólio técnico.

> **Escopo seguro:** todos os exercícios usam dados fictícios, executam em `127.0.0.1` e não coletam credenciais reais, não enviam mensagens e não fazem varredura de redes externas.

## Trilhas

| Lab | Tema | O que praticar |
|---|---|---|
| `01-phishing-awareness` | Phishing | identificar sinais de fraude em uma página estática, sem formulário de envio |
| `02-hashes` | Hashes | SHA-256, comparação segura e derivação de senha com PBKDF2 |
| `03-criptografia` | Criptografia | cifra de César, XOR didático e limites de algoritmos caseiros |
| `04-portas` | Portas | servidor TCP local e verificador restrito a localhost |
| `05-autenticacao` | Autenticação | armazenamento de senha com `scrypt`, sessão e proteção contra timing leaks |

## Requisitos

- Python 3.10+
- Nenhuma dependência externa para os labs básicos

## Execução rápida

```bash
python3 labs/02-hashes/hash_lab.py --text "mensagem de estudo"
python3 labs/03-criptografia/crypto_lab.py --demo
python3 labs/04-portas/port_lab.py server
# em outro terminal:
python3 labs/04-portas/port_lab.py check --port 8765
python3 labs/05-autenticacao/auth_lab.py
```

Abra `labs/01-phishing-awareness/index.html` diretamente no navegador. O lab de autenticação ficará disponível somente em `http://127.0.0.1:8080`.

## Roteiro sugerido

1. Leia o `README.md` de cada lab.
2. Execute o exemplo mínimo.
3. Altere uma variável marcada como exercício.
4. Registre observações e evidências em um caderno próprio.
5. Rode `python3 -m unittest discover -s tests -v` antes de enviar alterações.

## Aviso ético e legal

Use este repositório somente em ambientes próprios ou com autorização explícita. Não reutilize os exemplos para capturar senhas, enviar phishing, testar hosts de terceiros ou contornar controles de acesso. Para sistemas reais, prefira bibliotecas e serviços mantidos, revisão de segurança e políticas organizacionais.

## Licença

MIT — consulte [`LICENSE`](LICENSE).
