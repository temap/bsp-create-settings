'''
Created on Oct 9, 2012

@author:ejamesbe, chang
'''
import os
import xml.dom.minidom
import streamer
import xmlgrok

class EMIFGrokker(object):
    """ Parse an emif.xml input and translate to various
    outputs
    """
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
    TEMPLATE_DIR = os.path.dirname(SCRIPT_DIR) + '/src'
    
    SDRAM_CONFIG_H_FILENAME = "sdram_config.h"

    sdramHTemplate = ""
    
    def __init__(self, inputDir, outputDir, emifFileName='emif.xml', hpsFileName='hps.xml'):
        """ EMIFGrokker initialization """
        self.inputDir = inputDir
        self.outputDir = outputDir
        
        sdramDir = self.outputDir + "/sdram"
        if not os.path.isdir(sdramDir):
            os.makedirs(sdramDir)        
        
        self.emifFileName = inputDir + os.sep + emifFileName
        self.hpsFileName = inputDir + os.sep + hpsFileName        
        self.emifDom = xml.dom.minidom.parse(self.emifFileName)
        self.hpsDom = xml.dom.minidom.parse(self.hpsFileName)
        self.sequencerDefinesStream = None

        self.createFilesFromEMIF()

    def handleSettingNode(self, settingNode):
        if settingNode.hasAttribute('name') and settingNode.hasAttribute('value'):
            name = settingNode.getAttribute('name')
            value = settingNode.getAttribute('value')
            self.sequencerDefinesStream.write("#define " + name + ' ' + '(' + value + ')' + '\n')

    def updateTemplate(self, name, value):
        pattern = "${" + name + "}"
        self.sdramHTemplate = self.sdramHTemplate.replace(pattern, value)
        
    def handleEMIFControllerNode(self, node):
        
        derivedNoDmPins = 0
        derivedCtrlWidth = 0
        derivedEccEn = 0
        derivedEccCorrEn = 0

        self.mem_if_rd_to_wr_turnaround_oct = 0

        node = xmlgrok.firstElementChild(node)
        while node != None:
            name = node.getAttribute('name')
            value = node.getAttribute('value')
            
            if value == "true":
                value = "1"
            elif value == "false":
                value = "0"
            
            self.updateTemplate(name, value)
            
            if name == "MEM_IF_DM_PINS_EN":
                if value == "1":
                    derivedNoDmPins = 0
                else:
                    derivedNoDmPins = 1

            if name == "MEM_DQ_WIDTH":
                if value == "8":
                    derivedCtrlWidth = 0
                    derivedEccEn = 0
                    derivedEccCorrEn = 0
                elif value == "16":
                    derivedCtrlWidth = 1                    
                    derivedEccEn = 0
                    derivedEccCorrEn = 0
                elif value == "24":
                    derivedCtrlWidth = 1
                    derivedEccEn = 1
                    derivedEccCorrEn = 1
                elif value == "32":
                    derivedCtrlWidth = 2
                    derivedEccEn = 0
                    derivedEccCorrEn = 0
                elif value == "40":
                    derivedCtrlWidth = 2
                    derivedEccEn = 1
                    derivedEccCorrEn = 1

            if name == "MEM_IF_RD_TO_WR_TURNAROUND_OCT":
                self.mem_if_rd_to_wr_turnaround_oct = int(value)

            node = xmlgrok.nextElementSibling(node)
            
        self.updateTemplate("DERIVED_NODMPINS", str(derivedNoDmPins))
        self.updateTemplate("DERIVED_CTRLWIDTH", str(derivedCtrlWidth))
        self.updateTemplate("DERIVED_ECCEN", str(derivedEccEn))
        self.updateTemplate("DERIVED_ECCCORREN", str(derivedEccCorrEn))
 
    def handleEMIFPllNode(self, node):
        
        node = xmlgrok.firstElementChild(node)
        while node != None:
            name = node.getAttribute('name')
            value = node.getAttribute('value')
            
            self.updateTemplate(name, value)
            
            node = xmlgrok.nextElementSibling(node)
        
    def handleEMIFSequencerNode(self, node):
        
        derivedMemtype = 0
        derivedSelfrfshexit = 0

        self.afi_rate_ratio = 0
        
        node = xmlgrok.firstElementChild(node)
        while node != None:
            name = node.getAttribute('name')
            value = node.getAttribute('value')
            
            self.updateTemplate(name, value)

            if value.isdigit():
                intValue = int(value)
            else:
                intValue = 0
            
            if name == "DDR2" and intValue != 0:
                derivedMemtype = 1
                derivedSelfrfshexit = 200
            elif name == "DDR3" and intValue != 0:
                derivedMemtype = 2
                derivedSelfrfshexit = 512
            elif name == "LPDDR1" and intValue != 0:
                derivedMemtype = 3
                derivedSelfrfshexit = 200
            elif name == "LPDDR2" and intValue != 0:
                derivedMemtype = 4
                derivedSelfrfshexit = 200
            elif name == "AFI_RATE_RATIO" and intValue != 0:
                self.afi_rate_ratio = intValue

            node = xmlgrok.nextElementSibling(node)

        self.updateTemplate("DERIVED_MEMTYPE", str(derivedMemtype))
        self.updateTemplate("DERIVED_SELFRFSHEXIT", str(derivedSelfrfshexit))


    def handleHpsFpgaInterfaces(self, node):
        
        node = xmlgrok.firstElementChild(node)
        
        while node != None:
            name = node.getAttribute('name')
            value = node.getAttribute('value')
            
            self.updateTemplate(name, value)
            
            node = xmlgrok.nextElementSibling(node)

            
    def createFilesFromEMIF(self):
        
        sdramHTemplateFilename = self.TEMPLATE_DIR + "/sdram/" + self.SDRAM_CONFIG_H_FILENAME
        handle = open(sdramHTemplateFilename, "r")
        self.sdramHTemplate = handle.read()
        handle.close()
        
        # Get a list of all nodes with the emif element name
        emifNodeList = self.emifDom.getElementsByTagName('emif')
        if len(emifNodeList) > 1:
            print "*** WARNING:" + "Multiple emif Elements found in %s!" % self.emifFileName
        # For each of the emif element nodes, go through the child list
        # Note that currently there is only one emif Element
        # but this code will handle more than one emif node
        # In the future, multiple emif nodes may need additional code
        # to combine settings from the multiple emif Elements
        for emifNode in emifNodeList:
            # Currently, there are only 3 children of the emif Element:
            #     sequencer, controller, and pll
            # but this is left open-ended for future additions to the
            # specification for the emif.xml
            childNode = xmlgrok.firstElementChild(emifNode)
            while childNode != None:
                
                if childNode.nodeName == 'controller':
                    self.handleEMIFControllerNode(childNode)
                elif childNode.nodeName == 'sequencer':
                    self.handleEMIFSequencerNode(childNode)
                elif childNode.nodeName == 'pll':
                    self.handleEMIFPllNode(childNode)

                childNode = xmlgrok.nextElementSibling(childNode)
        
        data_rate_ratio = 2
        dwidth_ratio = self.afi_rate_ratio * data_rate_ratio
        if dwidth_ratio == 0:
            derivedClkRdToWr = 0
        else:
            derivedClkRdToWr = (self.mem_if_rd_to_wr_turnaround_oct / (dwidth_ratio / 2))

            if (self.mem_if_rd_to_wr_turnaround_oct % (dwidth_ratio / 2)) > 0:
                derivedClkRdToWr += 1

        self.updateTemplate("DERIVED_CLK_RD_TO_WR", str(derivedClkRdToWr))

        # MPFE information are stored in hps.xml despite we generate
        # them into sdram_config, so let's load hps.xml
        hpsNodeList = self.hpsDom.getElementsByTagName('hps')
        
        for hpsNode in hpsNodeList:
            
            childNode = xmlgrok.firstElementChild(hpsNode)
            
            while childNode != None:
                # MPFE info is part of fpga_interfaces
                if childNode.nodeName == 'fpga_interfaces':
                    self.handleHpsFpgaInterfaces(childNode)
                    
                childNode = xmlgrok.nextElementSibling(childNode)
                
        self.sequencerDefinesStream = streamer.Streamer(self.outputDir  + "/sdram/" + os.sep + EMIFGrokker.SDRAM_CONFIG_H_FILENAME, 'w')
        self.sequencerDefinesStream.open()
        self.sequencerDefinesStream.write(self.sdramHTemplate)
        self.sequencerDefinesStream.close()
