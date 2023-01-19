class MedicalCostConfig():
    type = "supervised";
    inputs = [
        "age",
        "sex",
        "bmi",
        "children",
        "smoker",
        "region",
    ];
    
    output = "charges"
    
    categorical_vars = [
        {
            "name": "sex",
            "replacement": {'male': 0, 'female': 1}
        },
        {
            "name": "smoker",
            "replacement": {'no': 0, 'yes': 1}
        },
    ];
    dummy_vars = [5];
    
    num_registers = 1338;
    initital_attributes_column_number = 0;
    num_final_columns_attributes = 6;
    num_column_target = 6;
    separator = ',';
    arquive = 'insurance.csv'
    
    def resultDataFrameIntoJson(self, data_frame):
        result = { "Medical_Costs": [] };
        for data in data_frame:
            objectResponse = { 'Medical_Insurance_Price' : float(data) };
            result['Medical_Costs'].append(objectResponse);

        return result;
        
            
    
    def serializeDataFrameIntoJson(self, data_frame):  
        result_algorithm = { 'data': [] };
        
        for data in data_frame.values:
            objectResponse = {};
            objectResponse["age"] = data[0];
            objectResponse["sex"] = data[1];
            objectResponse["bmi"] = data[2];
            objectResponse["children"] = data[3];
            objectResponse["smoker"] = data[4];
            objectResponse["region"    ] = data[5];
            
            result_algorithm['data'].append(objectResponse)
        
        return result_algorithm['data'];