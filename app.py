
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Bảng điểm và kết quả học tập của 10 sinh viên.")

# Tao du lieu
data = {
    "Họ tên": [
        "Nguyễn Văn An", "Trần Thị Bình",
        "Lê Hoàng Nam", "Phạm Minh Anh",
        "Hoàng Gia Huy", "Võ Thị Lan",
        "Đặng Quốc Bảo", "Bùi Ngọc Mai",
        "Đỗ Thành Công", "Nguyễn Thùy Linh"
    ],
    "Chuyên cần": [9, 8, 10, 7, 9, 8, 6, 10, 7, 9],
    "Giữa kỳ":    [8, 7, 9, 6, 8, 8, 7, 9, 6, 10],
    "Cuối kỳ":    [9, 8, 8, 7, 9, 7, 8, 10, 7, 9]
}

df = pd.DataFrame(data)

# Tinh diem tong ket
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
)

# Xep loai
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# Bang diem
st.subheader("1. Bảng điểm 10 sinh viên")
st.dataframe(
    df.round({"Tổng kết": 2}),
    use_container_width=True,
    hide_index=True
)

# Thong ke
st.subheader("2. Thống kê lớp")

diem_tb = df["Tổng kết"].mean()
diem_max = df["Tổng kết"].max()
diem_min = df["Tổng kết"].min()

c1, c2, c3 = st.columns(3)
c1.metric("Điểm trung bình", f"{diem_tb:.2f}")
c2.metric("Điểm cao nhất", f"{diem_max:.2f}")
c3.metric("Điểm thấp nhất", f"{diem_min:.2f}")

st.write("**Sinh viên có điểm cao nhất:**")
st.write(df.loc[df["Tổng kết"] == diem_max, "Họ tên"].to_list())

st.write("**Sinh viên có điểm thấp nhất:**")
st.write(df.loc[df["Tổng kết"] == diem_min, "Họ tên"].to_list())

so_sv_dat = int((df["Tổng kết"] >= 5).sum())
st.write(f"**Số sinh viên đạt từ 5 điểm:** {so_sv_dat}/10")

# Chon sinh vien
st.subheader("3. Tra cứu điểm cá nhân")

ten = st.selectbox("Chọn sinh viên", df["Họ tên"])
sv = df[df["Họ tên"] == ten].iloc[0]

c1, c2, c3 = st.columns(3)
c1.metric("Chuyên cần", f"{sv['Chuyên cần']:.1f}")
c2.metric("Giữa kỳ", f"{sv['Giữa kỳ']:.1f}")
c3.metric("Cuối kỳ", f"{sv['Cuối kỳ']:.1f}")

c4, c5 = st.columns(2)
c4.metric("Điểm tổng kết", f"{sv['Tổng kết']:.2f}")
c5.metric("Xếp loại", sv["Xếp loại"])

# Bieu do
st.subheader("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Họ tên"], df["Tổng kết"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", rotation=45)
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# Thong tin nguoi tao
st.divider()
st.caption("Người tạo ứng dụng: Bùi Duy Cường")
st.caption("MSSV: 060208004562")
