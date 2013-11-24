from encoder import Encoder as BaseEncoder

class PairBase(BaseEncoder):
	def __init__(self, writer):
		self.writer = writer

	def perform_bytes_length(self, values):
		enc = Encoder(values)
		sequences, pairs = enc.encode()

		self.writer.init()
		for value in sequences:
			self.writer.encode_uint(value)

		for index, pair in pairs.iteritems():
			self.writer.encode_uint(index)
			self.writer.encode_uint(pair[0])
			self.writer.encode_uint(pair[1])

		size = len(self.writer.get_bytes())

		return size + 1


class Pair(PairBase):
	def bytes_length(self, values):
		return self.perform_bytes_length(values)


class PairDiff(PairBase):
	def bytes_length(self, values):
		diff = self.calculate_diff(values)

		return self.perform_bytes_length(diff)


########################################################################
# yes, I know this is not optimal


class Encoder(object):
	def __init__(self, values):
		self.values = values[:]
		self.pairs  = {}
		self.used_values = set(values)
		self.last_allocated = 0

	def encode(self):
		while True:
			pair = self.find_most_frequent_pair()
			if pair is None:
				break

			self.replace(pair)

		return self.values, self.pairs


	def replace(self, pair):
		index = self.allocate_next()
		assert index not in self.pairs
		assert index not in pair

		self.pairs[index] = pair
		i = 0
		replace = 0
		while i < len(self.values) - 1:
			if self.values[i] == pair[0] and self.values[i + 1] == pair[1]:
				del self.values[i]
				self.values[i] = index
				replace += 1

			i += 1


	def allocate_next(self):

		def find_first_unused():
			for value in xrange(self.last_allocated + 1, max(self.used_values)):
				if value not in self.used_values:
					return value

		value = find_first_unused()
		if value is None:
			value = max(self.used_values) + 1

		self.used_values.add(value)
		self.last_allocated = value

		return value


	def find_most_frequent_pair(self):
		if len(self.values) <= 2:
			return

		# histogram
		d = {}
		for pair in zip(self.values, self.values[1:]):
			d[pair] = d.get(pair, 0) + 1

		# find best
		max_count = 0
		for pair, count in d.iteritems():
			if count > max_count:
				max_count = count
				best_pair = pair

		if max_count > 1:
			return best_pair


class Decoder(object):
	def __init__(self, sequence, pairs):
		self.sequence = sequence[:]
		self.pairs = pairs

	def decode(self):
		while True:
			if not self.expand():
				break

		return self.sequence

	def expand(self):
		i = 0
		n = 0
		while i < len(self.sequence):
			value = self.sequence[i]
			if value not in self.pairs:
				i += 1
				continue

			first, second = self.pairs[value]

			self.sequence[i] = second
			self.sequence.insert(i, first)
			i += 2
			n += 1

		return n


