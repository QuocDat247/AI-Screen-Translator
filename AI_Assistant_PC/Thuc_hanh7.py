import random

def agent_giai_thich():
    co_giam_gia = random.choice([True, False])
    muc_giam = random.randint(10, 100) if co_giam_gia else 0
    muc_do = random.choice(["ngan", "chi_tiet"])

    print(f"""Giảm giá: {co_giam_gia}
Mức giảm: {muc_giam}%
Mức độ: {muc_do}""")

    # 1. Quyết định
    if not co_giam_gia:
        ket_qua = "Không mua"
    elif muc_giam >= 30:
        ket_qua = "Mua nhiều"
    else:
        ket_qua = "Mua ít"

    # 2. Giải thích
    if muc_do == "chi_tiet":
        if ket_qua == "Không mua":
            giai_thich = "Vì không có giảm giá."
        elif ket_qua == "Mua ít":
            giai_thich = f"Vì giảm {muc_giam}% chưa đủ hấp dẫn."
        else:
            giai_thich = f"Vì giảm {muc_giam}% là mức cao."

        ket_qua = f"{ket_qua} - {giai_thich}"

    return ket_qua

print("Agent quyết định:", agent_giai_thich())