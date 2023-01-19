from sklearn.cluster import KMeans
import pandas as pd;

class KmeansAlgorithm():
    attributes = [];
    attributes_original = [];
    groups = [];
    attributes_groups = [];
    kmeans = {};
    
    
    def agroup(self, attributes, attributes_original, n_clusters):
        self.kmeans= KMeans(n_clusters = n_clusters, init = 'k-means++', random_state = 5, max_iter = 300)
        self.attributes = attributes;
        self.attributes_original = attributes_original;

        self.kmeans.fit(attributes);
        
        self.groups = self.kmeans.labels_;
        
        df_group = pd.DataFrame(self.groups, columns = ['Group']);
        self.attributes_groups = pd.concat([self.attributes_original, df_group], axis=1 );
        
        return self.attributes_groups;
        
    def getGroups(self):
        return self.groups;
    
    def getAttributesWithGroups(self):
        return self.attributes_groups;
    
    def validateAlgorithm(self, model):
        return {
            'centroids': self.kmeans.cluster_centers_.tolist(),
            'labels': self.kmeans.labels_.tolist(),
            'inertia': self.kmeans.inertia_,
            #'attributes_groups': model.convertDataFrameIntoArrayOfObjects(self.attributes_groups),
        }
        