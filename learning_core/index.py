import json as json;
import pandas as pd
from sklearn.model_selection import train_test_split;
from learning_core import PreProcessing as PP;
from learning_core.algorithms.supervised_learning.classifier import index as SupervisedLearningClassifier;
from learning_core.algorithms.supervised_learning.regression import index as SupervisedLearningRegression;
from learning_core.data.Model import BreastCancer ;
from learning_core.data.Model import Housing ;
from learning_core.data.Model import MedicalCost ;


PPD = PP.PreProcessingData();
SupervisedLearningClassifier = SupervisedLearningClassifier.SupervisedLearningClassifier();
SupervisedLearningRegression = SupervisedLearningRegression.SupervisedLearningRegression();

BreastCancerConfig = BreastCancer.BreastCancerConfig();
HousingConfig = Housing.HousingConfig();
MedicalCostConfig = MedicalCost.MedicalCostConfig();

class LerningCore():
    x_training = [];
    x_test = [];
    y_training = [];
    y_test = [];
    
    data_frame_official = [];
    
    result_algorithm = { 'data' : [] };
    
    def predictResult(self, config, data):
        model = self.getModel(config['modelName'])
        self.preProcessingData(config['modelName'], config['typeData']);
        
        methodLearning = self.getMethodLearning(config['method']);
        methodLearning.init({
            "x_training" : self.x_training,
            "x_test" : self.x_test,
            "y_training" : self.y_training,
            "y_test" : self.y_test,
            "predictors" : self.getPredictors(config['typeData']),
            "target" : PPD.target,
        });        
        
        return model.resultDataFrameIntoJson(methodLearning.predictResult(config['algorithm'],pd.read_json(json.dumps(data))))
    
    def preProcessingData(self, modelName, typeData):
        params = self.recoveFileInformation(modelName);
        self.data_frame_official = PPD.getForecastersAndTarget(params['arquive'], params['sep'], params['initital_predictors_column_number'], params['num_final_columns_forecasters'], params['num_column_target'], params['categorical_vars'], params['dummy_vars']);
        
        self.defineTrainningAndTestBase(typeData);
    
    def validateAlgorithms(self,modelName, typeData, method):
        self.preProcessingData(modelName, typeData)
        
        methodLearning = self.getMethodLearning(method);
        print('[LEARNING] - ', methodLearning);
        methodLearning.init({
            "x_training" : self.x_training,
            "x_test" : self.x_test,
            "y_training" : self.y_training,
            "y_test" : self.y_test,
            "predictors" : self.getPredictors(typeData),
            "target" : PPD.target,
        });
        self.result_algorithm['algorithms'] = methodLearning.validateAlgorithms(); 
        self.result_algorithm['data'] = self.recoveData(modelName, self.data_frame_official);

        return self.result_algorithm;   
    
    def recoveData(self, modelName, dataFrame):
        model = self.getModel(modelName);
        
        return model.serializeDataFrameIntoJson(dataFrame);
    
    def recoveFileInformation(self, modelName):
        model = self.getModel(modelName);
            
        if(model):
            return {
                'arquive': '/data/'+ model.arquive,
                'sep': model.separator,
                'initital_predictors_column_number': model.initital_predictors_column_number,
                'num_final_columns_forecasters': model.num_final_columns_forecasters,
                'num_column_target': model.num_column_target, 
                'categorical_vars': model.categorical_vars,
                'dummy_vars': model.dummy_vars,
            }
        else:
            return {};
    
    def defineTrainningAndTestBase(self, base):
        self.x_training, self.x_test, self.y_training, self.y_test = train_test_split(self.getPredictors(base), self.getTarget(), test_size = 0.3, random_state = 0)
    
    def getPredictors(self, base):
        return PPD.forecasters if base == 'normal' else PPD.forecasters_esc;
    
    def getPredictosEsc(self):
        return PPD.forecasters_esc;
    
    def getTarget(self):
        return PPD.target;
    
    def getMethodLearning(self, method):
        methodLearning = {};
        
        if(method == "supervised_classifier"):
            methodLearning = SupervisedLearningClassifier
        elif(method == "supervised_regression"):
            methodLearning = SupervisedLearningRegression
        
        return methodLearning
    
    def getModel(self, modelName):
        model = {};
        if(modelName == 'BreastCancer'):
            model = BreastCancerConfig
        elif(modelName == 'Housing'):
            model = HousingConfig
        elif(modelName == 'MedicalCost'):
            model = MedicalCostConfig
        
        return model;