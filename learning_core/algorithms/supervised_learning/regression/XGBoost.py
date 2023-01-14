from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import numpy as np


xg = XGBRegressor(n_estimators=180, max_depth=3, learning_rate=0.05, objective="reg:squarederror", random_state=10)
kfold = KFold(n_splits = 30, shuffle=True, random_state= 5)


class XGBoostAlgorithm():
    forecasters_base = [];
    target_base = [];
    
    x_training = [];
    y_training = [];
    determination_coefficient_training = 0.00;
    x_test = [];
    y_test = [];
    determination_coefficient_test = 0.00;
    
    predict_test = [];
    accuracy_test = 0.0;
    predict_training = [];
    accuracy_test = 0.0;
    
    average_cross_validation = 0.0;
    
    confusion_matrix_test = [];
    confusion_matrix_training = [];
    
    absolute_error = 0.0;
    mean_absolute_error = 0.0;
    mean_squared_error = 0.0;
    root_mean_squared_error = 0.0;

    def learning(self, x_training, y_training):
        self.x_training = x_training;
        self.y_training = y_training;

        xg.fit(x_training,y_training);
        self.determination_coefficient_training = xg.score(self.x_training, self.y_training);
        
    def predict(self, x_test, y_test=[]):
        self.x_test = x_test;
        self.y_test = y_test;
        self.determination_coefficient_test = xg.score(self.x_test, self.y_test);

        self.predict_test = xg.predict(x_test);
        
        return self.predict_test;
        
        
    
    def validateAlgorithm(self, forecasters_base, target_base):
        self.forecasters_base = forecasters_base;
        self.target_base = target_base;
        
        self.predict_training = xg.predict(self.x_training);
        #self.accuracy_training = accuracy_score(self.y_training, self.predict_training) * 100.0;
        
        #self.confusion_matrix_test = confusion_matrix(self.y_test, self.predict_test);
        #self.confusion_matrix_training = confusion_matrix(self.y_training, self.predict_training);
        self.average_cross_validation = cross_val_score(xg, forecasters_base, target_base, cv = kfold).mean() * 100.0;
        
        self.absolute_error = abs(self.y_test - self.predict_test).mean();
        self.mean_absolute_error = mean_absolute_error(self.y_test,self.predict_test);
        self.mean_squared_error = mean_squared_error(self.y_test,self.predict_test);
        self.root_mean_squared_error = np.sqrt(self.mean_squared_error);
        
        return {
            'determination_coefficient_training': self.determination_coefficient_training,
            'determination_coefficient_test': self.determination_coefficient_test,
            'average_cross_validation_score': self.average_cross_validation,
            'absolute_error': self.absolute_error,
            'mean_absolute_error': self.mean_absolute_error,
            'mean_squared_error': self.mean_squared_error,
            'root_mean_squared_error': self.root_mean_squared_error,
        }