print("歡迎使用論文翻譯機!\n請稍候片刻...")
import googletrans
import sys

translator = googletrans.Translator()

print("請貼上PDF段落，接著按下Enter鍵，接著按下Ctrl+D鍵")
print("請在以下貼上內容:")
while True:
    en_str_list = sys.stdin.readlines()
    en_str = " ".join(en_str_list)
    en_str = en_str.replace("\n", "")
    # print(en_str)
    tw_str = translator.translate(en_str, dest='zh-TW').text
    print(tw_str, "\n")
    print("請在以下貼上內容:")