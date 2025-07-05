tickers = [
    # Tech & Communication
    "AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "NVDA", "META", "TSLA", "ORCL", "CRM",
    "INTC", "AMD", "QCOM", "ADBE", "CSCO", "AVGO", "TXN", "MU", "NOW", "ZM",
    "DOCU", "UBER", "LYFT", "SNOW", "PANW", "FTNT", "ANET", "TEAM", "WDAY", "SHOP",
    "DDOG", "CRWD", "ZS", "NET", "OKTA", "PLTR", "SPLK", "MDB", "TWLO", "FSLY",

    # Financials
    "JPM", "BAC", "WFC", "GS", "MS", "C", "AXP", "SCHW", "BLK", "TROW",
    "AIG", "ALL", "CB", "TRV", "MTB", "FITB", "HBAN", "CFG", "KEY", "ZION",
    "DFS", "COF", "PGR", "PRU", "LNC", "AFL", "HIG", "MKTX", "NDAQ", "ICE",

    # Healthcare
    "JNJ", "PFE", "ABBV", "MRK", "LLY", "BMY", "UNH", "CVS", "TMO", "AMGN",
    "GILD", "VRTX", "REGN", "BIIB", "MDT", "ISRG", "SYK", "DHR", "ABT", "BDX",
    "CI", "HUM", "ZBH", "ALGN", "ILMN", "RMD", "BAX", "EW", "XRAY", "MRNA",

    # Consumer Defensive & Cyclical
    "PG", "KO", "PEP", "WMT", "COST", "TGT", "MCD", "SBUX", "NKE", "HD",
    "LOW", "EL", "KMB", "CL", "GIS", "CPB", "KR", "DG", "DLTR", "TSCO",
    "HSY", "MDLZ", "WBA", "TAP", "PM", "MO", "STZ", "KHC", "CHD", "HRL",

    # Energy
    "XOM", "CVX", "COP", "PSX", "VLO", "MPC", "EOG", "SLB", "HAL", "OXY",
    "BKR", "FANG", "APA", "DVN", "PXD", "KMI", "WMB", "ENB", "ET", "OKE",
    "HES", "MUR", "AR", "RRC", "NOG", "SM", "TELL", "CHX", "NOV", "CTRA",

    # Industrials
    "BA", "CAT", "GE", "DE", "MMM", "LMT", "NOC", "RTX", "HON", "GD",
    "UNP", "NSC", "CSX", "UPS", "FDX", "WM", "RSG", "EMR", "ETN", "PH",
    "CMI", "ITW", "DOV", "JCI", "IR", "TT", "MAS", "PNR", "XYL", "ALK",

    # Utilities
    "NEE", "DUK", "SO", "D", "AEP", "EXC", "SRE", "XEL", "ED", "PEG",
    "EIX", "PPL", "WEC", "AES", "CMS", "DTE", "AWK", "LNT", "NI", "CNP",
    "AEE", "ATO", "UGI", "IDA", "PNW", "ES", "NRG", "EVRG", "OGE", "SWX",

    # Real Estate
    "PLD", "AMT", "CCI", "EQIX", "SPG", "PSA", "DLR", "O", "VTR", "WELL",
    "AVB", "EQR", "EXR", "MAA", "ARE", "ESS", "UDR", "FRT", "BXP", "SLG",
    "INVH", "IRM", "PEAK", "SUI", "ELS", "CUBE", "STAG", "KIM", "REG", "NTST",

    # Consumer Discretionary
    "ROST", "TJX", "BBY", "ULTA", "LB", "KSS", "PVH", "NKE", "LULU", "YUM",
    "DPZ", "CMG", "MAR", "HLT", "RCL", "CCL", "HOG", "WHR", "BBWI", "ETSY",
    "EBAY", "TSCO", "DKS", "WSM", "W", "AZO", "ORLY", "GPC", "POOL", "RH",

    # Semiconductors
    "NVDA", "AMD", "INTC", "QCOM", "AVGO", "TXN", "MU", "ADI", "LSCC", "MPWR",
    "ASML", "TSM", "AMAT", "KLAC", "LRCX", "ON", "NXPI", "MRVL", "GFS", "WOLF",

    # ETFs (Optional for reference)
    "SPY", "QQQ", "DIA", "IWM", "VTI", "VOO", "ARKK", "XLK", "XLF", "XLE"
]

