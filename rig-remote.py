#!/usr/bin/env python

"""
Remote application that interacts with rigs using rigctl protocol.

Please refer to:
http://gqrx.dk/
http://gqrx.dk/doc/remote-control
http://sourceforge.net/apps/mediawiki/hamlib/index.php?title=Documentation

Author: Rafael Marmelo <rafael@defying.me>
Author: Simone Marzona <rafael@defying.me>

License: MIT License

Copyright (c) 2014 Rafael Marmelo
Copyright (c) 2015 Simone Marzona
Copyright (c) 2016 Tim Sweeney
"""

# import modules
import argparse
import logging
import os
import time
import textwrap
import tkinter as tk
from rig_remote.ui import RigRemote
from rig_remote.app_config import AppConfig
from rig_remote.constants import DEFAULT_BOOKMARK_FILENAME
from rig_remote.constants import DEFAULT_CONFIG_FILENAME
from rig_remote.constants import DEFAULT_LOG_FILENAME
from rig_remote.constants import DEFAULT_PREFIX
from rig_remote.utility import process_path

# helper functions
def input_arguments():
    """Argument parser.

    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(textwrap.fill(
            "Rig controller that interacts with a rig using the rigctl protocol.\
             ")),
        epilog="""Please refer to:
        https://github.com/Marzona/rig-remote/wiki
        http://gqrx.dk/,
        http://gqrx.dk/doc/remote-control,
        http://sourceforge.net/apps/mediawiki/hamlib/index.php?title=Documentation

        Author: Simone Marzona <marzona@knoway.info>
        Additional features: Tim Sweeney <mainetim@"GEE"mail.com>

        License: MIT License

        Copyright (c) 2015 Simone Marzona
        Copyright (c) 2016 Tim Sweeney""")

    parser.add_argument("--bookmarks",
                        "-b",
                        type=str,
                        required=False,
                        dest="alternate_bookmark_file",
                        help="Sets the full path for the bookmark file.")

    parser.add_argument("--config",
                        "-c",
                        type=str,
                        required=False,
                        dest="alternate_config_file",
                        help="Sets the full path for the config file.")

    parser.add_argument("--log",
                        "-l",
                        type=str,
                        required=False,
                        dest="alternate_log_file",
                        help="Sets the full path for the activity log file.")

    parser.add_argument("--prefix",
                        "-p",
                        type=str,
                        required=False,
                        dest="alternate_prefix",
                        help="Sets the directory prefix for default working files. " +
                        "NOTE: Individual path options override this prefix.")

    parser.add_argument("--verbose",
                        "-v",
                        dest="verbose",
                        action="store_true",
                        help="Increase log verbosity.")

    return parser.parse_args()

def log_configuration(verbose):
    """Logger configuration: time/date formatting.

    """

    os.environ["TZ"] = "UTC"

    # Windows doesn't support tzset. Ignore for now.
    try:
        time.tzset()
    except AttributeError:
        pass

    if verbose:
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p %Z")
    else:
        logging.basicConfig(level=logging.WARNING,
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p %Z")

    return logging.getLogger(__name__)

# entry point
if __name__ == "__main__":
    args = input_arguments()
    logger = log_configuration(args.verbose)

    if args.alternate_prefix:
        prefix = args.alternate_prefix
        dir_prefix = os.path.expanduser(prefix)
    else:
        dir_prefix = DEFAULT_PREFIX
    if args.alternate_config_file:
        conf = args.alternate_config_file
        config_file = process_path(conf)
    else:
        config_file = os.path.join(dir_prefix, DEFAULT_CONFIG_FILENAME)

    root = tk.Tk()
    ac = AppConfig(config_file)
    # set bookmarks and log filename in this order:
    #   use command line alternate path
    #   use path from config file
    #   use default path
    ac.read_conf()
    ac.write_conf()

    if args.alternate_bookmark_file != None:
        bookmarks = args.alternate_bookmark_file
        ac.config['bookmark_filename'] = process_path(bookmarks)
    else:
        try:
            if str(ac.config["bookmark_filename"]) == None:
                ac.config["bookmark_filename"] = os.path.join(dir_prefix, DEFAULT_BOOKMARK_FILENAME)
        except (ValueError,KeyError):
                ac.config["bookmark_filename"] = os.path.join(dir_prefix, DEFAULT_BOOKMARK_FILENAME)

    # set activity log filename
    if args.alternate_log_file != None:
        log = args.alternate_log_file
        ac.config['log_filename'] = process_path(log)
    else:
        ac.config['log_filename'] = os.path.join(dir_prefix, DEFAULT_LOG_FILENAME)
    app = RigRemote(root, ac)

    app.apply_config(ac)
    app.mainloop()
    if app.scan_thread != None :
        app.scanning.terminate()
