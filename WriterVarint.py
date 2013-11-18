from encoder.varint import encode

class WriterVarint:
	def init(self):
		self.bytes = ''

	def get_bytes(self):
		return self.bytes

	def encode_uint(self, value):
		self.bytes += encode(value)

	def append(self, bytes):
		self.bytes += bytes
