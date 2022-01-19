#!/bin/env python3

import os
import sys
import re

print("WARNING! don't forget to do voms-proxy-init before running the script.")
for filename in os.listdir("../2017"):
   print("-------------------------------------------------------------------------------------")
   if "cfg" in filename:
       sample = os.popen(f'grep config.Data.inputDataset ../2017/{filename}').read().split("=")
       data_flag = int(os.popen(f'grep -c data ../2017/{filename}').read()) 
       print("data flag = "+str(data_flag))
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
          print("filename2018 "+filename2018)
          for x in range(len(sampleline)):
              new_line = sample[0]+"= '"+sampleline[x]+"'\n" 
              print("new_line   "+new_line)
              if x > 0:
                  filename2018 = filename.split("_cfg.py")[0] + "_ext" + str(x) + "_cfg.py" 
                  print("2018 file name:  "+filename2018)
              with open(f"../2017/{filename}", 'r') as f:
                  with open(os.path.join(os.getcwd(), filename2018), 'w') as fo: 
                      for line in f:
                          line = line.replace("crab_script_data","crab_script_data_2018")
                          if data_flag == 0 and "config.JobType.inputFiles" not in line:
                              line = line.replace("crab_script","crab_script_2018")
                          line = line.replace("DoubleEG","EGamma")
                          line = line.replace("Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt","Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt")
                          line = line.replace("T3_CH_CERNBOX","T2_CH_CERN")
                          if "config.Data.inputDataset" not in line.strip("\n"):
                              fo.write(line)
                          else:
                              fo.write(new_line)
                      fo.write('config.Data.outLFNDirBase = "/store/group/phys_top/ExtraYukawa/test/"') 
                  fo.close()
              f.close()
os.rename(r'DoubleEGB_cfg.py',r'EgammaB_cfg.py')
os.rename(r'DoubleEGC_cfg.py',r'EgammaC_cfg.py')
os.rename(r'DoubleEGD_cfg.py',r'EgammaD_cfg.py')
os.rename(r'DoubleEGE_cfg.py',r'EgammaA_cfg.py')
os.rename(r'DoubleMuonE_cfg.py',r'DoubleMuonA_cfg.py')
os.rename(r'MuonEGE_cfg.py',r'MuonEGA_cfg.py')
os.rename(r'SingleMuonE_cfg.py',r'SingleMuonA_cfg.py')
os.rename(r'METE_cfg.py',r'META_cfg.py')
#os.popen('rm SingleEG*_cfg.py').read()
