import json

class HttpRequest:

	def __init__(self, host, port, method, data=None):
		self.host = host
		self.port = port
		self.method = method
		self.data = data
		self.request_dict = {'host': host, "port": port,
			"method": method, "data": data}
		self.request = json.dumps(self.request_dict, ensure_ascii=False).encode("utf-8")

class HttpResponse:

	def __init__(self, status_code=200, type_data='str', data=None):
		self.status_code = status_code
		self.type_data = type_data
		self.data = data
		if status_code == 404:
			self.data = json.dumps(self.data, ensure_ascii=False).encode("utf-8")

class JsonResponse:
	
	def __init__(self, status_code=200, type_data='json', data=None):
		self.status_code = status_code
		self.type_data = type_data
		self.data = data
		if not isinstance(self.data, dict):
			raise TypeDataResponseError(f"type data responce is not valid")
		self.data = json.dumps(self.data, ensure_ascii=False).encode("utf-8")