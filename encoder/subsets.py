import varint

class Subsets(object):
	def __init__(self, cutoff, writer):
		self.cutoff = cutoff
		self.writer = writer

	def bytes_length(self, values):
		return len(self.encode(values))

	def encode(self, values):
		prev = 0

		writer = self.writer
		writer.init()
		for value, subset in self.find_subsets(values):
			value_to_encode = (value - prev)*2
			if subset is not None:
				# lowest bit is set if subset is present
				value_to_encode += 1

			writer.encode_uint(value_to_encode)
			if subset is not None:
				writer.append(self.encode_subset(value, subset))

			prev = value

		return writer.get_bytes()

	def decode(self, buffer):
		list = []
		prev = 0
		while not buffer.eof():
			encoded_value = varint.decode(buffer)
			have_subset = encoded_value & 0x1

			value = (encoded_value >> 1) + prev
			prev = value

			list.append(value)

			if have_subset:
				subset = buffer.get() | (buffer.get() << 8) | (buffer.get() << 16) | (buffer.get() << 24)
				for i in xrange(32):
					if subset & (1 << i):
						list.append(value + i + 1)

		return list

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

