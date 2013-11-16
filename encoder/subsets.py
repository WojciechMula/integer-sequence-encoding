import varint

class Subsets(object):
	def __init__(self, cutoff = 0):
		self.cutoff = cutoff

	def bytes_length(self, values):
		return len(self.encode(values))

	def encode(self, values):
		bytes = ''
		prev = 0
		for value, subset in self.find_subsets(values):
			value_to_encode = (value - prev)*2
			if subset is not None:
				# lowest bit is set if subset is present
				value_to_encode += 1

			bytes += varint.encode(value_to_encode)
			if subset is not None:
				bytes += self.encode_subset(value, subset)

			prev = value

		return bytes

	def find_subsets(self, values):
		raise NotImplemented()


	def encode_subset(self, first_value, subset):
		"bitset encoding on 32 bit word"
		assert len(subset) <= 32

		dword = 0
		for v in subset:
			shift = (v - first_value - 1)
			assert shift >= 0 and shift < 32
			b = 1 << shift
			dword |= b

		return chr(dword & 0xff) + \
		       chr((dword >> 8) & 0xff) + \
		       chr((dword >> 16) & 0xff) + \
		       chr((dword >> 24) & 0xff)
