import collections
import doc

"""
Document renderer class for preloader source files

Each document renderer takes care of a full construction of
a specific file format using the required data model.  
"""
        
class pll_config_h:
    """
    pll_config.h renderer. 
    """
 
    def __init__(self, hpsModel, emifModel):
        
        self.hpsModel = hpsModel
        self.emifModel = emifModel
        self.doc = doc.generated_c_source("_PRELOADER_PLL_CONFIG_H_")


    def createContent(self):
        
        doc.c_source.line(self.doc)
        id = "CONFIG_HPS_DBCTRL_STAYOSC1"
        valueString = self.hpsModel.getSystemConfig("dbctrl_stayosc1")
        # Unfortunately hps.xml never tells us the data type of values
        # attributes. Here we workaround this type of problem, often
        # this is case-by-case, i.e. having to know which parameter that
        # we're dealing with, hence this ugly parameter-specific 
        # if-statement needs here to workaround the data type inconsistency
        if valueString.lower() == "true":
            value = "1"
        else:
            value = "0"
        doc.c_source.define(self.doc, id, "(" + value + ")")
        doc.c_source.line(self.doc)
        self.addMainPllSettings()
        doc.c_source.line(self.doc)
        self.addPeriphPllSettings()
        doc.c_source.line(self.doc)
        self.addSdramPllSettings()
        doc.c_source.line(self.doc)
        self.addClockFreq()
        doc.c_source.line(self.doc)
        self.addAlteraSettings()
        doc.c_source.line(self.doc)


    def addMainPllSettings(self):
        
        paramMap = collections.OrderedDict()
        
        paramMap["VCO_DENOM"] = "main_pll_n" 
        paramMap["VCO_NUMER"] = "main_pll_m"

        for key in paramMap.keys():
            id = "CONFIG_HPS_MAINPLLGRP_" + key
            value = self.hpsModel.getSystemConfig(paramMap[key])
            doc.c_source.define(self.doc, id, "(" + value + ")")
        
        
        # main_pll_c0, main_pll_c1, main_pll_c2 are fixed counters,
        # TODO: remove them if they're unused 
        doc.c_source.define(self.doc, "CONFIG_HPS_MAINPLLGRP_MPUCLK_CNT", "(0)")
        doc.c_source.define(self.doc, "CONFIG_HPS_MAINPLLGRP_MAINCLK_CNT", "(0)")
        doc.c_source.define(self.doc, "CONFIG_HPS_MAINPLLGRP_DBGATCLK_CNT", "(0)")
        
        
        paramMap = collections.OrderedDict()
        
        paramMap["MAINQSPICLK_CNT"] = "main_pll_c3" 
        paramMap["MAINNANDSDMMCCLK_CNT"] = "main_pll_c4" 
        paramMap["CFGS2FUSER0CLK_CNT"] = "main_pll_c5" 
        paramMap["MAINDIV_L3MPCLK"] = "l3_mp_clk_div" 
        paramMap["MAINDIV_L3SPCLK"] = "l3_sp_clk_div" 
        paramMap["MAINDIV_L4MPCLK"] = "l4_mp_clk_div" 
        paramMap["MAINDIV_L4SPCLK"] = "l4_sp_clk_div" 
        paramMap["DBGDIV_DBGATCLK"] = "dbg_at_clk_div" 
        paramMap["DBGDIV_DBGCLK"] = "dbg_clk_div" 
        paramMap["TRACEDIV_TRACECLK"] = "dbg_trace_clk_div" 
        paramMap["L4SRC_L4MP"] = "l4_mp_clk_source" 
        paramMap["L4SRC_L4SP"] = "l4_sp_clk_source"

        for key in paramMap.keys():
            id = "CONFIG_HPS_MAINPLLGRP_" + key
            value = self.hpsModel.getSystemConfig(paramMap[key])
            doc.c_source.define(self.doc, id, "(" + value + ")")

        
    def addPeriphPllSettings(self):
        
        paramMap = collections.OrderedDict()
        
        paramMap["VCO_DENOM"] = "periph_pll_n"
        paramMap["VCO_NUMER"] = "periph_pll_m"
        paramMap["VCO_PSRC"] = "periph_pll_source"
        paramMap["EMAC0CLK_CNT"] = "periph_pll_c0"
        paramMap["EMAC1CLK_CNT"] = "periph_pll_c1"
        paramMap["PERQSPICLK_CNT"] = "periph_pll_c2"
        paramMap["PERNANDSDMMCCLK_CNT"] = "periph_pll_c3"
        paramMap["PERBASECLK_CNT"] = "periph_pll_c4"
        paramMap["S2FUSER1CLK_CNT"] = "periph_pll_c5"
        paramMap["DIV_USBCLK"] = "usb_mp_clk_div"
        paramMap["DIV_SPIMCLK"] = "spi_m_clk_div"
        paramMap["DIV_CAN0CLK"] = "can0_clk_div"
        paramMap["DIV_CAN1CLK"] = "can1_clk_div"
        paramMap["GPIODIV_GPIODBCLK"] = "gpio_db_clk_div"
        paramMap["SRC_SDMMC"] = "sdmmc_clk_source"
        paramMap["SRC_NAND"] = "nand_clk_source"
        paramMap["SRC_QSPI"] = "qspi_clk_source"
        
        for key in paramMap.keys():
            id = "CONFIG_HPS_PERPLLGRP_" + key
            value = self.hpsModel.getSystemConfig(paramMap[key])
            doc.c_source.define(self.doc, id, "(" + value + ")")


    def addSdramPllSettings(self):
        
        # TODO: get static values from emif.xml
        value = self.emifModel.getPllDefine("PLL_MEM_CLK_DIV")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_VCO_DENOM", "(" + value + ")")
        value = self.emifModel.getPllDefine("PLL_MEM_CLK_MULT")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_VCO_NUMER", "(" + value + ")")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_VCO_SSRC", "(0)")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_DDRDQSCLK_CNT", "(1)")
        value = self.emifModel.getPllDefine("PLL_MEM_CLK_PHASE_DEG")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_DDRDQSCLK_PHASE", "(" + value + ")")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_DDR2XDQSCLK_CNT", "(0)")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_DDR2XDQSCLK_PHASE", "(0)")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_DDRDQCLK_CNT", "(1)")
        value = self.emifModel.getPllDefine("PLL_WRITE_CLK_PHASE_DEG")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_DDRDQCLK_PHASE", "(" + value + ")")
        # CASE:224223 - set based on value provided in hps.xml. If value doesn't exist. Hardcoded to value 5 as before.    
        try:
            value = self.hpsModel.getSystemConfig("sdram_pll_c5")
        except ValueError:
            value = "5"
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_S2FUSER2CLK_CNT", "(" + value +")")
        doc.c_source.define(self.doc, "CONFIG_HPS_SDRPLLGRP_S2FUSER2CLK_PHASE", "(0)")


    def addClockFreq(self):
        
        paramMap = collections.OrderedDict()
        
        paramMap["OSC1"] = "eosc1_clk_hz"
        paramMap["OSC2"] = "eosc2_clk_hz"
        paramMap["F2S_SDR_REF"] = "F2SCLK_SDRAMCLK_FREQ"
        paramMap["F2S_PER_REF"] = "F2SCLK_PERIPHCLK_FREQ"
        paramMap["MAINVCO"] = "main_pll_vco_hz"
        paramMap["PERVCO"] = "periph_pll_vco_hz"

        for key in paramMap.keys():
            id = "CONFIG_HPS_CLK_" + key + "_HZ"
            value = self.hpsModel.getSystemConfig(paramMap[key])
            doc.c_source.define(self.doc, id, "(" + value + ")")
            
        eosc1 = int(self.hpsModel.getSystemConfig("eosc1_clk_hz"))
        eosc2 = int(self.hpsModel.getSystemConfig("eosc2_clk_hz"))
        m = int(self.emifModel.getPllDefine("PLL_MEM_CLK_MULT"))
        n = int(self.emifModel.getPllDefine("PLL_MEM_CLK_DIV"))
        vco = int(round(eosc1 * (m + 1) / (n + 1)))
        doc.c_source.define(self.doc, "CONFIG_HPS_CLK_SDRVCO_HZ", "(" + str(vco) + ")")
        
        paramMap = collections.OrderedDict()
        
        paramMap["EMAC0"] = "emac0_clk_hz"
        paramMap["EMAC1"] = "emac1_clk_hz"
        paramMap["USBCLK"] = "usb_mp_clk_hz"
        paramMap["NAND"] = "nand_clk_hz"
        paramMap["SDMMC"] = "sdmmc_clk_hz"
        paramMap["QSPI"] = "qspi_clk_hz"
        paramMap["SPIM"] = "spi_m_clk_hz"
        paramMap["CAN0"] = "can0_clk_hz"
        paramMap["CAN1"] = "can1_clk_hz"
        paramMap["GPIODB"] = "gpio_db_clk_hz"
        paramMap["L4_MP"] = "l4_mp_clk_hz"
        paramMap["L4_SP"] = "l4_sp_clk_hz"
        
        for key in paramMap.keys():
            id = "CONFIG_HPS_CLK_" + key + "_HZ"
            value = self.hpsModel.getSystemConfig(paramMap[key])
            doc.c_source.define(self.doc, id, "(" + value + ")")
    
    
    def addAlteraSettings(self):
        
        paramMap = collections.OrderedDict()
        
        paramMap["MPUCLK"] = "main_pll_c0_internal" 
        paramMap["MAINCLK"] = "main_pll_c1_internal"
        paramMap["DBGATCLK"] = "main_pll_c2_internal"

        for key in paramMap.keys():
            id = "CONFIG_HPS_ALTERAGRP_" + key
            value = self.hpsModel.getSystemConfig(paramMap[key])
            doc.c_source.define(self.doc, id, "(" + value + ")")
        
    
    def __str__(self):
                     
        self.createContent()
        return str(self.doc)
