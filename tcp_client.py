#!/usr/bin/python3.12
from sys import argv
from socket import socket, AF_INET, SOCK_STREAM


def run(host=argv[1], port=80):
    """Run TCP client. How to use: python tcp_client.py google.com"""
    tcp_client = socket(AF_INET, SOCK_STREAM)
    tcp_client.connect((host, port))
    tcp_client.send(f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())

    server_response = tcp_client.recv(4096).decode()
    print(server_response)
    tcp_client.close()


run()
