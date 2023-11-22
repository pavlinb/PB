import streamlit as st

# Global Constant
DIP_SW = ['   ', ' 64', ' 32', ' 16', '  8', '  4', '  2', '  1']

def format_dip_switch(dip_val, color, message):
    """
    Helper function to format the output message for Dip Switch Value.
    """
    return f"{DIP_SW[dip_val]} <span style='color:{color}'><b>{message}</b></span>"

def convert_to_dip_switch(num):
    """
    Convert given number to binary and display corresponding dip switch status.
    """
    # Convert given number to binary and store into list
    binary_digits = list("{0:08b}".format(num))

    # Iterate binary digits backwards
    for i in range(7, -1, -1):
        # Display different messages based on the binary digit
        switch_status = format_dip_switch(i, 'red', 'OFF') if binary_digits[i] == '0' \
                        else format_dip_switch(i, 'green', 'ON')
        st.markdown(switch_status, unsafe_allow_html=True)

def app():
    """
    Main App Function
    """
    st.title("Professional DIP Switch Converter")

    try:
        # User Input for PROFIBUS Address
        pb_address = st.number_input('Въведете PROFIBUS адрес:', min_value=0, value=4, step=1)
        # Show the switch settings
        st.write('Настройки: ')
        convert_to_dip_switch(pb_address)
    except Exception as e:
        # Show error message for any exception
        st.error('Error: ' + str(e))

if __name__ == "__main__":
    app()
