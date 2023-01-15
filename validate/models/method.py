class MethodModel():
    method = [
        "supervised_regression",
        "supervised_classifier",
    ]
    
    def validate(self, value):
        if(value in self.method):
            return True;
        else: return False;