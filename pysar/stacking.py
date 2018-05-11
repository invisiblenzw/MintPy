#!/usr/bin/env python3
############################################################
# Program is part of PySAR                                 #
# Copyright(c) 2017, Zhang Yunjun                          #
# Author:  Zhang Yunjun                                    #
############################################################


import argparse
from pysar.utils import utils as ut
from pysar.objects import ifgramDatasetNames


#################################  Usage  ####################################
EXAMPLE = """example:
  stacking.py ifgramStack.h5 unwrapPhase -o averagePhaseVelocity.h5
  stacking.py ifgramStack.h5 coherence   -o averageSpatialCoherence.h5
"""


def create_parser():
    parser = argparse.ArgumentParser(description='Stack multiple layers dataset into one.',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog=EXAMPLE)

    parser.add_argument('file', help='File to be stacked')
    parser.add_argument('-d', '--dataset', dest='dataset_name', default=ifgramDatasetNames[0],
                        help='Dataset to be used for stacking, when input file is ifgramStack')
    parser.add_argument('-o', '--output', dest='outfile',
                        help='output file name')
    return parser


def cmd_line_parse(iargs=None):
    parser = create_parser()
    inps = parser.parse_args(args=iargs)
    return inps


#############################  Main Function  ################################
def main(iargs=None):
    inps = cmd_line_parse(iargs)
    print('\n*************** Stacking ******************')
    ut.temporal_average(inps.file, datasetName=inps.dataset_name, outFile=inps.outfile)
    return


##############################################################################
if __name__ == '__main__':
    main()
