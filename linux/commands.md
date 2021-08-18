# 常用命令

## 查找文件

```bash
find .                                              # 列出当前目录及子目录下所有文件和文件夹
find . -type f                                      # 当前目录搜索所有文件
find /home -name "*.txt"                            # 在/home目录下查找以.txt结尾的文件名
find /home -iname "*.txt"                           # 在/home目录下查找以.txt结尾的文件名, 忽略大小写
find . -name "*.txt" -o -name "*.pdf"               # 当前目录及子目录下查找所有以.txt和.pdf结尾的文件
find /usr/ -path "*local*"                          # 文件路径或文件包含path
find . -regex ".*\(\.txt\|\.pdf\)$"                 # 正则表达式匹配文件路径
find . -iregex ".*\(\.txt\|\.pdf\)$"                # 正则表达式匹配文件路径, 并忽略大小写
find /home ! -name "*.txt"                          # 查找/home 不已.txt结尾
find . -maxdepth 3 -type f                          # 向下最大深度限制为3
find . -type f -atime -7                            # 最近七天内被访问过的所有文件
find . -type f -atime +7                            # 超过七天内被访问过的所有文件
find . -type f -size +10k                           # 搜索大于10KB的文件
```

## 文件操作

```bash
cp -rfb ./* ../backup                               # 复制到当前目录的兄弟目录 backup
cp -r aaa/.* ./bbb                                  # 将 aaa 目录下的，所有`.`开头的文件，复制到 bbb 目录中

mv /usr/men/* .                                     # 将目录/usr/men中的所有文件移到当前目录
mv file_1.txt /home/office/                         # 移动文件
mv file_2.txt file_3.txt file_4.txt /home/office/   # 移动多个文件
mv -vn *.txt /home/office                           # 不要覆盖任何已存在的文件
mv -f *.txt /home/office                            # 强制覆盖已经存在的文件

dd if=/dev/zero of=sun.txt bs=1M count=1            # 创建了一个1M大小的文件sun.txt
```

## 文本搜索

```bash
grep "match_pattern" file_name                      # 搜索指定文件，返回包含“match_pattern” 的文本行
grep "match_pattern" file_name -n                   # 搜索指定文件，返回包含“match_pattern” 的文本行, 并输出行数
grep "match_pattern" file_1 file_2 file_3           # 搜索多个文件，返回包含“match_pattern” 的文本行
grep "match_pattern" file_name -v                   # 输出除之外的所有行
grep "match_pattern" file_name --color=auto         # 标记匹配颜色 --color： never、always、auto
grep -E "[1-9]+" file_name                          # 正则匹配查找
grep -E "[1-9]+" -o file_name                       # 只输出文件匹配部分
grep "text" . -r -n                                 # 递归搜索
grep "match_pattern" file_name -A 3                 # 匹配结果并输出之后3行
grep "match_pattern" file_name -B 3                 # 匹配结果并输出之前3行
```

## 统计文件/文件夹大小

```bash
du -sh .                                            # 显示当前目录大小
du -sh *                                            # 显示各个文件和目录大小
du -sh * | sort -rh                                 # 文件从大到小排序
du --time                                           # 显示目录或该目录子目录下所有文件的最后修改时间
du -sh * --time                                     # 显示当前目录各个文件/文件夹最后修改时间
du -sh ./*/                                         # 只显示当前目录下子目录的大小
```

## 组合使用

```bash
find . -type f -name "*.log" | xargs grep "warning"                                             # 查找符合条件文件，并搜索关键字
find . -name "*.py" | xargs cat | grep -v ^$ |wc -l                                             # 代码行数统计, 排除空行
grep -i "warning" > result.log                                                                  # 查找结果写入文件
echo `date +%Y%m%d%H%M%S` | xargs -I {} sh -c 'mkdir ./bak/{}; cp -a /mongodb/data ./bak/{}'    # 按日期创建文件夹备份
```
