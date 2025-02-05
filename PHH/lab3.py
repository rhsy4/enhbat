
hicheel1 = input("Хичээл 1-ийн нэр: ")
hicheel2 = input("Хичээл 2-ийн нэр: ")
index = int(input("Хичээл 1-ийн нэрэнд Хичээл 2-ын ямар дугаарт байгаа үсгийг хайх вэ?: "))

if 1 <= index <= len(hicheel2):
    searching_letter = hicheel2[index - 1]  # Python-д индекс 0-с эхэлдэг тул -1 хийнэ
    found_index = hicheel1.find(searching_letter) + 1  # 1-ээс эхлэн тоолох

    if found_index:
        print(f"{index} дугаар дахь '{searching_letter}' үсэг хичээл 1-ийн нэрэнд {found_index} дугаар дээр олдлоо.")
    else:
        print(f"{index} дугаар дахь '{searching_letter}' үсэг хичээл 1-ийн нэрэнд олдсонгүй.")
else:
    print("Алдаа: Оруулсан байрлал хичээл 2-ийн нэрний уртаас хэтэрсэн байна.")
