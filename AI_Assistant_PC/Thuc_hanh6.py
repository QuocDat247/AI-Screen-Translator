import random

def robot_tuoi_cay():
    troi_mua = random.choice([True, False])

    if not troi_mua:
        do_am_dat = random.randint(10, 60)
    else:
        do_am_dat = random.randint(50, 80)

    gio_trong_ngay = random.randint(0, 23)
    print(f"""Trời mưa: {troi_mua}
            Độ ẩm đất: {do_am_dat}
            Giờ trong ngày: {gio_trong_ngay}""")
    
    if troi_mua:
        return "Không tưới"
    else:
        if do_am_dat < 30:
            if gio_trong_ngay < 18:
                return "Tưới nhiều"
            else:
                return "Tưới ít"
        else:
            return "Không tưới"
        
hanh_dong = robot_tuoi_cay()
print(hanh_dong)