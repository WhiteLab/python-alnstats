# Data fields and initial values.
data = {
  'len' : 0, # Length of sequences
}

# Line 1 regex.
re_line1_fields = [
  [ # First half.
    r'(?P<name>[^:]+)',         # Machine name.
    r'(?P<run>\d+)',            # Run number.
    r'(?P<flow>[^:]+)',         # Flowcell name.
    r'(?P<lane>\d+)',           # Flowcell lane.
    r'(?P<tile>\d+)',           # Tile number.
    r'(?P<xpos>\d+)',           # X coordinate of cluster.
    r'(?P<ypos>\d+)',           # Y coordinate of cluster.
  ],
  [ # Second half.
    r'(?P<pair>\d)',            # Pair for paired end.
    r'(?P<pass>\w)',          # Passed filter.
    r'(?P<cntl>\d+)',           # Control bits.
    r'(?P<index>\w+)',  # Index sequence.
  ],
]
re_line1_sep1 = r' '
re_line1_sep2 = r':'
re_line1 = re_line1_sep1.join(map(re_line1_sep2.join,re_line1_fields))
re_line1 = r'^@{regex}$'.format(regex=re_line1)

# Line 2 regex.
re_line2_fields = [
  r'(?P<seq>\w+)',  # Sequence.
]
re_line2_sep1 = r''
re_line2 = re_line2_sep1.join(re_line2_fields)
re_line2 = r'^{regex}$'.format(regex=re_line2)

# Line 3 regex.
re_line3_fields = [
  [ # First half.
    r'(?P<name>[^:]+)',         # Machine name.
    r'(?P<run>\d+)',            # Run number.
    r'(?P<flow>[^:]+)',         # Flowcell name.
    r'(?P<lane>\d+)',           # Flowcell lane.
    r'(?P<tile>\d+)',           # Tile number.
    r'(?P<xpos>\d+)',           # X coordinate of cluster.
    r'(?P<ypos>\d+)',           # Y coordinate of cluster.
  ],
  [ # Second half.
    r'(?P<pair>\d)',            # Pair for paired end.
    r'(?P<pass>\w)',          # Passed filter.
    r'(?P<cntl>\d+)',           # Control bits.
    r'(?P<index>\w+)',  # Index sequence.
  ],
]
re_line3_sep1 = r' '
re_line3_sep2 = r':'
re_line3 = re_line3_sep1.join(map(re_line3_sep2.join,re_line3_fields))
re_line3 = r'^\+(?:{regex})?$'.format(regex=re_line3)

# Line 4 regex.
re_line4_fields = [
  r'(?P<qual>.+)',  # Sequence.
]
re_line4_sep1 = r''
re_line4 = re_line4_sep1.join(re_line4_fields)
re_line4 = r'^{regex}$'.format(regex=re_line4)

# Line regexes.
import re
regexes = [
  re_line1,
  re_line2,
  re_line3,
  re_line4,
]
regexes = map(lambda x: re.compile(x),regexes)

# Mappings.
mappings = {
  'name'  : str,
  'run'   : int,
  'flow'  : str,
  'lane'  : int,
  'tile'  : int,
  'xpos'  : int,
  'ypos'  : int,
  'pair'  : int,
  'pass'  : str,
  'cntl'  : int,
  'index' : str,
  'seq'   : str,
  'qual'  : str,
}

