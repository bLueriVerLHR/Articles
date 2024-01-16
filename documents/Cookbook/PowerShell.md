# PowerShell

参考：

- [Windows PowerShell Cookbook](https://book.douban.com/subject/2081681/)

PowerShell 的命令（叫 cmdlets）使用相同的格式 `Verb-Noun` 的语法。

## 开机运行

- 通过将脚本的快捷方式放到 `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup` 中可以实现
- 使用 `win + r` 启动 `taskschd.msc` 创建任务计划
  - Task Scheduler 不能直接运行 `*.ps1`, 需要额外创建一个命令脚本 `*.cmd`

```
PowerShell -Command "Set-ExecutionPolicy Unrestricted" >> "%USERPROFILE%\Documents\log.txt" 2>&1
PowerShell %USERPROFILE%\Documents\script.ps1 >> "%USERPROFILE%\Documents\log.txt" 2>&1
```

第一行赋予管理员权限，第二行执行脚本。

## 仅查看执行效果

如果只想查看执行后的效果，而不是真的执行，可以使用 `-whatif` 参数。

```
> Rename-Item index.html index.htm -whatif
What if: Performing the operation "Rename File" on target "Item: D:\Projects\articles_share\index.html Destination: D:\Projects\articles_share\index.htm".
```

## 执行路径带空格的内容

使用单引号 `'` 将路径包围，以 `&` 开头执行命令。
例如：

```
> & 'C:\Program Files\Program\Program.exe' arguments
```

对于当前路径下的文件，可以以 `.\` 开头。

## 单引号内用单引号

使用连续两个单引号。
例如：

```
> ''''
'
```

## 查看指令相关的缩写

使用 `Get-Help` 查询指令，就可以看到它的 `ALIASES` 中有其缩写。
也可以使用 `Get-Alias` 也即 `gal`，并用参数指定指令以获取别名。

同时，为了获取指令参数的缩写，可以用如下脚本：

```
> (Get-Command New-TimeSpan).Parameters.Values | Select Name,Aliases
```

其中 `New-TimeSpan` 可以是任意其他指令。
