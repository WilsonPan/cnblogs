# Python 常用方法

## Python 后台执行

1. 安装 python-daemon

    ```bash
    pip install python-daemon
    ```

2. 实现

    - 使用`DaemonContext`

    ```py
    with daemon.DaemonContext():
        run()
    ```
