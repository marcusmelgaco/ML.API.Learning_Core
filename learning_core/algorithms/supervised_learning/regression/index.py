from learning_core.algorithms.supervised_learning.regression import LinearRegression;
from learning_core.algorithms.supervised_learning.regression import SVR;
from learning_core.algorithms.supervised_learning.regression import DecisionTree;
from learning_core.algorithms.supervised_learning.regression import RandomForest;
from learning_core.algorithms.supervised_learning.regression import XGBoost;
from learning_core.algorithms.supervised_learning.regression import LGBM;
from learning_core.algorithms.supervised_learning.regression import CatBoost;
from learning_core.algorithms.supervised_learning.regression.ANN import MLPRegressor;


LinearRegression = LinearRegression.LinearRegressionAlgorithm();
SVR = SVR.SVRAlgorithm();
DecisionTree = DecisionTree.DecisionTreeAlgorithm();
RandomForest = RandomForest.RandomForestAlgorithm();
XGBoost = XGBoost.XGBoostAlgorithm();
LGBM = LGBM.LGBMAlgorithm();
CatBoost = CatBoost.CatBoostAlgorithm();
MLPRegressor = MLPRegressor.MLPRegressorAlgorithm();
class SupervisedLearningRegression():
    x_training = [];
    x_test = [];
    y_training = [];
    y_test = [];
    
    predictors = [];
    target = [];
    
    def init(self, data):
        self.x_training = data['x_training'];
        self.x_test = data['x_test'];
        self.y_training = data['y_training'];
        self.y_test = data['y_test'];
        self.predictors = data['predictors'];
        self.target = data['target'];
        
    
    def validateAlgorithms(self):
        algorithm_predict_infos = {};
        
        # Linear Regression
        algorithm_predict_infos['LinearRegression'] = self.LinearRegressionAlgorithm();
        
        # SVR
        algorithm_predict_infos['SVR'] = self.SVRAlgorithm();
        
        # DecisionTree
        algorithm_predict_infos['DecisionTree'] = self.DecisionTreeAlgorithm();
        
        # RandomForest
        algorithm_predict_infos['RandomForest'] = self.RandomForestAlgorithm();
        
        # XGBoost        
        algorithm_predict_infos['XGBoost'] = self.XGBoostAlgorithm();
        
        # LGBM        
        algorithm_predict_infos['LGBM'] = self.LGBMAlgorithm();
        
        # CatBoost        
        algorithm_predict_infos['CatBoost'] = self.CatBoostAlgorithm();
        
        # MLPRegressor        
        algorithm_predict_infos['MLPRegressor'] = self.MLPRegressorAlgorithm();
        

        return algorithm_predict_infos;
    
    def defineModel(self, modelName):
        model = {};

        if(modelName == "LinearRegression"):
            model = LinearRegression;
        elif(modelName == "SVR"):
            model = SVR;
        elif(modelName == "DecisionTree"):
            model = DecisionTree
        elif(modelName == "RandomForest"):
            model = RandomForest
        elif(modelName == "XGBoost"):
            model = XGBoost
        elif(modelName == "LGBM"):
            model = LGBM
        elif(modelName == "CatBoost"):
            model = CatBoost
        elif(modelName == "ANN.MLP"):
            model = MLPRegressor
        
        
        return model;
    
    def predictResult(self, algorithm, data):
        self.learning(algorithm);
        return self.predict(algorithm,data);
    
    def learning(self, algorithm):
        model = self.defineModel(algorithm);
        model.learning(self.x_training, self.y_training)
        
        return True;
    
    def predict(self, algorithm, data):
        model = self.defineModel(algorithm);
        return model.predict(data)
    
    def LinearRegressionAlgorithm(self):
        LinearRegression.learning(self.x_training, self.y_training);
        LinearRegression.predict(self.x_test, self.y_test);
        return LinearRegression.validateAlgorithm(self.predictors, self.target);
    
    def SVRAlgorithm(self):
        SVR.learning(self.x_training, self.y_training);
        SVR.predict(self.x_test, self.y_test);
        return SVR.validateAlgorithm(self.predictors, self.target);

    def DecisionTreeAlgorithm(self):
        DecisionTree.learning(self.x_training, self.y_training);
        DecisionTree.predict(self.x_test, self.y_test);
        return DecisionTree.validateAlgorithm(self.predictors, self.target);

    def RandomForestAlgorithm(self):
        RandomForest.learning(self.x_training, self.y_training);
        RandomForest.predict(self.x_test, self.y_test);
        return RandomForest.validateAlgorithm(self.predictors, self.target);
    
    def XGBoostAlgorithm(self):
        XGBoost.learning(self.x_training, self.y_training);
        XGBoost.predict(self.x_test, self.y_test);
        return XGBoost.validateAlgorithm(self.predictors, self.target);
    
    def LGBMAlgorithm(self):
        LGBM.learning(self.x_training, self.y_training);
        LGBM.predict(self.x_test, self.y_test);
        return LGBM.validateAlgorithm(self.predictors, self.target);
    
    def CatBoostAlgorithm(self):
        CatBoost.learning(self.x_training, self.y_training);
        CatBoost.predict(self.x_test, self.y_test);
        return CatBoost.validateAlgorithm(self.predictors, self.target);
    
    def MLPRegressorAlgorithm(self):
        MLPRegressor.learning(self.x_training, self.y_training);
        MLPRegressor.predict(self.x_test, self.y_test);
        return MLPRegressor.validateAlgorithm(self.predictors, self.target);
    