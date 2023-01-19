import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

class PreProcessingData():
    forecasters = [];
    forecasters_esc = [];
    forecasters_dummy_esc = [];
    attributes = [];
    
    target = [];
    
    path = os.path.dirname(__file__);
    
    def getForecastersAndTarget(self, arquive, sep, initital_attributes_column_number, num_final_columns_attributes, num_column_target = 1, categoricals_vars = [], dummy_vars = []):
        dataFrame = pd.read_csv(self.path+arquive, sep=sep, encoding='utf-8');
        dataFrameOfficial = pd.DataFrame.copy(dataFrame);
        
        if(len(categoricals_vars)):
            for categorical in categoricals_vars:
                dataFrameOfficial[categorical['name']].replace(categorical['replacement'], inplace=True);
    
        self.attributes = dataFrameOfficial.iloc[:, initital_attributes_column_number:num_final_columns_attributes];
        self.forecasters = dataFrameOfficial.iloc[:, initital_attributes_column_number:num_final_columns_attributes].values;
        self.target = dataFrameOfficial.iloc[:, num_column_target].values;
        
        #self.transformCategoricalVariables();
        #self.createDummyVariables();
        if(len(dummy_vars)):
            self.createDummyVariables(dummy_vars);
        self.scaleData();
        
        return dataFrameOfficial;
        
        
    #def transformCategoricalVariables(self, categorical_variables):
    #    print(self.forecasters);
    
    def createDummyVariables(self, dummyVars = []):
        self.forecasters = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), dummyVars)],remainder='passthrough').fit_transform(self.forecasters)
        
    def scaleData(self):
        self.forecasters_esc = StandardScaler().fit_transform(self.forecasters);
    
    