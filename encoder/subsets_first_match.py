import varint
from subsets import Subsets

class SubsetsFirstMatch(Subsets):

	def get_name(self):
		return 'Subsets (first match [cutoff=%d])' % self.cutoff

	#name = property(get_name)

	def find_subsets(self, values):
		"naive first match searching"

		def longest_subset(index):
			val = values[index]
			n   = 0
			for i in xrange(index + 1, len(values)):
				if values[i] - val > 32:
					break

				n += 1

			return n

		result = []
		i = 0
		while i < len(values):
			value = values[i]
			count = longest_subset(i)
			if count >= self.cutoff:
				subset = values[i+1 : i+count]
				i += count

				result.append((value, subset))
			else:
				result.append((value, None))
				i += 1

		return result

