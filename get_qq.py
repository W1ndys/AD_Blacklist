import re
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# 读取input.txt文件内容
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()
    logging.info("成功读取input.txt文件")

# 使用正则表达式提取所有QQ号
qq_numbers = re.findall(r"成员【(\d{7,11})】", content)
logging.info(f"提取到{len(qq_numbers)}个QQ号: {', '.join(qq_numbers)}")

# 将提取的QQ号写入output.txt文件
with open("output.txt", "w", encoding="utf-8") as file:
    for number in qq_numbers:
        file.write(number + "\n")
    logging.info("成功将QQ号写入output.txt文件")
