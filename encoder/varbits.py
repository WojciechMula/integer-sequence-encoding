class VarBits(object):
	def bytes_length(self, values):
		best_bits = 1
		best_bits_len = self.get_bits_len(best_bits, values)

		# find shortest representation
		for bits in xrange(2, 16):

			bits_len = self.get_bits_len(bits, values)
			if bits_len < best_bits_len:
				best_bits = bits
				best_bits_len = bits_len
		
		# save 1 byte - number of bits, then rest varbits array
		return 1 + (best_bits_len + best_bits - 1)/8

	def get_bits_len(self, bits, values):
		limit = 2**bits - 1
		
		return sum(get_bits_len(v, bits, limit) for v in values)


def get_bits_len(value, bits, limit):
	"returns number of bits required to save value"

	size = 0
	while value > limit:
		size += bits + 1
		value >>= bits

	size += bits + 1

	return size


if __name__ == '__main__':
	from varint import encode as varint_encode
	from varnibble import encode_length

	for i in [1, 7, 15, 255, 2000, 30000]:
		assert get_bits_len(i, 3, 2**3 - 1) == encode_length(i) * 4

		assert get_bits_len(i, 7, 2**7 - 1) == len(varint_encode(i)) * 8
