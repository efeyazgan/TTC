from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = 'SingleEG_C'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_script_dataC.sh'
# hadd nano will not be needed once nano tools are in cmssw
config.JobType.inputFiles = ['crab_script.py', '../scripts/haddnano.py','keep_and_drop.txt','Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt']
config.JobType.sendPythonFolder = True

config.section_("Data")
config.Data.inputDataset = ''
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 80
config.Data.lumiMask = 'Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = 'SingleEG_C'

config.section_("Site")
#config.Site.storageSite = "T2_CH_CERN"
config.Site.storageSite = "T3_CH_CERNBOX"
