# MacBook 软件安装与管理

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
    brew tap isen-ng/dotnet-sdk-versions
    brew cask install <version>

    ```

    - 卸载

    ```bash
    brew cask zap <version>
    ```

## 说明

- macos 连接 mssql 需要freetds

```bash
brew install freetds
```