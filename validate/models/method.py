class MethodModel():
    method = [
        "supervised_regression",
        "supervised_classifier",
        "unsupervised_grouping"
    ]
    
    def validate(self, value):
        if(value in self.method):
            return True;
        else: return False;