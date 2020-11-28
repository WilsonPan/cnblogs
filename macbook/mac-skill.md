# MacBook 使用技巧

## 使用技巧

- **开启终端翻墙**

    ```bash
    export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7891
    ```

## 常用命令

- **查询端口，结束进程**

    ```bash
    lsof -i tcp:<port>

    kill -9 <pid>
    ```

- **压缩**

    ```bash
    # 压缩当前目录（不包含子目录下文件
    zip file.zip *

    # 压缩当前目录（包含子目录）
    zip -r file.zip *

    # 压缩只符合条件文件
    zip file.zip *.cs

    # 压缩排除特定文件
    zip file.zip * -x 'bin/*'
    ```

- **解压**
  
    ```bash
    # 解压当前文件夹
    unzip file.zip

    # 解压指定文件夹
    unzip file.zip -d ./demo

    # 查看不解压
    unzip -v file.zip
    ```

## 文件操作

| 命令              | 说明               | 例子                     |
| ----------------- | ------------------ | ------------------------ |
| cd                | 打开目录           | cd program               |
| pwd               | 列出当前路径名称   | 123                      |
| ls                | 列出当前目录       | ls - la 显示目录详细内容 |
| mkdir             | 创建目录           | mkdir dir_name           |
| touch file.format | 创建指定格式文件   |
| cat               | 在终端显示文本     | cat file                 |
| rm                | 删除文件/非空目录  | rm filename/dri_name     |
| rm -rf            | 删除一个 非空 目录 | rm -rf dir               |
| grep              | 正则表达式搜索文件 |

## 快捷键

| 快捷键              | 功能               |
| ------------------- | ------------------ |
| command + space     | 聚焦搜索           |
| command + c         | 复制               |
| command + v         | 粘贴               |
| command + shift + . | 显示/隐藏 隐藏文件 |
| command + up        | 页顶               |
| command + down      | 页尾               |
| fn + left           | 行首               |
| fn + right          | 行尾               |
| fn + up             | page up            |
| fn + down           | page down          |
