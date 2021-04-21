# Centos 软件包管理

OS: Centos

## 安装软件包

### Yum 安装

- 列出可安装软件包
  
    ```bash
    yum list tomcat
    yum list git
    ```

- 安装软件包

    ```bash
    yum install git             
    yum -y install git          # 自动应答yes
    ```

### 编译安装

1. 下载

    ```bash
    cd /tmp
    wget https://codeload.github.com/git/git/tar.gz/v2.31.0
    ```

2. 解压

    ```bash
    tar -xzvf git-2.31.0.tar.gz 
    cd git-2.31.0/
    ```

3. 编译安装

    ```bash
    ./configure --prefix=/usr/local
    make && sudo make install
    ```

4. 编译安装

    ```bash
    make && make install
    ```

## 更新软件包

- 列出可更新软件包

    ```bash
    yum list updates                        # 列出所有可更新软件包
    yum list updates "mysql*"               # 列出mysql相关更新
    ```

- 更新

    ```bash
    yum update                              # 更新所有软件包和内核
    yum update mysql-community-client       # 更新指定软件包
    yum update --exclude=kernel*            # 排除某个软件包更新
    ```

- yum update 与 yum upgrade区别

  - yum update：升级所有包同时也升级软件和系统内核
  - yum upgrade：只升级所有包，不升级软件和系统内核

## 回滚更新

1. 查看更新历史

    ```bash
    yum history
    ```

2. 回滚指定更新Id

    ```bash
    yum history undo 7
    ```

## 卸载软件包

### Yum 卸载

- 列出已安装软件包

     ```bash
     yum list installed                     # 列出所有安装
     yum list installed "mysql*"            # 列出符合安装
     ```

- 删除软件包

    ```bash
    yum remove mysql-community-client       # 删除指定软件包
    yum groupremove group1                  # 删除指定软件组
    ```

### 手动卸载

1. 查询是否安装软件包

    ```bash
    rpm -qa | grep php
    ```

2. 删除已安装软件包

    > 根据第一步显示的软件包名，一个个删除

    ```bash
    sudo rpm -e php-common-5.4.16-48.el7.x86_64                         # 普通删除模式
    sudo rpm -e php                                                     # 强力删除模式，如果用上面命令删除时，提示有依赖的其他文件，则用该命令可以对其进行强力删除
    ```

## 清除缓存

```bash
yum clean packages       # 清除缓存目录下的软件包
yum clean headers        # 清除缓存目录下的 headers
yum clean oldheaders     # 清除缓存目录下旧的 headers
```
