# Varnibble encoding

from varnibble import encode_length

class VarnibbleDiff:

	def bytes_length(self, values):
		nibbles = 0
		last = 0

		for value in values:
			v = value - last
			last = value

			nibbles += encode_length(v)

		return (nibbles + 1)/2
