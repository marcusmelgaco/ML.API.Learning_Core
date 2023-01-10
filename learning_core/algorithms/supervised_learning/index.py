from learning_core.algorithms.supervised_learning import NaiveBayes;
from learning_core.algorithms.supervised_learning import SVM;
from learning_core.algorithms.supervised_learning import LogisticRegression;
from learning_core.algorithms.supervised_learning import KNN;
from learning_core.algorithms.supervised_learning import DecisionTree;
from learning_core.algorithms.supervised_learning import RandomForest;
from learning_core.algorithms.supervised_learning import XGBoost;
from learning_core.algorithms.supervised_learning import LGBM;
from learning_core.algorithms.supervised_learning import CatBoost;

NaiveBayes = NaiveBayes.NaiveBayesAlgorithm();
SVM = SVM.SVMAlgorithm();
LogisticRegression = LogisticRegression.LogisticRegressionAlgorithm();
KNN = KNN.KNNAlgorithm();
DecisionTree = DecisionTree.DecisionTreeAlgorithm();
RandomForest = RandomForest.RandomForestAlgorithm();
XGBoost = XGBoost.XGBoostAlgorithm();
LGBM = LGBM.LGBMAlgorithm();
CatBoost = CatBoost.CatBoostAlgorithm();

class SupervisedLearning():
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
        
        # Naive Bayes Algorithm
        algorithm_predict_infos['NaiveBayes'] = self.NaiveBayesAlgorithmValidate();
        
        #SVM Algorithm
        algorithm_predict_infos['SVM'] = self.SVMAlgorithmValidate();
        
        #Logistic Regression
        algorithm_predict_infos['LogisticRegression'] = self.LogisticRegressionAlgorithmValidate();
        
        #KNN
        algorithm_predict_infos['KNN'] = self.KNNAlgorithmValidate();
        
        #Decision Tree
        algorithm_predict_infos['DecisionTree'] = self.DecisionTreeAlgorithmValidate();
        
        #Random Forest
        algorithm_predict_infos['RandomForest'] = self.RandomForestAlgorithmValidate();
        
        #XGBoost
        algorithm_predict_infos['XGBoost'] = self.XGBoostAlgorithmValidate();
        
        #LGBM
        algorithm_predict_infos['LGBM'] = self.LGBMAlgorithmValidate();        
        
        #CatBoost
        algorithm_predict_infos['CatBoost'] = self.CatBoostAlgorithmValidate();
        
        return algorithm_predict_infos;
    
    def defineModel(self, modelName):
        model = {};

        if(modelName == "CatBoost"):
            model = CatBoost;
        elif(modelName == "DecisionTree"):
            model = DecisionTree;
        elif(modelName == "KNN"):
            model = KNN;
        elif(modelName == "LGBM"):
            model = LGBM;
        elif(modelName == "LogisticRegression"):
            model = LogisticRegression;
        elif(modelName == "NaiveBayes"):
            model = NaiveBayes;
        elif(modelName == "RandomForest"):
            model = RandomForest;
        elif(modelName == "SVM"):
            model = SVM;
        elif(modelName == "XGBoost"):
            model = XGBoost;
        
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
    
    def NaiveBayesAlgorithmValidate(self):
        NaiveBayes.learning(self.x_trainning, self.y_trainning);
        NaiveBayes.predict(self.x_test, self.y_test);
        return NaiveBayes.validateAlgorithm(self.predictors, self.target);

    def SVMAlgorithmValidate(self):
        SVM.learning(self.x_trainning, self.y_trainning);
        SVM.predict(self.x_test, self.y_test);
        return SVM.validateAlgorithm(self.predictors, self.target);
    
    def LogisticRegressionAlgorithmValidate(self):
        LogisticRegression.learning(self.x_trainning, self.y_trainning);
        LogisticRegression.predict(self.x_test, self.y_test);
        return LogisticRegression.validateAlgorithm(self.predictors, self.target);
    
    def KNNAlgorithmValidate(self):
        KNN.learning(self.x_trainning, self.y_trainning);
        KNN.predict(self.x_test, self.y_test);
        return KNN.validateAlgorithm(self.predictors, self.target);
    
    def DecisionTreeAlgorithmValidate(self):
        DecisionTree.learning(self.x_trainning, self.y_trainning);
        DecisionTree.predict(self.x_test, self.y_test);
        return DecisionTree.validateAlgorithm(self.predictors, self.target);
    
    def RandomForestAlgorithmValidate(self):
        RandomForest.learning(self.x_trainning, self.y_trainning);
        RandomForest.predict(self.x_test, self.y_test);
        return RandomForest.validateAlgorithm(self.predictors, self.target);
    
    def XGBoostAlgorithmValidate(self):
        XGBoost.learning(self.x_trainning, self.y_trainning);
        XGBoost.predict(self.x_test, self.y_test);
        return XGBoost.validateAlgorithm(self.predictors, self.target);
    
    def LGBMAlgorithmValidate(self):
        LGBM.learning(self.x_trainning, self.y_trainning);
        LGBM.predict(self.x_test, self.y_test);
        return LGBM.validateAlgorithm(self.predictors, self.target);
    
    def CatBoostAlgorithmValidate(self):
        CatBoost.learning(self.x_trainning, self.y_trainning);
        CatBoost.predict(self.x_test, self.y_test);
        return CatBoost.validateAlgorithm(self.predictors, self.target);