import random

def game_chien_dau():
    co_ke_dich = random.choice([True, False])
    mau = random.randint(0, 100)
    print(f"Có kẻ dịch không: {co_ke_dich}, máu bao nhiêu: {mau}")

    if co_ke_dich:
        if mau < 30:
            return "Chạy trốn"
        else:
            return "Tấn công"
    else:
        return "Đi tuần"

hanh_dong = game_chien_dau()
print(hanh_dong)