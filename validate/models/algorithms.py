import validate.models.method as MethodModel;

MethodModel = MethodModel.MethodModel();
class AlgorithmsModel():
    algorithms = {
        "supervised_classifier": [
            "CatBoost",
            "DecisionTree",
            "KNN",
            "LGBM",
            "LogisticRegression",
            "NaiveBayes",
            "RandomForest",
            "SVM",
            "XGBoost",
            "ANN.MLP",
        ],
        "supervised_regression": [
            "CatBoost",
            "DecisionTree",
            "LGBM",
            "LinearRegression",
            "RandomForest",
            "SVM",
            "XGBoost",
            "ANN.MLP",
        ]
    };
    
    def validate(self, method, value):
        if(method in self.algorithms):
            if(value in self.algorithms[method]):
                return True;
            else:
                return False;
        else: return False;
            