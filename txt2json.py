import json

# 读取文件内容
with open("qq.txt", "r") as file:
    lines = file.readlines()

# 去除每行的换行符并转换为整数
qq_numbers = [str(line.strip()) for line in lines]

# 将数据转换为JSON格式
qq_json = json.dumps(qq_numbers, indent=4)

# 将JSON数据写入文件
with open("qq.json", "w") as json_file:
    json_file.write(qq_json)

print("转换完成，数据已写入qq.json文件")
