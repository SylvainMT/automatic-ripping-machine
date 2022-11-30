#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Automatic-Ripping-Machine Development Tools
    log to cli and file manager
"""

import os
from colorama import Fore, Style


# Print message to the console/cli with colour
#  INPUT: message string, error boolean (1 - error, 0 - good)
#  OUTPUT: print to console
def console(msg, error=None):
    if error is None:
        print(msg)
    elif error == 1:
        print(f"{msg}\t[{Fore.RED}Error{Style.RESET_ALL}]")
    else:
        print(f"{msg}\t[{Fore.GREEN}Ok{Style.RESET_ALL}]")


# Print debug message to console
#  INPUT: message
#  OUTPUT: print to console
def debug(msg):
    console(f"DEBUG: {msg}")


# Print info message to console
#  INPUT: message
#  OUTPUT: print to console
def info(msg):
    console(f"INFO: {msg}")


# Print error message
#  INPUT: message
#  OUTPUT: print to console with error
def error(msg):
    console(msg, 1)
