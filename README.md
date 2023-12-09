[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## オープンソースソフトウェアに関するライセンス表記
使用したオープンソースソフトウェアに関するライセンスはthird-party-licenseディレクトリ内にあります。

## インストール方法
```bash
pip install ezLineNotify
```

## 使用方法
```python
from ezLineNotify import LineNotify, ImageURLs, Image, Sticker

line = LineNotify("LineNotifyのトークン")

#テキストの送信
line.send("Pythonからのメッセージ")

#写真の送信(URLから)
line.send("テキスト以外を送信する場合でもテキストは必須です", image=ImageURLs("サムネイルファイルのURL", "タップしたときに表示されるオリジナルファイルのURL"))

#写真の送信(ファイルから)
line.send("テキスト以外を送信する場合でもテキストは必須です", image=Image("画像ファイルのパス"))

#スタンプの送信 (スタンプのパッケージIDやIDはこちらから確認可能: https://developers.line.biz/ja/docs/messaging-api/sticker-list/)
line.send("テキスト以外を送信する場合でもテキストは必須です", sticker=Sticker(package_id=789, id=10859))

#通知を送らずに送信
line.send("このメッセージはサイレント送信されます", silent=True)
```
