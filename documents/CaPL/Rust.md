# Rust

参考：

- [The Rust Programming Language](https://doc.rust-lang.org/stable/book)

# 概述

Rust 是一种 **预编译静态类型**（Ahead-of-Time Compiled）语言。

## 创建项目

Cargo 是 Rust 的构建系统和包管理器。
它可以用于构建代码、下载依赖库并编译这些库。

> 依赖（Dependencies）是指代码所需要的库。

使用 Cargo 创建一个名称为 `hello` 的项目：

```
$ cargo new hello
$ cd hello
```

第一行命令新建了名为 `hello` 的目录和项目。在 `hello` 目录下，Cargo 生成了两个文件和一个目录：

- 一个 `Cargo.toml` 文件
- 一个 `src` 目录
- 一个位于 `src` 目录中的 `main.rs` 文件。

同时 Cargo 会在 `hello` 目录初始化了一个 git 仓库，以及一个 `.gitignore` 文件。

`Cargo.toml` 文件使用 TOML（Tom's Obvious, Minimal Language）格式，这是 Cargo 配置文件的格式。
自动生成的文件内容如下：

``` toml
[package]
name = "hello"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]

```

第一行，`[package]`，是一个片段（Section）标题，表明下面的语句用来配置一个包。
随着在这个文件增加更多的信息，还将增加其他片段。

接下来的三行设置了 Cargo 编译程序所需的配置：

- 项目的名称
- 项目的版本
- 要使用的 Rust 版本

最后一行，`[dependencies]`，是罗列项目依赖的片段的开始。
在 Rust 中，代码包被称为 crates。

Cargo 期望源文件存放在 `src` 目录中。
项目根目录只存放 `README`、`license` 信息、配置文件和其他跟代码无关的文件。

## 构建并运行项目

在 Cargo 生成的项目目录下运行如下命令来构建项目：

```
$ cargo build
   Compiling hello v0.1.0 (file:///hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
```

这个命令会创建一个可执行文件 `target/debug/hello`，而不是放在目前目录下。
由于默认的构建方法是调试构建（Debug Build），Cargo 会将可执行文件放在名为 `debug` 的目录中。

首次运行 `cargo build` 时，也会使 Cargo 在项目根目录创建一个新文件：`Cargo.lock`，这个文件记录项目依赖的实际版本。
程序员应该永远也不需要碰这个文件，让 Cargo 处理它就行了。

除了 `cargo build` 先编译后手动运行，也可以使用 `cargo run` 在一个命令中同时编译并运行生成的可执行文件：

```
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/hello`
Hello, world!
```

注意这一次并没有出现表明 Cargo 正在编译 `hello` 的输出。
Cargo 发现文件并没有被改变，所以它并没有重新编译，而是直接运行了可执行文件。

Cargo 还提供了一个叫 `cargo check` 的命令。
该命令快速检查代码确保其可以编译，但并不产生可执行文件：

```
$ cargo check
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
```

回顾下已学习的 Cargo 内容：

- 使用 `cargo new` 创建项目
- 使用 `cargo build` 构建项目
- 使用 `cargo run` 一步构建并运行项目
- 使用 `cargo check` 在不生成二进制文件的情况下构建项目来检查错误
- 有别于将构建结果放在与源码相同的目录，Cargo 会将其放到 `target/debug` 目录

# 基本程序知识

`main` 函数是程序的入口点。

``` rust
fn main() {
    // ...
}
```

`fn` 语法声明了一个新函数，小括号 `()` 表明没有参数，大括号 `{}` 包围函数体。
使用 `//` 作为行注释开始，使用 `/*` 和 `*/` 包围块注释。

默认情况下，Rust 设定了若干个会自动导入到每个程序作用域中的标准库内容，这组内容被称为 **预导入**（Preclude）内容。
如果你需要的类型不在预导入内容中，就必须使用 `use` 语句显式地将其引入作用域。
比如 `std` 下的 `io` 库：

``` rust
use std::io;
```

创建变量使用 `let`，使用等号（=）告诉 Rust 想将某个值 **绑定** 在变量上。
创建的变量默认是不可变的，如果期望变量可变，需要再加上 `mut`：

``` rust
let app = 20; // 不可变
let mut ban = 10; // 可变

app = 10; // -> error
ban = 20; // -> pass
```

接下来，创建一个 `String` 变量，`String` 是一个标准库提供的字符串类型，它是 UTF-8 编码的 **可增长** 文本块。

``` rust
let mut msg = String::new();
```

`::new` 那一行的 `::` 语法表明 `new` 是 `String` 类型的一个 **关联函数**（Associated Function）。
关联函数是 **针对类型** 实现的，在这个例子中是 `String`，而不是 `String` 的某个特定实例。
一些语言中把它称为 **静态方法**（Static Method）。

`new` 函数创建了一个新的空字符串，能够发现很多类型上有 `new` 函数，因为它是创建类型实例的惯用函数名。

总的来说，`let mut msg = String::new();` 这一行创建了一个可变变量，当前它绑定到一个新的 `String` 空实例上。

接下来我们尝试通过标准输入，获取输出到 `msg` 上。
编写如下代码：

``` rust
use std::io;

fn main() {
    let mut msg = String::new();
    io::stdin()
        .read_line(&mut msg)
        .expect("Failed to read line");
    println!("{msg}");
}
```

在程序的第一行使用 `use std::io;` 从标准库中引入了输入/输出功能。
现在调用 `io` 库中的函数 `stdin` 函数读取标准输入中的内容。
如果没有第一行的 `use`，依然可以通过 `std::io::stdin` 使用函数。

`stdin` 函数返回一个 ` std::io::Stdin` 的实例，这代表终端标准输入句柄的类型。

代码的下一部分，`.read_line(&mut msg)`，调用 `read_line` 方法从标准输入句柄获取用户输入。
同时将 `&mut msg` 作为参数传递给 `read_line()` 函数，让其将用户输入储存到这个字符串中。
`read_line` 的工作是，无论用户在标准输入中键入什么内容（包含换行符），都将其追加（**不会覆盖其原有内容**）到一个字符串中，因此它需要字符串作为参数。
这个字符串参数应该是 **可变的**，以便 `read_line` 将用户输入附加上去。

`&` 表示这个参数是一个 **引用**（Reference），它允许多处代码访问同一处数据，而无需在内存中多次拷贝。
引用是一个复杂的特性，Rust 的一个主要优势就是安全而简单的操纵引用。

