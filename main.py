import streamlit as st

dip_sw = ['   ', ' 64', ' 32', ' 16', '  8', '  4', '  2', '  1']

def dip_sw_convert(num):
    binary_digits = list("{0:08b}".format(num))
    for i in range(7, -1, -1):
        if binary_digits[i] == '0':
            binary_digits[i] = 'OFF'
            st.markdown(f"{dip_sw[i]} <span style='color:red; margin-left: 20px'><b>{binary_digits[i]}</b></span>", unsafe_allow_html=True)
        else:
            binary_digits[i] = 'ON'
            st.markdown(f"{dip_sw[i]} <span style='color:green'><b>{binary_digits[i]}</b></span>", unsafe_allow_html=True)
    return binary_digits

# Streamlit app code
st.title("DIP Switch Converter")

while True:
    try:
        pb_adr = st.number_input('Enter PROFIBUS address:', value=0, step=1, format="%d", min_value=0, max_value=126, key="pb_adr", help="3-digit number")       
    except ValueError:
        st.warning("Enter a valid integer.")
        continue
    else:
        if 0 <= pb_adr <= 126:
            break
        else:
            st.warning("Enter a valid 3-digit number.")

st.write('Settings:\n')
dip_sw_convert(pb_adr)
