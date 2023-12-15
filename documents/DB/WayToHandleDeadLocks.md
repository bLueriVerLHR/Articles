# 死锁处理

- Wait-Die 会导致更多 rollback，但 rollback 的代价更低：被 rollback 的事务做过的事情比较少。
- Wound-Wait 导致的 rollback 较少，但 rollback 的代价更高：被 rollback 的事务做过的事情比较多。
- No-Wait，就是请求不到锁就回滚，不去做判断。现在的一般看法是，不等比等好，尤其是应用于分布式事务时。

