import pytest
# TODO: add necessary import
import numpy as np
from ml.model import (
    compute_model_metrics,
    inference,
    train_model
)
from sklearn.ensemble import RandomForestClassifier


# from numpy documentation https://numpy.org/devdocs/reference/random/generated/numpy.random.randint.html
X = np.random.rand(3,2)
y = np.random.randint(2, size=3)
X_test = np.random.rand(3,2)
y_test = np.random.randint(2, size=3)
# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    # add description for the first test
    """
    # Your code here
    model = train_model(X,y)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    # add description for the second test
    """
    # Your code here
    model = train_model(X,y)
    preds = inference(model, X_test)
    assert 0<=preds.all()<=1



# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # add description for the third test
    """
    # Your code here
    model = train_model(X,y)
    preds = inference(model, X_test)
    p, r, fb = compute_model_metrics(y_test, preds)
    assert 0<=p<=1
    assert 0<=r<=1
    assert 0<=fb<=1