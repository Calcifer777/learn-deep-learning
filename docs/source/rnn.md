# Recurrent Neural Networks

RNNs try to solve the problem of predicting the next value or symbol in a sequence regardless of what the sequence represents

A simple form of RNN can be created by connecting the outputs from a fully connected layer to the inputs of that same layer.

The number of inputs (weights) to a single neuron is now a function of both the size of the input vector and the number of neurons in the layer. 

$h_t = tanh(W \cdot h_(t−1) + U x_t + b)$

In the feedforward network, we can have different weights for all connections, but in the recurrent layer, the weights need to be the same for each timestep. 

That is, just as convolutional layers have weight sharing within a layer, recurrent layers are like a feedforward network with weight sharing between layers. 