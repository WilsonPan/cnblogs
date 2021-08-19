# MacBook 软件安装与管理

- [MacBook 软件安装与管理](#macbook-软件安装与管理)
  - [Homebrew安装与卸载](#homebrew安装与卸载)
  - [Brew使用](#brew使用)
  - [服务管理](#服务管理)
  - [问题与解决](#问题与解决)

Homebrew是一款包管理工具，目前支持macOS和linux系统。主要有四个部分组成: brew、homebrew-core 、homebrew-cask、homebrew-bottles

Homebrew 通过简单的一条指令，就可以实现包管理，不需要关心各种依赖和文件路径的情况。

| 名称             | 说明                            |
| ---------------- | ------------------------------- |
| brew             | HomeBrew 源代码仓库             |
| homebrew-core    | HomeBrew 核心源                 |
| homebrew-cask    | 提供macOS应用和二进制文件的安装 |
| homebrew-bottles | 预编译二进制软件包              |

| 术语     | 说明                                                                  |
| -------- | --------------------------------------------------------------------- |
| Formulae | 软件包，包括了这个软件的依赖、源码位置及编译方法等， 主要是命令行工具 |
| Casks    | 已经编译好的应用包， 主要是GUI工具                                    |

## Homebrew安装与卸载

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"         # 安装

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"       # 卸载
```

默认安装源访问不稳定，可以在安装前切换`HOMEBREW_BREW_GIT_REMOTE`和`HOMEBREW_CORE_GIT_REMOTE` 使用不同源加速，安装完成后运行`brew update`更新

- 清华大学源
  
```bash
if [[ "$(uname -s)" == "Linux" ]]; then BREW_TYPE="linuxbrew"; else BREW_TYPE="homebrew"; fi
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/${BREW_TYPE}-core.git"
```

- 中科大源

```bash
if [[ "$(uname -s)" == "Linux" ]]; then BREW_TYPE="linuxbrew"; else BREW_TYPE="homebrew"; fi
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/${BREW_TYPE}-core.git"
```

- 官方源

```bash
if [[ "$(uname -s)" == "Linux" ]]; then BREW_TYPE="linuxbrew"; else BREW_TYPE="homebrew"; fi
export HOMEBREW_BREW_GIT_REMOTE="https://github.com/Homebrew/brew"
export HOMEBREW_CORE_GIT_REMOTE="https://github.com/Homebrew/${BREW_TYPE}-core.git"
```

## Brew使用

1. 搜索软件包

    ```bash
    brew search git                                                     # 搜索git , 包含Casks 和 Formulae
    brew search git --cask                                              # 只在 Casks 搜索git
    brew search git --formula                                           # 只在 Formulae 搜索git
    ```

2. 软件包安装与卸载

    ```bash
    brew update                                                         # 更新Homebrew

    brew install git                                                    # 安装 Formulae 或 Casks 软件包
    brew install google-chrome --cask                                   # 安装Casks 软件包
    brew install git --formula                                          # 安装Formulae 软件包
    brew install git --only-dependencies                                # 只安装依赖，不安装软件包

    brew uninstall git                                                  # 卸载软件包，但不删除依赖

    brew tap beeftornado/rmtree                                         # 安装rmtree命令
    brew rmtree git                                                     # 卸载软件包并删除依赖
    ```

3. 管理软件包

    ```bash
    brew list                                                           # 列出当前已安装软件包，包含Formulae 和 Casks
    brew list --formula                                                 # 只列出Formulae
    brew list --cask                                                    # 只列出Casks
    brew list --versions                                                # 列出已安装软件包版本

    brew outdated                                                       # 列出有更新的软件包
    brew outdated --formula                                             # 列出有更新的 Formula 包
    brew outdated --cask                                                # 列出有更新的 Casks 包

    brew upgrade                                                        # 更新过时的Formulae 和 Casks
    brew upgrade git                                                    # 更新指定软件包

    brew info git                                                       # 列出软件包信息   

    brew deps --tree --installed                                        # 列出当前已安装依赖关系  
    ```

4. 常用软件

    ```bash
    # Casks 
    
    brew cask install google-chrome                                     # google chrome
    brew cask install wechat                                            # 微信
    brew cask install wechatwork                                        # 企业微信
    brew cask install visual-studio-code                                # visual studio code    
    brew cask install jetbrains-toolbox                                 # jetbrains

    # Formulae
    brew install git                                                    # git
    brew install azure-cli                                              # azure cli
    brew install freetds                                                # freetds macos 连接 mssql 需要freetds
    brew install openjdk@11                                             # open jdk 11
    brew install python@3.9                                             # python3.9 版本
    ```

## 服务管理

```bash
brew services list                                                      # 列出已安装服务
brew services --all                                                     # 运行所有服务
brew services run <service>                                             # 运行服务
brew services start <service>                                           # 启动服务
brew services stop <service>                                            # 停止服务
brew services restart <service>                                         # 重启服务
brew services restart <service>                                         # 重启服务
brew services restart <service> --debug --verbose                       # 显示详细信息
brew services cleanup                                                   # 删除所有不使用服务
```

**例子**:

```bash
brew install nginx                                                      # 安装nginx
brew services start nginx                                               # 启动nginx
brew services stop nginx                                                # 停止nginx

vi /usr/local/etc/nginx/nginx.conf                                      # 配置文件
cd /usr/local/var/log/nginx/                                            # 日志路径
```

## 问题与解决

**问题**:

Error: Directory not empty @ dir_s_rmdir - /usr/local/Cellar/python/3.7.7

**解决**:

```bash
chown -R MyUser:staff /usr/local/Cellar/python/3.7.7
```
