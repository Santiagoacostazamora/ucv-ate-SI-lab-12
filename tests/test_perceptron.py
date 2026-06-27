"""Pruebas unitarias para el perceptron simple."""

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.dataset import training_data
from src.perceptron import Perceptron


def trained_model():
    model = Perceptron()
    model.train(training_data)
    return model


def test_prediction_approved_training_case():
    model = trained_model()
    assert model.predict([8, 1]) == 1


def test_prediction_rejected_training_case():
    model = trained_model()
    assert model.predict([1, 0]) == 0


def test_new_client_approved():
    model = trained_model()
    assert model.predict([9, 1]) == 1


def test_new_client_rejected():
    model = trained_model()
    assert model.predict([2, 0]) == 0


def test_activation_function():
    model = Perceptron()
    assert model.activation(0) == 1
    assert model.activation(5) == 1
    assert model.activation(-1) == 0


def test_model_weights_change_after_training():
    model = Perceptron()
    initial_weights = model.weights.copy()
    model.train(training_data)
    assert model.weights != initial_weights
