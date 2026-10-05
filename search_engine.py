from preprocessing import tien_xu_ly
from keyphrase_engine import (
    trich_xuat_tu_khoa,
    chuan_hoa_tu_khoa
)
from similarity import tinh_do_tuong_dong

class BoTimKiem:
    def __init__(
        self,
        danh_sach_dieu_luat,
        bo_vector_tfidf
    ):
        self.danh_sach_dieu_luat = danh_sach_dieu_luat
        self.bo_vector_tfidf = bo_vector_tfidf

        self.bang_dieu_luat = {}

        for dieu_luat in danh_sach_dieu_luat:
            ma_dieu = dieu_luat.get(
                "article_id",
                ""
            )

            self.bang_dieu_luat[ma_dieu] = dieu_luat

    def tim_kiem(
        self,
        cau_hoi,
        so_luong_ket_qua=6,
        trong_so_tu_khoa=0.3
    ):
        cau_hoi_da_xu_ly = tien_xu_ly(cau_hoi)

        tu_khoa_tim_duoc = trich_xuat_tu_khoa(
            cau_hoi_da_xu_ly
        )

        vecto_cau_hoi = (
            self.bo_vector_tfidf
            .chuyen_cau_hoi_thanh_vecto(
                cau_hoi_da_xu_ly
            )
        )

        diem_cosine = tinh_do_tuong_dong(
            vecto_cau_hoi,
            self.bo_vector_tfidf.ma_tran_tfidf
        )

        danh_sach_ket_qua = []

        for vi_tri, diem_co_so in enumerate(diem_cosine):
            ma_dieu = (
                self.bo_vector_tfidf
                .danh_sach_ma_dieu[vi_tri]
            )

            dieu_luat = self.bang_dieu_luat.get(
                ma_dieu
            )

            if dieu_luat is None:
                continue

            danh_sach_tu_khoa_dieu_luat = [
                chuan_hoa_tu_khoa(tu_khoa)
                for tu_khoa in dieu_luat.get(
                    "keyphrases",
                    []
                )
            ]

            so_tu_khoa_khop = 0

            for tu_khoa in tu_khoa_tim_duoc:
                if (
                    chuan_hoa_tu_khoa(tu_khoa)
                    in danh_sach_tu_khoa_dieu_luat
                ):
                    so_tu_khoa_khop += 1

            if tu_khoa_tim_duoc:
                diem_tu_khoa = (
                    so_tu_khoa_khop
                    / len(tu_khoa_tim_duoc)
                )
            else:
                diem_tu_khoa = 0.0

            diem_tong_hop = (
                (1 - trong_so_tu_khoa)
                * float(diem_co_so)
                + trong_so_tu_khoa
                * diem_tu_khoa
            )

            if diem_tong_hop > 0.02:
                ket_qua_dieu_luat = dict(dieu_luat)

                ket_qua_dieu_luat["score"] = round(
                    diem_tong_hop,
                    4
                )

                ket_qua_dieu_luat["cosine_score"] = round(
                    float(diem_co_so),
                    4
                )

                ket_qua_dieu_luat["keyphrase_score"] = round(
                    diem_tu_khoa,
                    4
                )

                ket_qua_dieu_luat[
                    "matched_keyphrases"
                ] = [
                    tu_khoa
                    for tu_khoa in tu_khoa_tim_duoc
                    if chuan_hoa_tu_khoa(tu_khoa)
                    in danh_sach_tu_khoa_dieu_luat
                ]

                danh_sach_ket_qua.append(
                    ket_qua_dieu_luat
                )

        danh_sach_ket_qua.sort(
            key=lambda dieu_luat: dieu_luat["score"],
            reverse=True
        )

        return danh_sach_ket_qua[
            :so_luong_ket_qua
        ]
