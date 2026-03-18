# Caesar Cipher.py
import nltk
import string
from nltk.corpus import brown
from collections import Counter
from nltk.tokenize import word_tokenize

nltk.download('brown')
nltk.download('universal_tagset')

words = brown.words()
word_freq = Counter(words)
top_5000 = [word for word, freq in word_freq.most_common(5000)]

while True:
    print("\n请选择操作：")
    print("1. 加密")
    print("2. 解密")
    print("3. 暴力破解（0-25所有偏移）")
    choice = input("输入数字(1/2/3): ")

    if choice == '3':  # 暴力破解
        message = input("请输入要破解的密文: ")
        print("\n尝试所有可能的偏移量：")
        for k in range(26):
            result = ""
            for char in message:
                if char.isupper():
                    result += chr((ord(char) - ord('A') - k) % 26 + ord('A'))
                elif char.islower():
                    result += chr((ord(char) - ord('a') - k) % 26 + ord('a'))
                else:
                    result += char

            clean_text = ''.join(
                char for char in result if char not in string.punctuation)
            tokens = word_tokenize(clean_text)
            if len(set(top_5000) & set(tokens)) > 0:
                print("*******以下为可能有意义的结果*******")
            print(f"偏移量 {k:2d}: {result} \n")
    else:  # 加密或解密
        if choice == '1':
            mode = "加密"
        else:
            mode = "解密"
        message = input("请输入要处理的文本: ")
        shift = int(input("请输入移位值(整数): "))

        # 解密时移位取反
        if mode == "解密":
            shift = -shift

        result = ""
        for char in message:
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += char

        print("结果:", result)

    # 询问是否继续
    again = input("\n是否继续？(y/n): ")
    if again.lower() != 'y':
        break

input("按回车键退出...")
