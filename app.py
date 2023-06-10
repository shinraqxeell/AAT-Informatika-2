import streamlit as st

# Title Web Page
st.set_page_config (page_title= "Pencarian Ganjil Dan Genap", page_icon=":book:", layout="wide"  )

def check_odd_even(number):
    if number % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

# Streamlit app code
def main():
    st.markdown ("<h4 style='text-align: center; color: white;'> Pengecekan Angka Ganjil Dan Genap Sebuah Angka </h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white;'> | Muhammad Wildan Hamid X-4 SMAN 103 Jakarta | </h4>", unsafe_allow_html=True)
    st.divider()

    st.markdown ("<h5 style='text-align: center; color: white;'> Masukan Angka </h5>", unsafe_allow_html=True)

    # User input
    number = st.number_input("", value=0, step=1)

    # Check odd/even
    result = check_odd_even(number)

    # Display result
    st.write(f" Angka Tersebut {number} Merupakan Bilangan {result}.")

if __name__ == "__main__":
    main()