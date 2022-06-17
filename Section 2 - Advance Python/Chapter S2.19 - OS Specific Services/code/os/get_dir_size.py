"""
URL: https://www.python.org/dev/peps/pep-0471/
"""
import os
import sys

def get_tree_size(path):
  """Return total size of files in path and subdirs. If
  is_dir() or stat() fails, print an error message to stderr
  and assume zero size (for example, file has been deleted).
  """
  total = 0
  for entry in os.scandir(path):
    try:
      is_dir = entry.is_dir(follow_symlinks=False)
    except OSError as error:
      print('Error calling is_dir():', error, file=sys.stderr)
      continue
    if is_dir:
      total += get_tree_size(entry.path)
    else:
      try:
        total += entry.stat(follow_symlinks=False).st_size
      except OSError as error:
        print('Error calling stat():', error, file=sys.stderr)
  return total


if __name__ == "__main__":
  print(get_tree_size(os.path.expanduser('~')))
