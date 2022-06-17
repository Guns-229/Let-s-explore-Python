from pathlib import Path

p = Path('.')

for f in p.glob('**/*.py'):
  print(f)
