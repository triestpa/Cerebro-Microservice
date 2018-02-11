"""Flask Server Module"""
from flask import Flask, current_app, request, jsonify
from classify import Classifier

app = Flask(__name__)
model = Classifier()

@app.route('/prediction', methods=['GET'])
def predict():
    """Predict the contents of the provided image"""
    url = request.args.get('url')

    if url is None:
        return jsonify(status_code='400', msg='Bad Request'), 400

    predictions = model.predict_url(url)
    current_app.logger.info('Predictions: %s', predictions)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
