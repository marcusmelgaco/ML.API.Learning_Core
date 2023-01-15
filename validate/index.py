import validate.models.data as DataModel;
import validate.models.type_data as TypeDataModel;
import validate.models.method as MethodModel;
import validate.models.algorithms as AlgorithmsModel;

from validate.request.predict_result import PredictResultValidate

DataModel = DataModel.DataModel();
TypeDataModel = TypeDataModel.TypeDataModel();
MethodModel = MethodModel.MethodModel();
AlgorithmsModel = AlgorithmsModel.AlgorithmsModel();

class ValidateRoutes():
    routes = {
        'predict-result': PredictResultValidate(),
        'validate-accuracy-algorithms': {},
    }
    
    def validate(self, endpoint, body):
        def fillItemNotFound(key, value):
            notFoundItem["key"] = key;
            notFoundItem["item"] = value;
            return notFoundItem;
        
        
        
        validate = self.routes[endpoint];
        
        brokenRules = {
            "error": "BrokenRules",
            "key_dependency": [],
            "key_required": [],
            "item_not_found": []
        };
        
        keys = list(validate.body.keys());
        
        for key in keys:       
            print("KEY => ", key)
            if(key in body):
                notFoundItem = {
                    "key": "",
                    "item": "",
                }
                
                if(key == "modelName"):
                    if(DataModel.validate(value=body[key]) != True):
                        brokenRules["item_not_found"].append(fillItemNotFound(key=key, value=body[key]));
                elif(key == "typeData"):
                    if(TypeDataModel.validate(value=body[key]) != True):
                        brokenRules["item_not_found"].append(fillItemNotFound(key=key, value=body[key]));
                elif(key == "method"):
                    if(MethodModel.validate(value=body[key]) != True):
                        brokenRules["item_not_found"].append(fillItemNotFound(key=key, value=body[key]));
                elif(key == "algorithm"):
                    if("method" in body):
                        if(AlgorithmsModel.validate(method=body['method'], value=body[key]) != True):
                            brokenRules["item_not_found"].append(fillItemNotFound(key=key, value=body[key]));
                    else:
                        brokenRules["key_dependency"].append({
                            "key": key,
                            "needs_key": "method"
                        })
            
            elif(validate.body[key]):
                brokenRules["key_required"].append(key);
                
        if(
            len(brokenRules["item_not_found"]) == 0 and
            len(brokenRules["key_required"]) == 0 and
            len(brokenRules["key_dependency"]) == 0
        ):
            return True
        else:
            return brokenRules;