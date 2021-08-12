# Python 开发环境

- [Python 开发环境](#python-开发环境)
  - [开发环境](#开发环境)
  - [Python包管理](#python包管理)

## 开发环境

1. 安装 Python 3

    ```js
    brew install python
    ```

2. 验证是否安装成功

    ```js
    python3 --verison
    ```

    > macOS 自带python2.7, 通过`brew install python`安装是多一个python3，可以通过安装Python虚拟环境管理设置Python3， 但我更喜欢底层虚拟环境（virtualenv）, 在每个项目中管理运行环境

3. 安装 IDE -- VS Code

    ```bash
    brew cask install visual-studio-code       # ingore if installed
    ```

    **插件**

    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Python 语言支持
    - [Visual Studio IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) - AI智能辅助
    - [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - 更好静态类型支持

4. 安装底层虚拟环境（virtualenv）

    安装

    ```bash
    pip install virtualenv                              # 安装 virtualenv
    virtualenv --version                                # 验证 virtualenv 是否成功
    cd project_name && virtualenv -p python3 venv       # 使用Python3创建虚拟环境   
    source venv/bin/activate                            # 激活虚拟环境
    deactivate                                          # 停用虚拟环境
    ```

## Python包管理

使用PIP管理[Python Packages](https://pypi.org/)

- 管理

```bash
pip check                                               # 检查是否有缺失包和包版本是否正确
pip show package_name                                   # 列出包信息

pip search package_name                                 # 查找包

pip list                                                # 列出已安装包
pip list --outdated                                     # 列出过时包
pip list --format=json                                  # 使用JOSN格式输出
```

- 安装卸载

```bash
pip install package_name                                # 安装最新版本
pip install package_name==1.0.4                         # 安装指定版本
pip install 'package_name>=1.0.4'                       # 安装版本不小于1.0.4
pip install 'package_name<=1.0.4'                       # 安装版本不大于1.0.4

pip install -r requirements.txt                         # 安装指定文件包列表
pip freeze > requirements.txt                           # 当前包引用生成指定文件
··
pip uninstall package_name                              # 卸载指定包
pip uninstall -r requirements.txt                       # 卸载指定文件包
```
