#!/usr/bin/env python3
"""Autenticação mínima e local; não usar em produção."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.cookies import SimpleCookie
import hashlib, hmac, secrets, urllib.parse

HOST, PORT = '127.0.0.1', 8080
USERNAME, DEMO_PASSWORD = 'aluno', 'laboratorio-123'
SALT = secrets.token_bytes(16)
PASSWORD_HASH = hashlib.scrypt(DEMO_PASSWORD.encode(), salt=SALT, n=2**14, r=8, p=1)
SESSIONS: set[str] = set()


def valid_password(value: str) -> bool:
    candidate = hashlib.scrypt(value.encode(), salt=SALT, n=2**14, r=8, p=1)
    return hmac.compare_digest(candidate, PASSWORD_HASH)


def page(message: str = '') -> bytes:
    return f'''<!doctype html><meta charset="utf-8"><title>Auth Lab</title>
    <h1>Autenticação local</h1><p>{message}</p>
    <form method="post"><label>Usuário <input name="username" autocomplete="off"></label>
    <label>Senha <input type="password" name="password"></label><button>Entrar</button></form>
    <p>Dados fictícios: aluno / laboratorio-123</p>'''.encode()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        cookie = SimpleCookie(self.headers.get('Cookie', ''))
        sid = cookie.get('sid')
        if sid and sid.value in SESSIONS: body = page('Sessão autenticada. Estude a validação do cookie.')
        else: body = page('Nenhuma sessão autenticada.')
        self.send_response(200); self.send_header('Content-Type', 'text/html; charset=utf-8'); self.end_headers(); self.wfile.write(body)

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0)); data = urllib.parse.parse_qs(self.rfile.read(length).decode())
        username = data.get('username', [''])[0]; password = data.get('password', [''])[0]
        if hmac.compare_digest(username, USERNAME) and valid_password(password):
            sid = secrets.token_urlsafe(24); SESSIONS.add(sid)
            self.send_response(303); self.send_header('Location', '/'); self.send_header('Set-Cookie', f'sid={sid}; HttpOnly; SameSite=Strict'); self.end_headers()
        else:
            self.send_response(401); self.send_header('Content-Type', 'text/html; charset=utf-8'); self.end_headers(); self.wfile.write(page('Falha de autenticação.'))

    def log_message(self, fmt, *args): print(fmt % args)

if __name__ == '__main__':
    print(f'Auth Lab em http://{HOST}:{PORT} — Ctrl+C para sair')
    HTTPServer((HOST, PORT), Handler).serve_forever()
