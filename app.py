import streamlit as st

from backend_api import BoXuLyBackend

# Khai báo tên trang web
st.set_page_config(
    page_title="Tra cứu Luật Giao thông",
    page_icon="⚖️",
    layout="wide"
)

@st.cache_resource
def khoi_tao_backend():
    """Lấy dữ liệu từ backend_api.py"""

    bo_backend = BoXuLyBackend(
        "data/law_database.json"
    )
    return bo_backend

bo_backend = khoi_tao_backend()

# Tiêu đề giao diện Streamlit
st.title("⚖️ Hệ thống tra cứu Luật Giao thông")

st.write(
    "Nhập câu hỏi hoặc tình huống giao thông "
    "để tìm các quy định pháp luật phù hợp."
)

# Ô nhập câu hỏi
cau_hoi = st.text_input(
    "Nhập câu hỏi:",
    placeholder="Ví dụ: Mức phạt khi xe máy vượt đèn đỏ là bao nhiêu?"
)

# Nút tra cứu
if st.button(
    "🔎 Tra cứu ngay",
    type="primary"
):
    # Kiểm tra điều kiện khi nhấn nút tra cứu
    if not cau_hoi.strip():

        # Cảnh báo lỗi khi ô nhập rỗng
        st.warning(
            "Vui lòng nhập câu hỏi trước khi tra cứu."
        )

    else:

        ket_qua_tra_cuu = (
            bo_backend.xu_ly_yeu_cau_tra_cuu(cau_hoi)
        )

        # Nếu không ó kết quả trả về
        if not ket_qua_tra_cuu["success"]:

            st.error(
                "Không thể thực hiện tra cứu."
            )

        else: # Tìm thấy các kết quả

            danh_sach_ket_qua = (
                ket_qua_tra_cuu["data"]
            )

            st.success(
                f"Tìm thấy {len(danh_sach_ket_qua)} "
                f"kết quả phù hợp."
            )

            if len(danh_sach_ket_qua) == 0:

                st.info(
                    "Không tìm thấy quy định pháp luật "
                    "phù hợp với câu hỏi."
                )

            for so_thu_tu, dieu_luat in enumerate(
                danh_sach_ket_qua,
                start=1
            ):

                with st.container():

                    st.subheader(
                        # Nếu tittle rỗng thì lấy mặc định là "Không có tiêu đề"
                        f"{so_thu_tu}. "
                        f"{dieu_luat.get('title', 'Không có tiêu đề')}"
                    )

                    st.write(
                        f"**Văn bản:** "
                        f"{dieu_luat.get('law_name', 'Không có')}"
                    )

                    st.write(
                        f"**Mã điều luật:** "
                        f"{dieu_luat.get('article_id', 'Không có')}"
                    )

                    st.write(
                        f"**Căn cứ pháp lý:** "
                        f"{dieu_luat.get("law_code","Không có thông tin")}"
                    )

                    st.write(
                        "**Nội dung quy định:**"
                    )

                    st.write(
                        dieu_luat.get(
                            "content_raw",
                            "Không có nội dung"
                        )
                    )

                    # Thông tin xử phạt
                    danh_sach_muc_phat = (
                        dieu_luat.get("penalties",[])
                    )

                    if danh_sach_muc_phat:

                        st.write(
                            "**Thông tin xử phạt:**"
                        )

                        for muc_phat in danh_sach_muc_phat:

                            loai_phuong_tien = (
                                muc_phat.get(
                                    "vehicle_type",
                                    "Không xác định"
                                )
                            )

                            muc_phat_toi_thieu = (
                                muc_phat.get(
                                    "min_fine",
                                    ""
                                )
                            )

                            muc_phat_toi_da = (
                                muc_phat.get(
                                    "max_fine",
                                    ""
                                )
                            )

                            tru_diem = (
                                muc_phat.get(
                                    "point_deduction",
                                    ""
                                )
                            )

                            hinh_thuc_bo_sung = (
                                muc_phat.get(
                                    "additional_penalty",
                                    ""
                                )
                            )

                            co_so_phap_ly = (
                                muc_phat.get(
                                    "legal_basis",
                                    ""
                                )
                            )

                            st.write(
                                f"- **Phương tiện:** "
                                f"{loai_phuong_tien}"
                            )

                            st.write(
                                f"- **Mức phạt:** "
                                f"{muc_phat_toi_thieu} "
                                f"đến "
                                f"{muc_phat_toi_da} đồng"
                            )

                            if tru_diem != "":

                                st.write(
                                    f"- **Trừ điểm GPLX:** "
                                    f"{tru_diem}"
                                )

                            if hinh_thuc_bo_sung:

                                st.write(
                                    f"- **Xử phạt bổ sung:** "
                                    f"{hinh_thuc_bo_sung}"
                                )

                            if co_so_phap_ly:

                                st.write(
                                    f"- **Căn cứ xử phạt:** "
                                    f"{co_so_phap_ly}"
                                )

                    # Lấy Điểm phù hợp (Cosine + phrase)            
                    diem_tong_hop = dieu_luat.get("score", 0)
                    
                    diem_cosine = dieu_luat.get("cosine_score", 0)
                    
                    diem_tu_khoa = dieu_luat.get("keyphrase_score", 0)

                    # In các giá trị
                    st.write(f"**Điểm phù hợp:** "
                            f"{diem_tong_hop * 100:.2f}%"
                    )
                    
                    st.write(
                            f"- Điểm Cosine Similarity: "
                            f"{diem_cosine:.4f}"
                    )
                    
                    st.write(
                            f"- Điểm từ khóa: "
                            f"{diem_tu_khoa:.4f}"
                    )
                    
                    danh_sach_tu_khoa_khop = (
                        dieu_luat.get("matched_keyphrases",[])
                    )
                    
                    if danh_sach_tu_khoa_khop:
                    
                        st.write(
                            "**Từ khóa tìm thấy:** "
                            + ", ".join(danh_sach_tu_khoa_khop)
                        )

                    st.divider()
