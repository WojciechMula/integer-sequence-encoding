import varint
from subsets import Subsets

class SubsetsGreedy(Subsets):

	def get_name(self):
		return 'Subsets (greedy [cutoff=%d])' % self.cutoff

	name = property(get_name)

	def find_subsets(self, values):
		"greedy best match searching"

		def longest(values, index, best):
			val0 = values[index]
			for i in xrange(index + best, len(values)):
				if values[i] - val0 > 32:
					return i - 1

			return 0

		def findbest(values, prev_best):
			best = 0
			best_idx = None
			for i in xrange(len(values)):
				idx = longest(values, i, best)
				if idx <= i:
					continue

				if values[idx] - values[i] > 32:
					continue

				n = idx - i + 1

				if n > best:
					best = n
					best_idx = i
					if n == prev_best:
						break

			return best_idx, best

		tmp = list(values[:])
		subsets = []
		prev_best = 32
		while True:
			idx, count = findbest(tmp, prev_best)
			if idx is None:
				break

			prev_best = count
			subsets.append(tmp[idx:idx+count])
			del tmp[idx:idx+count]


		# merging subsets and plain values
		result = []
		for val in tmp:
			result.append((val, None))
		
		for subset in subsets:
			val = subset[0]
			result.append((val, subset[1:]))

		result.sort(key=lambda x: x[0])

		return result
