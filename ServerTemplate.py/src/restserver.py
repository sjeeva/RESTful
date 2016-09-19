from flask import Flask
from flask import jsonify
from flask import make_response

app = Flask(__name__)

@app.route('/nouns', methods=['GET'])
def get_nouns():
    return 'All nouns details are listed'
    
@app.route('/nouns/<id>', methods=['GET'])
def get_noun(id):
    return 'the noun with ' + id + ' is listed'
	
@app.route('/nouns/<id>', methods=['POST'])
def create_noun(id):
	return 'the noun with ' + id + ' is inserted successfully'	

@app.route('/nouns/<id>', methods=['PUT'])
def update_noun(id):
	return 'the noun with ' + id + ' is updated'
	
@app.route('/nouns/<id>', methods=['DELETE'])
def delete_noun(id):
	return 'the noun with ' + id + ' is deleted'

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
