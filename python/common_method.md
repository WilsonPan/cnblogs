# Python 常用方法 


## 语法

- 三元表达式
  
    ```python
    value = 10 if 1 > 2 else 20

    # reusult = 20
    ```

## 文件相关

- 写入json
  
    ```python
    obj = {}
    obj["name"] = "wilson"

    # 格式化输出到文件
    with open(filename, 'w') as fp:
        json.dump(obj, fp, indent=4, separators=(',', ': '))
    ```

- 从文件读到json对象
    
    ```python
    with open(filename, 'r') as fp:
        json.load(fp)
    ```
