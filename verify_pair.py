from encoder.pair_encoder import Encoder, Decoder
from encoder.varint import encoded_size
from sampledata import sample, get_all

def verify(values):
	enc = Encoder(values)
	sequence, pairs = enc.encode()

	dec = Decoder(sequence, pairs)
	decoded = dec.decode()

	assert decoded == values


def demo(values):
	enc = Encoder(values)
	sequence, pairs = enc.encode()

	orig_size   = sum(encoded_size(v) for v in values)

	seq_size    = sum(encoded_size(v) for v in sequence)

	pairs_size  = sum(encoded_size(v) for v in pairs)
	pairs_size += sum(encoded_size(pair[0]) + encoded_size(pair[1]) for pair in pairs.itervalues())

	print 'original size: ', orig_size
	print
	print 'sequence size: ', seq_size
	print '   pairs size: ', pairs_size
	print '   total size: ', seq_size + pairs_size


if __name__ == '__main__':

	def get_diff(values):
		return [values[0]] + [b - a for a, b in zip(values, values[1:])]

	for index, count, name, values in get_all():
		print "verifying %d/%d..." % (index + 1, count)
		verify(get_diff(values))
		print "ok"

	print "encoding example"
	demo(get_diff(sample()))
