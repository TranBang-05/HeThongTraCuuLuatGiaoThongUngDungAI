import re
from pyvi import ViTokenizer

TU_DUNG_TIENG_VIET = {
    "cho", "hỏi", "bị", "là", "những", "các",
    "theo", "tại", "về", "như", "khi", "do", "với"
}

def chuan_hoa_van_ban(van_ban):
    if not isinstance(van_ban, str):
        return ""

    van_ban = van_ban.lower()
    van_ban = re.sub(r"[^\w\s]", " ", van_ban)
    van_ban = re.sub(r"\s+", " ", van_ban)

    return van_ban.strip()

def tien_xu_ly(van_ban):
    if not van_ban:
        return ""

    van_ban = chuan_hoa_van_ban(van_ban)
    van_ban_da_tach_tu = ViTokenizer.tokenize(van_ban)

    danh_sach_tu = van_ban_da_tach_tu.split()
    danh_sach_tu_sau_khi_loc = []

    for tu in danh_sach_tu:
        tu_khong_gach_duoi = tu.replace("_", " ")

        if tu_khong_gach_duoi not in TU_DUNG_TIENG_VIET:
            danh_sach_tu_sau_khi_loc.append(tu)

    van_ban_da_xu_ly = " ".join(
        danh_sach_tu_sau_khi_loc
    ).replace("_", " ")

    return van_ban_da_xu_ly
