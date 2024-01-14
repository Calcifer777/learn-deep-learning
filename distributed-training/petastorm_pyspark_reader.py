import warnings

from PIL import Image
from petastorm import TransformSpec, make_reader, make_batch_reader
from petastorm.pytorch import DataLoader
from torch import _test_serialization_subcmul
import torchvision.transforms.v2.functional as F

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=UserWarning)


def _transform_row(r):
    img = Image.frombytes(
        size=(r["h"], r["w"]),
        data=r["img"],
        mode=r["mode"],
    )
    r["img"] = F.pil_to_tensor(img)
    return r


transform = TransformSpec(_transform_row, removed_fields=["id"])

reader = make_reader(
    "file:///home/calcifer/tmp/check-petastorm/pandas",
    num_epochs=10,
    seed=1,
    shuffle_rows=True,
    transform_spec=transform,
)

with DataLoader(reader, batch_size=2) as dl:
    batch = next(iter(dl))
    print(batch["img"].shape)
