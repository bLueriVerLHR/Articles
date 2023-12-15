# Machine Learning System

机器学习部分，目前主要关注 `大语言模型` 和 `图神经网络` 这两个方向。

该分块非常的宽泛，但主要围绕机器学习这一个主题，对任何系统有关的，软硬件知识进行集中。

正在阅读的论文

- [ ] [Tango: rethinking quantization for graph neural network training on GPUs](https://doi.org/10.48550/arXiv.2308.00890)
- [ ] [GraNNDis: Efficient Unified Distributed Training Framework for Deep GNNs on Large Clusters](https://doi.org/10.48550/arXiv.2311.06837)
- [ ] [cuDNN: Efficient Primitives for Deep Learning](https://doi.org/10.48550/arXiv.1410.0759)
- [ ] [Going deeper with convolutions](https://doi.org/10.1109/CVPR.2015.7298594)
- [ ] [Fast Algorithms for Convolutional Neural Networks](https://doi.org/10.1109/CVPR.2016.435)
- [ ] [TensorFlow: A system for large-scale machine learning](https://dl.acm.org/doi/10.5555/3026877.3026899)
- [ ] [PyTorch: an imperative style, high-performance deep learning library](https://dl.acm.org/doi/10.5555/3454287.3455008)
- [ ] [TVM: an automated end-to-end optimizing compiler for deep learning](https://dl.acm.org/doi/10.5555/3291168.3291211)
- [ ] [nGraph-HE: a graph compiler for deep learning on homomorphically encrypted data](https://doi.org/10.1145/3310273.3323047)
- [ ] [Learning both weights and connections for efficient neural networks](https://dl.acm.org/doi/10.5555/2969239.2969366)
- [ ] [Cambricon-X: An accelerator for sparse neural networks](https://doi.org/10.1109/MICRO.2016.7783723)
- [ ] [SCNN: An accelerator for compressed-sparse convolutional neural networks](https://doi.org/10.1145/3079856.3080254)
- [ ] [Sparse Tensor Core: Algorithm and Hardware Co-Design for Vector-wise Sparse Neural Networks on Modern GPUs](https://doi.org/10.1145/3352460.3358269)
- [ ] [DianNao: a small-footprint high-throughput accelerator for ubiquitous machine-learning](https://doi.org/10.1145/2654822.2541967)
- [ ] [Balanced sparsity for efficient DNN inference on GPU](https://doi.org/10.1609/aaai.v33i01.33015676)
- [ ] [MLPerf: An Industry Standard Benchmark Suite for Machine Learning Performance](https://doi.org/10.1109/MM.2020.2974843)
- [ ] [Learning convolutional neural networks for graphs](https://dl.acm.org/doi/10.5555/3045390.3045603)
- [ ] [Lectures on Spectral Graph Theory](https://mathweb.ucsd.edu/~fan/cbms.pdf)
- [ ] [SPECTRAL GRAPH THEORY](https://mathweb.ucsd.edu/~fan/research/revised.html)
- [ ] [Multistep speed prediction on traffic networks: A deep learning approach considering spatio-temporal dependencies](https://doi.org/10.1016/j.trc.2019.05.039)
- [ ] [GNNFlow: A Distributed Framework for Continuous Temporal GNN Learning on Dynamic Graphs](https://doi.org/10.48550/arXiv.2311.17410)
  - DTDG、CTDG 两种动态图
    - DTDG 离散时间动态图，离散快照，会丢失连续性
    - CTDG 连续时间动态图，带连续时间
  - Motivation
    - 现有数据结构下，动态图的重构和划分开销大
      - 严格时间顺序，链表形式的顺序存取
    - 现有系统关于动态图特性的优化不足
  - Block-Based Neighborhood Storage
    - 采样算法 Temporal Neighborhood Sampling
  - Feature Cache on GPUs
    - 在 GPU 存储上添加 Cache 提高特征获取速度