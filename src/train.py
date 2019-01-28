import handler
import argparse
from datetime import datetime
import pickle
import json

parser = argparse.ArgumentParser()
parser.add_argument('--testDir','-td',help='path to test directory')
args = parser.parse_args()

exptDate = datetime.now().strftime("%Y%m%d%H%M%S")

configPath = args.testDir+'/config.yaml'
handler = handler.ExptHandler(configPath)
handler.train()

# dump
modelPath = args.testDir+'/%s.model'%exptDate
pickle.dump(handler.model, open(modelPath,'wb'))
logPath = args.testDir+'/%s.log'%exptDate
json.dump(handler.trainLog, open(logPath,'w'))
