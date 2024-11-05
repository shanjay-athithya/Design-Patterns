from langdetect import detect

text = "du bist?"

detected_language = detect(text)
print(detected_language)
