# Convolutional Neural Networks

## Description

In a convolutional layer, each neuron is associated with a square subset of the pixels in an image.  The region of pixels from which a neuron receives inputs is also known as its **receptive field**.

The number of weights in the neuron depends on the number of **channels** (or **feature map**) in the image (e.g. 3 channels for an input convolutional layer of an RGB images), and the dimension of the square covered by the neuron (a.k.a. **kernel size**).

Each channel corresponds to a specific feature of the input data of the convolutional layer. Simple features can be a vertical line, a horizontal line, a diagonal line, or a purple blob.
All the neurons within a single channel have identical weights (*weight sharing*).

The number of neurons in a convolutional layer depends on the image size, kernel size, and on the **stride**. The stride represents the pace of the convolution; that is, the number of steps between a neuron's receptive field and its successor.

Feature map: The grid of neurons in a single channel

Each neuron does not receive inputs from all pixels in the image. That is, it is not a fully connected network, but it is sparsely connected.

A convolutional layer has multiple output channels. 

A convolutional layer consists of multiple channels or feature maps. All
neurons within the same channel share weights.

When stacking multiple convolutional layers in a CNN, the feature maps for subsequent layers represent combinations of the features in the previous layer. We can envision a feature classifier that combines the outputs from multiple channels and thereby fire on more complex geometries

When the resolution (number of neurons per channel) of the first convolutional layer is lower than the resolution of the image, the receptive field of a neuron in the top convolutional layer is greater than that of a neuron in the bottom convolutional layer, even if they have the same kernel size. That arrangement enables neurons in the top layer to detect more complex features.

## Max Pooling

Max pooling is a way to reduce the size of a layer and can be used as an alternative to a large stride.

The max pooling operation combines a number of neurons, such as every 2×2 neurons, and outputs the max value of these four neurons. This reduces the number of outputs from a channel (and thereby from the entire layer) by a factor of four in the case of 2×2 pooling but without any weights that need to be learned. The effect of this is that the spatial resolution is decreased; that is, we no longer know as accurately where in an image a specific feature was found but we still know that the feature was present in the region that pooling was applied to.

## CNN properties

Translation invariance: In the case of object classification in an image, this means that even if an object is shifted (translated) horizontally or vertically to a different position in the image, the
network will still be able to recognize it

Translation invariance is achieved by employing weight sharing between neurons as well as making them sparsely connected.

Sparse connections imply fewer computations per neuron (because each neuron is not connected to all neurons in the preceding layer). 

Weight sharing implies fewer unique, but not fewer total, weights per layer. The number of unique weights in a convolutional layer is given by: 
```math
num_channels_in * kernel_size * num_channels_out
```

Therefore, the benefit of using a convolutional layer in terms of reducing the number of weights is not as significant for the layers deep into the network. The reasons for these effects are the following: The width and the height of the layers tend to decrease deeper into the network, which reduces the number of weights for a fully connected subsequent layer but does not affect a convolutional layer. Further, layers deep inside the network often have many more channels than the three color channels from the input image