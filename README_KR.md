# 🎵 miel-mac-nowplaying

> macOS의 최신 보안 환경에서도 작동하는 로컬 LLM 기반 '현재 재생 중' 트래커
> [View in English](./README.md)

`miel-mac-nowplaying`은 macOS에서 현재 재생 중인 미디어(Apple Music, Spotify, YouTube 등) 정보를 가져와 로컬 LLM(Ollama)을 사용하여 깔끔한 JSON 형식(아티스트, 제목)으로 파싱해주는 Python 유틸리티입니다.

---

## 💡 배경 및 동기

최근 macOS 업데이트로 인한 엄격한 권한 설정 및 API 변경으로 기존의 `nowplaying` 라이브러리가 작동하지 않을 때 사용 가능합니다. (참고: [Apple 고객지원 HT122400](https://support.apple.com/122400))

이 프로젝트는 이러한 제약을 우회하기 위해 **Swift 하위 프로세스**를 통해 macOS의 `MediaRemote.framework`에 직접 접근하는 방식을 사용합니다.

## ✨ 주요 기능

- **macOS Sequoia 호환:** 최신 macOS에서도 시스템 알림 센터 상태를 읽어 현재 재생 정보를 안정적으로 가져옵니다.
- **로컬 LLM 파싱:** Ollama(예: Qwen3 등)를 사용할 수 있습니다.

## 📂 프로젝트 구조

- `nowplaying.py`: Swift 코드를 실행하여 macOS `MediaRemote`로부터 원본 재생 정보(또는 정지 상태)를 가져옵니다.
- `llm_parser.py`: 수집된 문자열을 Ollama API로 전송하여 `artist`, `title`이 포함된 JSON으로 변환합니다.
- `main.py`: 전체 흐름을 제어하는 진입점입니다.

## 🚀 시작하기

### 필수 조건 (Prerequisites)
- **macOS** (MediaRemote 프레임워크 사용)
- **Xcode Command Line Tools**: Swift 코드를 실행하기 위해 필요합니다. (터미널에서 `xcode-select --install` 실행)
- **Python 3.8+**

### Optional
- **[Ollama](https://ollama.com/)**: 로컬 LLM 실행을 위해 설치되어 있어야 합니다.
  - 기본 모델로 `qwen3:8b`를 사용하도록 설정되어 있습니다. (변경 가능)

### 설치 (Installation)

1. 저장소를 클론합니다:
   ```bash
   git clone https://github.com/juyongSong/miel-mac-nowplaying.git
   cd miel-mac-nowplaying
   ```

2. 의존성 패키지를 설치합니다 (`requests`):
   ```bash
   pip install requests
   ```

3. Ollama 모델을 다운로드합니다:
   ```bash
   ollama pull qwen3:8b
   ```

### 사용법 (Usage)

#### 1. 단독 실행 (LLM 없이 원본 데이터만 확인)
Ollama 없이 현재 재생 중인 곡의 원본 텍스트만 빠르게 확인하려면 `nowplaying.py`를 직접 실행합니다.
```bash
python3 nowplaying.py
```
출력 예시:
```text
Billie Joe Armstrong, Norah Jones(노라 존스) - Put My Little Shoes Away
```

#### 2. LLM 파싱 포함 실행 (Ollama 필요)
1. **Ollama 서버 실행:**
   Ollama 앱을 실행하거나 터미널에서 `ollama serve`를 실행하여 백그라운드에서 API가 동작하도록 합니다.

2. **스크립트 실행:**
   ```bash
   python3 main.py
   ```

3. **실행 결과 예시:**
   
   음악이 재생 중일 때:
   ```text
   🔍 Checking current playback info...
   🎵 Raw Data: Billie Joe Armstrong, Norah Jones(노라 존스) - Put My Little Shoes Away
   🤖 AI is refining the information...
   ------------------------------
   ✅ Artist: Billie Joe Armstrong, Norah Jones
   ✅ Title: Put My Little Shoes Away
   ------------------------------
   ```

   일시정지 상태일 때:
   ```text
   🔍 Checking current playback info...
   ⏸️ Music is paused. (Skipping LLM request)
   ```

## ⚙️ 설정 (Configuration)

`llm_parser.py` 파일 상단에서 Ollama URL과 사용할 모델을 변경할 수 있습니다.

```python
# llm_parser.py

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:8b"  # 원하는 모델로 변경 (예: "llama3", "mistral")
```

## 🤝 기여하기 (Contributing)

이 프로젝트는 오픈 소스입니다. 버그 리포트, 기능 제안, PR은 언제나 환영합니다.

## 📄 라이선스 (License)

이 프로젝트는 MIT 라이선스를 따릅니다. `LICENSE` 파일을 참고하세요.
