# mycmdb
基于 python 3.7 + django 2.2.3 + AdminLTE-3.0.0-beta.1 实现的资产管理系统。基于 [刘江老师的教程](http://www.liujiangblog.com/course/django/116) ，练手项目，原教程功能简单，我在其基础上修改新增了不少功能，具体见 `screenshots` 文件夹中的效果预览图。目前功能非常不完善，我会持续更新，最终期望实现一个完整的运维系统（包含资产管理、批量执行、在线终端等）。


# 安装
```
# 安装相关库
pip install -r requirements.txt

# 运行
python manage.py runserver
```

访问首页：http://127.0.0.1:8000
账号： admin     密码：123456


# 效果
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/1.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/2.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/3.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/4.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/5.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/6.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/7.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/8.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/9.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/10.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/11.PNG?raw=true)
![效果](https://github.com/leffss/cmdb/blob/master/screenshots/12.PNG?raw=true)

# TODO
- [x] dashbord
- [x] 用户登陆
- [ ] 验证码登陆
- [x] 修改密码
- [x] 查看个人信息
- [ ] 新增用户
- [ ] 用户管理
- [ ] 权限管理
- [x] 查看资产列表
- [x] 查看资产详细
- [x] 删除资产
- [ ] 修改资产
- [ ] 新增硬件资产
- [x] 新增软件资产
- [ ] 搜索资产
- [ ] 自动更新资产信息
- [x] 用户日志审计
- [ ] 操作日志审计
- [ ] 所有表单数据验证