tickers2 = [
    # Tech & Communication (US & Global)
    "AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "NVDA", "META", "TSLA", "ORCL", "CRM",
    "INTC", "AMD", "QCOM", "ADBE", "CSCO", "AVGO", "TXN", "MU", "NOW", "ZM",
    "DOCU", "UBER", "LYFT", "SNOW", "PANW", "FTNT", "ANET", "TEAM", "WDAY", "SHOP",
    "DDOG", "CRWD", "ZS", "NET", "OKTA", "PLTR", "SPLK", "MDB", "TWLO", "FSLY",
    "ASML", "SMCI", "STM", "ERIC", "NOK", "GDDY", "CHKP", "HPE", "BR", "TDY",
    "HUBS", "KEYS", "VRSN", "CDW", "STX", "ADI", "LRCX", "KLAC", "AMAT", "MCHP",
    "QRVO", "NVMI", "MPWR", "SNPS", "CDNS", "SWKS", "MTSI", "HPQ", "IBM", "ACN",
    "TER", "JNPR", "DELL", "WDC", "AMKR", "FLEX", "WORK", "ZM", "COUP", "PATH",
    "ALRM", "MDB", "ZI", "ESTC", "BILL", "PAYC", "AYX", "DT", "CLDR", "CMCSA",
    "TMUS", "VZ", "T", "DIS", "NFLX", "ROKU", "EA", "LYV", "SONY", "TTWO",
    "PINS", "SNAP", "MTCH", "RDDT", "FOXA", "FOX", "NWSA", "NYT", "PARA", "WBD",
    "SAP", "TCEHY", "BIDU", "BABA", "YNDX", "TECHM", "INFY", "TCS", "WIPRO", "HCLTECH",
    "PERSISTENT", "LTIM", "MPHASIS", "COFORGE", "IT", "CYBR", "EXTR", "PSTG", "EBAY", "ETSY",
    "PDD", "BKNG", "TRIP", "8X8", "AFRM"

    # Major US Banks & Diversified Finance
    "JPM", "BAC", "WFC", "C", "GS", "MS", "USB", "BK", "PNC", "TFC",
    "ZION", "KEY", "FITB", "HBAN", "CFG", "RF", "FRC", "FBC", "SIVB",
    "ZION", "CMA", "CUBI", "CFG", "BXS", "MTB", "RF", "PNC", "USB", "ZION",

    # Asset Managers / Investment Services
    "BLK", "SCHW", "NDAQ", "ICE", "TROW", "AMG", "BEN", "LM", "BG", "IVZ",
    "LPLA", "MPW", "STT", "CINF", "ETFC", "SEIC", "MCO", "STWD", "AIG",

    # Insurance (Life, P&C)
    "MET", "PRU", "LNC", "AFL", "HIG", "ALL", "TRV", "CINF", "PGR", "CB",
    "WRB", "PBCT", "CNO", "UNM", "MKL", "PFG",

    # Exchanges & Clearing Houses
    "CME", "ICE", "NDAQ", "DTCC", "BX", "SI", "GS", "MS", "GS", "ICE",

    # Fintech & Specialized Finance
    "PYPL", "COIN", "UPST", "ALLY", "AXP", "DFS", "SYF", "STFC", "SBNY",
    "CAR", "PENN", "CASH", "OVAS", "LMND", "GS", "PYPL",

    # Regional & Community Banks
    "FHN", "BANF", "HBAN", "HOMB", "FULT", "ESXB", "FFIN", "FCFS", "CWBC",
    "PNBK", "PNC", "BOKF", "FULT", "ZION", "CUBI", "CMA", "CERC", "CAC",
    
    # Specialty Finance / Mortgage / Auto Finance
    "WEX", "GS", "ALLY", "SSTK", "MTGE", "FIG", "PFSI", "ABR", "RYAAY",
    "AMG", "FIG", "FIGS", "FNF", "LMR", "THG", "REXR", "LATN", "AGO",

    # Diversified Financials & Conglomerates
    "BRK.B", "BRK.A", "BEN", "AFL", "AXP", "COF", "CMA", "AIG", "BAC",
    "BK", "C", "GS", "JPM", "MS", "USB",

    # Credit & Payment Services
    "MA", "V", "AXP", "PYPL", "DFS", "SYF", "COF", "DFS",

    # Real Estate Investment Trusts (REITs) – diversified financial mix
    "MFA", "AGNC", "O", "SPG", "PLD", "PSA", "EQIX", "VNQ", "AVB", "MAA",
    
    # International & Global Financials
    "HSBC", "BARC", "STAN", "LLOY", "UBS", "DB", "CS", "ING", "SNY", "BZ.TO",
    "TD", "BNS", "RY", "CNR", "ITUB", "BBVA", "SAN", "BNP", "BNP.PA",

    # Financial Exchanges (Crypto-adjacent)
    "COIN", "SI", "IX", "NDAQ", "ICE",

    # Other Equities & Clearing/Exchange
    "ICE", "CME", "NDAQ", "DTCC",

    # Regional Picks (from Nasdaq Financial-100)
    "ABCB", "ACGL", "BANF", "BOKF", "CATY", "CINF", "COLB", "EWBC", "FRC", "FHN",
    "FCFS", "HWC", "HBAN", "IBTX", "LPLA", "TM", "MKTX", "MORN", "NAVI", "NTRS",
    "ONB", "PPBI", "PNFP", "BPOP", "SSB", "SMMF", "SYBT", "SNEX", "TCBI", "TRMK",
    "UMBF", "UCBI", "VLY", "VIRT", "WAFD", "WTFC", "WSFS"
    
    ##HEALTHCARE
    # Pharmaceuticals & Biotechnology
    "JNJ", "PFE", "ABBV", "MRK", "LLY", "BMY", "UNH", "CVS", "TMO", "AMGN",
    "GILD", "VRTX", "REGN", "BIIB", "MRNA", "ALXN", "INCY", "SGEN", "EXEL", "IDXX",
    "BNTX", "ACAD", "IONS", "BLUE", "CRSP", "IONS", "VTRS", "SAGE", "MYGN", "NBIX",
    "ACHV", "MRNA", "EDIT", "ALNY", "IONS", "DXCM",

    # Medical Devices & Diagnostics
    "MDT", "ISRG", "SYK", "DHR", "ABT", "BDX", "ZBH", "ALGN", "ILMN", "RMD",
    "BAX", "EW", "XRAY", "VAR", "MASI", "MTD", "PKI", "IDXX", "LH", "TFX",
    "HOLX", "CRL", "HUBS", "GPK", "AEMD", "SEM", "RGEN", "MDXG", "PRLB", "THRM",

    # Healthcare Providers & Services
    "HUM", "CI", "CNC", "DGX", "WST", "UHS", "LHCG", "CNC", "AMED", "HCA",
    "CNC", "CNC", "MCK", "LH", "CAH", "CNC", "RMD", "BAX", "UNH", "CVS",

    # Healthcare REITs & Other Healthcare Services
    "WELL", "VTR", "HCP", "OHI", "DOC", "HR", "MPW", "VTRS", "HST", "SBAC",

    # Additional Biotech & Pharma
    "BLUE", "CRSP", "EDIT", "IONS", "SGEN", "ACAD", "ALNY", "NBIX", "MYGN", "ACHV",
    "VTRS", "ARWR", "XLRN", "XOMA", "RDUS", "EXAS", "ARCT", "ALKS", "MARA",

    # International Healthcare & Other US Mid-Caps
    "AZN", "NVS", "RHHBY", "GSK", "SNY", "BAYRY", "DHR", "WBA", "BAX", "ZBH",
    "SYK", "ILMN", "HLS", "ABT", "MDT", "UNH", "CVS", "AMGN",

    # Diagnostics & Research Tools
    "QGEN", "ILMN", "IDXX", "TMO", "LH", "CRL", "DGX", "XRAY", "HOLX", "MCK",

    # Healthcare IT and Services
    "CI", "HUM", "DGX", "UHS", "AMED", "MCK", "CAH", "WST", "LHCG", "CNC",

    # Smaller Biotech / Pharma
    "BHVN", "VTRS", "ARWR", "XLRN", "PTCT", "RDUS", "EBS", "NKTR", "XOMA", "EXEL"

    ##CONSUMER
    # Consumer Defensive & Cyclical
    "PG", "KO", "PEP", "WMT", "COST", "TGT", "MCD", "SBUX", "NKE", "HD",
    "LOW", "EL", "KMB", "CL", "GIS", "CPB", "KR", "DG", "DLTR", "TSCO",
    "HSY", "MDLZ", "WBA", "TAP", "PM", "MO", "STZ", "KHC", "CHD", "HRL",
    
    # Additional Food & Beverage
    "MNST", "BF.B", "CAG", "MDLZ", "KDP", "KHC", "HRL", "CALM", "COTY", "SJM",
    "KR", "CPB", "MKC", "NWL", "ADM", "TSN", "BF.B", "CPB", "SJM",

    # Retail & Consumer Services
    "TJX", "ROST", "DLTR", "DG", "M", "GPS", "LB", "JWN", "ULTA", "TSCO",
    "LULU", "RH", "KSS", "BBY", "AZO", "ORLY", "GME", "FIVE", "AUTO", "AAP",

    # Restaurants & Leisure
    "YUM", "MCD", "SBUX", "DIN", "CMG", "RRGB", "BJRI", "DRI", "EAT", "PLAY",
    "PZZA", "WEN", "CAKE", "SONC", "DNKN", "SBUX", "YUMC", "PZZA", "MCD",

    # Apparel & Footwear
    "NKE", "ADDYY", "UA", "UAA", "VFC", "DECK", "RL", "PVH", "TIF", "CROX",
    "LEVI", "BURL", "LULU", "PVH", "TPR", "FIVE", "RL", "VFC", "CFR",

    # Consumer Electronics & Leisure Products
    "SONY", "AAPL", "BBY", "RBLX", "TTWO", "EA", "ATVI", "NKE", "SBUX", "COST",

    # Household Products
    "CLX", "PG", "KMB", "CHD", "EL", "CL", "KHC", "KR", "HSY", "MDLZ",

    # Tobacco & Alcohol
    "PM", "MO", "STZ", "TAP", "BTI", "DEO", "CCE", "MNST",

    # Miscellaneous Consumer
    "WHR", "LEG", "HAS", "MAT", "BBBY", "HNI", "POOL", "DHI", "LEN", "PHM",

    # E-commerce & Consumer Internet
    "AMZN", "EBAY", "SHOP", "ETSY", "PINS", "ROKU", "NFLX", "DIS", "CMCSA", "TTWO",

    # Specialty Retailers
    "ULTA", "FIVE", "TJX", "ROST", "DLTR", "DG", "KSS", "BBY", "LB", "AZO"

    ##ENERGY
    # Oil & Gas Majors
    "XOM", "CVX", "COP", "PSX", "VLO", "MPC", "EOG", "SLB", "HAL", "OXY",
    "BKR", "FANG", "APA", "DVN", "PXD", "KMI", "WMB", "ENB", "ET", "OKE",
    "HES", "MUR", "AR", "RRC", "NOG", "SM", "TELL", "CHX", "NOV", "CTRA",

    # Midstream & Pipelines
    "KMI", "WMB", "ET", "OKE", "ENB", "MMP", "EPD", "TRGP", "NS", "PAA",
    "PAGP", "CEQP", "MPLX", "WES", "TCI", "GLP", "MMP", "WMB", "EPD",

    # Oilfield Services & Equipment
    "SLB", "HAL", "BKR", "NOV", "FTI", "HP", "NBR", "PTEN", "OII", "DO",
    "CRR", "HAL", "SLCA", "LPI", "WPRT", "PDCE",

    # Renewable Energy & Utilities
    "NEE", "DUK", "SO", "AEP", "EXC", "PEG", "D", "SRE", "ES", "ED",
    "XEL", "EIX", "PCG", "NRG", "FE", "PPL", "AES", "NRG", "DTE", "ETR",

    # Coal & Alternative Fuels
    "BTU", "ARCH", "ANR", "CNX", "BTU", "CEIX", "PEIX", "BTU", "NEM",

    # Exploration & Production (Smaller Caps)
    "CHK", "MRO", "FANG", "DVN", "CLR", "MTDR", "BRY", "CXO", "EQT",
    "SWN", "GPOR", "PDCE", "CDEV", "RRC", "REXR", "PE", "GDP",

    # Specialty Energy & Equipment
    "TSLA", "FSLR", "ENPH", "RUN", "SEDG", "FSLY", "BE", "NEP", "PEGI", "HES",

    # LNG & Other Energy
    "LNG", "GLOP", "EOG", "OXY", "PBF", "VLO", "MPC", "PSX", "XOM",

    # Energy Infrastructure & Services
    "EQT", "MMP", "WMB", "ET", "OKE", "ENB", "TRGP", "EPD",

    # Others
    "CVX", "COP", "PSX", "MPC", "XOM", "SLB", "HAL", "NOV", "FANG", "APA",

    ##INDUSTRIAL
    # Aerospace & Defense
    "BA", "LMT", "NOC", "RTX", "GD", "TXT", "COL", "LHX", "BWXT", "TDY",
    "HEI", "AJRD", "CACI", "LDOS", "FLIR", "HII", "SPR", "SAIC", "PNR",

    # Machinery & Equipment
    "CAT", "DE", "EMR", "ETN", "PH", "CMI", "ITW", "DOV", "JCI", "IR",
    "TT", "MAS", "PNR", "XYL", "HUBB", "AOS", "FBHS", "MASI", "ROK", "NDSN",
    "KSU", "IEX", "ITC", "EXPD", "ODFL", "UPS", "FDX", "UNP", "CSX", "NSC",

    # Transportation & Logistics
    "UNP", "CSX", "NSC", "UPS", "FDX", "CHRW", "JBHT", "EXPD", "ODFL", "R",

    # Industrial Conglomerates
    "GE", "MMM", "EMR", "ROK", "PH", "ITW", "DOV", "XYL", "TT", "PNR",

    # Construction & Engineering
    "DHI", "LEN", "PHM", "MAS", "JCI", "MAS", "PCAR", "FLT", "MTL", "URI",
    "IEX", "ITW", "DOV", "PH", "ROK", "IR",

    # Building Products & Supplies
    "FBHS", "MAS", "AOS", "HUBB", "NDSN", "ROK", "MAS", "PNR", "XYL",

    # Waste Management & Environmental Services
    "WM", "RSG", "GFL", "CWT", "RSG",

    # Electrical Equipment & Components
    "ETN", "PH", "EMR", "HUBB", "PNR", "AOS",

    # Miscellaneous Industrials
    "ALK", "UAL", "DAL", "LUV", "JBLU", "EXPD", "CHRW", "JBHT", "ODFL",

    # Industrial Technology & Automation
    "ROK", "PH", "ITW", "EMR", "DOV", "AOS", "MAS", "FBHS", "HUBB",

    # Other Transportation & Infrastructure
    "CSX", "NSC", "UNP", "FDX", "UPS", "CHRW", "EXPD", "ODFL", "R", "JBHT",

    ##UTILITIES
    # Major Electric & Gas Utilities
    "NEE", "DUK", "SO", "D", "AEP", "EXC", "SRE", "XEL", "ED", "PEG",
    "EIX", "PPL", "WEC", "AES", "CMS", "DTE", "AWK", "LNT", "NI", "CNP",
    "AEE", "ATO", "UGI", "IDA", "PNW", "ES", "NRG", "EVRG", "OGE", "SWX",

    # Regional & Mid-Size Utilities
    "PNM", "AVA", "FE", "NWE", "WEC", "AVA", "LNT", "AEP", "ETR", "SJI",
    "WTRG", "PNW", "CWT", "SCG", "SR", "ALE", "EIX", "LNT", "PPL", "AVY",

    # Renewable & Clean Energy Utilities
    "NEE", "PEGI", "SEDG", "RUN", "ENPH", "FSLR", "BE", "CSIQ", "VWS", "PLUG",
    "BLNK", "FSLY", "SPWR", "DQ", "DNN", "NEX", "NEE", "ENPH",

    # Water Utilities & Infrastructure
    "AWK", "WTRG", "GWR", "XLU", "SJW", "AWK", "WTRG", "GWR", "SJW",

    # Utility Holding Companies & Diversified Utilities
    "EXC", "D", "ED", "PPL", "WEC", "CMS", "DTE", "ETR", "ES", "PEG",

    # Natural Gas Utilities & Midstream
    "UGI", "CNP", "PNW", "WGL", "NI", "AEE", "ATO", "FE", "WES", "MMP",

    # Smaller Utilities & Specialists
    "ATO", "SCG", "SJI", "PNM", "AVA", "NWE", "LNT", "AEP", "ETR",

    # Utility ETFs (for broad sector coverage)
    "XLU", "VPU", "IDU", "UTL",

    # Other Utilities & Infrastructure
    "OGE", "SWX", "EVRG", "NRG", "ES", "CNP", "PNW", "UGI", "IDA"

    ##REAL ESTATE
    # Major REITs
    "PLD", "AMT", "CCI", "EQIX", "SPG", "PSA", "DLR", "O", "VTR", "WELL",
    "AVB", "EQR", "EXR", "MAA", "ARE", "ESS", "UDR", "FRT", "BXP", "SLG",
    "INVH", "IRM", "PEAK", "SUI", "ELS", "CUBE", "STAG", "KIM", "REG", "NTST",

    # Residential REITs
    "EQR", "AVB", "MAA", "UDR", "ESS", "ARE", "BXP", "SLG", "REG", "KIM",
    "STAG", "INVH", "SUI", "ELS", "CUBE", "IRM", "EXR", "WELL",

    # Industrial REITs
    "PLD", "PSA", "DLR", "ARE", "STAG", "DRE", "FR", "ESRT", "KRG", "LXP",
    "TRNO", "PINE", "CTRE", "OPI", "LTC", "PLD", "ESRT", "AMT", "CCI",

    # Commercial REITs
    "SPG", "BXP", "SLG", "KIM", "O", "REG", "WELL", "PEAK", "VTR", "EXR",
    "ARE", "DRE", "ROIC", "FRT", "DLR", "CUBE", "STAG",

    # Mixed-Use & Specialty REITs
    "TCO", "WPG", "MAC", "SRC", "RPT", "LPT", "RPAI", "NNN", "SIR", "SKT",
    "IR", "ESRT", "HPP", "KRG", "LXP", "PINE", "CPT", "WRI", "IR", "SRC",

    # Property Management & Development Companies
    "SPG", "PLD", "INVH", "UDR", "MAA", "EQR", "ESS", "ARE", "BXP", "TCO",
    "MAC", "DRE", "FRT", "REG", "O", "KIM", "SLG", "VTR",

    # Healthcare REITs
    "VTR", "WELL", "PEAK", "IRM", "HCP", "MPW", "DOC", "OHI", "NHI", "HTA",
    "BAYL", "BMX", "CARE", "SNH", "IRM", "OHI",

    # Other Real Estate & Investment Funds
    "BX", "STT", "AIV", "AHT", "FRT", "REG", "O", "MFA", "HASI", "NLY", "LADR",

    # Other Niche REITs & Real Estate Funds
    "DFT", "COR", "TRNO", "BAM", "INN", "RGLD", "RWR", "REZ", "SRG", "PCTY"

    ##CONSUMER DISCRETIONARY
    # Retail & Discount Stores
    "ROST", "TJX", "BBY", "ULTA", "LB", "KSS", "PVH", "NKE", "LULU", "YUM",
    "DPZ", "CMG", "MAR", "HLT", "RCL", "CCL", "HOG", "WHR", "BBWI", "ETSY",
    "EBAY", "TSCO", "DKS", "WSM", "W", "AZO", "ORLY", "GPC", "POOL", "RH",

    # Auto Parts & Retail
    "AZO", "ORLY", "GPC", "KMX", "TSLA", "VROOM", "GPI", "CVNA", "SAH", "ABG",
    "KMX", "AMZN", "CARG", "EXEL", "CARS",

    # Apparel & Accessories
    "NKE", "LULU", "PVH", "ROST", "TJX", "LB", "KSS", "GPS", "RL", "VFC",
    "DECK", "HBI", "UAA", "UA", "TIF", "LEVI", "CROX", "CHWY", "SKECHERS", "RCKY",

    # Home Goods & Furnishings
    "WHR", "RH", "WSM", "LZB", "MHK", "NWL", "SHW", "CART", "TOL", "DHI",
    "LEN", "PHM", "MAS", "KIRK", "HD", "LOW", "TGT", "WMT",

    # Consumer Services & Leisure
    "MAR", "HLT", "RCL", "CCL", "YUM", "DPZ", "CMG", "CAKE", "SONC", "WEN",
    "PLAY", "EAT", "MCD", "SBUX", "PZZA", "DQ", "WGO", "HGV", "TRIP",

    # Automotive & Leisure
    "HOG", "RIDE", "TSLA", "PAG", "VTX", "BWA", "LEA", "LCII", "ACIW", "TAT",
    
    # Online & E-commerce Retailers
    "AMZN", "EBAY", "ETSY", "PINS", "SHOP", "ROKU", "W", "BBY", "PCTY", "VIPS",

    # Travel & Leisure
    "MAR", "HLT", "RCL", "CCL", "AAL", "UAL", "DAL", "LUV", "JBLU", "ALK",

    # Miscellaneous Consumer Discretionary
    "TAP", "STZ", "MO", "PM", "SBUX", "TSCO", "WMT", "KO", "PEP", "PG"

    ##SEMI-CONDUCTORS
    # Major Chipmakers & Foundries
    "NVDA", "AMD", "INTC", "QCOM", "AVGO", "TXN", "MU", "ADI", "LSCC", "MPWR",
    "ASML", "TSM", "AMAT", "KLAC", "LRCX", "ON", "NXPI", "MRVL", "GFS", "WOLF",

    # Semiconductor Equipment Manufacturers
    "AMAT", "KLAC", "LRCX", "ASML", "TER", "UFS", "NPTN", "MCHP", "TSEM",

    # Memory & Storage Chipmakers
    "MU", "WDC", "STX", "IMDT", "HPE", "STX", "SKHYN", "MC", "LAMR", "ONTX",

    # Analog Semiconductor Companies
    "TXN", "ADI", "MXIM", "SWKS", "NCR", "VSH", "LRCX", "MPWR", "LSCC",

    # Foundry & Contract Manufacturers
    "TSM", "GFS", "ASML", "UMC", "SMIC", "XFAB", "ON", "SK Hynix", "Tower Semiconductor",

    # Specialized & Emerging Chipmakers
    "MRVL", "QRVO", "QCOM", "NXP", "MCHP", "AMBA", "INPH", "ON", "LITE", "ZBRA",
    
    # RF & Optical Chip Manufacturers
    "SWKS", "QRVO", "LITE", "MCHP", "MRVL", "NXP", "LRCX",

    # Semiconductor ETFs
    "SOXX", "SMH", "XSD", "PSI", "FSEL", "FTEC", "SPYG", "SPLG", "QQQ", "XLK"

    ##ETFs
    # Broad Market ETFs
    "SPY", "QQQ", "DIA", "IWM", "VTI", "VOO", "VTV", "VUG", "IWV", "SCHB",
    
    # Sector-Specific ETFs
    "XLK", "XLF", "XLE", "XLI", "XLY", "XLC", "XLB", "XBI", "XRT", "XHE",
    "XTL", "XES", "XME", "XAR", "KBE", "KRE", "VDE", "VHT", "VPU", "VAW",
    
    # Thematic & Innovative ETFs
    "ARKK", "ARKW", "ARKG", "ARKF", "ARKQ", "ARKX", "IBB", "IBD", "IGV", "SKYY",
    
    # Bond & Fixed Income ETFs
    "BND", "AGG", "LQD", "HYG", "JNK", "TIP", "BIL", "SHY", "IEF", "TLT",
    
    # International ETFs
    "EFA", "EEM", "VXUS", "VWO", "EMB", "VEA", "VPL", "SCHF", "VGK", "GXC",
    
    # Real Estate ETFs
    "VNQ", "SCHH", "IYR", "SPG", "RLJ", "RWT", "PSA", "DLR", "O", "FRT",
    
    # Commodity & Natural Resources ETFs
    "GDX", "GLD", "SLV", "USO", "UNG", "DBO", "OIH", "VDE", "XLE", "IGE",
    
    # Dividend-Focused ETFs
    "SCHD", "VYM", "DVY", "HDV", "NOBL", "SPYD", "SDY", "DGRW", "DGRO", "SCHG",
    
    # Cryptocurrency ETFs
    "GBTC", "BITO", "ETHO", "BITO", "BITW", "BLKC", "BLCN", "ETHE", "BTCX",
    
    # Environmental, Social, and Governance (ESG) ETFs
    "SUSA", "ESGU", "XESG", "SUSA", "ESGV", "KLD", "ESGG", "SUSA", "ACSI",
    
    # Other Specialty ETFs
    "SPLG", "SPYG", "SPYV", "VUG", "VOOG", "SMDV", "SPXU", "SPXS", "SH", "BIB",
    "SPXL", "SSO", "UPRO", "FNGU", "MGK", "SPDW", "SPYG", "VYM", "VTI",
]

print(len(tickers2))