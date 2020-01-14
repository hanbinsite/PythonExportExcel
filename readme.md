1. 使用版本 python 3
2. 安装插件   openpyxl  、  smtplib  、  pymysql  、 redis
3. 执行样例   python Run.py

# 功能说明
1. 通过Run.py 内接收redis队列消息，通知本程序有导出数据需求，消息内容为任务id  
2. 通过任务id，读取数据库中保存的任务内容: sql语句、接收结果邮箱、excel表格标题
3. 进行sql查询之前，可以根据对应字符串进行替换成相应参数

# 任务数据库创建语句
CREATE TABLE `tasks` (  
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT COMMENT '主键',      
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '任务名称',   
  `type` enum('1','2') COLLATE utf8mb4_general_ci NOT NULL DEFAULT '2' COMMENT '类型:1=定时任务,2=单次任务',  
  `startTime` int(11) NOT NULL DEFAULT '0' COMMENT '任务开始时间',  
  `endTime` int(11) NOT NULL DEFAULT '0' COMMENT '任务结束时间',  
  `execTime` time DEFAULT NULL COMMENT '定时执行任务时间(hh:ii:ss)',  
  `execlTitle` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'excel标题',  
  `sql` varchar(2000) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '执行sql语句',  
  `email` text COLLATE utf8mb4_general_ci COMMENT '接收邮箱，多个邮箱以,分隔',  
  `lastTime` datetime DEFAULT NULL COMMENT '最后执行日期',  
  `status` enum('0','1') COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0' COMMENT '状态:0=保存,1=启用',  
  `created_at` datetime DEFAULT NULL COMMENT '创建时间',  
  `updated_at` datetime DEFAULT NULL COMMENT '更新时间',  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;  

# 保存数据记录内容要求
1. excel标题,以英文逗号分隔  id,姓名,密码,账号,手机号  
2. sql,因为需要对应导出标题，所以 字段 需要使用 as 对应到 excel标题  :  SELECT `id`,`name` as '姓名', `pwd` as '密码', `username` as '账号', `mobile` as '手机号' FROM `user`  
3. email  多个邮箱以英文逗号进行隔开 : 123@123.com,456@456.com

# 配置部分 configs 文件夹
1. database.py   数据库配置，可以配置多个数据库，获取的时候，传对应的名称即可
2. mail.py 发送推送邮件的邮箱，需要根据不同的服务提供商设置host、port
3. filesystem.py 文件保存路径配置,暂未使用  
4. redis.py  redis对应配置，在接收队列时使用
5. replace.py  需要替换的字符串配置，暂未使用
6. globaldata.py 全局使用变量，避免多个文件参数无法接收 

### 联系邮箱  1837261009@qq.com