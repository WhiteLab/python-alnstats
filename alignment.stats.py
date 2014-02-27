#!/usr/bin/env python
import os
import sys
import time
import logging
import argparse

import settings
import alnstats

def main(args):
  # Set up logging.
  logging.basicConfig(
    level     = args.loglevel,
    filename  = args.logfile,
    format    = '%(asctime)s %(name)-6s %(levelname)-4s %(message)s',)
  logging.info('Starting %s @ %s' % (__file__,os.getcwd()))
  logging.info('args : %s' % str(args))

  # Set up output.
  ofs = args.out and open(args.out,args.append and 'a' or 'w') or sys.stdout

  # Generate grouping subroutine.
  group = lambda x: settings.regex.match(os.path.basename(x)).group(0)

  # Generate groups.
  groups = dict()
  try: map(lambda x: groups.update({group(x):list()}), args.files)
  except AttributeError: raise ValueError('upgroupable files found')

  # Populate groups.
  map(lambda x: groups[group(x)].append(x), args.files)

  # Gather stats for each group.
  stats = map(lambda files: alnstats.alnstats(*files), groups.values())

  # Report header if necessary.
  ofs.write(args.header and '%s\n' % alnstats.header())

  # Report stats for each group.
  map(lambda x: ofs.write('%s\n' % x), stats)

  # Fin.
  return

if __name__ == '__main__':
  # Determine default logfile name.
  root = __file__.rsplit(os.sep,1)[0]
  name = __file__.rsplit(os.sep,1)[-1].rsplit('.',1)[0]
  date = time.strftime('%Y%m%d')
  logf = '{name}.{date}.log'.format(name=name,date=date)

  # Set up argument parser.
  parser = argparse.ArgumentParser(
    description = 'Alignment Statistics Parser',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
  )

  # Positional arguments.
  parser.add_argument('files',type=str,nargs='+',
                      help='Files from which to pull stats.')

  # Keyword arguments.
  parser.add_argument('--logfile',type=str,default=logf,
                      help='File for which to redirected log output.')
  parser.add_argument('--out',type=str,default=None,
                      help='Target output file.')

  # Flags.
  parser.add_argument('-d','--debug',dest='loglevel',action='store_const',
                      const=logging.DEBUG,default=logging.INFO,
                      help='Set logging level to debug.')
  parser.add_argument('-a','--append',action='store_const',
                      const=True,default=False,
                      help='Append output to file.')
  parser.add_argument('--header',action='store_const',
                      const=True,default=False,
                      help='Print out header.')

  # Parse argumensts and being execution.
  try: main(parser.parse_args())
  except Exception as err: logging.error(err)
