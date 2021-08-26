# Docker - 入门

## 数据管理

前面讲过镜像使用的是分层存储，容器也是如此。每一个容器运行时，是以镜像为基础层，在其上创建一个当前容器的存储层，我们可以称这个为容器运行时读写而准备的存储层为 容器存储层。

容器存储层的生存周期和容器一样，容器消亡时，容器存储层也随之消亡。因此，任何保存于容器存储层的信息都会随容器删除而丢失。

按照 Docker 最佳实践的要求，容器不应该向其存储层内写入任何数据，容器存储层要保持无状态化。所有的文件写入操作。

Docker 内部以及容器之间管理数据，在容器中管理数据主要有两种方式

- 数据卷（Volumes）
- 挂载主机目录 (Bind mounts)

### 数据卷（Volumes）

```bash
docker volume ls                                                    # 列出所有数据卷
docker volume create <volume_name>                                  # 创建一个数据卷
docker volume inspect <volume_name>                                 # 查看数据卷详细信息
docker volume rm <volume_name>                                      # 删除数据卷
docker volume prune                                                 # 清理无用数据卷
```
