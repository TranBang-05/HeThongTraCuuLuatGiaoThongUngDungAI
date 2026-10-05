import json

from vectorizer import BoVectorTFIDF
from search_engine import BoTimKiem

class BoXuLyBackend:
    def __init__(
        self,
        duong_dan_co_so_du_lieu="data/law_database.json"
    ):
        self.duong_dan_co_so_du_lieu = (
            duong_dan_co_so_du_lieu
        )

        with open(
            self.duong_dan_co_so_du_lieu,
            "r",
            encoding="utf-8"
        ) as tep_du_lieu:
            self.danh_sach_dieu_luat = json.load(
                tep_du_lieu
            )

        danh_sach_van_ban = []
        danh_sach_ma_dieu = []

        for dieu_luat in self.danh_sach_dieu_luat:
            ma_dieu = dieu_luat.get(
                "article_id",
                ""
            )

            tieu_de = dieu_luat.get(
                "title",
                ""
            )

            noi_dung = dieu_luat.get(
                "content_segmented",
                ""
            )

            danh_sach_tu_khoa = dieu_luat.get(
                "keyphrases",
                []
            )

            chuoi_tu_khoa = " ".join(
                danh_sach_tu_khoa
            )

            van_ban_ket_hop = (
                f"{tieu_de} "
                f"{noi_dung} "
                f"{chuoi_tu_khoa}"
            )

            danh_sach_van_ban.append(
                van_ban_ket_hop
            )

            danh_sach_ma_dieu.append(
                ma_dieu
            )

        self.bo_vector_tfidf = BoVectorTFIDF()

        self.bo_vector_tfidf.hoc_du_lieu(
            danh_sach_van_ban,
            danh_sach_ma_dieu
        )

        self.bo_tim_kiem = BoTimKiem(
            self.danh_sach_dieu_luat,
            self.bo_vector_tfidf
        )

    def xu_ly_yeu_cau_tra_cuu(
        self,
        cau_hoi
    ):
        ket_qua = self.bo_tim_kiem.tim_kiem(
            cau_hoi
        )

        return {
            "success": True,
            "data": ket_qua
        }
