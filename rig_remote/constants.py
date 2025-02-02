#!/usr/bin/env python
"""
Remote application that interacts with rigs using rigctl protocol.

Please refer to:
http://rig.dk/
http://rig.dk/doc/remote-control
http://sourceforge.net/apps/mediawiki/hamlib/index.php?title=Documentation

Author: Rafael Marmelo
Author: Simone Marzona

License: MIT License

Copyright (c) 2014 Rafael Marmelo
Copyright (c) 2015 Simone Marzona
Copyright (c) 2016 Tim Sweeney
"""

# module import
import os


# constant definition
RIG_TIMEOUT = 10
RESET_CMD_DICT = {"NONE": 0,
                  "SOFTWARE_RESET": 1,
                  "VFO_RESET": 2,
                  "MEMORY_CLEAR_RESET": 4,
                  "MASTER_RESET": 8
                  }

ALLOWED_RIGCTL_MODES = (
                        "USB",
                        "LSB",
                        "CW",
                        "CWR",
                        "RTTY",
                        "RTTYR",
                        "AM",
                        "FM",
                        "WFM",
                        "AMS",
                        "PKTLSB",
                        "PKTU",
                        "SB",
                        "PKTFM",
                        "ECSSUSB",
                        "ECSSLSB",
                        "WFM_ST",
                        "FAX",
                        "SAM",
                        "SAL",
                        "SAH",
                        "DSB",
                        )

ALLOWED_PARM_COMMANDS = ["ANN",
                         "APO",
                         "BACKLIGHT",
                         "BEEP",
                         "TIME",
                         "BAT",
                         "KEYLIGHT",
                         ]

ALLOWED_FUNC_COMMANDS = ["FAGC",
                         "NB",
                         "COMP",
                         "VOX",
                         "TONE",
                         "TSQL",
                         "SBKIN",
                         "FBKIN",
                         "ANF",
                         "NR",
                         "AIP",
                         "APF",
                         "MON",
                         "MN",
                         "RF",
                         "ARO",
                         "LOCK",
                         "MUTE",
                         "VSC",
                         "REV",
                         "SQL",
                         "ABM",
                         "BC",
                         "MBC",
                         "AFC",
                         "SATMODE",
                         "SCOPE",
                         "RESUME",
                         "TBURST",
                         "TUNER",
                         ]

ALLOWED_VFO_COMMANDS = ["VFOA",
                        "VFOB"
                        "VFOC",
                        "currVFO",
                        "VFO",
                        "MEM",
                        "Main",
                        "Sub",
                        "TX",
                        "RX",
                        ]

ALLOWED_SPLIT_MODES = ["AM",
                       "FM",
                       "CW",
                       "CWR",
                       "USB",
                       "LSB",
                       "RTTY",
                       "RTTYR",
                       "WFM",
                       "AMS",
                       "PKTLSB",
                       "PKTUSB",
                       "PKTFM",
                       "ECSSUSB",
                       "ECSSLSB",
                       "FAX",
                       "SAM",
                       "SAL",
                       "SAH",
                       "DSB",
                       ]

RIG_TIMEOUT=10
RESET_CMD_DICT={"NONE" : 0,
                "SOFTWARE_RESET": 1,
                "VFO_RESET": 2,
                "MEMORY_CLEAR_RESET": 4,
                "MASTER_RESET": 8}

ALLOWED_RIGCTL_MODES=("USB",
                      "LSB",
                      "CW",
                      "CWR",
                      "RTTY",
                      "RTTYR",
                      "AM",
                      "FM",
                      "WFM",
                      "AMS",
                      "PKTLSB",
                      "PKTU",
                      "SB",
                      "PKTFM",
                      "ECSSUSB",
                      "ECSSLSB",
                      "WFM_ST",
                      "FAX",
                      "SAM",
                      "SAL",
                      "SAH",
                      "DSB")

ALLOWED_PARM_COMMANDS=["ANN",
                       "APO",
                       "BACKLIGHT",
                       "BEEP",
                       "TIME",
                       "BAT",
                       "KEYLIGHT"]

ALLOWED_FUNC_COMMANDS=["FAGC",
                       "NB",
                       "COMP",
                       "VOX",
                       "TONE",
                       "TSQL",
                       "SBKIN",
                       "FBKIN",
                       "ANF",
                       "NR",
                       "AIP",
                       "APF",
                       "MON",
                       "MN",
                       "RF",
                       "ARO",
                       "LOCK",
                       "MUTE",
                       "VSC",
                       "REV",
                       "SQL",
                       "ABM",
                       "BC",
                       "MBC",
                       "AFC",
                       "SATMODE",
                       "SCOPE",
                       "RESUME",
                       "TBURST",
                       "TUNER"]

ALLOWED_VFO_COMMANDS=["VFOA",
                      "VFOB"
                      "VFOC",
                      "currVFO",
                      "VFO",
                      "MEM",
                      "Main",
                      "Sub",
                      "TX",
                      "RX"]

ALLOWED_SPLIT_MODES=["AM",
                     "FM",
                     "CW",
                     "CWR",
                     "USB",
                     "LSB",
                     "RTTY",
                     "RTTYR",
                     "WFM",
                     "AMS",
                     "PKTLSB",
                     "PKTUSB",
                     "PKTFM",
                     "ECSSUSB",
                     "ECSSLSB",
                     "FAX",
                     "SAM",
                     "SAL",
                     "SAH",
                     "DSB"]
