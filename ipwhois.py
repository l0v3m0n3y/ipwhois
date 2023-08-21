import requests
class Client():
	def __init__(self):
		self.api="http://ipwho.is"
	def get_my_ip(self):
		return requests.get(f"{self.api}/").json()
	def get_ip(self,ip: str):
		return requests.get(f"{self.api}/{ip}").json()