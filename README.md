---
title: M@RS Mail开发日志
tags: Python,Email,软件课设,pyqt4
grammar_cjkRuby: true
---

# MarsMail
废话不多说，先上图，看效果图：

- 主界面

![](http://opn1dyhml.bkt.clouddn.com/17-10-27/26456554.jpg)

- 通讯簿

![](http://opn1dyhml.bkt.clouddn.com/17-10-27/16696875.jpg)

- 关于

![](http://opn1dyhml.bkt.clouddn.com/17-10-27/88667824.jpg)

- 写信

![](http://opn1dyhml.bkt.clouddn.com/17-10-27/6013727.jpg)


一直想写一个ReadMe，但是总感觉耽误时间就拖着。。。虽然现在也觉得耽误时间，所有就稍微写一丢丢。
这个项目算是我有史以来最大的项目了吧
23333能力有限只能写些小项目~~

这个项目是一个邮件管理软件，用Python实现，界面使用的是pyqt，具体环境如下
> Python3.4

> Pyqt4

> eric 用于界面设计的IDE，超赞，将逻辑和界面划分开来，耦合性降低

> 具体使用到的包以后再说明吧


今天就写到这吧
2016.12.28 14:39 还有14天放假。


----------


------------华丽分割线----------------
2017.1.16 更新

**文件结构说明**：
- 根目录
可以忽略除Email以外的所有文件夹，其他文件夹是用于创建该软件的介绍页面的。

![根目录](http://i1.piimg.com/1949/c48440a4d75f2d97.png)

- 进入Email文件夹
进入之后结构如下图所示。其中**e4p**后缀为**eric**开发软件的应用后缀，**eric6Project文件夹也是**。
进入**Lib**文件夹即可。我也不知道为啥当时取名叫Lib ——_——

![Email文件夹](http://i1.piimg.com/1949/e1e296c7282ffe41.png)

- 进入Lib文件夹
**Avatars**: 头像库，用于给各个不同用户提供头像
**souce**: 软件界面图标以及logo (原谅我吧source拼错了，后来就不想改了)
**data**: 数据存储文件夹，主要用于存储邮件信息
**kindeditor**: 富文本编辑器，是前端插件(偷了个小懒,设计出一个富文本编辑器感觉工作量挺大的~~~)
**.idea**和**__pycahe__**可忽略

文件就不再介绍，看名字应该都能清楚。不明白的再留言私戳吧。


![Lib文件夹](http://i1.piimg.com/1949/11c5d25de48839e1.png)


----------


该程序使用说明：
**在使用前请确保正确安装Pyqt4！！！
在使用前请确保正确安装Pyqt4！！！
在使用前请确保正确安装Pyqt4！！！**

正确的打开方式是命令行进入Lib文件夹，然后输入下面命令即可。
```powershell
python main.py
```

写在最后：代码肯定还有很多问题，感兴趣的小伙伴体验了这个程序后，如果有什么建议都可留言，一定虚心接受~~~
