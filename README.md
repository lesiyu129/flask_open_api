# flask的安装

```shell
# 设置源
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
# 下载
pip install Flask
```

## 一个最小的API应用

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"impoet flask

```
