# Leaky Address Masking

Linear Address Masking（LAM），由 Intel 宣布的特性，用于让处理器在解引用一个 64-bit 指针之前使用掩码忽视一些高位数据。
该特性类似于 AMD 的 Upper Address Ignore（UAI）和 ARM 的 Top-Byte Ignore（TBI），允许软件可以利用未被翻译的高位地址值来存储元数据。

- LAM: <https://lwn.net/Articles/902094/>
- UAI: <https://lwn.net/Articles/888914/>
- TBI: <https://www.linaro.org/blog/top-byte-ignore-for-fun-and-memory-savings/>

部分研究人员想出了一个办法，称为 SLAM，以利用这个特性来绕过指针检查，带来了新的一组 Spectre 攻击方法。

- SLAM: <https://www.vusec.net/projects/slam/>


