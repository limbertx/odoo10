
from BaseError import BaseError

class ModelError(BaseError):
	"""
	Clase encargada de manejar las excepciones que se crean en los modelos
	"""
	def __init__(self, expresion, message):
		self.expresion = expresion
		self.message = message