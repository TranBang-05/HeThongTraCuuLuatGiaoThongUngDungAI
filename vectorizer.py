from sklearn.feature_extraction.text import TfidfVectorizer

class BoVectorTFIDF:
    def __init__(self):
        self.bo_chuyen_doi = TfidfVectorizer(
            ngram_range=(1, 2),
            min_df=1,
            max_df=0.9
        )

        self.ma_tran_tfidf = None
        self.danh_sach_ma_dieu = []

    def hoc_du_lieu(self, danh_sach_van_ban, danh_sach_ma_dieu):
        self.ma_tran_tfidf = self.bo_chuyen_doi.fit_transform(
            danh_sach_van_ban
        )

        self.danh_sach_ma_dieu = danh_sach_ma_dieu

        return self.ma_tran_tfidf

    def chuyen_cau_hoi_thanh_vecto(self, cau_hoi):
        if self.ma_tran_tfidf is None:
            raise ValueError(
                "Bộ TF-IDF chưa được học dữ liệu."
            )

        return self.bo_chuyen_doi.transform([cau_hoi])
