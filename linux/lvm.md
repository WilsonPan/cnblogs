# LVM - 逻辑卷管理

## 简介

LVM(Logical Volume Manager), 即逻辑卷管理，是Linux环境下对磁盘分区进行管理的一种机制。

### 相关名词

**PV（physical volume）**
物理卷

- 逻辑卷管理系统最底层
- 物理分区中划出了一个特殊的区域

**VG（volume group）**
卷组

- 至少要包括一物理卷
- 动态的添加卷到卷组中

**LV (logical volume)**
逻辑卷

- 逻辑卷建立在卷组基础上
- 动态扩展和缩小空间

**PE（physical extent）**
物理区域

- 物理卷中可用于分配的最小存储单元
- 逻辑卷中可用于分配的最小存储单元

**LE（logical extent）**
逻辑区域

- 逻辑卷中可用于分配的最小存储单元

### 优缺点

**优点**:

1. 文件系统可以跨多个磁盘，文件系统大小不会受物理磁盘的限制
2. 动态的扩展文件系统的大小
3. 镜像的方式冗余重要的数据
4. 导出整个卷组到另外一台机器

**缺点**:

1. 在从卷组中移除一个磁盘的时候必须使用reducevg命令，需要root权限
2. 卷组中的一个磁盘损坏时，整个卷组都会受到影响

## 相关命令

### 磁盘管理

```bash
fdisk -l                                        # 查看机器上磁盘信息
parted -l                                       # 文件系统类型
df -h                                           # 显示磁盘的相关信息
mkfs.ext4 /dev/sdb                              # 格式化磁盘格式 ext4
mount /dev/sdb /mnt/data/                       # 挂载磁盘到目录/mnt/data/ 
```

### 卷组

```bash
vgdisplay                                       # 显示LVM卷组的信息
vgscan                                          # 扫描并显示系统中的卷组
vgcreate vg01 /dev/sdb                          # 创建名为vg01卷组
vgremove vg01                                   # 删除vg0卷组，删除包含逻辑卷
```

### 逻辑卷

```bash
lvdisplay                                       # 显示逻辑卷属性
lvscan                                          # 扫描并显示系统中逻辑卷
lvcreate --size 10G --name snap01 /dev/vg01     # 创建逻辑卷
lvremove /dev/vg01/snap01                       # 删除逻辑卷 
```

### 动态扩容/缩容

- ext2/ext3/ext4文件系统的调整命令是resize2fs（增大和减小都支持）

```bash
lvextend -L 120G /dev/mapper/centos-home     #增大至120G
lvextend -L +20G /dev/mapper/centos-home     #增加20G
lvreduce -L 50G /dev/mapper/centos-home      #减小至50G
lvreduce -L -8G /dev/mapper/centos-home      #减小8G
resize2fs /dev/mapper/centos-home            #执行调整
```

- xfs文件系统的调整命令是xfs_growfs（只支持增大）

```bash
lvextend -L 120G /dev/mapper/centos-home     #增大至120G
lvextend -L +20G /dev/mapper/centos-home     #增加20G
xfs_growfs /dev/mapper/centos-home           #执行调整
```
