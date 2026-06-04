import random

def mua_hang():
    co_giam_gia = random.choice(["Có", "Không"])
    ngan_sach = random.randint(1, 100)
    if co_giam_gia == "Có":
        muc_giam = random.randint(10, 100)
    else:
        muc_giam = 0

    print(f"""Có giảm giá không: {co_giam_gia}
            Mức giảm là: {muc_giam}
            Ngân sách hiện tại: {ngan_sach}""")
    
    if co_giam_gia == "Không":
        return "Không mua"
    else:
        if muc_giam >= 30:
            if ngan_sach >= 50:
                return "Mua nhiều"
            else:
                return "Mua ít"
        else:
            return "Mua ít"

hanh_dong = mua_hang()
print(hanh_dong)