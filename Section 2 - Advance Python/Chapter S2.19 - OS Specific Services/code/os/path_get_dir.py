from pathlib import Path


p = Path('..')

for d in [x for x in p.iterdir() if x.is_dir()]:
  print(d)

