# Varnibble encoding
from encoder import Encoder

class Varnibble(Encoder):

	def bytes_length(self, values):
		nibbles = sum(encode_length(v) for v in values)

		return (nibbles + 1)/2


class VarnibbleDiff(Varnibble):

	def bytes_length(self, values):
		diff = self.calculate_diff(values)

		return super(VarnibbleDiff, self).bytes_length(diff)


def encode_length(value):
	"encode single value, returns number of nibbles"

	count = 1
	while value > 7:
		value >>= 3
		count  += 1

	return count

