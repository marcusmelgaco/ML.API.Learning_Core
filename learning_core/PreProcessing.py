import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

class PreProcessingData():
    forecasters = [];
    forecasters_esc = [];
    
    target = [];
    
    path = os.path.dirname(__file__);
    
    def getForecastersAndTarget(self, arquive, sep, initital_predictors_column_number, num_final_columns_forecasters, num_column_target = 1):
        dataFrame = pd.read_csv(self.path+arquive, sep=sep, encoding='utf-8');
        dataFrameOfficial = pd.DataFrame.copy(dataFrame);
        dataFrameOfficial['diagnosis'].replace({'B': 0, 'M': 1}, inplace=True);
    
        self.forecasters = dataFrameOfficial.iloc[:, initital_predictors_column_number:num_final_columns_forecasters].values;
        self.target = dataFrameOfficial.iloc[:, num_column_target].values;
        
        #self.transformCategoricalVariables();
        #self.createDummyVariables();
        self.scaleData();
        
        return dataFrameOfficial;
        
        
    #def transformCategoricalVariables(self, categorical_variables):
    #    print(self.forecasters);
    
    #def createDummyVariables(self):
        
    def scaleData(self):
        self.forecasters_esc = StandardScaler().fit_transform(self.forecasters);
    
    