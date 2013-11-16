import os
import struct

DIR = 'bindata'

def get_all():
	names = []
	for name in os.listdir(DIR):
		if name.endswith('.idx'):
			names.append(name)

	count = len(names)
	for index, name in enumerate(sorted(names)):
		yield index, count, name, get(name)


def get(name):
	with open(DIR + '/' + name, 'rb') as f:
		bytes = f.read()
		n = len(bytes)/4
		fmt = '%di' % n

		return struct.unpack(fmt, bytes)


def sample():
	"one of the longest sample"

	return get('a2f.idx')
