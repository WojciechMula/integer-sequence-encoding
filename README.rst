Programs and sample data used to research some types of encoding
set of unsigned integers.

Detailed article: http://0x80.pl/articles/integer-sequence-encoding.html


Short results
------------------------------------------------------------------------

::

*                             32-bit words:    2429252 (100.00%)
*                                   Varint:    1208400 (49.74%)
*                            Varint [diff]:     621208 (25.57%)
*                                  VarBits:    1140529 (46.95%)
*                           VarBits [diff]:     341600 (14.06%)
*            Minimum number of bits [diff]:     561041 (23.10%)
*                                Varnibble:    1425929 (58.70%)
*                         Varnibble [diff]:     387867 (15.97%)
*            Subsets (first match, varint):     373508 (15.38%)
*         Subsets (first match, varnibble):     365738 (15.06%)
*    best: Subsets (first match) or varint:     368778 (15.18%)
* best: Subsets (first match) or varnibble:     337743 (13.90%)
