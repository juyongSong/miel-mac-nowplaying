from nowplaying import get_now_playing
from llm_parser import parse_music_info

if __name__ == "__main__":
    print("🔍 Checking current playback info...")
    
    raw_music_title = get_now_playing()
    
    if raw_music_title == "PAUSED":
        print("⏸️ Music is paused. (Skipping LLM request)")
        
    elif raw_music_title:
        print(f"🎵 Raw Data: {raw_music_title}")
        print("🤖 AI is refining the information...")
        
        parsed_data = parse_music_info(raw_music_title)
        
        print("-" * 30)
        if "error" not in parsed_data:
            print(f"✅ Artist: {parsed_data.get('artist')}")
            print(f"✅ Title: {parsed_data.get('title')}")
        else:
            print(f"❌ Error: {parsed_data['error']}")
        print("-" * 30)
        
    else:
        print("🎵 No music playing or unable to fetch info.")