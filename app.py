#streamlit run app.py

import streamlit as st
from crawling import news_crawling, weather_crawling
from voice import stt, tts
from kakao_msg import send_kakao_text, send_kakao_list
from slack_msg import send_slack_text, send_slack_file



st.title("Data Pipeline")

tab1, tab2 = st.tabs(['Weather', 'News'])

with tab1:
    st.write("세계 도시의 오늘 날씨를 알려드립니다.")
    city = st.text_input("어느 도시의 날씨가 궁금하세요?")
    mic = st.button("음성 인식")

    if mic:
        tts("어느 도시의 날씨가 궁금하세요?", "weather_guide_1")
        city = stt()
        with st.spinner(f"{city}의 날씨를 알아볼게요. 잠시만 기다려주세요."):
            tts(f"{city}의 날씨를 알아볼게요. 잠시만 기다려주세요.", f"weather_guide_{city}")
            weather_info = weather_crawling(city)
            st.write(weather_info)
            tts(weather_info, f"weather_info_{city}")
            #    tts(f"{city}의 결과를 찾지 못했어요. 다시 한 번 시도해주세요.", f"weather_error_{city}")

        if st.button("KakaoTalk"):
            send_kakao_text(weather_info, city)
        if st.button("Slack"):
            send_slack_text(weather_info)


with tab2:
    pass