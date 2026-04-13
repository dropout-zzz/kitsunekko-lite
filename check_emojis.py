#!/usr/bin/env python
import argparse
import subprocess
import sys
import re

_ap = argparse.ArgumentParser()
_ap.add_argument('directories', nargs='+', metavar='DIRECTORY')
_args = _ap.parse_args()

if any(_directory.startswith('-') for _directory in _args.directories):
  _ap.error('directory names should not start with dashes')

_CMD = ['find',
        *_args.directories,
        '-type', 'f',
        '(',
        '-name', '*.ass',
        '-o',
        '-name', '*.srt',
        ')']

def get_file_list() -> list[str]:
  return subprocess.check_output(_CMD,
                                 text=True
                                ).splitlines()

_PATTERN = re.compile('(?:☎️|☎|🔊|📺️) ')

def is_line_bad(s: str) -> bool:
  return _PATTERN.search(s) is not None

_status = 0

for _file in get_file_list():
  if _file == '':
    continue

  with open(_file, 'r', encoding='utf-8', newline='\n') as _f:
    for _line_no, _line in enumerate(_f, start=1):
      _line = _line.removesuffix('\n')

      if is_line_bad(_line):
        print(f'{_file}:{_line_no}:{_line}', file=sys.stderr)
        _status = 1

sys.exit(_status)
