# WPS 使用技巧记录

- [WPS 使用技巧记录](#wps-使用技巧记录)
  - [快捷键](#快捷键)
  - [函数](#函数)
    - [VLOOKUP](#vlookup)
  - [常用技巧](#常用技巧)

## 快捷键

| 快捷键              | 作用     |
| ------------------- | -------- |
| command + shift + C | 复制格式 |
| command + shift + V | 粘贴格式 |

## 函数

### VLOOKUP

语法

```bash
VLOOKUP（lookup_value，table_array，col_index_num，[range_lookup]）
```

| 变量名        | 是否必须 | 说明                               | 默认值 |
| ------------- | -------- | ---------------------------------- | ------ |
| lookup_value  | 是       | 查找值                             | -      |
| table_array   | 是       | 查找区域（第一列查找匹配的列）     | -      |
| col_index_num | 是       | 需要显示列，1开始                  | -      |
| range_lookup  | 否       | FALSE : 精确查找， TRUE： 近似匹配 | TRUE   |

- 例子

```bash
=VLOOKUP(A1,C1:D3,2,FALSE)                          # 从C1:C3 等于A1 ，显示对应D列
=VLOOKUP(A1,C1:D3,2,TRUE)                           # 从C1:C3 近似A1 ，显示对应D列

=VLOOKUP(A1 & "*",C$1:D$3,2,TRUE)                   # 通配符查找
=VLOOKUP(A1 & "*",sheet1!C$1:D$3,2,TRUE)            # 跨sheet查找
```

- 说明

1. `C$1:D$3` : 数字前加`$`锁定行内容，下拉保持查找范围一致

## 常用技巧
