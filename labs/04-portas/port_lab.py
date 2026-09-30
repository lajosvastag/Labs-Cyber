#!/usr/bin/env python3
import argparse, socket

HOST = '127.0.0.1'
DEFAULT_PORT = 8765

def serve(port: int) -> None:
    with socket.socket() as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, port)); sock.listen(1)
        print(f'Servidor didático em http://{HOST}:{port} — Ctrl+C para sair')
        while True:
            conn, address = sock.accept()
            with conn:
                conn.recv(1024)
                conn.sendall(b'LAB OK\n')
                print('Conexão local recebida de', address[0])

def check(port: int) -> None:
    with socket.socket() as sock:
        sock.settimeout(1)
        result = sock.connect_ex((HOST, port))
    print(f'{HOST}:{port}: ' + ('aberta' if result == 0 else 'fechada'))

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest='command', required=True)
server = sub.add_parser('server'); server.add_argument('--port', type=int, default=DEFAULT_PORT)
checker = sub.add_parser('check'); checker.add_argument('--port', type=int, default=DEFAULT_PORT)
args = parser.parse_args()
if not 1 <= args.port <= 65535: parser.error('porta inválida')
if args.command == 'server': serve(args.port)
else: check(args.port)
