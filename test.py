from sampledata import get_all
from encoder.dword import DWord

def main(encoders):
	for name, values in get_all():
		print name, '(bytes)'
		for encoder in encoders:
			print '* %s: %d' % (encoder.name, encoder.bytes_length(values))


if __name__ == '__main__':
	encoders = [
		DWord(),
	]

	main(encoders)
