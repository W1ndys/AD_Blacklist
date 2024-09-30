# AD_Blacklist

用于存放迎新时期发现的违规广告 QQ 号

**欢迎各位师傅 Pull Request**

有误报的请及时反馈。

## 黑名单 QQ

- [qq.txt](./qq.txt)
- [qq.json](./qq.json)
- [qq.db](./qq.db)

## Pull Request 须知

请将 QQ 号添加到 `qq.txt` 文件中，并确保每行一个 QQ 号，格式如下：

```
2373913403
2398872365
2399421613
2446498651
```

推送后，GitHub Action 会自动整理删除重复 QQ，并生成对应的 db 和 json 文件。

Pull Request 时请附上证明材料，如违规截图、链接等。

## Python 脚本解释

- [txt2json.py](./txt2json.py): 将 `qq.txt` 文件转换为 `qq.json` 文件。
- [txt2db.py](./txt2db.py): 将 `qq.txt` 文件转换为 `qq.db` 文件。
  
### 数据库说明

- [qq.db](./qq.db): 一个 SQLite 数据库，包含所有的 QQ 号。

### 下载压缩包

[点击下载](https://github.com/W1ndys/AD_Blacklist/archive/refs/heads/main.zip)

