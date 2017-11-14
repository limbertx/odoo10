class ResponseJson(object):
	def __init__(self, 	error, message,	status, values):
		self.error = error
		self.message = message
		self.status = status
		self.values = values