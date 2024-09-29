import sqlite3
import os

# 删除原来的数据库文件（如果存在）
db_filename = "qq.db"
if os.path.exists(db_filename):
    os.remove(db_filename)

# 读取文件内容
with open("qq.txt", "r") as file:
    lines = file.readlines()

# 去除每行的换行符并转换为字符串
qq_numbers = [str(line.strip()) for line in lines]

# 连接到SQLite数据库（如果数据库不存在，则会自动创建）
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# 创建表（如果表不存在），并设置qq_number为唯一
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS qq_numbers (
        qq_number TEXT NOT NULL UNIQUE
    )
"""
)

# 插入数据
cursor.executemany(
    "INSERT OR IGNORE INTO qq_numbers (qq_number) VALUES (?)",
    [(num,) for num in qq_numbers],
)

# 提交事务并关闭连接
conn.commit()
conn.close()

print("转换完成，数据已写入qq.db数据库")
