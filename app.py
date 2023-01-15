from flask import Flask, jsonify, request, make_response
from learning_core import index as learning_core
from validate.index import ValidateRoutes;

app = Flask(__name__)
app.config['DEBUG'] = True

LC = learning_core.LerningCore();


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Status': 404, 'Error': 'Resource not found'}), 404)


@app.route('/api/v1/validate-accuracy-algorithms', methods=['POST'])
def validateAccuracyAlgorithms():
    req = request.json;
    
    result_algorithm = LC.validateAlgorithms(modelName=req['modelName'], typeData=req['typeData'], method=req['method']); 
    return make_response(result_algorithm, 200);

@app.route('/api/v1/predict-result', methods=['POST'])
def predictResult():
    req = request.json;
    validateRoute = ValidateRoutes.validate(self=ValidateRoutes, endpoint="predict-result", body=req['config']);
    
    if( validateRoute != True):
        return make_response(validateRoute, 500);
    
    result_algorithm = LC.predictResult(req['config'], req['data']);

    return make_response(result_algorithm, 200);


app.run(debug=True)
