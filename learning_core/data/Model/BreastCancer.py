class BreastCancerConfig():
    inputs = [
        'radius_mean',
        'texture_mean',
        'perimeter_mean',
        'area_mean',
        'smoothness_mean',
        'compactness_mean',
        'concavity_mean',
        "concave points_mean",
        'symmetry_mean',
        'fractal_dimension_mean',
        'radius_se',
        'texture_se',
        'perimeter_se',
        'area_se',
        'smoothness_se',
        'compactness_se',
        'concavity_se',
        "concave points_se",
        'symmetry_se',
        'fractal_dimension_se',
        'radius_worst',
        'texture_worst',
        'perimeter_worst',
        'area_worst',
        'smoothness_worst',
        'compactness_worst',
        'concavity_worst',
        "concave_points_worst",
        'symmetry_worst',
        'fractal_dimension_worst',
    ];
    
    output = "diagnosis"
    
    categorical_vars = [
        {
            "name": "diagnosis",
            "replacement": {'B': 0, 'M': 1}
        },
    ]
    
    dummy_vars = [];
    
    num_registers = 569;
    initital_predictors_column_number = 2;
    num_final_columns_forecasters = 32;
    num_column_target = 1;
    separator = ',';
    arquive = 'data_cancer2.csv'
    
    def resultDataFrameIntoJson(self, data_frame):
        result = { "diagnosis": [] };
        
        for data in data_frame:
            objectResponse = { 'BreastCancer' : '' };
            if(data == 1):
                objectResponse['BreastCancer'] = 'Malign'
            else: objectResponse['BreastCancer'] = 'Benign'
            result['diagnosis'].append(objectResponse);
        
        return result;
        
            
    
    def serializeDataFrameIntoJson(self, data_frame):  
        result_algorithm = { 'data': [] };
        
        for data in data_frame.values:
            objectResponse = {};
            objectResponse['radius_mean'] = data[2];
            objectResponse['texture_mean'] = data[3];
            objectResponse['perimeter_mean'] = data[4];
            objectResponse['area_mean'] = data[5];
            objectResponse['smoothness_mean'] = data[6];
            objectResponse['compactness_mean'] = data[7];
            objectResponse['concavity_mean'] = data[8];
            objectResponse['concave points_mean'] = data[9];
            objectResponse['symmetry_mean'] = data[10];
            objectResponse['fractal_dimension_mean'] = data[11];
            objectResponse['radius_se'] = data[12];
            objectResponse['texture_se'] = data[13];
            objectResponse['perimeter_se'] = data[14];
            objectResponse['area_se'] = data[15];
            objectResponse['smoothness_se'] = data[16];
            objectResponse['compactness_se'] = data[17];
            objectResponse['concavity_se'] = data[18];
            objectResponse['concave points_se'] = data[19];
            objectResponse['symmetry_se'] = data[20];
            objectResponse['fractal_dimension_se'] = data[21];
            objectResponse['radius_worst'] = data[22];
            objectResponse['texture_worst'] = data[23];
            objectResponse['perimeter_worst'] = data[24];
            objectResponse['area_worst'] = data[25];
            objectResponse['smoothness_worst'] = data[26];
            objectResponse['compactness_worst'] = data[27];
            objectResponse['concavity_worst'] = data[28];
            objectResponse['concave points_worst'] = data[29];
            objectResponse['symmetry_worst'] = data[30];
            objectResponse['fractal_dimension_worst'] = data[31];
            result_algorithm['data'].append(objectResponse)
        
        return result_algorithm['data'];