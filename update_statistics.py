#!/usr/bin/env python
import json
import subprocess
import re

def count_files() -> int:
  _CMD = 'git ls-files --format=1 | wc -l'

  return int(
    re.fullmatch(r'\d+',
                 subprocess.check_output(_CMD,
                                         shell=True,
                                         text=True
                                        ).removesuffix('\n')
                ).group(0)
  )


with open('statistics.json', 'w') as _f:
  json.dump({
    'nfiles': count_files(),
  }, _f, indent=2)

  _f.write('\n')
