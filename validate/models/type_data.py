class TypeDataModel():
    typeData = [
        "normal",
        "esc"
    ]
    
    def validate(self, value):
        return value in self.typeData
        