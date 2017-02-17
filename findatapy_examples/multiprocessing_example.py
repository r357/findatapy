__author__ = 'saeedamen'  # Saeed Amen

#
# Copyright 2016 Cuemacro
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and limitations under the License.
#

from findatapy.market import Market, MarketDataRequest, MarketDataGenerator
from findatapy.util import DataConstants, LoggerManager

def load_tickers():
    logger = LoggerManager.getLogger(__name__)

    market = Market(market_data_generator=MarketDataGenerator())

    DataConstants.market_thread_technique = 'thread'

    # get recent list of S&P500 (some of these will fail eg. BRK.B because incorrect ticker - findatapy should handle
    # this error gracefully)
    tickers = ["MMM",
        "ABT",
        "ABBV",
        "ACN",
        "ATVI",
        "AYI",
        "ADBE",
        "AAP",
        "AES",
        "AET",
        "AMG",
        "AFL",
        "A",
        "APD",
        "AKAM",
        "ALK",
        "ALB",
        "AGN",
        "LNT",
        "ALXN",
        "ALLE",
        "ADS",
        "ALL",
        "GOOGL",
        "GOOG",
        "MO",
        "AMZN",
        "AEE",
        "AAL",
        "AEP",
        "AXP",
        "AIG",
        "AMT",
        "AWK",
        "AMP",
        "ABC",
        "AME",
        "AMGN",
        "APH",
        "APC",
        "ADI",
        "ANTM",
        "AON",
        "APA",
        "AIV",
        "AAPL",
        "AMAT",
        "ADM",
        "ARNC",
        "AJG",
        "AIZ",
        "T",
        "ADSK",
        "ADP",
        "AN",
        "AZO",
        "AVB",
        "AVY",
        "BHI",
        "BLL",
        "BAC",
        "BK",
        "BCR",
        "BAX",
        "BBT",
        "BDX",
        "BBBY",
        "BRK.B",
        "BBY",
        "BIIB",
        "BLK",
        "HRB",
        "BA",
        "BWA",
        "BXP",
        "BSX",
        "BMY",
        "AVGO",
        "BF.B",
        "CHRW",
        "CA",
        "COG",
        "CPB",
        "COF",
        "CAH",
        "HSIC",
        "KMX",
        "CCL",
        "CAT",
        "CBG",
        "CBS",
        "CELG",
        "CNC",
        "CNP",
        "CTL",
        "CERN",
        "CF",
        "SCHW",
        "CHTR",
        "CHK",
        "CVX",
        "CMG",
        "CB",
        "CHD",
        "CI",
        "XEC",
        "CINF",
        "CTAS",
        "CSCO",
        "C",
        "CFG",
        "CTXS",
        "CLX",
        "CME",
        "CMS",
        "COH",
        "KO",
        "CTSH",
        "CL",
        "CMCSA",
        "CMA",
        "CAG",
        "CXO",
        "COP",
        "ED",
        "STZ",
        "GLW",
        "COST",
        "COTY",
        "CCI",
        "CSRA",
        "CSX",
        "CMI",
        "CVS",
        "DHI",
        "DHR",
        "DRI",
        "DVA",
        "DE",
        "DLPH",
        "DAL",
        "XRAY",
        "DVN",
        "DLR",
        "DFS",
        "DISCA",
        "DISCK",
        "DG",
        "DLTR",
        "D",
        "DOV",
        "DOW",
        "DPS",
        "DTE",
        "DD",
        "DUK",
        "DNB",
        "ETFC",
        "EMN",
        "ETN",
        "EBAY",
        "ECL",
        "EIX",
        "EW",
        "EA",
        "EMR",
        "ENDP",
        "ETR",
        "EVHC",
        "EOG",
        "EQT",
        "EFX",
        "EQIX",
        "EQR",
        "ESS",
        "EL",
        "ES",
        "EXC",
        "EXPE",
        "EXPD",
        "ESRX",
        "EXR",
        "XOM",
        "FFIV",
        "FB",
        "FAST",
        "FRT",
        "FDX",
        "FIS",
        "FITB",
        "FSLR",
        "FE",
        "FISV",
        "FLIR",
        "FLS",
        "FLR",
        "FMC",
        "FTI",
        "FL",
        "F",
        "FTV",
        "FBHS",
        "BEN",
        "FCX",
        "FTR",
        "GPS",
        "GRMN",
        "GD",
        "GE",
        "GGP",
        "GIS",
        "GM",
        "GPC",
        "GILD",
        "GPN",
        "GS",
        "GT",
        "GWW",
        "HAL",
        "HBI",
        "HOG",
        "HAR",
        "HRS",
        "HIG",
        "HAS",
        "HCA",
        "HCP",
        "HP",
        "HES",
        "HPE",
        "HOLX",
        "HD",
        "HON",
        "HRL",
        "HST",
        "HPQ",
        "HUM",
        "HBAN",
        "IDXX",
        "ITW",
        "ILMN",
        "IR",
        "INTC",
        "ICE",
        "IBM",
        "IP",
        "IPG",
        "IFF",
        "INTU",
        "ISRG",
        "IVZ",
        "IRM",
        "JEC",
        "JBHT",
        "SJM",
        "JNJ",
        "JCI",
        "JPM",
        "JNPR",
        "KSU",
        "K",
        "KEY",
        "KMB",
        "KIM",
        "KMI",
        "KLAC",
        "KSS",
        "KHC",
        "KR",
        "LB",
        "LLL",
        "LH",
        "LRCX",
        "LEG",
        "LEN",
        "LVLT",
        "LUK",
        "LLY",
        "LNC",
        "LLTC",
        "LKQ",
        "LMT",
        "L",
        "LOW",
        "LYB",
        "MTB",
        "MAC",
        "M",
        "MNK",
        "MRO",
        "MPC",
        "MAR",
        "MMC",
        "MLM",
        "MAS",
        "MA",
        "MAT",
        "MKC",
        "MCD",
        "MCK",
        "MJN",
        "MDT",
        "MRK",
        "MET",
        "MTD",
        "KORS",
        "MCHP",
        "MU",
        "MSFT",
        "MAA",
        "MHK",
        "TAP",
        "MDLZ",
        "MON",
        "MNST",
        "MCO",
        "MS",
        "MOS",
        "MSI",
        "MUR",
        "MYL",
        "NDAQ",
        "NOV",
        "NAVI",
        "NTAP",
        "NFLX",
        "NWL",
        "NFX",
        "NEM",
        "NWSA",
        "NWS",
        "NEE",
        "NLSN",
        "NKE",
        "NI",
        "NBL",
        "JWN",
        "NSC",
        "NTRS",
        "NOC",
        "NRG",
        "NUE",
        "NVDA",
        "ORLY",
        "OXY",
        "OMC",
        "OKE",
        "ORCL",
        "PCAR",
        "PH",
        "PDCO",
        "PAYX",
        "PYPL",
        "PNR",
        "PBCT",
        "PEP",
        "PKI",
        "PRGO",
        "PFE",
        "PCG",
        "PM",
        "PSX",
        "PNW",
        "PXD",
        "PBI",
        "PNC",
        "RL",
        "PPG",
        "PPL",
        "PX",
        "PCLN",
        "PFG",
        "PG",
        "PGR",
        "PLD",
        "PRU",
        "PEG",
        "PSA",
        "PHM",
        "PVH",
        "QRVO",
        "PWR",
        "QCOM",
        "DGX",
        "RRC",
        "RTN",
        "O",
        "RHT",
        "REGN",
        "RF",
        "RSG",
        "RAI",
        "RHI",
        "ROK",
        "COL",
        "ROP",
        "ROST",
        "RCL",
        "R",
        "CRM",
        "SCG",
        "SLB",
        "SNI",
        "STX",
        "SEE",
        "SRE",
        "SHW",
        "SIG",
        "SPG",
        "SWKS",
        "SLG",
        "SNA",
        "SO",
        "LUV",
        "SWN",
        "SE",
        "SPGI",
        "SWK",
        "SPLS",
        "SBUX",
        "STT",
        "SRCL",
        "SYK",
        "STI",
        "SYMC",
        "SYF",
        "SYY",
        "TROW",
        "TGT",
        "TEL",
        "TGNA",
        "TDC",
        "TSO",
        "TXN",
        "TXT",
        "COO",
        "HSY",
        "TRV",
        "TMO",
        "TIF",
        "TWX",
        "TJX",
        "TMK",
        "TSS",
        "TSCO",
        "TDG",
        "RIG",
        "TRIP",
        "FOXA",
        "FOX",
        "TSN",
        "UDR",
        "ULTA",
        "USB",
        "UA",
        "UAA",
        "UNP",
        "UAL",
        "UNH",
        "UPS",
        "URI",
        "UTX",
        "UHS",
        "UNM",
        "URBN",
        "VFC",
        "VLO",
        "VAR",
        "VTR",
        "VRSN",
        "VRSK",
        "VZ",
        "VRTX",
        "VIAB",
        "V",
        "VNO",
        "VMC",
        "WMT",
        "WBA",
        "DIS",
        "WM",
        "WAT",
        "WEC",
        "WFC",
        "HCN",
        "WDC",
        "WU",
        "WRK",
        "WY",
        "WHR",
        "WFM",
        "WMB",
        "WLTW",
        "WYN",
        "WYNN",
        "XEL",
        "XRX",
        "XLNX",
        "XL",
        "XYL",
        "YHOO",
        "YUM",
        "ZBH",
        "ZION",
        "ZTS",
    ]

    # download equities data from Yahoo
    md_request = MarketDataRequest(
        start_date="decade",  # start date
        data_source='yahoo',  # use Bloomberg as data source
        tickers=tickers,  # ticker (findatapy)
        fields=['close'],  # which fields to download
        vendor_tickers=tickers,  # ticker (Yahoo)
        vendor_fields=['Close'])  # which Bloomberg fields to download)


    logger.info("Loading data with threading")

    df = market.fetch_market(md_request)

    logger.info("Loading data with multiprocessing")

    DataConstants.market_thread_technique = 'multiprocessing'

    df = market.fetch_market(md_request)

    logger.info("Loaded data with multiprocessing")

if __name__ == "__main__":

    ###### below line CRUCIAL when running Windows, otherwise multiprocessing doesn't work! (not necessary on Linux)
    try:
        import multiprocess; multiprocess.freeze_support()
    except: pass

    load_tickers()