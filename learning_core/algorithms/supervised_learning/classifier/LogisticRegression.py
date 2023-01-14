from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

logistic = LogisticRegression(random_state=1, max_iter=500, penalty="l2",
                               tol=0.0001, C=1,solver="lbfgs")

kfold = KFold(n_splits = 30, shuffle=True, random_state = 5)

class LogisticRegressionAlgorithm:
    forecasters_base = [];
    target_base = [];
    
    x_training = [];
    y_training = [];
    x_test = [];
    y_test = [];
    
    predict_test = [];
    accuracy_test = 0.0;
    predict_training = [];
    accuracy_test = 0.0;
    
    average_cross_validation = 0.0;
    
    confusion_matrix_test = [];
    confusion_matrix_training = [];

    def learning(self, x_training, y_training):
        self.x_training = x_training;
        self.y_training = y_training;

        logistic.fit(x_training,y_training);
        
    def predict(self, x_test, y_test=[], accuracy=True):
        self.x_test = x_test;
        self.y_test = y_test;

        self.predict_test = logistic.predict(x_test);
        
        if(accuracy and len(y_test) > 0):
            self.accuracy_test = accuracy_score(y_test, self.predict_test) * 100.0;
        
        return self.predict_test;
        
        
    
    def validateAlgorithm(self, forecasters_base, target_base):
        self.forecasters_base = forecasters_base;
        self.target_base = target_base;
        
        self.predict_training = logistic.predict(self.x_training);
        self.accuracy_training = accuracy_score(self.y_training, self.predict_training) * 100.0;
        
        self.confusion_matrix_test = confusion_matrix(self.y_test, self.predict_test);
        self.confusion_matrix_training = confusion_matrix(self.y_training, self.predict_training);
        self.average_cross_validation = cross_val_score(logistic, forecasters_base, target_base, cv = kfold).mean() * 100.0;
        
        return {
            'accuracy_training': self.accuracy_training,
            'accuracy_test': self.accuracy_test,
            'average_cross_validation': self.average_cross_validation,
        }
    
    def getIntercept(self):
        return logistic.intercept_;
    
    def getCoef(self):
        return logistic.coef_;