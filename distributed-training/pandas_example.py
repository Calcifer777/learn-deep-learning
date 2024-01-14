from pathlib import Path
import posixpath
import numpy as np
import pandas as pd
import pyarrow as pa
from pyarrow.dataset import Dataset
from PIL import Image


##### PANDAS #####

num_img = 100
img_arrs = (
    np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8) for _ in range(num_img)
)

records = []

for i in img_arrs:
    img = Image.fromarray(i)
    r = dict(
        h=img.height,
        w=img.width,
        mode="RGB",
        img=img.tobytes(),
    )
    records.append(r)


path_out = Path("pandas/")
path_out.mkdir(exist_ok=True, parents=True)


def memory_usage_mb(df: pd.DataFrame):
    return df.memory_usage(deep=True).sum() / (2**20)


def write_chunked(df: pd.DataFrame, chunk_size_mb: int, path: Path):
    mb = memory_usage_mb(df)
    num_chunks = (mb // chunk_size_mb) + 1
    lines_per_chunk = int(chunk_size_mb * len(df) / mb)
    for id_, l in enumerate(np.arange(0, len(df), lines_per_chunk)):
        df.iloc[l : l + lines_per_chunk].to_parquet(path / f"{id_}.parquet")


df = pd.DataFrame.from_records(records)

print(f"DF size: {memory_usage_mb(df):.2f} Mb")

write_chunked(df, 10, path_out)
