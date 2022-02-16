#!/bin/env python3

import os
import sys
import re

filesfolders = os.listdir(".")
folders = []
for filen in filesfolders:
    if os.path.isdir(os.path.join(os.path.abspath("."), filen)):
        if filen.startswith("crab_"):
            print(os.popen("crab status -d "+filen).read())
