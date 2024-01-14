from pathlib import Path
import random
from typing import Optional

import numpy as np
import pandas as pd
from PIL import Image

from petastorm.codecs import (
    ScalarCodec,
    CompressedImageCodec,
    NdarrayCodec,
)
from petastorm.unischema import Unischema, UnischemaField, dict_to_spark_row
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import IntegerType
import pyspark.sql

num_img = 10
img_arrs = (
    np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8) for _ in range(num_img)
)

records = []

for idx, i in enumerate(img_arrs):
    # img = Image.fromarray(i)
    records.append(Row(id=idx, img=i))


path_out = Path("petastorm/")

schema = Unischema(
    "HelloWorldSchema",
    [
        UnischemaField(
            "id",
            np.int32,
            (256, 256, 3),
            ScalarCodec(IntegerType()),
            False,
        ),
        UnischemaField(
            "image1",
            np.uint8,
            (256, 256, 3),  # image dimension
            CompressedImageCodec("png"),
            False,
        ),
    ],
)

spark_schema = schema.as_spark_schema()

print(spark_schema)

spark: SparkSession = SparkSession.builder.master("local[2]").getOrCreate()  # type: ignore
sdf = spark.sparkContext.parallelize(range(len(records))).map(
    records, schema.as_spark_schema()
)

# sdf.printSchema()


# def pandas_memory_usage_mb(df: pd.DataFrame):
#     return df.memory_usage(deep=True).sum() / (2**20)


# def write_in_chunks(
#     df: pyspark.sql.DataFrame, path_out: str, chunk_size_mb: Optional[int] = None
# ):
#     writer = sdf.write.mode("overwrite")
#     if chunk_size_mb is not None:
#         sample = df.sample(0.01).toPandas()
#         mb = pandas_memory_usage_mb(sample) * 100
#         lines_per_chunk = int(chunk_size_mb * len(sample) * 100 / mb)
#         writer.option("maxRecordsPerFile", lines_per_chunk)

#     writer.parquet(path_out, compression="snappy")


# write_in_chunks(sdf, path_out.as_posix(), None)
# # write_in_chunks(sdf, path_out.as_posix(), 10)
