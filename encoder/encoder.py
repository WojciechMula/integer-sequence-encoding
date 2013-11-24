class Encoder(object):
	def bytes_length(self, values):
		raise NotImplementedError()

	def calculate_diff(self, values):
		diff = [values[0]] + [b - a for a, b in zip(values, values[1:])]
		assert len(diff) == len(values)

		return diff
