"""Implementacion desde cero de un perceptron simple."""


class Perceptron:
    """Perceptron simple para clasificacion binaria."""

    def __init__(self, learning_rate=0.1):
        self.weights = [0.0, 0.0]
        self.bias = 0.0
        self.learning_rate = learning_rate

    def activation(self, value):
        """Funcion escalon: retorna 1 si el valor es mayor o igual a 0."""
        return 1 if value >= 0 else 0

    def predict(self, inputs):
        """Realiza una prediccion usando pesos, entradas y bias."""
        total = self.bias

        for index, input_value in enumerate(inputs):
            total += input_value * self.weights[index]

        return self.activation(total)

    def train(self, training_data, epochs=20):
        """Entrena el perceptron ajustando pesos y bias."""
        for _ in range(epochs):
            for inputs, expected in training_data:
                prediction = self.predict(inputs)
                error = expected - prediction

                for index, input_value in enumerate(inputs):
                    self.weights[index] += self.learning_rate * error * input_value

                self.bias += self.learning_rate * error
