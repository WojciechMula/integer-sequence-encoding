from sampledata import get_all

from encoder.dword import DWord
from encoder.varint import Varint
from encoder.varint_diff import VarintDiff
from encoder.subsets_first_match import SubsetsFirstMatch
from encoder.subsets_greedy import SubsetsGreedy

def main(encoders):
	summary = dict((encoder.name, 0) for encoder in encoders)

	for index, count, name, values in get_all():
		print '%s (%d/%d)' % (name, index + 1, count)
		for encoder in encoders:
			name = encoder.name
			size = encoder.bytes_length(values)
			print '* %40s: %10d' % (name, size)

			summary[name] += size
	else:
		print
		print '=' * 72
		for encoder in encoders:
			name = encoder.name
			size = summary[name]
			print '* %40s: %10d' % (name, size)


if __name__ == '__main__':
	encoders = [
		DWord(),
		Varint(),
		VarintDiff(),
		SubsetsFirstMatch(6),
		SubsetsGreedy(0),
	]

	main(encoders)
