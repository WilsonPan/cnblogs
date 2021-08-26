# Docker - 入门

- [Docker - 入门](#docker---入门)
  - [数据管理](#数据管理)
    - [数据卷（Volumes）](#数据卷volumes)
    - [挂载主机目录](#挂载主机目录)
  - [Docker Compose](#docker-compose)
    - [使用](#使用)

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

```bash
docker pull mongodb

docker volume create mongodb_data

docker run -d -p 27017:27017 --mount source=mongodb_data,target=/data/db --name mongo mongo
```

### 挂载主机目录

```bash
cd $HOME && mkdir mongodb_data

docker run -d -p 27017:27017 --mount type=bind,source=$HOME/mongodb_data,target=/data/db --name mongo mongo
```

## Docker Compose

Docker-Compose 是 Docker 的一种编排服务，是一个用于在 Docker 上定义并运行复杂应用的工具，可以让用户在集群中部署分布式应用。

通过 Docker-Compose 用户可以很容易地用一个配置文件定义一个多容器的应用，然后使用一条指令安装这个应用的所有依赖，完成构建。Docker-Compose 解决了容器与容器之间如何管理编排的问题。

Compose 中有两个重要的概念：

服务 (service) ：一个应用的容器，实际上可以包括若干运行相同镜像的容器实例。
项目 (project) ：由一组关联的应用容器组成的一个完整业务单元，在 docker-compose.yml 文件中定义。

### 使用

1. 安装docker-compose

    > Docker Desktop集成docker-compose，若没有使用pip安装，Docker Desktop集成docker集成是V2，若想更新最新，也可以使用下面更新

    ```bash
    pip3 install docker-compose
    ```

2. 新建app.py编写下面代码

    ```py
    from flask import Flask
    from redis import Redis

    app = Flask(__name__)
    redis = Redis(host='redis', port=6379)


    @app.route('/')
    def hello():
        count = redis.incr('hits')
        return 'Hello World! 该页面已被访问 {} 次。\n'.format(count)


    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True)
    ```

3. 编写`Dockerfile`文件

    ```bash
    FROM python:3.9-alpine
    ADD . /code
    WORKDIR /code
    RUN pip install redis flask
    CMD ["python", "app.py"]
    ```

4. 编写`docker-compose.yml`文件

    ```bash
    version: '3'

    services:

    web:
        build: .
        ports:
        - "5000:5000"

    redis:
        image: "redis:alpine"
    ```

5. 启动

    ```bash
    docker-compose up
    ```

6. 关闭

    ```bash
    docker-compose down
    ```
