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

#ifndef __SDRAM_CONFIG_H
#define __SDRAM_CONFIG_H

#define CONFIG_HPS_SDR_CTRLCFG_CTRLCFG_MEMTYPE			(${DERIVED_MEMTYPE})
#define CONFIG_HPS_SDR_CTRLCFG_CTRLCFG_MEMBL			(${MEM_BURST_LENGTH})
#define CONFIG_HPS_SDR_CTRLCFG_CTRLCFG_ADDRORDER		(${ADDR_ORDER})
#define CONFIG_HPS_SDR_CTRLCFG_CTRLCFG_ECCEN			(${DERIVED_ECCEN})
#define CONFIG_HPS_SDR_CTRLCFG_CTRLCFG_ECCCORREN		(${DERIVED_ECCCORREN})
#define CONFIG_HPS_SDR_CTRLCFG_CTRLCFG_REORDEREN		(1)
#define CONFIG_HPS_SDR_CTRLCFG_CTRLCFG_STARVELIMIT		(10)
#define CONFIG_HPS_SDR_CTRLCFG_CTRLCFG_DQSTRKEN			(${USE_HPS_DQS_TRACKING})
#define CONFIG_HPS_SDR_CTRLCFG_CTRLCFG_NODMPINS			(${DERIVED_NODMPINS})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING1_TCWL			(${MEM_WTCL_INT})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING1_AL			(0)
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING1_TCL			(${MEM_TCL})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING1_TRRD			(${MEM_TRRD})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING1_TFAW			(${MEM_TFAW})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING1_TRFC			(${MEM_TRFC})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING2_IF_TREFI		(${MEM_TREFI})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING2_IF_TRCD		(${MEM_TRCD})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING2_IF_TRP		(${MEM_TRP})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING2_IF_TWR		(${MEM_TWR})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING2_IF_TWTR		(${MEM_TWTR})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING3_TRTP			(${MEM_TRTP})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING3_TRAS			(${MEM_TRAS})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING3_TRC			(${MEM_TRC})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING3_TMRD			(${MEM_TMRD_CK})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING3_TCCD			(4)
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING4_SELFRFSHEXIT		(${DERIVED_SELFRFSHEXIT})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMTIMING4_PWRDOWNEXIT		(3)
#define CONFIG_HPS_SDR_CTRLCFG_LOWPWRTIMING_AUTOPDCYCLES	(0)
#define CONFIG_HPS_SDR_CTRLCFG_LOWPWRTIMING_CLKDISABLECYCLES	(8)
#define CONFIG_HPS_SDR_CTRLCFG_DRAMADDRW_COLBITS		(${MEM_IF_COL_ADDR_WIDTH})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMADDRW_ROWBITS		(${MEM_IF_ROW_ADDR_WIDTH})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMADDRW_BANKBITS		(${MEM_IF_BANKADDR_WIDTH})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMADDRW_CSBITS			(${DEVICE_DEPTH})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMIFWIDTH_IFWIDTH		(${MEM_DQ_WIDTH})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMDEVWIDTH_DEVWIDTH		(8)
#define CONFIG_HPS_SDR_CTRLCFG_DRAMINTR_INTREN			(0)
#define CONFIG_HPS_SDR_CTRLCFG_LOWPWREQ_SELFRFSHMASK		(3)
#define CONFIG_HPS_SDR_CTRLCFG_STATICCFG_MEMBL			(2)
#define CONFIG_HPS_SDR_CTRLCFG_STATICCFG_USEECCASDATA		(0)
#define CONFIG_HPS_SDR_CTRLCFG_CTRLWIDTH_CTRLWIDTH		(${DERIVED_CTRLWIDTH})
#define CONFIG_HPS_SDR_CTRLCFG_PORTCFG_AUTOPCHEN		(0)
#define CONFIG_HPS_SDR_CTRLCFG_FIFOCFG_SYNCMODE			(0)
#define CONFIG_HPS_SDR_CTRLCFG_FIFOCFG_INCSYNC			(0)
#define CONFIG_HPS_SDR_CTRLCFG_MPPRIORITY_USERPRIORITY		(0x0)
#define CONFIG_HPS_SDR_CTRLCFG_MPWIEIGHT_0_STATICWEIGHT_31_0	(0x21084210)
#define CONFIG_HPS_SDR_CTRLCFG_MPWIEIGHT_1_STATICWEIGHT_49_32	(0x10441)
#define CONFIG_HPS_SDR_CTRLCFG_MPWIEIGHT_1_SUMOFWEIGHT_13_0	(0x78)
#define CONFIG_HPS_SDR_CTRLCFG_MPWIEIGHT_2_SUMOFWEIGHT_45_14	(0x0)
#define CONFIG_HPS_SDR_CTRLCFG_MPWIEIGHT_3_SUMOFWEIGHT_63_46	(0x0)
#define CONFIG_HPS_SDR_CTRLCFG_PHYCTRL_PHYCTRL_0		(0x200)

