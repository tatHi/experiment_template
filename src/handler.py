import yaml
import model
import dataset

class ExptHandler:
    def __init__(self, configPath):
        self.config = yaml.load(open(configPath, 'r+'))
        self.dataset = dataset.Dataset(self.config['datasetPath'])
        self.model = model.Model(self.config)

    def train(self):
        self.trainLog = []
        
        for epoch in range(self.config['maxEpoch']):
            print('-'*30)
            print('epoch %d/%d'%(epoch+1, self.config['maxEpoch']))
            
            # training
            self.model = trainProc(self.model, self.dataset.data['train'])
            
            # evaluating
            trainScore = evalProc(self.model, self.dataset.data['train'])
            validScore = evalProc(self.model, self.dataset.data['valid'])
            testScore = evalProc(self.model, self.dataset.data['test'])
            
            # write log
            epochLog = {'epoch':epoch, 'trainScore':trainScore, 
                        'validScore':validScore, 'testScore':testScore}
            self.trainLog.append(epochLog)

def trainProc(model, data):
    # something about model training
    for line in data:
        text = line['text']
        label = line['label']
        model.predict(text)
    model.update()
    print('training done')
    return model

def evalProc(model, data):
    correctNum = 0
    size = len(data)
    for line in data:
        text = line['text']
        label = line['label']
        pred = model.predict(line)
        if pred==label:
            correctNum += 1
    accRate = correctNum/size
    print('evaluate:')
    print('\tcorrect:%d'%correctNum)
    print('\tdataSize:%d'%size)
    print('\taccRate:%f'%(accRate))
