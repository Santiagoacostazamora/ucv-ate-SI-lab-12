"""Programa principal del laboratorio de perceptron simple."""

from src.dataset import training_data
from src.perceptron import Perceptron


def show_prediction(model, client_data):
    """Muestra la prediccion para un cliente."""
    prediction = model.predict(client_data)
    status = "Credito aprobado" if prediction == 1 else "Credito rechazado"

    print(f"Datos del cliente: {client_data}")
    print(f"Prediccion: {prediction}")
    print(f"Resultado: {status}")


def main():
    """Entrena el modelo y realiza predicciones de ejemplo."""
    model = Perceptron(learning_rate=0.1)
    model.train(training_data, epochs=20)

    print("Laboratorio UCV - Perceptron Simple")
    print("Pesos aprendidos:", model.weights)
    print("Bias aprendido:", model.bias)
    print("-" * 40)

    show_prediction(model, [9, 1])
    print("-" * 40)
    show_prediction(model, [2, 0])


if __name__ == "__main__":
    main()
