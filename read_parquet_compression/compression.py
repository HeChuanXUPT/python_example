# get compression from parquet file
# Usage: compression.py <parquet file>
# pip install parquet-cli

import sys

import pyarrow.parquet as pq

if __name__ == '__main__':
    file = sys.argv[1]
    print('file:', file)
    r = pq.ParquetFile(file)
    print('compression:', r.metadata.row_group(0).column(0).compression)

