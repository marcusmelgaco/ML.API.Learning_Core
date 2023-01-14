class HousingConfig():
    inputs = [
        'RM',
        'LSTAT',
        'PTRATIO'
    ];
    
    output = "MEDV"
    
    categorical_vars = []
    
    num_registers = 489;
    initital_predictors_column_number = 0;
    num_final_columns_forecasters = 3;
    num_column_target = 3;
    separator = ',';
    arquive = 'housing.csv'
    
    def resultDataFrameIntoJson(self, data_frame):
        result = { "diagnosis": [] };
        
        for data in data_frame:
            objectResponse = { 'Value_Housing' : data };
            result['Value_Housing'].append(objectResponse);
        
        return result;
        
            
    
    def serializeDataFrameIntoJson(self, data_frame):  
        result_algorithm = { 'data': [] };
        
        for data in data_frame.values:
            objectResponse = {};
            objectResponse['RM'] = data[0];
            objectResponse['LSTAT'] = data[1];
            objectResponse['PTRATIO'] = data[2];
            
            result_algorithm['data'].append(objectResponse)
        
        return result_algorithm['data'];