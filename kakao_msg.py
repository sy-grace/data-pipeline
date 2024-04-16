from PyKakao import Message

service_key ="4ce964786e4b4b6cd4cc087c5fd85419"
access_token = "chh2S_lFOHC2VPwvKqsHcBXzMG0O6hY0VlQKKwyoAAABjuRu93YFVMIyByjmyg"

def send_kakao_text(txt, city):
    # 메시지 API 인스턴스 생성
    MSG = Message(service_key=service_key)

    # 액세스 토큰 설정
    MSG.set_access_token(access_token)

    message_type = "text"  # 메시지 유형 - 텍스트
    text = txt
    link = {
    "web_url": f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={city}+날씨",
    "mobile_web_url": f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={city}+날씨",
    }
    button_title = f"{city} 날씨" 

    MSG.send_message_to_me(
        message_type=message_type, 
        text=text,
        link=link,
        button_title=button_title,
    )

def send_kakao_list(df):
    try:
        # 메시지 API 인스턴스 생성
        MSG = Message(service_key=service_key)

        # 액세스 토큰 설정
        MSG.set_access_token(access_token)

        message_type = "list"  # 메시지 유형 - 리스트

        header_title = "Daily IT News"
        header_link = {
            "web_url": "https://news.naver.com/breakingnews/section/105/230",
            "mobile_web_url": "https://news.naver.com/breakingnews/section/105/230",
        }
        contents = []
        for i in range(3):
            contents.append({
                "title": df['제목'][i],
                "description": f"{df['언론사'][i]} | {df['시간'][i]}",
                "image_url": df['이미지url'][i],
                "image_width": 400,
                "image_height": 400,
                "link": {
                    "web_url": df['기사url'][i],
                    "mobile_web_url": df['기사url'][i],
                }
            })
        
        buttons = [
            {
                "title": "더보기",
                "link": {
                    "web_url": "https://news.naver.com/breakingnews/section/105/230",
                    "mobile_web_url": "https://news.naver.com/breakingnews/section/105/230"
                },
            },
        ]

        MSG.send_message_to_me(
            message_type=message_type,
            header_title=header_title,
            header_link=header_link,
            contents=contents,
            buttons=buttons,
        )
        return "메시지 전송 성공"
    except Exception as e:
        return '메시지 전송 실패'