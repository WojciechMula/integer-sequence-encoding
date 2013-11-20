import os
from columns import *

def get_plot_script(file, output, column1, column2, title):
	SCRIPT = """
set terminal png medium size 720,480

set output "%(output)s"
set title  "%(title)s"
set xlabel "samples"
set ylabel "compression [%%]"
set xrange [1:855]
unset key

plot '%(file)s' using (100 * ($%(column1)d - $%(column2)d)/$%(column2)d) with lines lt rgb "blue"
"""
	return SCRIPT % locals()

def get_size_script(file, output, column, title):
	SCRIPT = """
set terminal png medium size 720,480

set output "%(output)s"
set title  "%(title)s"
set xlabel "samples"
set ylabel "size [B]"
set xrange [1:855]
unset key

plot '%(file)s' using %(column)d with lines lt rgb "blue"
"""

	return SCRIPT % locals()


def comparision():
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
		column1 = COLUMNS.index(column1_name) + 1
		column2 = COLUMNS.index(column2_name) + 1
		title = '%s vs %s' % (column1_name, column2_name)

		filename = '%s.gnuplot' % name
		with open(filename, 'w') as f:
			script = get_plot_script('results.csv', name + '.png', column1, column2, title)
			f.write(script)

		os.system("gnuplot %s" % filename)


def size():
	name = 'varint_diff_samples_size'
	filename = name + '.gnuplot'
	with open(filename, 'w') as f:
		title  = 'Size of samples [varint-differences]'
		column = COLUMNS.index(varint_diff) + 1
		script = get_size_script('results.csv', name + '.png', column, title)
		f.write(script)

	os.system("gnuplot %s" % filename)


if __name__ == '__main__':
	comparision()
	size()
