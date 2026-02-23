# 🎵 miel-mac-nowplaying

> A local LLM-powered 'Now Playing' tracker that works on the latest macOS security environment.
> [한국어 문서 보기 (View in Korean)](./README_KR.md)

`miel-mac-nowplaying` is a Python utility that retrieves currently playing media information (Apple Music, Spotify, YouTube, etc.) on macOS and parses it into a clean JSON format (Artist, Title) using a local LLM (Ollama).

---

## 💡 Background & Motivation

Due to recent macOS updates introducing strict permission settings and API changes, many existing `nowplaying` libraries have stopped working properly.

To bypass these restrictions, this project uses a **Swift subprocess** to directly access the `MediaRemote.framework` on macOS. Furthermore, instead of using fragile Regex rules to clean up unstructured data like YouTube titles (e.g., `Artist - Topic - Title`), it leverages a **Local LLM** to accurately separate the artist and track name.

## ✨ Features

- **macOS Sequoia Compatible:** Reliably reads the playback status from the system Notification Center, supporting the latest macOS versions.
- **Local LLM Parsing:** Uses Ollama (e.g., Qwen, Llama 3) to refine data, ensuring **zero cost** and **privacy protection** without external API calls.
- **Modular Architecture:** Data collection (`listener.py`) and parsing (`llm_parser.py`) are separated for easy maintenance and scalability.

## 📂 Project Structure

- `listener.py`: Executes Swift code to fetch the raw playback information (or paused state) from macOS `MediaRemote`.
- `llm_parser.py`: Sends the collected string to the Ollama API and converts it into a JSON containing `artist` and `title`.
- `main.py`: The entry point that orchestrates the entire flow.

## 🚀 Getting Started

### Prerequisites
- **macOS** (Requires MediaRemote framework)
- **Python 3.8+**
- **[Ollama](https://ollama.com/)**: Must be installed to run the local LLM.
  - Default model is configured as `qwen3:8b` (Changeable).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/juyongSong/miel-mac-nowplaying.git
   cd miel-mac-nowplaying
   ```

2. Install dependencies (`requests`):
   ```bash
   pip install requests
   ```

3. Download the Ollama model:
   ```bash
   ollama pull qwen3:8b
   ```

### Usage

1. **Start Ollama Server:**
   Run the Ollama app or execute `ollama serve` in your terminal to ensure the API is running in the background.

2. **Run the Script:**
   ```bash
   python3 main.py
   ```

3. **Example Output:**
   
   When music is playing:
   ```text
   🔍 Checking current playback info...
   🎵 Raw Data: NewJeans - OMG
   🤖 AI is refining the information...
   ------------------------------
   ✅ Artist: NewJeans
   ✅ Title: OMG
   ------------------------------
   ```

   When paused:
   ```text
   🔍 Checking current playback info...
   ⏸️ Music is paused. (Skipping LLM request)
   ```

## ⚙️ Configuration

You can change the Ollama URL and the model to use at the top of the `llm_parser.py` file.

```python
# llm_parser.py

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:8b"  # Change to your preferred model (e.g., "llama3", "mistral")
```

## 🤝 Contributing

This project is open source. Bug reports, feature suggestions, and PRs are always welcome.

## 📄 License

This project follows the MIT License. See the `LICENSE` file for details.
