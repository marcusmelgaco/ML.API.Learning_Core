import json as json;
import pandas as pd
from sklearn.model_selection import train_test_split;
from learning_core import PreProcessing as PP;
from learning_core.algorithms.supervised_learning.classifier import index as SupervisedLearningClassifier;
from learning_core.algorithms.supervised_learning.regression import index as SupervisedLearningRegression;
from learning_core.algorithms.unsupervised_learning.grouping import index as UnsupervisedLearningGrouping;
from learning_core.data.Model import BreastCancer ;
from learning_core.data.Model import Housing ;
from learning_core.data.Model import MedicalCost ;
from learning_core.data.Model import WineClustering;


PPD = PP.PreProcessingData();

SupervisedLearningClassifier = SupervisedLearningClassifier.SupervisedLearningClassifier();
SupervisedLearningRegression = SupervisedLearningRegression.SupervisedLearningRegression();
UnsupervisedLearningGrouping = UnsupervisedLearningGrouping.UnsupervisedLearningGrouping();

BreastCancerConfig = BreastCancer.BreastCancerConfig();
HousingConfig = Housing.HousingConfig();
MedicalCostConfig = MedicalCost.MedicalCostConfig();
WineClusteringConfig = WineClustering.WineClusteringConfig();

class LerningCore():
    x_training = [];
    x_test = [];
    y_training = [];
    y_test = [];
    
    model_data = {};
    type_data = "";
    
    data_frame_official = [];
    
    method_learning = {};
    
    result_algorithm = { 'data' : [] };
    
    def predictResult(self, config, data):
        self.model_data = self.getModel(config['modelName']);
        self.type_data = config['typeData'];
        
        self.preProcessingData(config['modelName']);
        self.getMethodLearning(config['method']);
        self.initMethodLeaning();
        
        return self.model_data.resultDataFrameIntoJson(self.method_learning.predictResult(config['algorithm'],pd.read_json(json.dumps(data))))
    
    def preProcessingData(self, modelName):
        params = self.recoveFileInformation();
        self.data_frame_official = PPD.getForecastersAndTarget(params['arquive'], params['sep'], params['initital_attributes_column_number'], params['num_final_columns_attributes'], params['num_column_target'], params['categorical_vars'], params['dummy_vars']);
        
        self.defineTrainningAndTestBase();
    
    def validateAlgorithms(self, modelName, typeData, method):
        self.model_data = self.getModel(modelName);
        self.type_data = typeData;
        
        self.preProcessingData(modelName)
        self.getMethodLearning(method);
        self.initMethodLeaning();
        
        self.result_algorithm['algorithms'] = self.method_learning.validateAlgorithms(); 
        self.result_algorithm['data'] = self.recoveData(self.data_frame_official);

        return self.result_algorithm;   
    
    def initMethodLeaning(self):
        if(self.model_data.type == "supervised"):
            self.method_learning.init({
                "x_training" : self.x_training,
                "x_test" : self.x_test,
                "y_training" : self.y_training,
                "y_test" : self.y_test,
                "predictors" : self.getPredictors(),
                "target" : PPD.target,
            });
        elif(self.model_data.type == "unsupervised"):
            self.method_learning.init({
                "attributes" : self.getPredictors(),
                "attributes_original": PPD.attributes,
                "model": self.model_data
            });
    
    def recoveData(self, dataFrame):
        return self.model_data.serializeDataFrameIntoJson(dataFrame);
    
    def recoveFileInformation(self): 
        if(self.model_data):
            return {
                'arquive': '/data/'+ self.model_data.arquive,
                'sep': self.model_data.separator,
                'initital_attributes_column_number': self.model_data.initital_attributes_column_number,
                'num_final_columns_attributes': self.model_data.num_final_columns_attributes,
                'num_column_target': self.model_data.num_column_target, 
                'categorical_vars': self.model_data.categorical_vars,
                'dummy_vars': self.model_data.dummy_vars,
            }
        else:
            return {};
    
    def defineTrainningAndTestBase(self):
        self.x_training, self.x_test, self.y_training, self.y_test = train_test_split(self.getPredictors(), self.getTarget(), test_size = 0.3, random_state = 0)
    
    def getPredictors(self):
        return PPD.forecasters if self.type_data == 'normal' else PPD.forecasters_esc;
    
    def getPredictosEsc(self):
        return PPD.forecasters_esc;
    
    def getTarget(self):
        return PPD.target;
    
    def getMethodLearning(self, method):
        if(method == "supervised_classifier"):
            self.method_learning = SupervisedLearningClassifier
        elif(method == "supervised_regression"):
            self.method_learning = SupervisedLearningRegression
        elif(method == "unsupervised_grouping"):
            self.method_learning = UnsupervisedLearningGrouping
    
    def getModel(self, modelName):
        model = {};
        if(modelName == 'BreastCancer'):
            model = BreastCancerConfig
        elif(modelName == 'Housing'):
            model = HousingConfig
        elif(modelName == 'MedicalCost'):
            model = MedicalCostConfig
        elif(modelName == 'WineClustering'):
            model = WineClusteringConfig
        
        return model;