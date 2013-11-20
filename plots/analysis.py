import sys
from columns import *

def load_csv(name):
	data = []
	with open(name) as f:
		for index, line in enumerate(f):
			if index == 0:
				continue

			#print line
			data.append(map(int, line.replace(',', ' ').split()))

	return data


data = load_csv('results.csv')
length = len(data)


plots = {
	'bitfields_vs_varint':
		(bitfields, varint_diff),

	'varnibble_vs_varint':
		(varnibble_diff, varint_diff),

	'subsets_varnibble_vs_varint':
		(subsets_first_match_varnibble, varint_diff),

	'subsets_varint_vs_varint':
		(subsets_first_match_varint, varint_diff),

	'best_subsets_varnibble_vs_varint':
		(best_subsets_first_match_or_varnibble, varint_diff),

	'best_subsets_varint_vs_varint':
		(best_subsets_first_match_or_varint, varint_diff),
}


for name, (column1_name, column2_name) in plots.iteritems():
	column1 = get_column_index(column1_name)
	column2 = get_column_index(column2_name)
	title = '%s vs %s' % (column1_name, column2_name)

	greater = 0
	less = 0
	equal = 0

	sum1 = 0
	sum2 = 0

	sum_less = 0
	sum_greater = 0
	sum_equal = 0
	for row in data:
		size1 = row[column1]
		size2 = row[column2]

		sum1 += size1
		sum2 += size2

		if row[column1] < row[column2]:
			less += 1
			sum_less += size1
		elif row[column1] > row[column2]:
			greater += 1
			sum_greater += size1
		else:
			equal += 1
			sum_equal += size1

	print
	print title
	print '* compression: %.2f%%' % (100.0*sum1/sum2)
	print '*     greater: %10d %7.2f%% %10d' % (greater, 100.0*greater/length, sum_greater)
	print '*       equal: %10d %7.2f%% %10d' % (equal,   100.0*equal/length, sum_equal)
	print '*        less: %10d %7.2f%% %10d' % (less,    100.0*less/length, sum_less)
