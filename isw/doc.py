"""
Generic document construction classes.

These classes are templates for creating documents that are not bound
to a specific usage nor data model.
"""

class document(object):
    """
    An abstract document class which does not dictate
    how a document should be constructed or manipulated.
     
    It's sole purpose is to describe the entire document
    in smaller units
    """

    class entry(object):
        """ 
        An entry is the smallest unit 
        """
        
        def __init__(self, parent):
            if parent != None:
                parent.add(self)

    class block(entry):
        """
        A block is the smallest collection unit
        consists of entries and blocks.
        """
        
        def __init__(self, parent):
            super(document.block, self).__init__(parent)
            self.entries = []
            
        def add(self, entry):
            self.entries.append(entry)
    
    
    def __init__(self):
        self.entries = []
        
    def add(self, entry):
        self.entries.append(entry)

    
class text(document):
    """ 
    A simple text document implementation 
    """
    
    class string(document.entry):
        """
        The smallest unit of a text file is a string
        """
        
        def __init__(self, parent, stringString=None):
            super(text.string, self).__init__(parent)
            self.stringString = stringString
             
        def __str__(self):
            if (self.stringString != None):
                return self.stringString
            else:
                return ""
        

    class line(string):
        """
        A line is a string with EOL character
        """
        
        def __str__(self):
            return super(text.line, self).__str__() + "\n"
            
    class block(document.block):
        """
        A block of text which can be made up of
        strings or lines
        """
        
        def __str__(self):
            
            blockString = ""
            
            for entry in self.entries:
                blockString += str(entry)
                
            return blockString

            
    def __str__(self):
        
        textString = ""
        
        for entry in self.entries:
            textString += str(entry)
            
        return textString


class c_source(text):
    """
    A simple C header document implementation
    """
    
    class define(text.string):
        
        def __init__(self, parent, id, token=None):
            super(c_source.define, self).__init__(parent, id)
            self.token = token
    
        def __str__(self):
            
            defineString = "#define" + " " + super(c_source.define, self).__str__()

            if self.token != None:
                defineString += " " + self.token
            
            defineString += "\n"
            
            return defineString
    
    class comment_string(text.string):
        
        def __str__(self):
            return "/*" + " " + super(c_source.comment_string, self).__str__() + " " + "*/"
            
    class comment_line(comment_string):
        
        def __str__(self):
            return super(c_source.comment_line, self).__str__() + "\n"

    class block(text.block):
        
        def __init__(self, parent, prologue=None, epilogue=None):
            super(c_source.block, self).__init__(parent)
            
            self.prologue = None
            self.epilogue = None
            
            if prologue != None:
                self.prologue = prologue
                
            if epilogue != None:
                self.epilogue = epilogue

        def __str__(self):
            
            blockString = ""
            
            if self.prologue != None:
                blockString += str(self.prologue)
            
            blockString += super(c_source.block, self).__str__()
            
            if self.epilogue != None:
                blockString += str(self.epilogue)
            
            return blockString
    
    class comment_block(block):
        
        def __init__(self, parent, comments):
            super(c_source.comment_block, self).__init__(parent, "/*\n", " */\n")
            for comment in comments.split("\n"):
                self.add(comment)
        
        def add(self, entry):
            super(c_source.block, self).add(" * " + entry + "\n")
        
    class ifndef_block(block):
        
        def __init__(self, parent, id):
            prologue = text.line(None, "#ifndef" + " " + id)
            epilogue = text.block(None)
            text.string(epilogue, "#endif")
            text.string(epilogue, " ")
            c_source.comment_line(epilogue, id)
            super(c_source.ifndef_block, self).__init__(parent, prologue, epilogue)


class generated_c_source(c_source):

    def __init__(self, filename):
        
        super(generated_c_source, self).__init__()
        
        self.entries.append(c_source.comment_line(None, "GENERATED FILE - DO NOT EDIT"))
        
        licenseHeader = """\
Copyright Altera Corporation (C) 2012-2014. All rights reserved\n\
\n\
SPDX-License-Identifier:    BSD-3-Clause\n\
\n\
Redistribution and use in source and binary forms, with or without\n\
modification, are permitted provided that the following conditions are met:\n\
   * Redistributions of source code must retain the above copyright\n\
     notice, this list of conditions and the following disclaimer.\n\
   * Redistributions in binary form must reproduce the above copyright\n\
     notice, this list of conditions and the following disclaimer in the\n\
     documentation and/or other materials provided with the distribution.\n\
   * Neither the name of Altera Corporation nor the\n\
     names of its contributors may be used to endorse or promote products\n\
     derived from this software without specific prior written permission.\n\
\n\
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND\n\
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED\n\
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\n\
DISCLAIMED. IN NO EVENT SHALL ALTERA CORPORATION BE LIABLE FOR ANY\n\
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n\
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n\
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\n\
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n\
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS\n\
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."""
            
        self.entries.append(c_source.comment_block(None, licenseHeader))
        self.entries.append(text.line(None))
        
        self.body = c_source.ifndef_block(None, filename)
        self.body.add(c_source.define(None, filename))
        self.entries.append(self.body)
        
    def add(self, entry):
        self.body.add(entry)