import random

def temp():
    nhiet_do = random.randint(1, 50)
    print(f"Nhiệt độ hiện tại là: {nhiet_do}")

    if nhiet_do > 30:
        if nhiet_do > 35:
            return "Bật quạt mạnh"
        else:
            return "Bật quạt vừa"
    else:
        return "Tắt quạt"
    
hanh_dong = temp()
print(hanh_dong)