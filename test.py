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


def main(encoders):
	summary = dict((encoder.name, 0) for encoder in encoders)

	for index, count, name, values in get_all():
		print '%s (%d/%d)' % (name, index + 1, count)

		base_size = None
		for encoder in encoders:
			name = encoder.name
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
		for encoder in encoders:
			name = encoder.name
			size = summary[name]
			if base_size is None:
				base_size = size

			perc = 100.0 * size/base_size

			print '* %40s: %10d (%0.2f%%)' % (name, size, perc)


if __name__ == '__main__':
	encoders = [
		DWord(),
		Varint(),
		VarintDiff(),
		SubsetsFirstMatch(6),
		#SubsetsGreedy(0),
		#Minbits(),
		MinbitsDiff(),
		#CombineTwo('varint & subsets first match', 
		#	VarintDiff(),
		#	SubsetsFirstMatch(6)
		#),
		#CombineTwo('varint & subsets greedy', 
		#	VarintDiff(),
		#	SubsetsGreedy()
		#),
		Varnibble(),
		VarnibbleDiff(),
	]

	main(encoders)
