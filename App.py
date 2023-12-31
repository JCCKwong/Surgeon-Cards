import streamlit as st
import PIL.Image
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="UofT Uro Surgeon Cards",
                   page_icon="https://cdn.pixabay.com/photo/2022/09/20/10/27/urology-7467570_1280.png"
                   )

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
logo = PIL.Image.open('images/uofturo.png')

st.title("UofT Urology Surgeon Cards")
st.write('Developed by Jethro Kwong')

# Search by Procedure
procedure_list = df['Procedure'].sort_values(ascending=True).unique()
procedure_select = st.selectbox('Select Procedure', (procedure_list))
staff_list = df[df['Procedure']==procedure_select]['Staff'].sort_values(ascending=True).unique()
staff_select = st.selectbox('Select Staff', (staff_list))

submit = st.button("SUBMIT")
equipment_setup, keysteps, dictation, postop_ccac = st.tabs(["Equipment & Setup", "Key Steps", "Dictation", "Post-op & CCAC"])
if submit:
    filtered_df = df[(df['Procedure'] == procedure_select) & (df['Staff'] == staff_select)].reset_index(drop=True)

    with equipment_setup:
        st.header('Equipment List')
        st.write(filtered_df['Equipment'][0])
        st.header('Setup')
        st.write(filtered_df['Setup'][0])

    with keysteps:
        st.header("Key Steps")
        st.write(filtered_df['Key steps'][0])

    with dictation:
        st.header("Dictation")
        st.write(filtered_df['Dictation'][0])

    with postop_ccac:
        st.header('Post-op Care')
        st.write(filtered_df['Post-op'][0])
        st.header('CCAC')
        st.write(filtered_df['CCAC'][0])

st.image(logo, use_column_width=True)
