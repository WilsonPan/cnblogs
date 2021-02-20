# Git 常用命令介绍

Git是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。

Git有很多GUI工具，如[Git Extensions](https://github.com/gitextensions/gitextensions) 、 [Sourcetree](https://www.sourcetreeapp.com/)

但是实际工作中，掌握简单git命令，不但可以加深对Git使用了解，还能提高工作效率

## 名词

Git 有三种状态，你的文件可能处于其中之一

| **文件状态**        | **描述**                           |
| ------------------- | ---------------------------------- |
| 已提交（committed） | 数据已经安全地保存在本地数据库中   |
| 已修改（modified）  | 修改了文件，但还没保存到数据库中   |
| 已暂存（staged）    | 对一个已修改文件的当前版本做了标记 |

基本概念

| **名词** | **解析**                                                        | **文件状态** |
| -------- | --------------------------------------------------------------- | ------------ |
| 工作区   | 当前处于版本控制的目录                                          | 已修改       |
| 暂存区   | 保存即将提交到文件列表信息，一般存放在 .git 目录下的 index 文件 | 已暂存       |
| 本地仓库 | 版本控制的本地数据库                                            | 已提交       |
| 远程仓库 | 服务器保存仓库数据                                              | -            |

一般工作流程

1. 工作区修改       ->  `vi file`
2. 添加暂存区       ->  `git add .`
3. 提交本地仓库     ->  `git commit -m 'message'`
4. 推送到远程仓库   ->  `git push`

## 仓库

- 创建一个新仓库/重新初始化已有仓库

    ```bash
    git init                    #初始化仓库
    git init --template=<dir>   #使用模版创建仓库
    git init -b live            #覆盖初始分支名称 
    ```

- 克隆远程仓库

    ```bash
    git clone <git-url>                     # 克隆远程仓库
    git clone <git-url> --depth 1           # 创建一个指定深度的浅克隆, 1:每个分支最后一次提交
    git clone <git-url> --no-tags           # 不要克隆任何标签，并且后续获取操作也不下载它们
    git clone <git-url> --single-branch     # 只克隆一个分支、HEAD 或 --branch
    ```

## 工作区操作

- 添加暂存区
  
    ```bash
    git add <file>                          # 添加指定文件到暂存
    git add .                               # 添加所有改变的已跟踪文件和未跟踪文件
    git add <file> -f/--force               # 允许添加忽略的文件
    ```

- 提交

    ```bash
    git commit -m 'commit message'          # 提交并写入提交信息
    git commit -a                           # 提交所有已跟踪文件
    git commit -o/--only                    # 提交指定的文件
    git commit --dry-run                    # 显示将要提交的内容
    ```

- 还原

    ```bash
    git restore text.txt                    # 恢复指定文件工作区修改
    git restore tools/                      # 恢复指定目录修改
    git restore text.txt --source=main      # 恢复到指定分支
    ```

- 删除
  
    ```bash
    git rm text.txt                         # 删除已跟踪文件
    git rm -r -f wilson/                    # 删除已跟踪文件和本地文件
    git rm -r --cached wilson/              # 删除已跟踪文件，保留本地文件
    git rm wilson.txt -f -n                 # 演示删除文件
    ```

## 分支管理

- 列出分支
  
    ```bash
    git branch                              # 列出所有本地分支
    git branch -a                           # 列出远程跟踪及本地分支
    ```

- 创建/删除/拷贝/重命名分支

    ```bash
    git checkout -b <branch_name>           # 创建并检出一个新的分支
    git checkout -B <branch_name>           # 创建/重置并检出一个分支
    git branch -d <branch_name>             # 删除完全合并的分支
    git branch -D <branch_name>             # 删除分支（即使没有合并）
    git branch -c <branch_name>             # 拷贝一个分支和它的引用日志
    git branch -C <branch_name>             # 拷贝一个分支，即使目标已存在
    git branch -m <branch_name>             # 移动/重命名一个分支，以及它的引用日志
    git branch -M <branch_name>             # 移动/重命名一个分支，即使目标已存在
    ```

- 合并分支
  
    ```bash
    git merge <branch_name>                                 # 与当前分支合并
    git merge <branch_name> -n                              # 在合并的最后不显示差异统计
    git merge <branch_name> --stat                          # 在合并的最后显示差异统计
    git merge <branch_name> --squash                        # 创建一个单独的提交而不是做一次合并
    git merge <branch_name> --allow-unrelated-histories     # 允许合并不相关的历史
    ```

- 合并提交

    ```bash
    git rebase -i HEAD~3                                    # 交互式合并最近3次提交
    git rebase -i <commit_id>                               # 变基到指定提交
    ```

- 标签

    ```bash
    git tag --list                                          # 列出标签名称
    git tag -a 'v001' -m 'release at 2021/02/20 12:00'      # 打 tag
    git checkout <tag_name>                                 # checkout tag
    git push --tag                                          # 推送tag到远程
    git tag -d <tag_name>                                   # 删除本地tag
    git push origin -d tag <tag_name>                       # 删除远程tag
    ```

- 还原分支

    **未推送**

    ```bash
    git reset <commit_id>                   # 重置 HEAD
    git reset <commit_id> --hard            # 重置 HEAD、索引和工作区
    git reset <commit_id> --keep            # 重置 HEAD、索引, 保留工作区修改
    ```

    **已推送**

    ```bash
    git revert <commit_id>                      # 还原修改，新建一个新的提交，提交历史不会覆盖

    git reset <commit_id> && git push --force   # 重置HEAD，强制推送，覆盖提交历史
    ```

## 检查历史和状态

- 查看差异

    ```bash
    git diff                                    # 显示工作区与索引、仓库之间差异
    git diff --name-only                        # 只显示变更文件
    git diff --stat                             # 显示变更统计
    git diff <file_name>                        # 显示指定文件差异
    git diff <commit_id>                        # 显示与指定提交差异
    git diff <branch_name>                      # 显示与指定分支差异
    ```

## 协同工作

## 其他

- 配置

    ```bash
    git config --list                               # 列出所有配置
    git config --list --local                       # 列出所有本地配置
    git config --list --global                      # 列出所有全局配置

    git config user.name "Wilson Pan"               # 设置提交名称
    git config user.email wilsonpan@github.com      # 设置提交邮箱
    git config --global pull.rebase=false           # 全局设置
    git config --unset user.name                    # 删除变量名    
    ```

- 设置别名
  
  ```bash
  git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"                                  # git lg 查看日志

  git config --global alias.last 'lg -p -1'         # 显示最近一次提交变更
  ```

- 常用查看

    ```bash
    git remote -v                                   # 查看仓库远程地址
    git branch                                      # 列出当前分支
    git branch -a                                   # 列出所有分支
    git branch -d <branch_name>                     # 删除完全合并的分支
    git branch -D <branch_name>                     # 删除分支（即使没有合并）
    ```