ALLOWED_BOOKMARK_TASKS = ["load", "save"]
DIRMODE = 644
CBB_MODES = ('',
             'AM',
             'FM',
             'WFM',
             'WFM_ST',
             'LSB',
             'USB',
             'CW',
             'CWL',
             'CWU',
             )

# scanning constants
# once tuned a freq, check this number of times for a signal
SIGNAL_CHECKS = 2
# time to wait between checks on the same frequency
NO_SIGNAL_DELAY = .1
# once we send the cmd for tuning a freq, wait this time
TIME_WAIT_FOR_TUNE = .25
# minimum interval in hertz
MIN_INTERVAL = 1000
# fictional mode set for active frequencies
UNKNOWN_MODE = "unknown"
# monitoring mode delay
MONITOR_MODE_DELAY = 2

# dictionary for mapping between rig modes and rig-remote modes
# the key is the rig-remote namings and the value is the rig naming

MODE_MAP = {}
MODE_MAP["AM"] = "AM"
MODE_MAP["FM"] = "NarrowFM"
MODE_MAP["WFM_ST"] = "WFM(stereo)"
MODE_MAP["WFM"] = "WFM(mono)"
MODE_MAP["LSB"] = "LSB"
MODE_MAP["USB"] = "USB"
MODE_MAP["CW"] = "CW"
MODE_MAP["CWL"] = "CW-L"
MODE_MAP["CWU"] = "CW-U"

REVERSE_MODE_MAP = {}
REVERSE_MODE_MAP["AM"] = "AM"
REVERSE_MODE_MAP["Narrow FM"] = "FM"
REVERSE_MODE_MAP["WFM (stereo)"] = "WFM_ST"
REVERSE_MODE_MAP["WFM (mono)"] = "WFM"
REVERSE_MODE_MAP["LSB"] = "LSB"
REVERSE_MODE_MAP["USB"] = "USB"
REVERSE_MODE_MAP["CW"] = "CW"
REVERSE_MODE_MAP["CW-L"] = "CWL"
REVERSE_MODE_MAP["CW-U"] = "CWU"

SUPPORTED_SCANNING_ACTIONS = ("start",
                              "stop")
SUPPORTED_SYNC_ACTIONS = SUPPORTED_SCANNING_ACTIONS

SYNC_INTERVAL = 0.2

SUPPORTED_SCANNING_MODES = ("bookmarks",
                            "frequency")
DEFAULT_CONFIG = {"hostname1" : "127.0.0.1",
                  "port1" : "7356",
                  "hostname2" : "127.0.0.1",
                  "port2" : "7357",
                  "interval" : "1",
                  "delay" : "5",
                  "passes" : "0",
                  "sgn_level" : "-30",
                  "range_min" : "24,000",
                  "range_max" : "1800,000",
                  "wait" : "false",
                  "record" : "false",
                  "log" : "false",
                  "always_on_top" : "true",
                  "save_exit" : "false",
                  "aggr_scan" : "false",
                  "auto_bookmark" : "false",
                  "log_filename" : None,
                  "bookmark_filename" : None}

LEN_BM = 4


class BM(object):
    "Helper class with 4 attribs."

    freq, mode, desc, lockout = list(range(LEN_BM))

UI_EVENT_TIMER_DELAY = 1000
QUEUE_MAX_SIZE = 10

DEFAULT_PREFIX = os.path.expanduser("~/.rig-remote")
DEFAULT_CONFIG_FILENAME = 'rig-remote.conf'
DEFAULT_LOG_FILENAME = 'rig-remote-log.txt'
DEFAULT_BOOKMARK_FILENAME = 'rig-remote-bookmarks.csv'
ABOUT = """
Rig remote is a software for controlling a rig
via tcp/ip and RigCtl.

GitHub: https://github.com/Marzona/rig-remote

Project wiki: https://github.com/Marzona/rig-remote/wiki

GoogleGroups: https://groups.google.com/forum/#!forum/rig-remote
"""

GQRX_BOOKMARK_FIRST_LINE = "# Tag name          ;  color\n"
GQRX_FIRST_BOOKMARK = 5

GQRX_BOOKMARK_HEADER = [
                        ["# Tag name          ","  color"],
                        ["Untagged            "," #c0c0c0"],
                        ["Marine VHF          "," #c0c0c0"],
                        [],
                        ["# Frequency "," Name                     ",
                         " Modulation          ",
                         "  Bandwidth"," Tags"],
                        ]
SCANNING_CONFIG = ["range_min",
                   "range_max",
                   "delay",
                   "interval",
                   "auto_bookmark",
                   "sgn_level",
                   "wait",
                   "record",
                   "aggr_scan",
                   "passes",
                   ]
MAIN_CONFIG = ["always_on_top",
               "save_exit",
               "bookmark_filename",
               "log",
               "log_filename"
               ]
MONITOR_CONFIG = ["monitor_mode_loops"]
RIG_URI_CONFIG = ["port1",
                  "hostname1",
                  "port2",
                  "hostname2"
                  ]
CONFIG_SECTIONS = [
                   "Scanning",
                   "Main",
                   "Rig URI",
                   "Monitor",
                  ]
UPGRADE_MESSAGE = ("This config file may deserve an "\
                   "upgrade, please execute the "\
                   "following comand: "\
                   "python ./config_checker.py -uc ~/.rig-remote/ or "\
                   "Check https://github.com/Marzona/rig-remote/wiki/User-Manual#config_checker "\
                   "for more info.")
