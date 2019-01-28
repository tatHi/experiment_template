import json
class Dataset:
    def __init__(self, datasetPath):
        # main data
        self.data = {} # dataset for model
        
        # information of data
        self.vocabSize = None
        self.labelSize = None 

        # build this
        self.__readData(datasetPath)

    def __readData(self, datasetPath):
        print('build dataset:')
        rawData = open(datasetPath,'r+')
        self.data = json.load(rawData)

        # build information of data
        vocab = set()
        labels = set()
        for ty,lines in self.data.items():
            print('\t[%s]'%ty)
            for line in lines:
                text = line['text']
                label = line['label']
                print('\t%s, %s'%(text,label))
                vocab |= set(text.split())
                labels.add(label)
        self.vocabSize = len(vocab)
        self.labels = len(labels)

