#!/bin/env python3

import os
import sys
import re

import os
#
print("Read the files from 2017 configurations and convert them to search for 2018 datasets")
#
for filename in os.listdir(os.getcwd()):
#   with open(os.path.join(os.getcwd(), filename), 'r') as f:
   if "cfg" in filename:
       sample = os.popen(f'grep config.Data.inputDataset ../2017/{filename}').read().split("=")
       if len(sample) > 1:
          print(filename)
          sample = sample[1].replace(" ","").replace("'","")
          head, sep, tail = sample.partition('UL')
          head = head+sep
          head = head.replace("2017","2018")
          if "2018F" in head:
              continue
          if "SIM" in sample:
              head = head.replace("UL","UL18*/NANOAODSIM\"")
          else:
              head = head.replace("DoubleEG","EGamma")
              head = head.replace("UL","UL2018*/NANOAOD\"").replace("2018E","2018A")
          dasstr = f'dasgoclient -query=\"dataset={head} | grep NanoAODv9 | grep -v JMENano'
#          print(head)
#          print(sample)
          print(dasstr)
          print(os.popen(dasstr).read())
          print("-------------------------------------------------------------------------------------")
