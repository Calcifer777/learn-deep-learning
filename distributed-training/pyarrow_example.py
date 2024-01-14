from pathlib import Path
import posixpath
import numpy as np
import pandas as pd
from pandas import (
    DataFrame,
)
import pyarrow
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow.dataset import Dataset
from pyarrow import Table
from PIL import Image


num_img = 1000
img_arrs = [
    np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8) for _ in range(num_img)
]

records = []

for i in img_arrs:
    img = Image.fromarray(i)
    r = dict(
        h=img.height,
        w=img.width,
        # img_ref=img.tobytes(),
        img_ref=np.array(img),
    )
    records.append(r)


path_out = Path("pyarrow/")
path_out.mkdir(exist_ok=True, parents=True)


df = DataFrame.from_records(records)
# write_chunked(df, 10, path_out)


table = pa.Table.from_pandas(df)
table_batched = pa.Table.to_batches(table, 10)
pq.write_table(
    table=table,
    where=(path_out / "out.parquet").as_posix(),
    compression="gzip",
    write_batch_size=10,
)


pq.write_to_dataset(
    table=table,
    root_path=path_out.as_posix(),
)

# table: Table = pyarrow.Table.from_pandas(df)

# pa.array(img_arrs[0])
