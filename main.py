import streamlit as st

st.set_page_config(
    page_title="JSHIR",
    page_icon="📕",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# st.title("JSHIR Define Generator")
st.markdown("<h1 style='color: rgba(255,26, 202, 0.8); text-align: center; border-radius: 10px; font-family: Helvetica;'>JSHIR Define Generator</h1>", unsafe_allow_html=True)
jshir = st.text_input('JSHIRNI kiriting', max_chars=14, value="31711946030025")

oy_nomlari ={
    1: "Yanvar",
    2: "Fevral",
    3: "Mart",
    4: "Aprel",
    5: "May",
    6: "Iyun",
    7: "Iyul",
    8: "Avgust",
    9: "Sentabr",
    10: "Oktyabr",
    11: "Noyabr",
    12: "Dekabr"   
}

def main():
    if jshir:
        if int(len(jshir))<14:
            st.write("Iltimos 14 tadan kam bo'lmagan belgi kiriting", icon="error")
        else:
            col1, col2 = st.columns([1,3])
            jins = int(jshir[0])
            kun = int(jshir[1]+jshir[2])
            oy = int(jshir[3]+jshir[4])
            yil =int("19"+jshir[5]+jshir[6]) if(jins==3 or jins ==4) else int("20"+jshir[5]+jshir[6])
            with col1.expander("Ma'lumotlarni yoyish"):
                st.json({
                    "Murojaat": "Janob" if(jins%2!=0) else "Honim",
                    "Kun": kun,
                    "Oy": oy_nomlari[oy],
                    "Yil": yil, 
                })
            col2.markdown(f"<h4 style='color: blue; text-align: center;'>Hurmatli {"Janob" if(jins%2!=0) else "Honim"}. Siz {kun}-{oy_nomlari[oy]}, {yil} da tug'ilgansiz. Sizning yoshingiz {2024-yil} da</h4>",unsafe_allow_html=True)
            
main()
with st.sidebar:
    st.title("salom")
    st.balloons()