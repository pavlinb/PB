import streamlit as st

def dip_sw_convert(num):
    binary_digits = list("{0:08b}".format(num))
    for i in range(7, -1, -1):
        if binary_digits[i] == '0':
            binary_digits[i] = '  OFF'
            st.write(dip_sw[i], binary_digits[i])
        else:
            binary_digits[i] = 'ON'
            st.write(dip_sw[i], '\033[32m' + binary_digits[i] + '\x1b[0m')
    return binary_digits

# Streamlit app code
st.title("DIP Switch Converter")

while True:
    try:
        pb_adr = st.number_input('Enter PROFIBUS address:', value=0, step=1)       
    except ValueError:
        st.warning("Enter a valid integer.")
        continue
    else:
        break

st.write('Settings:\n')
dip_sw_convert(pb_adr)
