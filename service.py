import bentoml

from bentoml.io import NumpyNdarray

# model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")

model_runner = model_ref.to_runner()

svc = bentoml.Service("mlzoomcamp_homework_prediction", runners=[model_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def predict(application_data):
    prediction = model_runner.predict.run(application_data)
    print (prediction)
    return prediction