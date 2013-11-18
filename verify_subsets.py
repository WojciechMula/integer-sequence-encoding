from encoder.subsets_first_match import SubsetsFirstMatch
from encoder.subsets_greedy import SubsetsGreedy
from WriterVarint import WriterVarint
from ByteString import ByteString
from sampledata import sample

def verify(encoder, values):
	bytes = encoder.encode(values)
	buffer = ByteString(bytes)

	decoded_values = encoder.decode(buffer)

	assert set(values) == set(decoded_values)


if __name__ == '__main__':
	values = sample()

	encoders = [
		SubsetsFirstMatch('first match', 6, WriterVarint()),
		SubsetsGreedy('greedy', 0, WriterVarint())
	]

	for encoder in encoders:
		print "testing", encoder.name
		verify(encoder, values)
		print "... OK"
