from encoder import Encoder


class DWord(Encoder):
	"constant word size = 32 bits"

	def bytes_length(self, values):
		return len(values) * 4
