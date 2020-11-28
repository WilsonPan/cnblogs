# Python 开发环境

> 环境
- OS: macOS Big Sur
- IDE: VSCode

## 开发环境

1. 安装 Python 3

    ```bash
    brew install python
    ``` 
    
    验证是否安装成功

    ```bash
    python3 --verison
    ```

    > macOS 自带python2.7, 通过`brew install python`安装是多一个python3，可以通过安装Python虚拟环境管理设置Python3， 但我更喜欢底层虚拟环境（virtualenv）, 在每个项目中管理运行环境


2. 安装 IDE -- VS Code

    ```bash
    # install vscode (ingore if installed)
    brew cask install visual-studio-code
    ```

    插件
    
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Python 语言支持
    - [Visual Studio IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) - AI智能辅助
    - [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - 更好静态类型支持


3. 安装底层虚拟环境（virtualenv）

    安装

    ```bash
    pip install virtualenv
    ```

    验证

    ```bash
    virtualenv --version
    ```

    创建虚拟环境

    ```bash
    # 进去项目目录
    cd project_name

    # 使用指定Python版本
    virtualenv -p python3 venv
    ```

    激活虚拟环境
    
    ```bash
    source venv/bin/activate
    ```

    停用虚拟环境

    ```bash
    deactivate
    ```

