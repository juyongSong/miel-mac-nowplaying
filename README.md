# 🎵 miel-mac-nowplaying

> A local LLM-powered 'Now Playing' tracker that works on the latest macOS security environment.
> [한국어 문서 보기 (View in Korean)](./README_KR.md)

`miel-mac-nowplaying` is a Python utility that retrieves currently playing media information (Apple Music, Spotify, YouTube, etc.) on macOS and parses it into a clean JSON format (Artist, Title) using a local LLM (Ollama).

---

## 💡 Background & Motivation

Due to recent macOS updates introducing strict permission settings and API changes, many existing `nowplaying` libraries have stopped working properly.

To bypass these restrictions, this project uses a **Swift subprocess** to directly access the `MediaRemote.framework` on macOS.

## ✨ Features

- **macOS Sequoia Compatible:** Reliably reads the playback status from the system Notification Center, supporting the latest macOS versions.
- **Local LLM Parsing:** Uses Ollama (e.g., Qwen3) to refine data.

## 📂 Project Structure

- `nowplaying.py`: Executes Swift code to fetch the raw playback information (or paused state) from macOS `MediaRemote`.
- `llm_parser.py`: Sends the collected string to the Ollama API and converts it into a JSON containing `artist` and `title`.
- `main.py`: The entry point that orchestrates the entire flow.

## 🚀 Getting Started

### Prerequisites
- **macOS** (Requires MediaRemote framework)
- **Python 3.8+**

### Optional
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

#### 1. Standalone Execution (Raw data only, no LLM)
To quickly check the raw text of the currently playing track without Ollama, run `nowplaying.py` directly.
```bash
python3 nowplaying.py
```
Example Output:
```text
Billie Joe Armstrong, Norah Jones(노라 존스) - Put My Little Shoes Away
```

#### 2. Execution with LLM Parsing (Requires Ollama)
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
   🎵 Raw Data: Billie Joe Armstrong, Norah Jones(노라 존스) - Put My Little Shoes Away
   🤖 AI is refining the information...
   ------------------------------
   ✅ Artist: Billie Joe Armstrong, Norah Jones
   ✅ Title: Put My Little Shoes Away
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
