import os

dwords = "32-bit words"
varint = "Varint"
varint_diff = "Varint [diff]"
bitfields = "Minimum number of bits [diff]"
varnibble = "Varnibble"
varnibble_diff = "Varnibble [diff]"
subsets_first_match_varint = "Subsets (first match, varint)"
subsets_first_match_varnibble = "Subsets (first match, varnibble)"
subsets_greedy_varint = "Subsets (greedy, varint)"
subsets_greedy_varnibble = "Subsets (greedy, varnibble)"
best_subsets_first_match_or_varint = "best: Subsets (first match) or varint"
best_subsets_greedy_or_varint = "best: Subsets (greedy) or varint"
best_subsets_first_match_or_varnibble = "best: Subsets (first match) or varnibble"
best_subsets_greedy_or_varnibble = "best: Subsets (greedy) or varnibble"

COLUMNS = [
	"id",
	"32-bit words",
	"Varint",
	"Varint [diff]",
	"Minimum number of bits [diff]",
	"Varnibble",
	"Varnibble [diff]",
	"Subsets (first match, varint)",
	"Subsets (first match, varnibble)",
	"Subsets (greedy, varint)",
	"Subsets (greedy, varnibble)",
	"best: Subsets (first match) or varint",
	"best: Subsets (greedy) or varint",
	"best: Subsets (first match) or varnibble",
	"best: Subsets (greedy) or varnibble",
]

GNUPLOT_SCRIPT = """
set terminal png medium size 720,480

set output "%(output)s"
set title  "%(title)s"
set xlabel "samples"
set ylabel "compression [%%]"
set xrange [1:855]
unset key

plot '%(file)s' using ($%(column1)d/$%(column2)d) with lines
"""

def get_plot_script(file, output, column1, column2, title):
	return GNUPLOT_SCRIPT % locals()

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
		(subsets_first_match_varint, varint_diff),
}

for name, (column1_name, column2_name) in plots.iteritems():
	column1 = COLUMNS.index(column1_name) + 1
	column2 = COLUMNS.index(column2_name) + 1
	title = '%s vs %s' % (column1_name, column2_name)

	filename = '%s.gnuplot' % name
	with open(filename, 'w') as f:
		script = get_plot_script('results.csv', name + '.png', column1, column2, title)
		f.write(script)
