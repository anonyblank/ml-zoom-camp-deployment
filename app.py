import pickle5 as pickle
from flask import Flask, request, jsonify
import numpy as np

with open('./model2.bin', 'rb') as mf:
    model = pickle.load(mf)

with open('./dv.bin', 'rb') as df:
    dv = pickle.load(df)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hello"


@app.route('/predict', methods=['POST'])
def predict():
    client = dict(request.json)
    client_feature = dv.transform(client)
    client_pred_label = np.round(model.predict_proba(client_feature)[:, 1], 3)

    return jsonify({"probability": float(client_pred_label)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9696', debug=True)
