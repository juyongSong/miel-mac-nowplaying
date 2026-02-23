import requests
import json

# --- Configuration & Constants ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:8b"

def parse_music_info(raw_title):
    """Extracts artist and title from a YouTube-style string."""
    prompt = f"""
    Extract 'artist' and 'title' from the following YouTube title.
    Output MUST be in JSON format.
    'title' should NOT include any extra information like (Official Music Video), [Lyrics], etc.
    'title' does NOT include the artist name.

    Extract 'artist' and 'title' from the YouTube string.
    Remove suffixes like ' - Topic' or ' - 주제' from the artist name.

    Examples:
    Input: "BTS - Topic - Dynamite"
    Output: {{"artist": "BTS", "title": "Dynamite"}}

    Input: "IU - 주제 - 밤편지"
    Output: {{"artist": "IU", "title": "밤편지"}}
    
    Input: "{raw_title}"
    Output:
    """
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.1}
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        result = response.json()
        return json.loads(result['response'])
    except Exception as e:
        return {"error": f"LLM parsing failed: {str(e)}"}