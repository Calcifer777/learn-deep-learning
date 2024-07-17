# TiniML and Efficient Deep Learning Computing

## Overview

### Layers

| Layer           | Inputs               | Outputs              | Weights                   |
| --------------- | -------------------- | -------------------- | ------------------------- |
| Fully connected | $(n, c_i)$           | $(n, c_o)$           | $W: (c_o, c_i)$           |
| 1D Convolution  | $(n, c_i, w_i)$      | $(n, c_o, w_o)$      | $W: (c_o, c_i, k_w)$      |
| 2D Convolution  | $(n, c_i, w_i, h_i)$ | $(n, c_o, w_o, h_o)$ | $W: (c_o, c_i, k_w, k_h)$ |
| Pooling         |                      |                      | N/D                       |
| Normalization   |                      |                      | $\mu, \sigma$             |
| Activation      |                      |                      |                           |

### Convolution layer

Receptive field increases with the number of layers: $L \cdot (k-1) + 1$

Output size: $o_w = \frac{i_w + 2*{padding}_w - k_w}{stride} + 1$

_Grouped convolution_: uses multiple kernels for each group of channels. For $g$
groups, the number of parameters is reduced by g.

_Depth-wise convolution_: grouped convolution in which the number of groups is the
same as the number of channels

## Efficiency metrics

Memory:

- number of parameters
- model size: num parameters x bit width
- total / peak number of activations

Computation:

- MAC (multiply and aggregate)
  - Matrix multiplication: ($A: (m, n), B: (n, k)$) m x n x k MACs
- FLOP
- FLOPS
- OP
- OPS

Time:

- latency
  - how much time it takes to complete a task
  - can be reduced overlapping data movement and computation operations
- throughput: the rate at which data is processed

Greater filter sizes increase the number of parameters, but reduce the

## Efficient Inference

### Pruning and Sparsity

#### Granularities

For convolutional layers:

- fine-grained
- pattern-based
- vector-level
- kernel-level
- channel-level

#### Criteria

- Magnitude ($L1$ / $L2$ / $L_p$)
- Scaling
- Second-order
- Percentage-of-zero
- Regression-based: minimize reconstruction error of the corresponding layer's
  output

#### How to choose the pruning ratio

- Analyze the sensitivity of pruning each layer to the model accuracy
- NetAdapt: iteratively find the per-layer pruning ratio to meet a global
  resource constraing (e.g. latency, energy, ...)

#### Finetuning pruned models

- Learning rate is 10%-1% of the origiral learning rate
- When doing iterative pruning
  - each pruning stage is followed by a FT stage
  - Add regularization (L1, L2) to penalize non-zero parameters or encourage
    smaller parameters
- Iterative magnitude pruning (lottery ticket hypothesis)

#### Resources

**Tutorials**

- [Torch Pruning Tutorial](https://pytorch.org/tutorials/intermediate/pruning_tutorial.html)
- [Deepgram Pruning Tutorial](https://deepgram.com/learn/model-pruning-distillation-and-quantization-part-1)

**Libraries**

- [Intel Neural Compressor](https://github.com/intel/neural-compressor)
- [MIT AMC](https://github.com/mit-han-lab/amc)
- [Torch Pruning](https://github.com/VainF/Torch-Pruning)

### Quantization

#### Resources

- [Torch Dynamic Quantization Tutorial](https://pytorch.org/tutorials/advanced/dynamic_quantization_tutorial.html)

### Neural Architecture search

### Knowledge Distillation
