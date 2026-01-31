# hikarinostudio-tools

ヒカリノスタジオ用ツール集

## create_review_stories.py

LINEチャットからお客様の口コミを抽出し、Instagramストーリーズ用の画像を生成するスクリプト。

### 仕様
- サイズ: 1080 x 1920px（Instagram Stories）
- 背景: 白、口コミボックス: 薄灰色
- 3件ずつ掲載
- Apple絵文字対応（Playwright + WebKit使用）

### 必要なライブラリ
```bash
pip install playwright pillow
playwright install webkit
```

### 使い方
```bash
python3 create_review_stories.py
```

### 出力先
```
~/Desktop/review_stories/
```
