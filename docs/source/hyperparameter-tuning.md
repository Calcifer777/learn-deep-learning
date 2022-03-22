# Hyperparameter tuning

## Common issues

### Saturated neurons

Saturated neurons are insensitive to input changes because their derivative is 0 in the saturated region. This is one cause of the vanishing gradient problem where the backpropagated error is 0 and the weights are not adjusted.

### How to prevent saturated neurons

#### Weight initialization

Glorot initialization is recommended for tanh- and sigmoid-based neurons, and He initialization is recommended for ReLU-based neurons.

Both of these take the number of inputs into account, and Glorot initialization also takes the number of outputs into account. 

Both Glorot and He initialization exist in two flavors, one that is based on a uniform random
distribution (default for Glorot) and one that is based on a normal random distribution (default for He).

#### Input standardization

Standardizing the input data to be centered around 0 and with most values close to 0 will reduce the risk of saturating neurons from the start

#### Batch normalization

The idea is to normalize values inside of the network as well and thereby prevent hidden neurons from becoming saturated.

Batch normalization can be done either on the input of the activation function or on the output of the activation function

#### Output layer loss function: cross entropy loss

For sigmoid-based neurons, a cross-entropy activation function can prevent the vanishing gradient problem, as the derivative of this loss function varies more than the on of the MSE.

The cross-entropy loss function is not suitable for tanh-based neurons.

#### Hidden layers activation function choice: relu activation

The activation function should be nonlinear and is even often referred to as a nonlinearity instead of activation function.

An obvious benefit with the ReLU function is that it is cheap to compute. The implementation involves testing only whether the input value is less than 0, and if so, it is set to 0. 

A potential problem with the ReLU function is when a neuron starts off as being saturated in one direction due to a combination of how the weights and inputs happen to interact. Then that neuron will not participate in the network at all because its derivative is 0. In this situation, the neuron is said to be dead. 

One way to look at this is that using ReLUs gives the network the ability to remove certain connections altogether, and it thereby builds its own network topology, but it could also be that it accidentally kills neurons that could be useful if they had not happened to die.  

A variation of the ReLU function known as leaky ReLU - defined so its derivative is never 0 - can be used to prevent this problem.

## Variations of gradient descent

Momentum: in addition to computing a new gradient every iteration, the new gradient is combined with the gradient from the previous iteration

Adaptive learning rate: the learning rate adapts over time on the basis of historical values of the gradient

Gradient clipping (to prevent exploding gradients)

## Regularization techniques

### Early stopping

Useful when the errors show a U-shaped curve

### Weight decay

Add a penalty term to the loss function based on a function of the weights. Because the learning algorithm tries to minimize the loss function, this error term provides incentive to minimize the weights. This results in decreasing weights that do not contribute significantly to solving the general problem.

Flavors:
- L1 regularization: the penalty term is added to the sum of the weights
- L2 regularization: the penalty term is added to the squared sum of the weights

### Dropout

It is done by randomly removing a subset of the neurons from the network during training. The subset of removed neurons varies throughout each training epoch. 

The number of removed neurons (the dropout rate) is controlled by a parameter, where a common value is 20%.