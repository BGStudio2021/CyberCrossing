# CyberCrossing
利用 Flask 实现的赛博红绿灯。
## 使用方法
克隆源码后通过 pip 安装依赖：
```
pip install requirements.txt -r
```
调整`config.ini`中的配置：
|    项目    |    说明    |
| ---------- | ---------- |
| port | HTTP 服务器端口号 |
| G_0 | 方向 0 的绿灯时长 |
| Y_0 | 方向 0 的黄灯时长 |
| G_1 | 方向 1 的绿灯时长 |
| Y_1 | 方向 1 的黄灯时长 |

之后运行`app.py`即可
