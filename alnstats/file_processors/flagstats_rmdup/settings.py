# Data fields and initial values.
data = {
  'merge' : 0, # Number of reads post-merge
  'align' : 0, # Number of reads post-align post-merge
}

# Recognized file extensions.
import os
import re
regex = r'^.*/[^\.]+{extension}$'
extensions = [
  '.rmdup.srt.bam.flagstats',
]
extensions = map(lambda x: re.compile(regex.format(extension=x)), extensions)
