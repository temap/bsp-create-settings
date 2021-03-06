#! /usr/bin/env python

'''
Created on Sep 20, 2012

@author:ejamesbe
'''

import glob
import optparse
import os
import shutil

import emif
import hps
import iocsr

import renderer
import model
import collections
import sys

def printUsage():
    print "Usage:\n\t%s\n" % \
          ("sys.argv[0], --input_dir=<path to iswinfo directory> --output_dir=<path store output files>")
    exit(1)

def verifyInputDir(dir):
    if not os.path.isdir(dir):
        print "There is no such directory '%s'!\n" % (dir)
        exit(1)

def verifyOutputDir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)

if __name__ == '__main__':
    # Do some rudimentary command line processing until it is proven we need something
    # heavier, such as argparse (preferred, but 2.7+ only) or optparse

    inputDir = '.'
    outputDir = '.'
    
    progVersion = '%prog 0.1'
    progDesc = 'Generate board-specific files for the preloader'
    optParser = optparse.OptionParser(version=progVersion, description=progDesc)
    optParser.add_option('-i', '--input-dir', action='store', type='string', dest='inputDir', default='.',
                         help='input-dir is usually the iswinfo directory')
    optParser.add_option('-o', '--output-dir', action='store', type='string', dest='outputDir', default='.',
                         help='output-dir is usually the directory containing the preloader source')
    
    (options, args) = optParser.parse_args()
    
    for arg in args:
        print "***WARNING: I don't understand '%s', so I am ignoring it\n" % (arg)

    inputDir = options.inputDir
    verifyInputDir(inputDir)
    outputDir = options.outputDir
    
    verifyOutputDir(outputDir)

    emif = emif.EMIFGrokker(inputDir, outputDir, 'emif.xml')
    hps = hps.HPSGrokker(inputDir, outputDir)

    pllConfigH = outputDir + "/" + "pll_config.h"
    print "Generating file: " + pllConfigH
    hpsModel = model.hps.create(inputDir + "/" + "hps.xml")
    emifModel = model.emif.create(inputDir +"/" + "emif.xml")
    
    content=str(renderer.pll_config_h(hpsModel, emifModel))
    f = open(pllConfigH, "w")
    print >>f, content
    f.close()
        
    # For all the .hiof files, make a iocsr_config.[h|c]
    # TODO: This only works for the last .hiof file found
    #       If we really want to handle more than one
    # .hiof file, we need to come up with an output file
    # naming convention.
    hiof_list = glob.glob(inputDir + os.sep + "*.hiof")
    if len(hiof_list) < 1:
        print "***Error: No .hiof files found in input!"
        
    elif len(hiof_list) > 1:
        print "***Error: We don't handle more than one .hiof file yet"
        print "          Only the last .hiof file in the list will be converted"
        print "          hiof files found:"
        for f in hiof_list:
            print "              " + f
            
    for hiof_file_path in hiof_list:
        hiof_file = os.path.basename(hiof_file_path)
        # CHA: This is literally a hack
        #    to avoid IOCSRGrokker having to parse hps.xml to determine
        #    device family for output file name, instead we'll just
        #    get it from HPSGrokker
        iocsr = iocsr.IOCSRGrokker(hps.getDeviceFamily(), inputDir, outputDir, hiof_file)

    # Copy some of the files from the input directory to the output directory
    # because some files generated by Quartus are used directly by the
    # preloader
    # TODO: Right now, just copy them all
    # Change of plan: Chin Huat says that BSP Edit [Generate] is going to do the 
    # file copy.  Commenting this for now.  When we have BSP Editor doing the work
    # all this can be removed.
    if False:
        print "Copying these files from %s to %s:" % (inputDir, outputDir)
        file_list = glob.glob(inputDir + os.sep + "*")
        for f in file_list:
            print "    %s" % (os.path.basename(f))
            shutil.copy2(f, outputDir)
        