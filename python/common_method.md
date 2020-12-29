# Python 常用方法 


## 语法

- **三元表达式**
  
    ```python
    value = 10 if 1 > 2 else 20

    # reusult = 20
    ```

- **Lambda** 
    
    ```python
    array = [12, 65, 54, 39, 102, 339, 221, 50, 70, 10]

    result = list(filter(lambda m: m < 20, array))

    print(result)
    ```

- **获取对象唯一Id**

    ```python
    x = ('apple', 'banana', 'cherry')
    y = id(x)
    print(y)
    ```

- **动态导入搜索路径**
  
  ```python
  import sys
  sys.path.append('<path')
  ```

- **获取变量类型**
    
    ```python
    val = {}

    print(type(val))
    ```
## 文件相关

- **写入json**
  
    ```python
    obj = {}
    obj["name"] = "wilson"

    # 格式化输出到文件
    with open(filename, 'w') as fp:
        json.dump(obj, fp, indent=4, separators=(',', ': '))
    ```

- **从文件读到json对象**
    
    ```python
    with open(filename, 'r') as fp:
        json.load(fp)
    ```
