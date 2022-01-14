#!/bin/env python3

import os
import sys
import re

for filename in os.listdir("../2017"):
   print("-------------------------------------------------------------------------------------")
   if "cfg" in filename:
       sample = os.popen(f'grep config.Data.inputDataset ../2017/{filename}').read().split("=")
       if len(sample) > 1:
          era = filename.split("_cfg")[0][-1]
          sample_and_era = filename.split("_cfg")[0].replace(filename.split("_cfg")[0][-1],"_"+filename.split("_cfg")[0][-1])
          print(sample_and_era)
          sample_tmp = sample[1].replace(" ","").replace("'","")
          head, sep, tail = sample_tmp.partition('UL')
          head = head+sep
          head = head.replace("2017","2018")
          if "2018F" in head:
              continue
          if "SIM" in sample_tmp:
              head = head.replace("UL","UL18*/NANOAODSIM\"")
          else:
              head = head.replace("DoubleEG","EGamma")
              head = head.replace("UL","UL2018*/NANOAOD\"").replace("2018E","2018A")
          dasstr = f'dasgoclient -query=\"dataset={head} | grep NanoAODv9 | grep -v JMENano'
          print(dasstr)
          sample[1] = os.popen(dasstr).read().rstrip()
          sampleline = os.popen(dasstr).read().rstrip().splitlines()
          print(sampleline)       
          filename2018 = filename
          for x in range(len(sampleline)):
              new_line = sample[0]+"= '"+sampleline[x]+"'\n" 
              if x > 0:
                  filename2018 = filename.split("_cfg.py")[0] + "_ext" + str(x) + "_cfg.py" 
                  print(filename2018)
              with open(f"../2017/{filename}", 'r') as f:
                  with open(os.path.join(os.getcwd(), filename2018), 'w') as fo: 
                      for line in f:
                          line = line.replace("DoubleEG","EGamma")
                          line = line.replace("Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt","Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt")
                          if "config.Data.inputDataset" not in line.strip("\n"):
                              fo.write(line)
                          else:
                              fo.write(new_line)
                  fo.close()
              f.close()
