from sklearn.metrics.pairwise import cosine_similarity

def tinh_do_tuong_dong(vecto_cau_hoi, ma_tran_tfidf):
    diem_tuong_dong = cosine_similarity(
        vecto_cau_hoi,
        ma_tran_tfidf
    )[0]

    return diem_tuong_dong
