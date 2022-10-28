#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def main():
    # in1_fname should be ddCTCF from iced
    # in2_fname should be dCTCF from iced
    # bin_fname should be bed file with bin locations from the raw folder
    
    in1_fname = "analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix"
    in2_fname = "analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix"
    bin_fname = "analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed"
    
    # in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1
                                       
    d1 = data1[(data1['F1'] >= start_bin) &
                        (data1['F2'] <= end_bin)]
    d2 = data2[(data2['F1'] >= start_bin) &
    
                        (data2['F2'] <= end_bin)]
    # log transform data                 
    d1['score'] = numpy.log(d1['score'])
    d2['score'] = numpy.log(d2['score'])
    
    # subtract minimum value
    d1_amin = numpy.amin(d1['score'])
    d1['score'] = d1['score'] - d1_amin

    d2_amin = numpy.amin(d2['score'])
    d2['score'] = d2['score'] - d2_amin

if __name__ == "__main__":
    main()