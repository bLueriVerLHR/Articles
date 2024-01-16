# 文章

非常欢迎在 [Issue](https://github.com/bLueriVerLHR/articles_share/issues) 中提出疑问，
或者提交 [PR](https://github.com/bLueriVerLHR/articles_share/pulls) 一起完善文档。

| Abbreviation | Meaning                           |
| ------------ | --------------------------------- |
| CaPL         | Compiler and Programming Language |
| MLSys        | Machine Learning System           |

``` json
{
  "editor.fontFamily": "'Sarasa Mono SC', monospace"
}
```

``` plantuml
@startmindmap
* Papers
  * Blog
    * Leaky Address Masking: Exploiting Unmasked Spectre Gadgets with Noncanonical Address Translation
      * https://download.vusec.net/papers/slam_sp24.pdf
      * https://www.vusec.net/projects/slam/
    * Why ACPI?
      * https://mjg59.dreamwidth.org/68350.html
  * MLSys
    * MaxK-GNN: Towards Theoretical Speed Limits for Accelerating Graph Neural Networks Training
      * https://doi.org/10.48550/arXiv.2312.08656
      * 提出了非线性函数 MaxK 和对应的 Compressed Balanced Sparse Row（CBSR）用于存储结果特征矩阵的数据与索引
      * 基于 CBSR 数据结构设计了全新的内核函数
        * 在向前传播中设计了 Sparse Matrix-Matrix Multiplication（SpGEMM）内核函数
        * 在向后传播中设计了 Sampled Sparse Matrix Dense Matrix Multiplication（SSpMM）内核函数
    * FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU
      * https://doi.org/10.48550/arXiv.2303.06865
      * 将分散的 batch 重新合并成一组，块内的 batch 以每次都共享同一层权重，完成一层权重后再进行下一层计算的 layer-by-layer 方式计算
        * FlexGen 目的在提高吞吐，故以延迟作为代价提高吞吐
        * 现有系统，基本上是 batch-by-batch 每次优先处理完一个 batch 再处理下一个 batch，吞吐不是很高
      * 提出一个推理时内存峰值估算方法
    * GNNFlow: A Distributed Framework for Continuous Temporal GNN Learning on Dynamic Graphs
      * https://doi.org/10.48550/arXiv.2311.17410
      * DTDG、CTDG 两种动态图
        * DTDG 离散时间动态图，离散快照，会丢失连续性
        * CTDG 连续时间动态图，带连续时间
      * Motivation
        * 现有数据结构下，动态图的重构和划分开销大
          * 严格时间顺序，链表形式的顺序存取
        * 现有系统关于动态图特性的优化不足
      * Block-Based Neighborhood Storage
        * 采样算法 Temporal Neighborhood Sampling
      * Feature Cache on GPUs
        * 在 GPU 存储上添加 Cache 提高特征获取速度
    * SpotServe: Serving Generative Large Language Models on Preemptible Instances
      * https://doi.org/10.48550/arXiv.2311.15566
      * 使用 Spot Instance 部署大语言模型推理服务
      * 完成了动态重并行化，低成本实例迁移和对 Grace Period 的高效利用
        * 搜索可行配置空间找到最佳配置，配置在离线期间计算性能情况
        * 以 Token 为单位迁移实例，无需从头开始推理
    * Tango: rethinking quantization for graph neural network training on GPUs
      * https://doi.org/10.48550/arXiv.2308.00890
    * GraNNDis: Efficient Unified Distributed Training Framework for Deep GNNs on Large Clusters
      * https://doi.org/10.48550/arXiv.2311.06837
    * cuDNN: Efficient Primitives for Deep Learning
      * https://doi.org/10.48550/arXiv.1410.0759
    * Going deeper with convolutions
      * https://doi.org/10.1109/CVPR.2015.7298594
    * Fast Algorithms for Convolutional Neural Networks
      * https://doi.org/10.1109/CVPR.2016.435
    * TensorFlow: A system for large-scale machine learning
      * https://dl.acm.org/doi/10.5555/3026877.3026899
    * PyTorch: an imperative style, high-performance deep learning library
      * https://dl.acm.org/doi/10.5555/3454287.3455008
    * TVM: an automated end-to-end optimizing compiler for deep learning
      * https://dl.acm.org/doi/10.5555/3291168.3291211
    * nGraph-HE: a graph compiler for deep learning on homomorphically encrypted data
      * https://doi.org/10.1145/3310273.3323047
    * Learning both weights and connections for efficient neural networks
      * https://dl.acm.org/doi/10.5555/2969239.2969366
    * Cambricon-X: An accelerator for sparse neural networks
      * https://doi.org/10.1109/MICRO.2016.7783723
    * SCNN: An accelerator for compressed-sparse convolutional neural networks
      * https://doi.org/10.1145/3079856.3080254
    * Sparse Tensor Core: Algorithm and Hardware Co-Design for Vector-wise Sparse Neural Networks on Modern GPUs
      * https://doi.org/10.1145/3352460.3358269
    * DianNao: a small-footprint high-throughput accelerator for ubiquitous machine-learning
      * https://doi.org/10.1145/2654822.2541967
    * Balanced sparsity for efficient DNN inference on GPU
      * https://doi.org/10.1609/aaai.v33i01.33015676
    * MLPerf: An Industry Standard Benchmark Suite for Machine Learning Performance
      * https://doi.org/10.1109/MM.2020.2974843
    * Learning convolutional neural networks for graphs
      * https://doi.org/10.1109/MM.2020.2974843
    * Lectures on Spectral Graph Theory
      * https://mathweb.ucsd.edu/~fan/cbms.pdf
    * Spectral Graph Theory
      * https://mathweb.ucsd.edu/~fan/research/revised.html
    * Multistep speed prediction on traffic networks: A deep learning approach considering spatio-temporal dependencies
      * https://doi.org/10.1016/j.trc.2019.05.039
  * Database
    * NUMASK: High Performance Scalable Skip List for NUMA
      * https://doi.org/10.4230/LIPIcs.DISC.2018.18
      * 新型跳表，利用 NUMA 性质，将跳表项分布在不同地方
      * 本地缓存解决大部分读写，本地找不到就向外部设备查询
    * The full story of 1000 cores: An examination of concurrency control on real(ly) large multi-socket hardware
      * https://doi.org/10.1007/s00778-022-00742-4
      * 多种并发控制方法进行测试
    * ScaleDB: A Scalable, Asynchronous In-Memory Database
      * https://www.usenix.org/conference/osdi23/presentation/mehdi
      * 使用写缓冲暂存需要更新的内容，并异步更新到存储和索引上
      * 异步更新完成前，点查询可以靠写缓冲获得结果；范围查询 OCC 验证时出现非一致性问题则 Abort
    * On optimistic methods for concurrency control
      * https://doi.org/10.1145/319566.319567
    * Staring into the abyss: an evaluation of concurrency control with one thousand cores
      * https://doi.org/10.14778/2735508.2735511
    * A timestamp-based concurrency control algorithm for heterogeneous distributed databases
      * https://doi.org/10.1109/ICCI.1993.315333
    * FOEDUS: OLTP Engine for a Thousand Cores and NVRAM
      * https://doi.org/10.1145/2723372.2746480
    * An Elastic Multi-Core Allocation Mechanism for Database Systems
      * https://doi.org/10.1109/ICDE.2018.00050
    * Zen: a high-throughput log-free OLTP engine for non-volatile main memory
      * https://doi.org/10.14778/3446095.3446105
@endmindmap
```