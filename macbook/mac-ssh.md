# MacBook SSH使用

## 普通使用

1. 打开终端
2. `ssh <username>@<ip>`
3. 输入密码

## 高阶使用

- **使用公钥私钥连接**  (避免每次连接输入密码)

    ```bash
    cd ~/.ssh

    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"   # 可选，若未生成ssh

    ssh-copy-id -i id_rsa.pub user@host                     # 复制公钥到服务器

    ssh-add -K id_rsa                                       # 将SSH密钥添加到ssh-agent，Macos才需要                               
    ```

- **设置别名** （方便记忆）

1. 添加配置

    ```bash
    cd ~/.ssh

    touch config            # 可选，若当前未创建

    vim config              # 编辑
    ```

2. 添加如下配置信息

    ```js
    Host wilson
    HostName 100.100.100.100
    User root
    IdentitiesOnly yes
    ```

3. 使用`ssh wilson`直接连接

## 常用SSH命令

- 复制本地文件/文件夹 到服务器
  
```bash
# 复制文件
scp appsettings.json root@101.100.100.101:/app
scp appsettings.json wilson:/app

# 复制目录
scp -r /wilson root@101.100.100.101:/app
scp -r /wilson wilson:/app
```

- 从服务器复制文件到本地目
  
```bash
# 复制文件
scp root@101.100.100.101:/opt/soft/demo.tar /opt/soft/
scp wilson:/opt/soft/demo.tar /opt/soft/

# 复制目录
scp -r root@101.100.100.101:/opt/soft/test /opt/soft/
scp -r wilson:/opt/soft/test /opt/soft/
```
