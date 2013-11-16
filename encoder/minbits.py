# constant word size [determined]
#
# - first byte store number of bits per filed
# - next is a array of bitfields - each bitfield contain value

from math import log


class Minbits:
	name = 'Min bits'

	def minbits_count(self, values):
		# minimum bits count to store maximum value from array
		entrophy = log(max(values), 2.0)

		return int(max(1.0, entrophy))

	def bytes_length(self, values):
		bits = len(values) * self.minbits_count(values)

		return 1 + (bits + 7)/8
