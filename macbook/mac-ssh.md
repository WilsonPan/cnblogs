# MacBook SSH使用


## 普通使用

1. 打开终端
2. `ssh <username>@<ip>`
3. 输入密码


## 高阶使用

- **使用公钥私钥连接**
> 避免每次连接输入密码

1. `cd ~/.ssh`
2. `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
> 可选，若未生成
3. `ssh-copy-id -i <公钥文件> user@host`    
> 复制公钥到服务器  eg: `ssh-copy-id -i id_rsa.pub user@host`
4. `ssh-add -K <私钥文件>`
> 将SSH密钥添加到ssh-agent，Macos才需要 ， eg: `ssh-add -K id_rsa`


- **设置别名**
> 记住账号和IP比较困难，特别是服务器多起来的时候

1. `cd ~/.ssh`
2. `touch config` 
> 可选，当前目录没有才需要创建新文件
3. `vim config`
> 编辑配置文件
4. 增加配置
   
```js
Host wilson
HostName 100.100.100.100
User root
IdentitiesOnly yes
```
5. 使用`ssh wilson`直接连接