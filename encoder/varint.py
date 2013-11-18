# Varint encoding

class Varint:

	def bytes_length(self, values):
		return sum(len(encode(v)) for v in values)


def encode(value):
	"encode single value, returns bytes"

	bytes = ''
	while value > 127:
		byte    = (value & 0x7f) | 0x80
		bytes  += chr(byte)
		value >>= 7

	bytes += chr(value)

	return bytes


def decode(buffer):
	value = 0
	shift = 0
	while True:
		b = buffer.get()
		if b <= 127:
			value = value | (b << shift)
			return value

		else:
			b = b & 0x7f
			value = value | (b << shift)
			shift += 7


if __name__ == '__main__':
	from buffer import Buffer

	for x in [15, 127, 128, 4324234]:
		bytes = encode(x)
		y = decode(Buffer(bytes))

		assert x == y
