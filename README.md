# snakflake

- 一个多进程安全的时间戳计数器

- 雪花ID 生成器,可被多进程使用

增加ID

#### 集群环境中如何自动分配机器ID


从查询的资料，大致有这些方案，优劣不一

- 利用数据库自增ID
    
    这个应该是常规后端开发来说，最容易实现的：通过IP 进行hash 然后做唯一查询or插入，以自增ID 做机器ID。但缺点是，集群服务，以docker 这类的容器部署为例，是会频繁更新的，很容易发生超出机器id 掩码上限？

- zookeeper 和redis
    
    这里主要是zookeeper，是利用持久存储。从介绍看，直观感受是，在IP 频繁变化时（同上，docker 集群部署），很容易超出上限。
    
    因为都没有一个对失效IP占用ID 的循环利用的机制。
    
- redis 枪占模式
    
    hash ip后,除以1024(掩码)得到整数,然后枪占KEY_+index 进行枪占。抢占成功则停止，失败则index+1 继续。
    
    原文中提到在程序结束时删除抢占的index，但是程序如何正常结束呢？
    
    所以在想，以固定间隔时间更新缓存。每次更新缓存都设置一个过期时间？过期时间大于更新时间
    
    那么这种缓存更新的策略，是否耗费资源？


