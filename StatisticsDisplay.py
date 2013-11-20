class StatisticsDisplay:
	def __init__(self, names):
		self.names = names
		self.name_len = max(map(len, self.names))


	def write_item(self, name, num, total, item):
		print '%s (%d/%d)' % (name, num, total)

		base_size = None
		for name in self.names:
			size = item[name]
			if base_size is None:
				base_size = size

			perc = 100.0 * size/base_size

			print '* %*s: %10d (%5.2f%%)' % (self.name_len, name, size, perc)


	def write_summary(self, summary):
		print
		print '=' * 72

		base_size = None
		for name in self.names:
			size = summary[name]
			if base_size is None:
				base_size = size

			perc = 100.0 * size/base_size

			print '* %*s: %10d (%5.2f%%)' % (self.name_len, name, size, perc)
