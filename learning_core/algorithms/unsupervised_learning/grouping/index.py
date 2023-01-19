from learning_core.algorithms.unsupervised_learning.grouping import Kmeans

Kmeans = Kmeans.KmeansAlgorithm()

class UnsupervisedLearningGrouping():
    attributes = [];
    model = {};
    
    def init(self, data):
        self.attributes = data['attributes'];
        self.attributes_original = data['attributes_original'];
        self.model = data['model'];
        
    
    def validateAlgorithms(self):
        algorithm_predict_infos = {};
        
        #Kmeans
        algorithm_predict_infos['Kmeans'] = self.KmeansAlgorithmValidate();
        
        return algorithm_predict_infos;
    
    def defineModel(self, modelName):
        model = {};

        if(modelName == "Kmeans"):
            model = Kmeans;
        elif(modelName == ""):
            model = {};
        
        return model;
    
    def agroup(self, algorithm):
        model = self.defineModel(algorithm);
        return model.agroup(self.attributes, self.attributes_original, self.model.n_clusters);
    
    def KmeansAlgorithmValidate(self):
        self.agroup("Kmeans")
        validate = Kmeans.validateAlgorithm(self.model)
        
        return validate;
