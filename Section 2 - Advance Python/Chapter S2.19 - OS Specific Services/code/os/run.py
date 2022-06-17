import subprocess
import os
import platform


def execute(cmd_list, timeout=None):
  """
  """

  stdout = ""
  stderr = ""

  try:
    process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(timeout=timeout)
    return_code = process.returncode
  except subprocess.TimeoutExpired:
    process.kill()
    process.wait()
    return_code = process.returncode
  except OSError:
    return_code = -1
  return stdout, stderr, return_code

def has_java():
  cmd = ["java", "-version"]
  _, _, ret = execute(cmd)
  print(ret)
  return ret == 0


ret = has_java()
print(ret)
