# constant word size [determined]

from math import log


class Minbits:
	name = 'Min bits'

	def minbits_count(self, values):
		entrophy = log(max(values), 2.0)

		return int(max(1.0, entrophy))

	def bytes_length(self, values):
		bits = len(values) * self.minbits_count(values)

		return 1 + (bits + 7)/8
