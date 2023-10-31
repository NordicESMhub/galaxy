import argparse
import xarray as xr
import numpy as np
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument(
        'output', help='output filename to store resulting image (png format)'
    )

args = parser.parse_args()

ds = xr.Dataset(
    {"foo": (("x", "y"), np.random.rand(4, 5))},
    coords={
        "x": [10, 20, 30, 40],
        "y": pd.date_range("2000-01-01", periods=5),
        "z": ("x", list("abcd")),
    },
)

print(args.output)

ds.to_zarr(args.output)

