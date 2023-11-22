import streamlit as st

# Global Constant
DIP_SW = ['   ', ' 64', ' 32', ' 16', '  8', '  4', '  2', '  1']

def convert_to_dip_switch(num):
    # Convert given number to binary and store into list
    binary_digits = list("{0:08b}".format(num))

    # Start a new expander for each settings
    with st.beta_expander(f"Настройки за адрес: {num}", expanded=True):
        for i in range(7, -1, -1):
            # Display different messages based on the binary digit
            if binary_digits[i] == '0':
                st.markdown(DIP_SW[i], unsafe_allow_html=True)
                st.markdown(":red_circle: OFF", unsafe_allow_html=True)
            else:
                st.markdown(DIP_SW[i], unsafe_allow_html=True)
                st.markdown(":green_circle: ON", unsafe_allow_html=True)

def app():
    """
    Main App Function
    """
    st.title("Professional DIP Switch Converter")
    st.header("Въведете PROFIBUS адрес:")

    # User Input for PROFIBUS Address
    pb_address = st.number_input('', min_value=0, value=4, step=1)

    # Show the switch settings
    convert_to_dip_switch(pb_address)

if __name__ == "__main__":
    app()
