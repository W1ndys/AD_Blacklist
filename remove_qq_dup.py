import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# 读取qq.txt文件
with open("qq.txt", "r") as file:
    qq_numbers = file.readlines()
    logging.info("成功读取qq.txt文件")

# 去除重复的QQ号并排序
unique_qq_numbers = sorted(set(qq.strip() for qq in qq_numbers))
logging.info(f"去重后剩余{len(unique_qq_numbers)}个QQ号")

# 将去重后的QQ号写回文件
with open("qq.txt", "w") as file:
    for qq in unique_qq_numbers:
        file.write(f"{qq}\n")
    logging.info("成功将去重后的QQ号写回qq.txt文件")
