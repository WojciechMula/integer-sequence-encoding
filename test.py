from sampledata import get_all

from encoder.dword import DWord
from encoder.varint import Varint
from encoder.varint_diff import VarintDiff
from encoder.subsets_first_match import SubsetsFirstMatch
from encoder.subsets_greedy import SubsetsGreedy
from encoder.minbits import Minbits
from encoder.minbits_diff import MinbitsDiff
from encoder.combine_two import CombineTwo
from encoder.varnibble import Varnibble
from encoder.varnibble_diff import VarnibbleDiff

from WriterVarint import WriterVarint
from WriterVarnibble import WriterVarnibble


def main(encoders):
	summary = dict((name, 0) for name, encoder in encoders)

	for index, count, name, values in get_all():
		print '%s (%d/%d)' % (name, index + 1, count)

		base_size = None
		for name, encoder in encoders:
			size = encoder.bytes_length(values)
			if base_size is None:
				base_size = size

			perc = 100.0 * size/base_size

			print '* %40s: %10d (%0.2f%%)' % (name, size, perc)

			summary[name] += size
	else:
		print
		print '=' * 72

		base_size = None
		for name, encoder in encoders:
			size = summary[name]
			if base_size is None:
				base_size = size

			perc = 100.0 * size/base_size

			print '* %40s: %10d (%0.2f%%)' % (name, size, perc)


if __name__ == '__main__':
	subset_cutoff = 6
	encoders = [
		('32-bit words',
			DWord()
		),

		('Varint',
			Varint()
		),

		('Varint [diff]',
			VarintDiff()
		),

		('#Minimum number of bits',
			Minbits()
		),

		('Minimum number of bits [diff]',
			MinbitsDiff()
		),

		('Varnibble',
			Varnibble()
		),

		('Varnibble [diff]',
			VarnibbleDiff()
		),

		('Subsets (first match, varint)',
			SubsetsFirstMatch(subset_cutoff, WriterVarint())
		),

		('Subsets (first match, varnibble)',
			SubsetsFirstMatch(subset_cutoff, WriterVarnibble())
		),

		('Subsets (greedy, varint)',
			SubsetsGreedy(subset_cutoff, WriterVarint())
		),

		('Subsets (greedy, varnibble)',
			SubsetsGreedy(subset_cutoff, WriterVarnibble())
		),

		('best: Subsets (first match) or varint',
			CombineTwo(
				VarintDiff(),
				SubsetsFirstMatch(subset_cutoff, WriterVarint())
			)
		),

		('best: Subsets (greedy) or varint',
			CombineTwo(
				VarintDiff(),
				SubsetsGreedy(subset_cutoff, WriterVarint())
			)
		),

		('best: Subsets (first match) or varnibble',
			CombineTwo(
				VarnibbleDiff(),
				SubsetsFirstMatch(subset_cutoff, WriterVarnibble())
			)
		),

		('best: Subsets (greedy) or varnibble',
			CombineTwo(
				VarnibbleDiff(),
				SubsetsGreedy(subset_cutoff, WriterVarnibble())
			)
		),
	]

	encoders = [(name, enc) for name, enc in encoders if name[0] != '#']

	main(encoders)
