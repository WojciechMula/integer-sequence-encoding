class CombineTwo(object):
	def __init__(self, name, encoder1, encoder2):
		self.name = name
		self.encoder1 = encoder1
		self.encoder2 = encoder2

	def bytes_length(self, values):
		size1 = self.encoder1.bytes_length(values)
		size2 = self.encoder2.bytes_length(values)

		return min(size1, size2)

