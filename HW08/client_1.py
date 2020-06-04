"""client"""
import socket
import json
from http_R import HttpRequest

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

print("CLIENT IS RUNNING\n")


with open("urls.txt") as f:
	for url in f:
		http_request = HttpRequest(host='localhost', port=9090, method="GET", data=url[:-1])
		sock.sendall(http_request.request)
		encode_data = sock.recv(2048 * 10)
		data = encode_data.decode("utf-8")
		# data = json.loads(encode_data.decode("utf-8"))
		print(f"{data}\n")

sock.close()
print("\nCLIENT SHUT DOWN")