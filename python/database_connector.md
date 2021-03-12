# Python 连接常用数据库

- [Python 连接常用数据库](#python-连接常用数据库)
  - [Mongodb](#mongodb)
  - [Azure SQL databases](#azure-sql-databases)
  - [MySQL](#mysql)

## Mongodb

1. 安装`pymongo`包

    ```bash
    pip install pymongo
    ```

2. 插入数据

    ```python
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017/")

    # get or create database
    db = client["Demo"]

    # get or create collection
    col = db["customers"]

    # insert one record
    data = col.insert_one({
        "name": "wilson",
        "sex": 1,
        "address": "tian he",
        "created": datetime.now()
    })

    # close connection
    client.close()
    ```

3. 查询数据

    ```python
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017/")

    # get or create database
    db = client["Demo"]

    # get or create collection
    col = db["customers"]

    # find one 
    data = col.find_one()
    print(data)

    # find all
    datas = col.find()

    for data in datas:
        print(data)
    ```

## Azure SQL databases

1. 安装`freetds`驱动

    ```bash
    brew install freetds
    ```

2. 安装`pymssql`包

    ```bash
    pip install pymssql
    ```

3. 插入数据

    ```python
    import pymssql  
    conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')  
    cursor = conn.cursor()  
    cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express', 'SQLEXPRESS', 0, 0, CURRENT_TIMESTAMP)")  
    row = cursor.fetchone()  
    while row:  
        print "Inserted Product ID : " +str(row[0])  
        row = cursor.fetchone()  
    conn.commit()
    conn.close()
    ```

4. 查询数据

    ```python
    import pymssql  
    conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')  
    cursor = conn.cursor()  
    cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')  
    row = cursor.fetchone()  
    while row:  
        print str(row[0]) + " " + str(row[1]) + " " + str(row[2])     
        row = cursor.fetchone()
    ```

## MySQL

1. 安装`pymysql`包

    ```bash
    pip install pymysql
    ```

2. 查询数据

    ```python
    import pymysql

    conn = pymysql.connect(
        host='127.0.0.1', user='root', password='123456', database='demo'
    )

    cursor = conn.cursor()

    sql = 'SELECT * FROM customers LIMIT 5'

    cursor.execute(sql)

    result = cursor.fetchone()

    print(result)

    cursor.close()

    conn.close()
    ```

3. 插入数据

    ```python
    import pymysql

    conn = pymysql.connect(
        host='127.0.0.1', user='root', password='123456', database='demo'
    )

    cursor = conn.cursor()

    sql = 'INSERT INTO customers(name,phone) VALUES(%s,%s)'
    val = ('Wilson', '1388888888')

    cursor.execute(sql, val)

    conn.commit()

    print(cursor.rowcount, " record inserted.")

    cursor.close()

    conn.close()
    ```
