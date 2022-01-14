from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = 'MuonEG_B'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_script_2018_dataB.sh'
# hadd nano will not be needed once nano tools are in cmssw
config.JobType.inputFiles = ['crab_script_2018.py', '../scripts/haddnano.py','keep_and_drop.txt','Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt']
config.JobType.sendPythonFolder = True

config.section_("Data")
config.Data.inputDataset = '/MuonEG/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 80
config.Data.lumiMask = 'Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = 'MuonEG_B'

config.section_("Site")
#config.Site.storageSite = "T2_CH_CERN"
config.Site.storageSite = "T3_CH_CERNBOX"
