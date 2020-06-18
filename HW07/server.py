#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from http_R import HttpResponse
from parsing import func_parsing
import json

def server(func_server, host='localhost', port=9090, count_listen=1):

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
	sock.bind((host, port))
	sock.listen(count_listen)

	print("SERVER IS RUNNING\n")
	while True:
		try:
			conn, addr = sock.accept()
			print(f"New connection from {addr}")
		except:
			break
		while True:
			encode_request = conn.recv(1024)
			if not encode_request:
				print()
				break
			try:
				request = json.loads(encode_request.decode("utf-8"))
			except:
				print("Неправильный url")
			print(request)
			try:
				response = func_parsing(request['data'])
				data_response = response.data
				status_code = response.status_code
				if data_response:
					conn.sendall(data_response)
				else:
					status_code = 404
					conn.sendall(HttpResponse(status_code=404, 
						data={'error': '404', 'message': 'not found'}).data)
			except:
				status_code = 404
				conn.sendall(HttpResponse(status_code=404,
					data={'error': '404', 'message': 'not found'}).data)
			# print(f"{status_code}\n")
		conn.close()
