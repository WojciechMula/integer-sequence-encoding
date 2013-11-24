# constant word size [determined]
#
# - first byte store number of bits per filed
# - next is a array of bitfields - each bitfield contain value

from encoder import Encoder
from math import log

class Minbits(Encoder):

	def minbits_count(self, values):
		# minimum bits count to store maximum value from array
		entrophy = log(max(values), 2.0)

		return int(max(1.0, entrophy))

	def bytes_length(self, values):
		bits = len(values) * self.minbits_count(values)

		return 1 + (bits + 7)/8


class MinbitsDiff(Minbits):

	def bytes_length(self, values):
		diff = self.calculate_diff(values)[1:]
		bits = len(diff) * self.minbits_count(diff)

		return 1 + 4 + (bits + 7)/8
