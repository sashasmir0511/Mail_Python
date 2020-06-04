#!/usr/bin/env python
# -*- coding: utf-8 -*-                                                                                                                     

import socket
import json
from http_R import HttpRequest

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

print("CLIENT IS RUNNING")

while True:
	try:
		print("print url:")
		url = str(input())
		http_request = HttpRequest(host='local', port = 9090,
			method = "GET", data = url)
		sock.sendall(http_request.request)
		encode_data = sock.recv(1024)
		data = json.loads(encode_data.decode("utf-8"))
		print(f"{data}\n")
	except:
		sock.close()
		break