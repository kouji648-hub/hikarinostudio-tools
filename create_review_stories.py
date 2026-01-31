#!/usr/bin/env python3
"""
Instagramストーリーズ用の口コミ画像を生成
サンプル画像に忠実に再現
"""

import asyncio
import os
import random
from playwright.async_api import async_playwright

# 口コミデータ（原文・絵文字付き）
reviews_raw = [
    {
        "text": "とっても素敵なお写真ありがとうございます！！<br>たくさんアンパンマンであやしてくださったおかげでニコニコで過ごせて良かったです！<br>早速待ち受けにしました。可愛すぎます。雰囲気最高でした。",
    },
    {
        "text": "素敵な写真をたくさん撮っていただきありがとうございました🙇‍♀️♡♡<br>写真全部良すぎて感動しました( ; ; )✨<br>本当にありがとうございました😭♡♡♡♡",
    },
    {
        "text": "可愛すぎる撮影をありがとうございました☺️✨<br>むすめたちの最高の笑顔、可愛い姿、はじめてのお化粧して女の子になったすがたを見せていただきありがとうございました🕊️<br>最高な撮影時間に感激です😌",
    },
    {
        "text": "撮影ありがとうございました！両親から連絡がありカメラマンさんが素敵に撮ってくださっていたと喜んでおりました😊<br>急な日程でのお願いに応えてくださりありがとうございました✨✨",
    },
    {
        "text": "こちらこそ七五三の撮影をして頂きありがとうございました🙇‍♀️✨<br>初めての袴と着物で機嫌がもつか心配でしたが、無事に撮影が出来て良かったです！！",
    },
    {
        "text": "素敵な写真をたくさんありがとうございました😊<br>また機会がありましたらよろしくお願いします🙏",
    },
    {
        "text": "最後まで楽しく撮影ができて本当に良かったです😋⭐️",
    },
    {
        "text": "楽しい撮影時間をありがとうございました🙇‍♀️<br>また機会があればよろしくお願いします🫶",
    },
    {
        "text": "こちらこそ楽しく撮影できました🥰<br>またお願いするときはよろしくお願いしますね🙏<br>ありがとうございました✨",
    },
    {
        "text": "可愛い写真データをありがとうございます💕💕<br>姉弟２人で撮るのは大変でしたが、すごく楽しい思い出になりました！！",
    },
]

def generate_html(review_list):
    """HTMLテンプレートを生成（参考画像に近い大胆な傾きと配置）"""
    reviews_html = ""
    for i, review in enumerate(review_list):
        rotation = random.uniform(-12, 12)
        offset_x = random.randint(-30, 30)
        reviews_html += f'''
        <div class="review-box" style="transform: rotate({rotation:.1f}deg) translateX({offset_x}px);">
            <div class="review-text">{review["text"]}</div>
        </div>
        '''

    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @font-face {{
                font-family: 'Apple Color Emoji';
                src: local('Apple Color Emoji');
            }}
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                width: 1080px;
                height: 1920px;
                background: #ffffff;
                font-family: "Apple Color Emoji", "Hiragino Kaku Gothic ProN", "Hiragino Sans", -apple-system, BlinkMacSystemFont, sans-serif;
                padding: 80px 50px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                gap: 120px;
            }}
            .review-box {{
                background: #f5f5f5;
                border-radius: 25px;
                padding: 40px 45px;
                position: relative;
            }}
            .review-box::before {{
                content: '';
                position: absolute;
                left: 25px;
                top: 50%;
                transform: translateY(-50%);
                width: 0;
                height: 0;
                border-top: 15px solid transparent;
                border-bottom: 15px solid transparent;
                border-right: 20px solid #f5f5f5;
                margin-left: -20px;
            }}
            .review-text {{
                font-size: 38px;
                color: #333333;
                line-height: 1.7;
            }}
        </style>
    </head>
    <body>
        {reviews_html}
    </body>
    </html>
    '''
    return html

async def create_story_image(review_list, output_path):
    """Playwrightを使って画像を生成"""
    html = generate_html(review_list)

    async with async_playwright() as p:
        browser = await p.webkit.launch()
        page = await browser.new_page(viewport={'width': 1080, 'height': 1920}, device_scale_factor=2)
        await page.set_content(html)
        await page.screenshot(path=output_path, full_page=False)
        await browser.close()

    print(f"Created: {output_path}")

async def main():
    output_dir = os.path.expanduser("~/Desktop/review_stories")
    os.makedirs(output_dir, exist_ok=True)

    for i in range(0, len(reviews_raw), 3):
        group = reviews_raw[i:i+3]
        image_num = (i // 3) + 1
        output_path = os.path.join(output_dir, f"review_story_{image_num}.png")
        await create_story_image(group, output_path)

    print(f"\n完了！{output_dir} に画像を生成しました。")

if __name__ == "__main__":
    asyncio.run(main())
