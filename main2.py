import streamlit as st

dip_sw = ['   ', ' 64', ' 32', ' 16', '  8', '  4', '  2', '  1']


def dip_sw_convert(num):
    binary_digits = list("{0:08b}".format(num))
    for i in range(7, -1, -1):
        if binary_digits[i] == '0':
            binary_digits[i] = 'OFF'
            #st.markdown(f"{dip_sw[i]} <span style='color:red; margin-left: 20px'><b>{binary_digits[i]}</b></span>", unsafe_allow_html=True)
            on = st.toggle(f'{dip_sw[i]}', value=True, key = i)
        else:
            binary_digits[i] = 'ON'
            #st.markdown(f"{dip_sw[i]} <span style='color:green'><b>{binary_digits[i]}</b></span>", unsafe_allow_html=True)
            on = st.toggle(f'{dip_sw[i]}', value=False, key = i)
    return binary_digits

# Streamlit app code
st.title("DIP Switch Converter")

while True:
    try:
        pb_adr = st.number_input('Въведете PROFIBUS адрес:', min_value=0, max_value=126, value=4, step=1)       
    except ValueError:
        st.warning("Въведете цяло число.")
        continue
    else:
        break

st.write('Настройки:\n')
#on = st.toggle('', value=False)
dip_sw_convert(pb_adr)
#st.balloons()
#st.snow()
