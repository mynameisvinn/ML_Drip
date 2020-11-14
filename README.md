# ML Drip
Deploy a scikit estimator in the simplest way possible.

## Example
First, fit an estimator `clf`.
```python
# fit your estimator the way you usually do

X, y = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
```
Instantiate a `Drip` object with `clf`. 
```python
api = Drip(clf, port=8080)  # clf is exposed
```
Clients can hit `api` for predictions:
```python
import json
import requests

X_test = list(iris['data'][0])
requests.post('http://localhost:8080', json=json.dumps({'X_test': X_test}))  # returns [0]
```