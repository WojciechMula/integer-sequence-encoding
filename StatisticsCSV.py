class StatisticsCSV:

	def __init__(self, names):
		self.names = names

		print '# id, ', ', '.join('"%s"' % name for name in self.names)


	def write_item(self, name, num, total, item):
		print ', '.join([str(num)] + [str(item[name]) for name in self.names])


	def write_summary(self, summary):
		pass
