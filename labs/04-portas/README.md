# 04 — Portas

Este lab cria um servidor TCP em `127.0.0.1:8765` e testa somente esse endereço. Não altere o host para examinar sistemas que não sejam seus.

```bash
python3 port_lab.py server
# outro terminal
python3 port_lab.py check --port 8765
```

O objetivo é relacionar porta, socket, serviço e superfície de exposição — não fazer reconnaissance em redes reais.
