# 寄存器分配

## 控制流图

在讨论寄存器分配优化的时候，最常用的 ir 是控制流图（Control Flow Graph，CFG）。
在不引起混淆的时候，也会用流图称呼控制流图。

做如下定义：

```
P   :   F+                      # 程序 P 由若干函数 F 构成
    ;
F   :   f(x*) { B+ }            # 函数由若干形式参数 x 和函数体构成
    ;                           # 函数体由若干基本块 B 构成
B   :   L: S* J                 # 基本块由标签 L，包含的若干语句 S 和跳转语句 J 构成
    ;
S   :   y = f(x*)               # 语句可以是函数调用，需要若干参数 x 的加载，状态保存和跳转
    |   y = t(x*)               # 语句可以是一条指令，需要若干数据 x 参与
    |   [y] = x                 # 语句可以是一个数据存储操作，意思是将 x 上的值，保存到 y 上的值作为地址所指向的存储器位置上
    |   y = [x]                 # 语句可以是一个数据加载操作，意思是将 x 上的值作为地址所指向的存储器位置上的值加载到 y 上
    |   y = x                   # 语句可以是一个数据移动操作
    ;
J   :   goto L                  # 跳转可以一个无条件跳转
    |   if x then L else L      # 跳转可以是有条件跳转。当 x 为 true，前往 then 对应的标签 L 的位置；当 x 为 false，前往 else 对应的标签 L 的位置。
    |   return x                # 跳转可以是函数返回值，可能有 x 可能没有 x。
    ;
```

关于流图，还有几条补充规则：

1. 函数包含唯一一个入口基本块；函数必须包含至少一个退出块，退出块最后一条指令必定是 return。
2. 每个基本块 B 单入单出，即执行流必须从基本块第一条指令进入，最后一条指令跳出，不得从中间进入或者从中间跳出。
3. 函数可以有无限的形式参数或局部变量。
4. 可以对基本控制流进行拓展以增加新的功能。

> 函数调用作为一组操作，本质可以看作一条复杂的指令。
> 
> 当 `inline` 技术足够好，就可以将函数完全内联在程序内，成为一组可以优化的基本块。

一般的，程序的控制流可以被表示为以基本块 B 为节点，跳转 J 的方向为有向边的有向图 $G$。
其中：

$$
G = (V, E)
$$

$$
V = \{ v_1, v_2, \dots, v_n \}
$$

$$
E = \{(x, y) | x, y \in V \}
$$

对任意给定节点基本块 $b$，我们记该节点的度为 $degree(b)$，该节点所有邻接点构成的集合为 $adj(b)$。

接下来按照如上的定义，在程序从高级语言的结构化形式转换成线性的非结构化形式之后，需要通过算法才能转换成流图。
可以使用如下算法进行：

```
fn mark_leaders:
  create iterator it on unstructured control flow
  while it not reach end:
    if *it is J:
      mark *next(it) and targets of J as leader
    it = next(it)

fn create_basic_blocks:
  create iterator it on unstructured control flow
  let set<B> to hold basic blocks
  while it not reach end:
    let B as current basic block
    while it not reach end && *it is not marked as leader:
      add *it to B
      it = next(it)
    
    if last statement of B is not return-like:
      build jump edge from B to targets
      # note that target block may not have been built yet
      # we can use targets' leader as destination or use other method

    add B to set<B>
    it = next(it)
  return set<B>

fn build_cfg:
  let unstructured control flow as ucf
  do mark_leaders on ucf
  do create_basic_blocks on ucf get set<B>
  return set<B>
```

上述三个算法中，iterator 是用于遍历非结构化控制流的迭代器，具体实现依照语言而定。

第一个算法会给非结构化控制流中，未来会作为基本块的第一条指令设置为 leader。

第二个算法，则是将两个被标记为 leader 的语句 `a` 和 `b` 之间 `[a, b)` 的语句组成一个基本块，最后再构建出跳转边。
跳转目的地的基本块不一定已经创建出来了，所以需要额外使用手段对基本块进行标号。

算法 `build_cfg` 在控制流上完成后，就可以将非结构化控制流转换成控制流图了。

## 活跃分析

对程序中，值以及值可能的流动进行的一类分析被称为 **数据流分析**（data-flow analysis）

一般的，我们可以定义对变量的读为 `use`，对变量的写为 `def`。
结构良好的程序，在遇到 `use` 前，一定会遇到一个 `def` 点作为初始化。
如果没有遇到对应的 `def` 点，可以认为该变量未初始化就被使用。

我们可以对语句 S 的各种形式定义 `use` 集合和 `def` 集合：

```
use(y = t(x*))  = { x* }
use(y = f(x*))  = { x* }
use([y] = x)    = { x, y }
use(y = [x])    = { x }
use(y = x)      = { x }

def(y = t(x*))  = { y }
def(y = f(x*))  = { y }
def([y] = x)    = {   }
def(y = [x])    = { y }
def(y = x)      = { y }
```

对于跳转 J，我们也可以得到其对应的 `use` 集合和 `def` 集合：

```
use(goto L)             = {   }
use(if x then L else L) = { x }
use(return x)           = { x }

def(J)                  = {   }
```

对于给定的变量 x，假定从其中一个定义点 p 到使用点 q 的路径是 l。
如果对于该路径 l 上的任意点 r，r 和 q 之间没有对变量 x 的其他定义，则我们称变量 x 在程序点 r 上是活跃的（live）。
分析变量活跃点的程序分析被称为活跃分析（liveness analysis）。

## 图着色

## 线性扫描

## 线性规划

## PBQP 分配