import xorbits.pandas as pd
from datasets import load_dataset
import time
import pdb

dataset = load_dataset(path="oscar-corpus/OSCAR-2201",
                        name="is", 
                        split="train",
                        cache_dir="./cache")

df = pd.DataFrame(dataset.to_pandas(), chunk_size=396183).execute()

start = time.time()
res = df.dedup().execute()
print(res)
print(f"Time: {time.time() - start:.2f}s")