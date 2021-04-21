# Centos 软件管理

## 安装软件

### Yum

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
    make 
    make install
    ```
