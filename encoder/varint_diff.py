# Varint with difference encoding

from varint import encode

class VarintDiff:
	def bytes_length(self, values):
		size = 0
		last = 0

		for value in values:
			v = value - last
			last = value

			size += len(encode(v))

		return size
