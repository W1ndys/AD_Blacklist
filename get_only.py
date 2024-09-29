# 读取qq.txt文件
with open("qq.txt", "r") as file:
    qq_numbers = file.readlines()

# 去除重复的QQ号并排序
unique_qq_numbers = sorted(set(qq.strip() for qq in qq_numbers))

# 将去重后的QQ号写回文件
with open("qq.txt", "w") as file:
    for qq in unique_qq_numbers:
        file.write(f"{qq}\n")