#define CONFIG_HPS_SDR_CTRLCFG_CPORTWIDTH_CPORTWIDTH		(0x44555)
#define CONFIG_HPS_SDR_CTRLCFG_CPORTWMAP_CPORTWMAP		(0x2C011000)
#define CONFIG_HPS_SDR_CTRLCFG_CPORTRMAP_CPORTRMAP		(0xB00088)
#define CONFIG_HPS_SDR_CTRLCFG_RFIFOCMAP_RFIFOCMAP		(0x760210)
#define CONFIG_HPS_SDR_CTRLCFG_WFIFOCMAP_WFIFOCMAP		(0x980543)
#define CONFIG_HPS_SDR_CTRLCFG_CPORTRDWR_CPORTRDWR		(0x5A56A)
#define CONFIG_HPS_SDR_CTRLCFG_MPPACING_0_THRESHOLD1_31_0	(0x20820820)
#define CONFIG_HPS_SDR_CTRLCFG_MPPACING_1_THRESHOLD1_59_32	(0x8208208)
#define CONFIG_HPS_SDR_CTRLCFG_MPPACING_1_THRESHOLD2_3_0	(0)
#define CONFIG_HPS_SDR_CTRLCFG_MPPACING_2_THRESHOLD2_35_4	(0x41041041)
#define CONFIG_HPS_SDR_CTRLCFG_MPPACING_3_THRESHOLD2_59_36	(0x410410)
#define CONFIG_HPS_SDR_CTRLCFG_MPTHRESHOLDRST_0_THRESHOLDRSTCYCLES_31_0 \
(0x01010101)
#define CONFIG_HPS_SDR_CTRLCFG_MPTHRESHOLDRST_1_THRESHOLDRSTCYCLES_63_32 \
(0x01010101)
#define CONFIG_HPS_SDR_CTRLCFG_MPTHRESHOLDRST_2_THRESHOLDRSTCYCLES_79_64 \
(0x0101)
#define CONFIG_HPS_SDR_CTRLCFG_DRAMODT_READ			(${CFG_READ_ODT_CHIP})
#define CONFIG_HPS_SDR_CTRLCFG_DRAMODT_WRITE			(${CFG_WRITE_ODT_CHIP})
#define CONFIG_HPS_SDR_CTRLCFG_FPGAPORTRST_READ_PORT_USED	(${F2SDRAM_READ_PORT_USED})
#define CONFIG_HPS_SDR_CTRLCFG_FPGAPORTRST_WRITE_PORT_USED	(${F2SDRAM_WRITE_PORT_USED})
#define CONFIG_HPS_SDR_CTRLCFG_FPGAPORTRST_COMMAND_PORT_USED	(${F2SDRAM_COMMAND_PORT_USED})
#define CONFIG_HPS_SDR_CTRLCFG_FPGAPORTRST			(${F2SDRAM_RESET_PORT_USED})

#define CONFIG_HPS_SDR_CTRLCFG_EXTRATIME1_CFG_EXTRA_CTL_CLK_RD_TO_WR (${DERIVED_CLK_RD_TO_WR})
#define CONFIG_HPS_SDR_CTRLCFG_EXTRATIME1_CFG_EXTRA_CTL_CLK_RD_TO_WR_BC (${DERIVED_CLK_RD_TO_WR})
#define CONFIG_HPS_SDR_CTRLCFG_EXTRATIME1_CFG_EXTRA_CTL_CLK_RD_TO_WR_DIFF_CHIP (${DERIVED_CLK_RD_TO_WR})


#endif	/*#ifndef__SDRAM_CONFIG_H*/