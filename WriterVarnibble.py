class WriterVarnibble:
	def init(self):
		self.bytes  = ''
		self.last   = None

	def get_bytes(self):
		if self.last is None:
			return self.bytes
		else:
			return self.bytes + chr(self.last)

	def encode_uint(self, value):
		while value > 0:
			if value > 7:
				v = (value & 0x07) | 0x08
			else:
				v = (value & 0x07)

			self.write_nibble(v)

			value >>= 3

	def append(self, bytes):
		for byte in map(ord, bytes):
			self.write_nibble(byte & 0x0f)
			self.write_nibble((byte & 0xf0) >> 4)

	def write_nibble(self, nibble):
		assert 0 <= nibble <= 15

		if self.last is None:
			self.last = nibble
		else:
			self.bytes += chr(self.last | (nibble << 4))
			self.last = None


if __name__ == '__main__':
	writer = WriterVarnibble()
	writer.init()

	assert writer.get_bytes() == ''

	writer.write_nibble(10)

	assert writer.get_bytes() == chr(10)

	writer.append('word')

	assert len(writer.get_bytes()) == 5


	writer.init()
	writer.encode_uint(0x2f)
	
	# 31 = 0x1f = 0b0010_1111
	# encoded as  0b0101_1111 = 0x5f

	assert writer.get_bytes() == chr(0x5f)
