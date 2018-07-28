'''
Created on Oct 9, 2012

@author: ejamesbe
'''
import os
import struct

class Streamer(object):
    def __init__(self, fileName, mode='r'):
        self.fileName = fileName
        self.mode = mode
        self.file = None
        self.sentinel = None
        if '+' in mode or 'w' in mode or 'a' in mode:
            self.fileMode = 'write'
        else:
            self.fileMode = 'read'

    def close(self):
        if self.file != None:
            self.file.close()
            self.file = None

    def open(self):
        if self.fileName != None:
            if self.file == None:
                if self.fileMode == 'write':
                    print "Generating file: %s..." % self.fileName
                else:
                    print "Reading file: %s..." % self.fileName
                self.file = open(self.fileName, self.mode)

    def read(self, numBytes):
        if self.file == None:
            print "***Error: Attempted to read from unopened file %s" \
                  % (self.fileName)
            exit(-1)
            
        else:
            return self.file.read(numBytes)
        
    def readUnsignedInt(self):
        return struct.unpack('I', self.read(4))[0]
    
    def readUnsignedShort(self):
        return struct.unpack('H', self.read(2))[0]

    def readBytesAsString(self, numBytes):
        ''' Read some bytes from a binary file
        and interpret the data values as a String
        '''
        bytes = self.read(numBytes)
        # We don't like nulls
        bytes = bytes.replace('\x00', '')
        s = ''
        for b in bytes:
            s += b
        return s


    ###self.fileExtension = IOCSRGrokker.byteArrayToStr(self.hiofStream.read(IOCSRGrokker.IOCSR_FILE_EXTENSION_MAX_LEN))


    def write(self, str):
        if self.file == None:
            print "***Error: Attempted to write to unopened file %s" \
                % (self.fileName)
            exit(-1)

        else:
            self.file.write("%s" % str)

    def writeLicenseHeader(self):
        licenseHeader = """\
/* GENERATED FILE - DO NOT EDIT */
/* 
 * Copyright Altera Corporation (C) 2012-2014. All rights reserved
 * 
 * SPDX-License-Identifier:    BSD-3-Clause
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *    * Redistributions of source code must retain the above copyright
 *      notice, this list of conditions and the following disclaimer.
 *    * Redistributions in binary form must reproduce the above copyright
 *      notice, this list of conditions and the following disclaimer in the
 *      documentation and/or other materials provided with the distribution.
 *    * Neither the name of Altera Corporation nor the
 *      names of its contributors may be used to endorse or promote products
 *      derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL ALTERA CORPORATION BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

"""
        self.file.write("%s" % licenseHeader)
                
    def writeSentinelStart(self, sentinel):
        self.sentinel = sentinel
        self.file.write("%s\n%s\n\n" % (\
            "#ifndef " + self.sentinel,
            "#define " + self.sentinel))

    def writeSentinelEnd(self):
        self.file.write("\n%s\n" % ("#endif /* " + self.sentinel + "*/"))
