from listener import get_now_playing
from llm_parser import parse_music_info

if __name__ == "__main__":
    print("🔍 현재 재생 중인 곡 정보를 확인합니다...")
    
    raw_music_title = get_now_playing()
    
    if raw_music_title == "PAUSED":
        print("⏸️ 음악이 일시정지 상태입니다. (LLM 요청을 건너뜁니다)")
        
    elif raw_music_title:
        print(f"🎵 원본 데이터: {raw_music_title}")
        print("🤖 AI가 정보를 정제 중입니다...")
        
        parsed_data = parse_music_info(raw_music_title)
        
        print("-" * 30)
        if "error" not in parsed_data:
            print(f"✅ 가수: {parsed_data.get('artist')}")
            print(f"✅ 제목: {parsed_data.get('title')}")
        else:
            print(f"❌ 에러 발생: {parsed_data['error']}")
        print("-" * 30)
        
    else:
        print("🎵 현재 재생 중인 음악이 없거나 정보를 가져올 수 없습니다.")