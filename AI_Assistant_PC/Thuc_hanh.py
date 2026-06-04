import random

def kiem_tra_di_choi():
    troi_mua = random.choice([True, False])
    co_ao_mua = random.choice([True, False])
    print(f"Trời có mưa không: {troi_mua}, Có áo mưa không: {co_ao_mua}")

    if troi_mua:
        if co_ao_mua:
            return "Đi được"
        else:
            return "Không đi"
    else:
        return "Đi bình thường"

hanh_dong = kiem_tra_di_choi()
print(hanh_dong)