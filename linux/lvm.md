# LVM - 逻辑卷管理

## 简介

## 磁盘管理

```bash
fdisk -l                                        # 查看机器上磁盘信息
parted -l                                       # 文件系统类型
df -h                                           # 显示磁盘的相关信息
mkfs.ext4 /dev/sdb                              # 格式化磁盘格式 ext4
mount /dev/sdb /mnt/data/                       # 挂载磁盘到目录/mnt/data/ 
```

## 卷组

```bash
vgdisplay                                       # 显示LVM卷组的信息
vgscan                                          # 扫描并显示系统中的卷组
vgcreate vg01 /dev/sdb                          # 创建名为vg01卷组
vgremove vg01                                   # 删除vg0卷组，删除包含逻辑卷
```

## 逻辑卷

```bash
lvdisplay                                       # 显示逻辑卷属性
lvscan                                          # 扫描并显示系统中逻辑卷
lvcreate --size 10G --name snap01 /dev/vg01     # 创建逻辑卷
lvremove /dev/vg01/snap01                       # 删除逻辑卷 
```
