class DataModel():
    data = [
        "BreastCancer",
        "Housing",
        "MedicalCost"
    ]
    
    def validate(self, value):
        return value in self.data
        