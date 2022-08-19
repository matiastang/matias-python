<!--
 * @Author: matiastang
 * @Date: 2022-08-19 09:50:43
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-19 14:23:29
 * @FilePath: /matias-python/md/定时任务/APScheduler.md
 * @Description: APScheduler
-->
# APScheduler

[APScheduler](https://www.it610.com/article/1530077944314097664.htm)
[APScheduler](https://zhuanlan.zhihu.com/p/491679794)

## 调度器

BlockingScheduler : 阻塞式调度器：适用于只跑调度器的程序。
BackgroundScheduler: 后台调度器：适用于非阻塞的情况，调度器会在后台独立运行
AsyncIOScheduler : AsyncIO调度器，适用于应用使用AsnycIO的情况。
GeventScheduler : Gevent调度器，适用于应用通过Gevent的情况。
TornadoScheduler: Tornado调度器，适用于构建Tornado应用。
TwistedScheduler:Twisted调度器，适用于构建Twisted应用。
QtScheduler: Qt调度器，适用于构建Qt应用。

## 触发器
date:日期：触发任务运行的具体日期
interval: 间隔：触发任务运行的时间间隔
cron: 周期：触发任务运行的周期
2.2、触发器公共参数
id:启动任务的ID具有唯一性
name： 设置启动任务的名称
coalesce :当由于某种原因导致某个job积攒了好几次没有实际运行（比如说系统挂了5分钟后恢复，有一个任务是每分钟跑一次的，按道理说这5分钟内本来是“计划”运行5次的，但实际没有执行），如果coalesce为True，下次这个job被submit给executor时，只会执行1次，也就是最后这次，如果为False，那么会执行5次（不一定，因为还有其他条件，看后面misfire_grace_time的解释）
max_instance: 就是说同一个job同一时间最多有几个实例再跑，比如一个耗时10分钟的job，被指定每分钟运行1次，如果我们max_instance值为5，那么在第6~10分钟上，新的运行实例不会被执行，因为已经有5个实例在跑了
misfire_grace_time:设想和上述coalesce类似的场景，如果一个job本来14:00有一次执行，但是由于某种原因没有被调度上，现在14:01了，这个14:00的运行实例被提交时，会检查它预订运行的时间和当下时间的差值（这里是1分钟），大于我们设置的30秒限制，那么这个运行实例不会被执行。
replace_existing: 如果调度的job在一个持久化的存储器里，当初始化应用程序时，必须要为job定义一个显示的ID并使用replace_existing=True, 否则每次应用程序重启时都会得到那个job的一个新副本

### cron 触发器 在特定时间周期性地触发，和Linux crontab格式兼容。
它是功能最强大的触发器

参数	说明
year (int 或 str)	年，4位数字
month (int 或 str)	月 (范围1-12)
day (int 或 str)	日 (范围1-31)
week (int 或 str)	周 (范围1-53)
day_of_week (int 或 str)	周内第几天或者星期几 (范围0-6 或者 mon,tue,wed,thu,fri,sat,sun)
hour (int 或 str)	时 (范围0-23)
minute (int 或 str)	分 (范围0-59)
second (int 或 str)	秒 (范围0-59)
start_date (datetime 或 str)	最早开始日期(包含)
end_date (datetime 或 str)	最晚结束时间(包含)
timezone (datetime.tzinfo 或str)	指定时区
表达式	参数类型	描述
*	所有	通配符。例：minutes=*即每分钟触发
*/a	所有	可被a整除的通配符
a-b	所有	范围a-b触发
a-b/c	所有	范围a-b，且可被c整除时触发
xth y	日	第几个星期几触发。x为第几个，y为星期几
last x	日	一个月中，最后个星期几触发
last	日	一个月最后一天触发
x,y,z	所有	组合表达式，可以组合确定值或上方的表达式