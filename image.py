import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Mengatur judul aplikasi
st.title("Loan Application Dashboard")

# Sidebar untuk navigasi
menu = st.sidebar.selectbox("Select Page", ["Home", "Dataset", "Visualization"])

# Halaman Home
if menu == "Home":
    st.header("Welcome to the Loan Application Dashboard!")
    # Menampilkan gambar (ganti path sesuai lokasi file)
    st.image("D:/hariini/Screenshot 2024-11-26 094810.png", caption="Loan Application", use_column_width=True)

# Halaman Dataset
elif menu == "Dataset":
    st.header("Dataset")
    # Membuat dataset contoh
    data = pd.DataFrame({
        "Loan_ID": ["LP001002", "LP001003", "LP001005", "LP001006", "LP001008"],
        "Gender": ["Male", "Male", "Male", "Male", "Male"],
        "Married": ["No", "Yes", "Yes", "Yes", "No"],
        "Dependents": [0, 1, 0, 0, 0],
        "Education": ["Graduate", "Graduate", "Graduate", "Graduate", "Not Graduate"],
        "Self_Employed": ["No", "Yes", "No", "No", "No"],
        "ApplicantIncome": [5849, 4583, 3000, 2583, 6000],
        "LoanAmount": [None, 128, 66, 120, 141],
    })

    # Menangani missing data pada kolom LoanAmount
    data['LoanAmount'].fillna(data['LoanAmount'].median(), inplace=True)

    # Menampilkan dataset
    st.write("Dataset: (Missing values handled)")
    st.dataframe(data)

# Halaman Visualization
elif menu == "Visualization":
    st.header("Applicant Income VS Loan Amount")
    # Dataset yang sama dengan halaman dataset
    data = pd.DataFrame({
        "Loan_ID": ["LP001002", "LP001003", "LP001005", "LP001006", "LP001008"],
        "Gender": ["Male", "Male", "Male", "Male", "Male"],
        "Married": ["No", "Yes", "Yes", "Yes", "No"],
        "Dependents": [0, 1, 0, 0, 0],
        "Education": ["Graduate", "Graduate", "Graduate", "Graduate", "Not Graduate"],
        "Self_Employed": ["No", "Yes", "No", "No", "No"],
        "ApplicantIncome": [5849, 4583, 3000, 2583, 6000],
        "LoanAmount": [None, 128, 66, 120, 141],
    })

    # Menangani missing data pada kolom LoanAmount
    data['LoanAmount'].fillna(data['LoanAmount'].median(), inplace=True)

    # Plot grafik
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Menggambar bar chart untuk Applicant Income dan Loan Amount
    ax.bar(data["Loan_ID"], data["ApplicantIncome"], label="Applicant Income", width=0.4, align='center', color='blue')
    ax.bar(data["Loan_ID"], data["LoanAmount"], label="Loan Amount", width=0.4, align='edge', color='orange')

    # Mengatur label dan judul grafik
    ax.set_xlabel("Loan ID")
    ax.set_ylabel("Value")
    ax.set_title("Applicant Income VS Loan Amount")
    ax.legend()

    # Menampilkan grafik
    st.pyplot(fig)

    # Menampilkan informasi lebih lanjut tentang visualisasi
    st.write("""
    Grafik di atas menunjukkan perbandingan antara **Income Pemohon** dan **Jumlah Pinjaman** yang diajukan. 
    Bar biru menunjukkan penghasilan pemohon, sementara bar oranye menunjukkan jumlah pinjaman yang diajukan. 
    Hal ini dapat membantu dalam analisis hubungan antara penghasilan pemohon dan besaran pinjaman yang disetujui.
    """)
