# constant word size [determined]
#
# - first byte store number of bits per filed
# - 4 bytes saves first value in array
# - next is a array of bitfields - each bitfield contain difference

from minbits import Minbits


class MinbitsDiff(Minbits):
	name = 'Min bits (diff)'

	def bytes_length(self, values):
		diff = [curr - prev for prev, curr in zip(values, values[1:])]
		bits = len(diff) * self.minbits_count(diff)

		return 1 + 4 + (bits + 7)/8
