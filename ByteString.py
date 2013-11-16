class ByteString(object):
	"filelike byte string access"

	def __init__(self, data):
		self.data = data
		self.index = 0

	def eof(self):
		return self.index == len(self.data)

	def peek(self):
		return ord(self.data[self.index])

	def get(self):
		if self.eof():
			print self.index, repr(self.data)
			raise StopIteration

		b = self.peek()
		self.index += 1

		return b


if __name__ == '__main__':
	data = chr(50) + chr(80)

	buf = ByteString(data)

	assert buf.eof() == False

	assert buf.peek() == 50
	assert buf.peek() == 50
	assert buf.eof() == False

	assert buf.get() == 50
	assert buf.get() == 80
	assert buf.eof() == True
