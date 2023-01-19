class DataModel():
    data = [
        "BreastCancer",
        "Housing",
        "MedicalCost",
        "WineClustering"
    ]
    
    def validate(self, value):
        return value in self.data
        