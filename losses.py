import numpy as np


def MSE(labels, outputs):
    return np.mean(np.power(labels - outputs, 2))


def MSE_deriv(labels, outputs):
    return 2 * (outputs - labels)/np.size(labels)


def binary_crossentropy(labels, outputs):
    outputs_clipped = np.clip(outputs, 1e-15, 1-1e-15)  # avoids div by 0
    return np.mean((1 - labels) * np.log(1 - outputs_clipped) + labels * np.log(outputs_clipped))


def binary_crossentropy_deriv(labels, outputs):
    outputs_clipped = np.clip(outputs, 1e-15, 1-1e-15)  # avoids div by 0
    return np.mean(((1-labels)/(1-outputs_clipped) - labels/outputs_clipped))
