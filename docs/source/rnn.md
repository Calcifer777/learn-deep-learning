# Recurrent Neural Networks

RNNs try to solve the problem of predicting the next value or symbol in a sequence regardless of what the sequence represents

A simple form of RNN can be created by connecting the outputs from a fully connected layer to the inputs of that same layer.

The number of inputs (weights) to a single neuron is now a function of both the size of the input vector and the number of neurons in the layer. 

$h_t = tanh(W \cdot h_(t−1) + U x_t + b)$

In the feedforward network, we can have different weights for all connections, but in the recurrent layer, the weights need to be the same for each timestep. 

That is, just as convolutional layers have weight sharing within a layer, recurrent layers are like a feedforward network with weight sharing between layers. 

## Gated Units

### LSTM

LSTM is an example of the more general concept of gated units. 

Each LSTM cell has an internal state. At each timestep, this internal state gets updated. The new value is a weighted sum of the internal state from the previous timestep and the input activation function for the current timestep. 

The weights are dynamically controlled and are known as gates. The inputs to the input activation function result from a concatenation of the outputs from the previous layer ($x$) as well as the outputs from the current layer from the previous timestep ($h$), just as in a regular RNN. Finally, the output of the LSTM layer is computed by feeding the internal state through the output activation function and multiplying the result by another gate. All the gates are controlled by a concatenation of $x$ and $h$.

It consists of logistic sigmoid functions known as gates in addition to traditional activation functions. The concept of a gate allows for the ability to selectively decide when to remember a value.

It implements CEC to prevent the vanishing gradinet problem.

Constant error carousel (CEC): CEC results in a behavior similar to weight values of 1 during backpropagation.

Gates:
- remember gate (sigmoid):
- forget gate (sigmoid)
- output gate (sigmoid)

### GRU

The gated recurrent unit (GRU), simplifies the LSTM architecture. 

It is simpler in that it does not have an internal cell state; it has only a single activation function, and the forget and remember gates are combined into a single update gate