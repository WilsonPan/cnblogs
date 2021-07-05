# MacBook 软件安装与管理

- [MacBook 软件安装与管理](#macbook-软件安装与管理)
  - [软件管理](#软件管理)
  - [软件使用](#软件使用)

## 软件管理

- 安装Brew

1. 访问[brew](https://brew.sh)

2. 复制命令在终端执行

- Brew 使用

1. 搜索软件

    ```bash
    brew search chrome
    ```

2. cask 安装（编译好的源， 一般用于有GUI程序安装，eg. chrome ,vscode)

    ```bash
    brew cask install google-chrome
    ```

3. brew 安装（代码编译，一般用于命令，第三方库安装）

    ```bash
    brew install curl
    ```

4. 列出当前安装情况

    ```bash
    brew list
    ```

5. 卸载软件

    ```bash
    brew uninstall google-chrome
    ```

6. 更新软件

    ```bash
    brew upgrade google-chrome
    ```

7. 常用软件

    ```bash
    brew cask install google-chrome

    # 微信
    brew cask install wechat

    # 企业微信
    brew cask install wechatwork

    brew cask install visual-studio-code

    # jetbrains
    brew cask install jetbrains-toolbox

    # git
    brew install git

    brew cask install dotnet-sdk

    ```

8. [dotnet sdk 历史版本](https://github.com/isen-ng/homebrew-dotnet-sdk-versions)

    - 安装  

    ```bash
    brew tap isen-ng/dotnet-sdk-versions        # 添加新的Tap
    brew install --cask <version>               # 安装指定版本
    brew uninstall --zap --cask <version>       # 卸载指定版本
    ```

9. 高级使用

    ```bash
    brew list --cask                            # 列出所有Casks
    brew outdated --cask                        # 列出可更新Casks
    brew deps --tree --installed                # 列出当前已安装依赖关系
    ```

## 软件使用

- macos 连接 mssql 需要freetds

    ```bash
    brew install freetds
    ```

- nginx使用

1. 安装

    ```bash
    brew install nginx
    ```

2. 服务启动

    ```bash
    brew services start nginx
    ```

3. 关闭服务

    ```bash
    brew services stop nginx
    ```

4. 配置与日志文件路径

    ```bash
    # 配置
    cd /usr/local/etc/nginx

    # 日志
    cd /usr/local/var/log/nginx/
    ```
