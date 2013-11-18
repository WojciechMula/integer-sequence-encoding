from sampledata import get_all

class Stats:
	def __init__(self):
		self.count = 0
		self.sum = 0
		self.min = None
		self.max = None

value  = Stats()
length = Stats()

for i, count, name, values in get_all():
	value.count += 1

	if value.min is None:
		value.min = min(values)
		value.max = max(values)
	else:
		value.min = min(value.min, min(values))
		value.max = max(value.max, max(values))

	if length.min is None:
		length.min = length.max = len(values)
		
	length.min = min(length.min, len(values))
	length.max = max(length.max, len(values))
	length.count += 1
	length.sum += len(values)


def print_int(value, label):
	print '%10s: %d' % (label, value)

print 'values:'
print_int(value.count, 'count')
print_int(value.min, 'min value')
print_int(value.max, 'max value')

print
print 'collection lengths:'
print_int(length.min, 'min')
print_int(length.max, 'max')

print_int(int(length.sum/float(length.count)), 'avg')
