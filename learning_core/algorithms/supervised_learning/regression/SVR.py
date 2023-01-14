from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import numpy as np

svr = SVR(kernel='rbf')
x_scaler = StandardScaler();
y_scaler = StandardScaler();
x_scaler_validate = StandardScaler();
y_scaler_validate = StandardScaler();
kfold = KFold(n_splits = 30, shuffle=True, random_state = 5)

class SVRAlgorithm:
    forecasters_base = [];
    target_base = [];
    forecasters_base_scaler = [];
    target_base_scaler = [];
    
    x_training = [];
    y_training = [];
    x_training_scaler = [];
    y_training_scaler = [];
    x_test = [];
    y_test = [];
    x_test_scaler = [];
    y_test_scaler = [];
    
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

        self.scaleData('train');
        
        svr.fit(self.x_training_scaler,self.y_training_scaler.ravel());
        self.determination_coefficient_training = svr.score(self.x_training_scaler, self.y_training_scaler);
        
    def predict(self, x_test, y_test=[]):
        self.x_test = x_test;
        self.y_test = y_test;
        
        self.scaleData('test');
        
        self.determination_coefficient_test = svr.score(self.x_test_scaler, self.y_test_scaler);

        self.predict_test = svr.predict(self.x_test_scaler);
        
        return self.predict_test;
        
    def scaleData(self, type = ""):
        if(type == 'test'):
            self.x_test_scaler = x_scaler.transform(self.x_test);
            self.y_test_scaler = y_scaler.transform(self.y_test.reshape(-1,1));
        elif('train'):
            self.x_training_scaler = x_scaler.fit_transform(self.x_training);
            self.y_training_scaler = y_scaler.fit_transform(self.y_training.reshape(-1,1));
    
    def validateAlgorithm(self, forecasters_base, target_base):
        self.forecasters_base = forecasters_base;
        self.target_base = target_base;
        self.forecasters_base_scaler = x_scaler_validate.fit_transform(self.forecasters_base);
        self.target_base_scaler = y_scaler_validate.fit_transform(self.target_base.reshape(-1,1));
        
        self.predict_test = y_scaler.inverse_transform(self.predict_test.reshape(-1, 1))
        
        self.predict_training = svr.predict(self.x_training_scaler);
        #self.accuracy_training = accuracy_score(self.y_training, self.predict_training) * 100.0;
        
        #self.confusion_matrix_test = confusion_matrix(self.y_test, self.predict_test);
        #self.confusion_matrix_training = confusion_matrix(self.y_training, self.predict_training);
        self.average_cross_validation = cross_val_score(svr, self.forecasters_base_scaler, self.target_base_scaler.ravel(), cv = kfold).mean() * 100.0;
        
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
    
    def getIntercept(self):
        return svr.intercept_;
    
    def getCoef(self):
        return svr.coef_;