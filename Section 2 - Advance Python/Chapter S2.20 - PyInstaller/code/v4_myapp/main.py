import math_lib
from configparser import  ConfigParser as cf
import pkgutil


def main(nums):
  print(nums)
  total = math_lib.sum_all(*nums)
  print(total)

if __name__ == "__main__":
  config = cf()
  conf_file = help_bin = pkgutil.get_data(".", 'data.ini')
  print(conf_file)
  config.read(conf_file)
  data = config.get('data', 'url')
  print(data)
  main([1, 2, 4])

