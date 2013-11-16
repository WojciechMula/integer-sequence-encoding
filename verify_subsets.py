from encoder.subsets_first_match import SubsetsFirstMatch
from encoder.subsets_greedy import SubsetsGreedy
from ByteString import ByteString
from sampledata import sample

def verify(encoder, values):
	bytes = encoder.encode(values)
	buffer = ByteString(bytes)

	decoded_values = encoder.decode(buffer)

	assert set(values) == set(decoded_values)


if __name__ == '__main__':
	values = sample()

	verify(SubsetsFirstMatch(6), values)
	verify(SubsetsGreedy(0), values)

