# Database

- [ ] [On optimistic methods for concurrency control](https://doi.org/10.1145/319566.319567)
- [ ] [Staring into the abyss: an evaluation of concurrency control with one thousand cores](https://doi.org/10.14778/2735508.2735511)
- [ ] [A timestamp-based concurrency control algorithm for heterogeneous distributed databases](https://doi.org/10.1109/ICCI.1993.315333)
- [ ] [FOEDUS: OLTP Engine for a Thousand Cores and NVRAM](https://doi.org/10.1145/2723372.2746480)
- [ ] [An Elastic Multi-Core Allocation Mechanism for Database Systems](https://doi.org/10.1109/ICDE.2018.00050)
- [ ] [Zen: a high-throughput log-free OLTP engine for non-volatile main memory](https://doi.org/10.14778/3446095.3446105)
- [ ] [NUMASK: High Performance Scalable Skip List for NUMA](https://doi.org/10.4230/LIPIcs.DISC.2018.18)
  - 新型跳表，利用 NUMA 性质，将跳表项分布在不同地方。
  - 本地缓存解决大部分读写，本地找不到就向外部设备查询。
- [ ] [The full story of 1000 cores: An examination of concurrency control on real(ly) large multi-socket hardware](https://doi.org/10.1007/s00778-022-00742-4)
  - 多种并发控制方法进行测试
- [ ] [ScaleDB: A Scalable, Asynchronous In-Memory Database](https://www.usenix.org/conference/osdi23/presentation/mehdi)
  - 使用写缓冲暂存需要更新的内容，并异步更新到存储和索引上。
  - 异步更新完成前，点查询可以靠写缓冲获得结果；范围查询 OCC 验证时出现非一致性问题则 Abort。