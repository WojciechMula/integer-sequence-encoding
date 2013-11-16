import os
import struct

DIR = 'bindata'

def get_all():
	for name in os.listdir(DIR):
		if not name.endswith('.idx'):
			continue

		yield name, get(name)


def get(name):
	with open(DIR + '/' + name, 'rb') as f:
		bytes = f.read()
		n = len(bytes)/4
		fmt = '%di' % n

		return struct.unpack(fmt, bytes)


def sample():
	"one of the longest sample"

	return get('a2f.idx')
