# python-Seq2Seq-model

名大会話コーパスの対話データを Seq2Seq model のために整形するためのプログラム。

# DEMO

input : ..
output : ..

# Features

input, output ファイルにそれぞれわけて作成する。

# Requirement

## application

- Python 3.7.3
- MeCab mecab of 0.996

## Python Install package

- gensim 3.8.3
- mecab 0.996.2
- mecab-python-windows 0.996.3

# Usage

```bash
git clone https://github.com/air-flow/python-Seq2Seq-corpus.git
python main.py
```

# Note

このプログラムの諸注意事項

[名大会話コーパス](https://mmsrv.ninjal.ac.jp/nucc/)の文字化資料をダウンロードして任意の場所に配置している。
プログラム中の、`path`に該当パスを入れてください。

## MeCab

MeCab の辞書に、NEologd を使用してます。

## Works Cited

[Keras で実装する Seq2Seq 　－その１　日本語訓練データの準備](https://qiita.com/gacky01/items/26cd642731e3eddde60d)
