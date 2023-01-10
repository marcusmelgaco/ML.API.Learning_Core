import json as json;
import pandas as pd
from sklearn.model_selection import train_test_split;
from learning_core import PreProcessing as PP;
from learning_core.algorithms.supervised_learning import NaiveBayes;
from learning_core.algorithms.supervised_learning import SVM;
from learning_core.algorithms.supervised_learning import LogisticRegression;
from learning_core.algorithms.supervised_learning import KNN;
from learning_core.algorithms.supervised_learning import DecisionTree;
from learning_core.algorithms.supervised_learning import RandomForest;
from learning_core.algorithms.supervised_learning import XGBoost;
from learning_core.algorithms.supervised_learning import LGBM;
from learning_core.algorithms.supervised_learning import CatBoost;
from learning_core.algorithms.supervised_learning import index as SupervisedLearning;
from learning_core.data.Model import BreastCancer ;


PPD = PP.PreProcessingData();

SupervisedLearning = SupervisedLearning.SupervisedLearning();
NBAlgorithm = NaiveBayes.NaiveBayesAlgorithm();
SVM = SVM.SVMAlgorithm();
LogisticRegression = LogisticRegression.LogisticRegressionAlgorithm();
KNN = KNN.KNNAlgorithm();
DecisionTree = DecisionTree.DecisionTreeAlgorithm();
RandomForest = RandomForest.RandomForestAlgorithm();
XGBoost = XGBoost.XGBoostAlgorithm();
LGBM = LGBM.LGBMAlgorithm();
CatBoost = CatBoost.CatBoostAlgorithm();
BreastCancerConfig = BreastCancer.BreastCancerConfig();


print(BreastCancerConfig.output);
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
        self.data_frame_official = PPD.getForecastersAndTarget(params['arquive'], params['sep'], params['initital_predictors_column_number'], params['num_final_columns_forecasters'], params['num_column_target']);
        
        self.defineTrainningAndTestBase(typeData);
    
    def validateAlgorithms(self,modelName, typeData, method):
        self.preProcessingData(modelName, typeData)
        
        methodLearning = self.getMethodLearning(method);
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
        model = {};
        if(modelName == 'BreastCancer'):
            model = BreastCancerConfig;
        else: return [];
        
        return model.serializeDataFrameIntoJson(dataFrame);
    
    def recoveFileInformation(self, modelName):
        model = {};
        
        if(modelName == 'BreastCancer'):
            model = BreastCancerConfig;
            
        if(model):
            return {
                'arquive': '/data/'+ model.arquive,
                'sep': model.separator,
                'initital_predictors_column_number': model.initital_predictors_column_number,
                'num_final_columns_forecasters': model.num_final_columns_forecasters,
                'num_column_target': model.num_column_target,   
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
        return SupervisedLearning if method == 'supervised' else {}
    
    def getModel(self, modelName):
        model = {};
        if(modelName == 'BreastCancer'):
            model = BreastCancerConfig;
        
        return model;