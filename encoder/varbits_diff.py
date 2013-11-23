from varbits import VarBits

class VarBitsDiff(VarBits):
	def bytes_length(self, values):
		diff = [values[0]] + [b - a for a, b in zip(values, values[1:])]
		assert len(diff) == len(values)

		return super(VarBitsDiff, self).bytes_length(diff)
