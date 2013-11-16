from sampledata import get_all

from encoder.dword import DWord
from encoder.varint import Varint
from encoder.varint_diff import VarintDiff

def main(encoders):
	summary = dict((encoder.name, 0) for encoder in encoders)

	for name, values in get_all():
		print name, '(bytes)'
		for encoder in encoders:
			name = encoder.name
			size = encoder.bytes_length(values)
			print '* %30s: %10d' % (name, size)

			summary[name] += size
	else:
		print
		print '=' * 72
		for encoder in encoders:
			name = encoder.name
			size = summary[name]
			print '* %30s: %10d' % (name, size)


if __name__ == '__main__':
	encoders = [
		DWord(),
		Varint(),
		VarintDiff(),
	]

	main(encoders)
