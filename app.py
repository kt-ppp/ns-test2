import os
import socket

host = "argocd-repo-server.argocd.svc.cluster.local"
port = 8081

try:
    with socket.create_connection((host, port), timeout=6):
        print("TCP connection: OK")
except OSError as e:
    print(f"TCP connection: FAILED ({e})")
