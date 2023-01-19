class WineClusteringConfig():
    type = "unsupervised";
    inputs = [
        "Alcohol",
        "Malic_Acid",
        "Ash",
        "Ash_Alcanity",
        "Magnesium",
        "Total_Phenols",
        "Flavanoids",
        "Nonflavanoid_Phenols",
        "Proanthocyanins",
        "Color_Intensity",
        "Hue",
        "OD280",
        "Proline"
    ];
    
    n_clusters = 3;
    
    categorical_vars = [
    ];
    dummy_vars = [];
    
    num_registers = 179;
    initital_attributes_column_number = 0;
    num_final_columns_attributes = 13;
    num_column_target = 0;
    separator = ',';
    arquive = 'wine-clustering.csv'
    
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
            objectResponse["Alcohol"] = data[0];
            objectResponse["Malic_Acid"] = data[1];
            objectResponse["Ash"] = data[2];
            objectResponse["Ash_Alcanity"] = data[3];
            objectResponse["Magnesium"] = data[4];
            objectResponse["Total_Phenols"] = data[5];
            objectResponse["Flavanoids"] = data[6];
            objectResponse["Nonflavanoid_Phenols"] = data[7];
            objectResponse["Proanthocyanins"] = data[8];
            objectResponse["Color_Intensity"] = data[9];
            objectResponse["Hue"] = data[10];
            objectResponse["OD280"] = data[11];
            objectResponse["Proline"] = data[12];
            
            result_algorithm['data'].append(objectResponse)
        
        return result_algorithm['data'];
    
    def convertDataFrameIntoArrayOfObjects(self, data_frame):  
        result_algorithm = [];
        
        for data in data_frame.values:
            objectResponse = {};
            objectResponse["Alcohol"] = data[0];
            objectResponse["Malic_Acid"] = data[1];
            objectResponse["Ash"] = data[2];
            objectResponse["Ash_Alcanity"] = data[3];
            objectResponse["Magnesium"] = data[4];
            objectResponse["Total_Phenols"] = data[5];
            objectResponse["Flavanoids"] = data[6];
            objectResponse["Nonflavanoid_Phenols"] = data[7];
            objectResponse["Proanthocyanins"] = data[8];
            objectResponse["Color_Intensity"] = data[9];
            objectResponse["Hue"] = data[10];
            objectResponse["OD280"] = data[11];
            objectResponse["Proline"] = data[12];
            objectResponse["Group"] = data[13];
            
            result_algorithm.append(objectResponse)
        
        return result_algorithm;