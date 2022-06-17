import math_lib
import argparse

def main(nums):
  print(nums)
  total = math_lib.sum_all(*nums)
  print(total)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--sum", help="display a sum of a given numbers",
                      nargs="+")
  args = parser.parse_args()
  print(args.sum)
  main(args.sum)
