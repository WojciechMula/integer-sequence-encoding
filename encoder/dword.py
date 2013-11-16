# constant word size = 32 bits

class DWord:
	name = '32 bits words'

	def bytes_length(self, values):
		return len(values) * 4
