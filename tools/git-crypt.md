# 保护Git仓库敏感信息

代码中无可避免有一些敏感信息，包含但不限于，数据库信息，密钥，账号信息等等。通常我们会把这些信息放在配置文件，这些信息若泄露会造成安全问题。

以前我们做法，是把配置文件通过`.gitignore`排除配置文件，但是这些配置文件通常经常变动，没有一个地方统一维护，靠线下互相传，效率低下不说，也没法维护。

**那能不能既方便又安全管理敏感信息？**答案当然是有，不然就没今天这篇文章

下面就介绍如何利用[git-crypt](https://github.com/AGWA/git-crypt/)达到想要的效果

## 安装

- Mac OS X

    ```bash
    brew install git-crypt
    brew install gpg
    ```

- Linux

    ```bash
    make && make install PREFIX=/usr/local
    ```

- Windows

    1. [下载git-crypt.exe](https://github.com/oholovko/git-crypt-windows/releases)
    2. 放在Path目录/添加Path目录

> 此方法为未尝试

## 使用

1. 生成密钥

    ```bash
    git-crypt init
    ```

2. 创建`.gitattributes`文件并编辑指定的加密文件

    ```bash
    touch .gitattributes    

    vi .gitattributes
    ```

    格式如下

    ```text
    appsettings.json filter=git-crypt diff=git-crypt
    *.key filter=git-crypt diff=git-crypt
    config/**.json filter=git-crypt diff=git-crypt
    ```

3. 生成密钥

    ```bash
    gpg --gen-key # 按提示输入相关信息
    ```

4. 配置git-crypt

    ```bash
    git-crypt add-gpg-user <USER_ID>  # <USER_ID>填入上面输入的名称/key，不然会报错
    ```

## 原理

## 引用

[git-crypt](https://github.com/AGWA/git-crypt/)

[git-crypt-windows](https://github.com/oholovko/git-crypt-windows)

[Github - MD](https://github.com/WilsonPan/cnblogs/blob/main/tools/git-crypt.md)
