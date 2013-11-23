# column titles & order in result.csv

dwords = "32-bit words"
varint = "Varint"
varint_diff = "Varint [diff]"
varbits = "VarBits"
varbits_diff = "VarBits [diff]"
bitfields = "Minimum number of bits [diff]"
varnibble = "Varnibble"
varnibble_diff = "Varnibble [diff]"
subsets_first_match_varint = "Subsets (first match, varint)"
subsets_first_match_varnibble = "Subsets (first match, varnibble)"
subsets_greedy_varint = "Subsets (greedy, varint)"
subsets_greedy_varnibble = "Subsets (greedy, varnibble)"
best_subsets_first_match_or_varint = "best: Subsets (first match) or varint"
best_subsets_greedy_or_varint = "best: Subsets (greedy) or varint"
best_subsets_first_match_or_varnibble = "best: Subsets (first match) or varnibble"
best_subsets_greedy_or_varnibble = "best: Subsets (greedy) or varnibble"

COLUMNS = [
	"id",  "32-bit words",
	"Varint",
	"Varint [diff]",
	"VarBits",
	"VarBits [diff]",
	"Minimum number of bits [diff]",
	"Varnibble",
	"Varnibble [diff]",
	"Subsets (first match, varint)",
	"Subsets (first match, varnibble)",
	"best: Subsets (first match) or varint",
	"best: Subsets (first match) or varnibble"
]

def get_column_index(name):
	return COLUMNS.index(name)
