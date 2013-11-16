# constant word size [determined]

from minbits import Minbits


class MinbitsDiff(Minbits):
	name = 'Min bits (diff)'

	def bytes_length(self, values):
		diff = [curr - prev for prev, curr in zip(values, values[1:])]
		bits = len(diff) * self.minbits_count(diff)

		return 1 + 4 + (bits + 7)/8
