import re

# 读取input.txt文件内容
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()

# 使用正则表达式提取所有QQ号
qq_numbers = re.findall(r"成员【(\d{7,11})】", content)

# 将提取的QQ号写入output.txt文件
with open("output.txt", "w", encoding="utf-8") as file:
    for number in qq_numbers:
        file.write(number + "\n")
