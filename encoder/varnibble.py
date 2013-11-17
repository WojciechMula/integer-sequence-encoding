# Varnibble encoding

class Varnibble:
	name = 'Varnibble'

	def bytes_length(self, values):
		nibbles = sum(encode_length(v) for v in values)

		return (nibbles + 1)/2


def encode_length(value):
	"encode single value, returns number of nibbles"

	count = 1
	while value > 7:
		value >>= 3
		count  += 1

	return count

