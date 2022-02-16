#!/bin/env python3

import os
import sys
import re

path = "configs_v9/2018"
files = os.listdir(path)
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        if ".pyc" not in file and "init" not in file  and "list_input_sample" not in file:
            os.popen("crab submit -c configs_v9/2018/"+file).read()
            fld = os.popen('ls -td -- */ | head -n 1').read().rstrip()
            fld = "rm "+fld+"/inputs/*.tgz"
            os.popen(fld).read().rstrip()
