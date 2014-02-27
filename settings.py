# -*- coding: utf-8 -*-
# HGAC Regex construction.
# TODO MOVE TO REGEX REPOSITORY (╯°□°）╯︵ ┻━┻
import re
re_fields = [
  r'(?P<bid>\d{4}-\d+)', # BID
  r'(?P<date>\d{6})',    # Date
  r'(?P<mac>[^_]+)',     # Machine
  r'(?P<run>\d{4})',     # Run
  r'(?P<bar>[^_]+)',     # Barcode
  r'(?P<lane>\d)',       # Lane
]
re_sep = r'_'
regex = re.compile('{regex}'.format(regex=re_sep.join(re_fields)))
