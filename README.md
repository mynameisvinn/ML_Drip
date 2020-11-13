# ML Drip
deploy machine learning models in the simplest way possible.

## Example
First, fit an estimator `clf`.
```python
# fit your estimator
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
```
Then, instantiate a `Drip` object with `clf`. 
```python
api = Drip(clf, port=8080)
```
Clients can hit `api` for predictions:
```python
import json
import requests

X_test = list(iris['data'][0])
requests.post('http://localhost:8080', json=json.dumps({'X_test': X_test}))  # returns [0]
```