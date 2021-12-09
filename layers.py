import numpy as np


class Layer:
    def __init__(self):
        self.input = None
        self.output = None


    # computes the output of the layer for a given input
    def forward_propagation(self, input):
        raise NotImplementedError


    # computes the delta-error over the input for a given delta-error over the
    # output and updates any parameter
    def backward_propagation(self, output_error, learning_rate):
        raise NotImplementedError


class FullyConnectedLayer(Layer):
    # in_size = number of input neurons
    # out_size = number of output neurons
    def __init__(self, in_size, out_size, activation = None, activation_deriv = None):
        self.weights = np.random.rand(in_size, out_size) - 0.5  # so to have few <0 and few >0
        self.bias = np.random.rand(1, out_size) - 0.5  # so to have few <0 and few >0
        self.activation = activation
        self.activation_deriv = activation_deriv


    def forward_propagation(self, input):
        self.input = input
        self.output = np.dot(self.input, self.weights) + self.bias
        if not(self.activation is None):
            self.activation_input = self.output
            self.output = self.activation(self.output)
        return self.output


    def backward_propagation(self, gradient, eta):
        if not(self.activation_deriv is None):
            gradient = np.multiply(self.activation_deriv(self.activation_input), gradient)
        weights_update = np.dot(self.input.T, gradient)

        self.weights -= eta * weights_update
        self.bias -= eta * gradient

        input_error = np.dot(gradient, self.weights.T)
        return input_error


class ActivationLayer(Layer):
    def __init__(self, activation, activation_deriv):
        self.activation = activation
        self.activation_deriv = activation_deriv


    def forward_propagation(self, input):
        self.input = input
        self.output = self.activation(self.input)
        return self.output


    def backward_propagation(self, gradient, eta):
        return np.multiply(self.activation_deriv(self.input), gradient)
