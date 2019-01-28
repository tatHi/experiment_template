# ml model
class Model:
    def __init__(self, config):
        self.hyp1 = config['hyp1']
        self.hyp2 = config['hyp2']
        self.hyp3 = config['hyp3']
        print('parameters for model:')
        print('\thyp1:%d'%self.hyp1)
        print('\thyp2:%d'%self.hyp2)
        print('\thyp3:%d'%self.hyp3)
    
    def predict(self, inputData):
        # process of predicting
        predictedLabel = None
        if '0' in inputData:
            predictedLabel = 0
        else:
            predictedLabel = 1
        return predictedLabel

    def update(self):
        print('model updated')
