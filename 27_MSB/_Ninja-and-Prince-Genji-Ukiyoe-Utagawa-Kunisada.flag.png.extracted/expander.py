import glob
import zlib
import sys

#for filename in sys.argv:
with open("29.zlib", 'rb') as compressed:
    with open("29.zlib" + '-decompressed', 'wb') as expanded:
        data = zlib.decompress(compressed.read())
        expanded.write(data)
