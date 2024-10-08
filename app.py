import numpy as np
from flask import Flask, request, render_template
import pickle

# flask app
flask_app = Flask(__name__)
model = pickle.load(open("randomclf.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text="The Predicted Crop is {}".format(prediction[0]))

