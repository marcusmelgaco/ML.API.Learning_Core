from learning_core.algorithms.supervised_learning.classifier import NaiveBayes;
from learning_core.algorithms.supervised_learning.classifier import SVM;
from learning_core.algorithms.supervised_learning.classifier import LogisticRegression;
from learning_core.algorithms.supervised_learning.classifier import KNN;
from learning_core.algorithms.supervised_learning.classifier import DecisionTree;
from learning_core.algorithms.supervised_learning.classifier import RandomForest;
from learning_core.algorithms.supervised_learning.classifier import XGBoost;
from learning_core.algorithms.supervised_learning.classifier import LGBM;
from learning_core.algorithms.supervised_learning.classifier import CatBoost;
from learning_core.algorithms.supervised_learning.classifier.ANN import MLPClassifier;

NaiveBayes = NaiveBayes.NaiveBayesAlgorithm();
SVM = SVM.SVMAlgorithm();
LogisticRegression = LogisticRegression.LogisticRegressionAlgorithm();
KNN = KNN.KNNAlgorithm();
DecisionTree = DecisionTree.DecisionTreeAlgorithm();
RandomForest = RandomForest.RandomForestAlgorithm();
XGBoost = XGBoost.XGBoostAlgorithm();
LGBM = LGBM.LGBMAlgorithm();
CatBoost = CatBoost.CatBoostAlgorithm();
MLPClassifier = MLPClassifier.MLPClassifierAlgorithm();

class SupervisedLearningClassifier():
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
        
        #MLPClassifier
        algorithm_predict_infos['MLPClassifier'] = self.MLPClassifierAlgorithmValidate();
        
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
        elif(modelName == "ANN.MLP"):
            model = MLPClassifier;
        
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
        NaiveBayes.learning(self.x_training, self.y_training);
        NaiveBayes.predict(self.x_test, self.y_test);
        return NaiveBayes.validateAlgorithm(self.predictors, self.target);

    def SVMAlgorithmValidate(self):
        SVM.learning(self.x_training, self.y_training);
        SVM.predict(self.x_test, self.y_test);
        return SVM.validateAlgorithm(self.predictors, self.target);
    
    def LogisticRegressionAlgorithmValidate(self):
        LogisticRegression.learning(self.x_training, self.y_training);
        LogisticRegression.predict(self.x_test, self.y_test);
        return LogisticRegression.validateAlgorithm(self.predictors, self.target);
    
    def KNNAlgorithmValidate(self):
        KNN.learning(self.x_training, self.y_training);
        KNN.predict(self.x_test, self.y_test);
        return KNN.validateAlgorithm(self.predictors, self.target);
    
    def DecisionTreeAlgorithmValidate(self):
        DecisionTree.learning(self.x_training, self.y_training);
        DecisionTree.predict(self.x_test, self.y_test);
        return DecisionTree.validateAlgorithm(self.predictors, self.target);
    
    def RandomForestAlgorithmValidate(self):
        RandomForest.learning(self.x_training, self.y_training);
        RandomForest.predict(self.x_test, self.y_test);
        return RandomForest.validateAlgorithm(self.predictors, self.target);
    
    def XGBoostAlgorithmValidate(self):
        XGBoost.learning(self.x_training, self.y_training);
        XGBoost.predict(self.x_test, self.y_test);
        return XGBoost.validateAlgorithm(self.predictors, self.target);
    
    def LGBMAlgorithmValidate(self):
        LGBM.learning(self.x_training, self.y_training);
        LGBM.predict(self.x_test, self.y_test);
        return LGBM.validateAlgorithm(self.predictors, self.target);
    
    def CatBoostAlgorithmValidate(self):
        CatBoost.learning(self.x_training, self.y_training);
        CatBoost.predict(self.x_test, self.y_test);
        return CatBoost.validateAlgorithm(self.predictors, self.target);
    
    MLPClassifier
    
    def MLPClassifierAlgorithmValidate(self):
        MLPClassifier.learning(self.x_training, self.y_training);
        MLPClassifier.predict(self.x_test, self.y_test);
        return MLPClassifier.validateAlgorithm(self.predictors, self.target);