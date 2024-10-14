import streamlit as st
import datetime

x = datetime.datetime.now()


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

with open('source/style.css') as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1>JSHIR Define Generator</h1>", unsafe_allow_html=True)

with st.expander("JSHSHIR (PINFL) nima va uni qanday aniqlash mumkin?",expanded=False):
    st.image('source/images.jpg',caption="JSHSHIR (PINFL)", width=500)
    st.markdown("""
                <h5>JSHSHIR – jismoniy shaxsning shaxsiy identifikasion raqami bo‘lib, u har bir fuqaroning pasportida yozilgan bo‘ladi. Pasportni yangisiga almashtirsangiz ham, seriya va raqam o‘zgarishi mumkin, ammo JSHSHIR o‘zgarmaydi (o‘ta kamdan-kam uchraydigan hollar bundan mustasno).</h5>
                <h5>Uni aniqlash juda oson. Quyida ko‘rsatilgan surat orqali pasportingizdan 14 ta raqamni toping, ana shu Sizning JSHSHIRingiz bo‘ladi.</h5>
                <h5>Shu o‘rinda, 16 yoshga to‘lgan, lekin hali pasport olmagan abituriyentlar tezroq pasport olishga harakat qilishlari kerak. Chunki pasport bo‘lmasa JSHSHIR raqam ham bo‘lmaydi, bu degani abituriyentlar hujjat topshira olmay qolishlari mumkin. Pasportini yo‘qotgan/shikastlagan abituriyentlar ham pasportini tezroq yangilashi lozim.</h5>
                """,unsafe_allow_html=True)
jshir = st.chat_input('JSHIRNI kiriting', max_chars=14)

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
    try:
        if jshir:
            if int(len(jshir))<14:
                st.write("Iltimos 14 tadan kam bo'lmagan belgi kiriting", icon="error")
            else:
                col1, col2 = st.columns([1,3])
                jins = int(jshir[0])
                kun = int(jshir[1]+jshir[2])
                oy = int(jshir[3]+jshir[4])
                yil =int("19"+jshir[5]+jshir[6]) if(jins==3 or jins ==4) else int("20"+jshir[5]+jshir[6])
                nazorat_raqami = (7*jins+3*int(jshir[1])+1*int(jshir[2])+7*int(jshir[3])+3*int(jshir[4])+1*int(jshir[5])+7*int(jshir[6])+3*int(jshir[7])+1*int(jshir[8])+7*int(jshir[9])+3*int(jshir[10])+1*int(jshir[11])+7*int(jshir[12]))%10
                
                tuman_kodi = int(jshir[7]+jshir[8]+jshir[9])
                pasport_navbatingiz = int(jshir[10]+jshir[11]+jshir[12])
                kiritilganlik="✅ To'g'ri to'ldirilgan" if (nazorat_raqami==int(jshir[13])) else "🚫 Xato to'ldirilgan"
                with col1.expander("Ma'lumotlarni yoyish"):
                    st.json({
                        "Murojaat": "Janob" if(jins%2!=0) else "Honim",
                        "Kun": kun,
                        "Oy": oy_nomlari[oy],
                        "Yil": yil, 
                    })
                col2.text_area(label="Natija",value=f"Hurmatli {"Janob" if(jins%2!=0) else "Honim"}. Siz {kun}-{oy_nomlari[oy]}, {yil}-yilda tug'ilgansiz.\nSizning yoshingiz {x.year-yil} da. Tuman, shahar kodingiz: {tuman_kodi}, navbatingiz: {pasport_navbatingiz}, nazorat raqami: {nazorat_raqami}.\n {kiritilganlik}", disabled=True)
    except Exception as e:
        st.error(f'Xatolik sodir bo`ldi : {e}', icon="🚨")
            
main()
with st.sidebar:
    st.markdown("<h5>O'z shaxsiy identifikatsiya raqamingizni kiritgan holda o'zingiz haqingizda ma'lumotga ega bo'ling</h5><br />📘Manbaa: <a href='https://xushnudbek.uz/posts/jshshir-pinfl-nima-va-uni-qanday-aniqlash-mumkin'>JSHSHIR</a>",unsafe_allow_html=True)
    st.markdown("<div class='circle-container'><img id='circleImage' src='https://avatars.githubusercontent.com/u/71746304?s=400&u=12a8397519c5065d6af00235fb2ac9b1d2e9965b&v=4' alt='Rasm'> </div><br/> <div id='badges' align='center'> <a href='https://t.me/shohabbosdev'> <img src='https://img.shields.io/badge/telegram-blue?logo=telegram&logoColor=white' alt='Bu telegram badges'> </a> <a href='https://youtube.com/@shohabbosdev'> <img src='https://img.shields.io/badge/youtube-white?logo=youtube&logoColor=red' alt='Bu youtube badges'> </a> <a href='https://instagram.com/shohabbosdev'>  <img src='https://img.shields.io/badge/instagram-red?logo=instagram&logoColor=white' alt='Bu instagram badges'></a> <a href='https://facebook.com/shohabbosdev'>  <img src='https://img.shields.io/badge/facebook-white?logo=facebook&logoColor=blue' alt='Bu facebook badges'> </a><a href='https://x.com/shohabbosdev'> <img src='https://img.shields.io/badge/twitter-black?logo=x&logoColor=white' alt='Bu twitter badges'/>  </a><br>  <img src='https://komarev.com/ghpvc/?username=freedom-1&label=PROFILNI+KORISHLAR+SONI' alt=''/> </div>",unsafe_allow_html=True)
