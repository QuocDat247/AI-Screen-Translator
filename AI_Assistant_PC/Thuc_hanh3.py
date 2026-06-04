import random

def mua_do_an():
    doi = random.choice([True, False])
    tien = random.randint(1, 100)
    print(f"Có đói không: {doi}, số tiền đang có: {tien}")

    if doi:
        if tien >= 50:
            return "Ăn ngon"
        else:
            return "Ăn tạm"
    else:
        return "Không ăn"

hanh_dong = mua_do_an()
print(hanh_dong)