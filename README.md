# ShipGame

## 相关说明

1. 代码结构之文件夹说明
   1. agent: 主要包含智能体类
   2. envs: 仿真环境的实现
   3. useless_envs： 用于存放较大更新后的环境代码
2. 研发路线：
   1. 实现无干扰信号下的搜索
   2. 在上条基础上增加方针要素

## 开发配置

the virtualenv in ubuntu 18 (dell)  is "xxx_E2".

本场景主要是针对无人反潜机，所建立的仿真环境，并采用强化学习算法进行求解


```commandline
env_cmd.py: 环境命令集合
env_config.py: 环境配置
env_submarine: 潜艇仿真环境
```

## 仿真环境

```ba	
__init__()
reset( )
step( action)
reward(s, a, s')
```

### 1 仿真环境介绍

背景介绍：该仿真环境用来模拟无人反潜机在海域搜索潜艇场景，无人反潜机的搜索策略由深度强化学习提供。

### 2 仿真环境版本介绍

