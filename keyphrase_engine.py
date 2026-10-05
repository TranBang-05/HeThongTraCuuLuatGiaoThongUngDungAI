import re

TU_KHOA_CHUYEN_NGANH = {
    "PHUONG_TIEN": [
        "xe máy",
        "ô tô",
        "xe đạp",
        "xe tải",
        "container",
        "xe máy chuyên dùng",
        "xe đạp máy",
        "xe mô tô"
    ],
    "HANH_VI_VI_PHAM": [
        "nồng độ cồn",
        "lái xe uống rượu",
        "hơi thở có cồn",
        "quá tốc độ",
        "vượt đèn đỏ",
        "đi ngược chiều",
        "không đội mũ bảo hiểm",
        "ghế trẻ em"
    ],
    "CHE_TAI": [
        "phạt tiền",
        "mức phạt",
        "trừ điểm gplx",
        "tước bằng lái",
        "tạm giữ xe",
        "thu hồi biển số"
    ],
    "HA_TANG_BIEN_BAO": [
        "đường cao tốc",
        "biển báo cấm",
        "vạch kẻ đường",
        "làn đường",
        "biển định danh"
    ]
}

def chuan_hoa_tu_khoa(tu_khoa):
    tu_khoa = tu_khoa.lower()
    tu_khoa = re.sub(r"[^\w\s]", " ", tu_khoa)
    tu_khoa = re.sub(r"\s+", " ", tu_khoa)

    return tu_khoa.strip()

def trich_xuat_tu_khoa(cau_hoi):
    cau_hoi = chuan_hoa_tu_khoa(cau_hoi)
    danh_sach_tu_khoa = []

    for nhom_tu_khoa in TU_KHOA_CHUYEN_NGANH.values():
        for tu_khoa in nhom_tu_khoa:
            tu_khoa_da_chuan_hoa = chuan_hoa_tu_khoa(tu_khoa)

            if tu_khoa_da_chuan_hoa in cau_hoi:
                danh_sach_tu_khoa.append(tu_khoa_da_chuan_hoa)

    return danh_sach_tu_khoa

def tinh_diem_tu_khoa(cau_hoi, danh_sach_tu_khoa):
    if not danh_sach_tu_khoa:
        return 0.0

    cau_hoi = chuan_hoa_tu_khoa(cau_hoi)
    so_tu_khoa_khop = 0

    for tu_khoa in danh_sach_tu_khoa:
        tu_khoa = chuan_hoa_tu_khoa(tu_khoa)

        if tu_khoa in cau_hoi:
            so_tu_khoa_khop += 1

    return so_tu_khoa_khop / len(danh_sach_tu_khoa)
