# chatlog_converter 사용법

HTML 형태의 대화 로그를 `scheme.json` 규격(JSON)으로 변환하는 파서/CLI입니다.

## 설치/환경 준비 (uv 권장)

이 프로젝트는 `pyproject.toml` + `uv.lock`으로 의존성을 관리합니다. `requirements.txt`는 사용하지 않습니다.

```bash
# 1) 가상환경 활성화 (프로젝트에 .venv가 있는 경우)
source .venv/bin/activate

# 2) 의존성 동기화
uv sync

# (옵션) 잠금파일 재생성/업데이트가 필요할 때
uv lock --upgrade
```

설치 없이도 모듈 실행 방식으로 바로 사용할 수 있습니다.

## CLI 사용법

설치 후에는 콘솔 스크립트 `ai-chatlog-converter`가 제공됩니다. (이전 이름 `chatlog-convert`도 호환 별칭으로 동작)

```bash
ai-chatlog-converter -i input.html -o out.json
```

긴 옵션도 지원합니다.

```bash
ai-chatlog-converter --input input.html --output out.json
```

설치 없이 즉시 실행하고 싶다면 다음 중 하나를 사용하세요.

```bash
# 저장소 최상위에서 래퍼 실행
python main.py -i input.html -o out.json

# 모듈 실행 방식
python -m chatlog_converter.cli -i input.html -o out.json

# uv로 바로 실행
uv run ai-chatlog-converter -i input.html -o out.json
```

## 라이브러리 사용법 (파이썬 코드에서 import)

파일 간 변환을 한 번에:

```python
from chatlog_converter import convert_file_to_json

convert_file_to_json("input.html", "out.json")
```

결과를 메모리에서 바로 쓰고 싶다면:

```python
from chatlog_converter import parse_file

conversations = parse_file("input.html")  # list[dict]
print(conversations[0]["title"])  # 예: "API 대화 기록 불러오기"
```

이미 HTML 문자열을 갖고 있다면:

```python
from chatlog_converter import parse_html_to_conversations

conversations = parse_html_to_conversations(html_str)
```

## 입력 HTML 구조

- 여러 개의 `div.conversation` 블록
- 각 블록 내부:
  - 제목: `h4`
  - 여러 개의 메시지: `pre.message`
    - 메시지 내부:
      - 작성자: `<div class="author">AUTHOR</div>`
      - 본문: `<div>TEXT...</div>`

예시:

```html
<div class="conversation">
  <h4>API 대화 기록 불러오기</h4>
  <pre class="message">
    <div class="author">user</div>
    <div>사용자의 chatgpt 대화기록 을 모두 참조해서 가져올수있는 api 를 openai는 제공하나 ?</div>
  </pre>
  <pre class="message">
    <div class="author">ChatGPT</div>
    <div>OpenAI는 사용자의 대화 기록 전체를 가져오는 API는 제공하지 않는다...</div>
  </pre>
</div>
```

## 출력 JSON 구조

최상위는 대화 배열입니다.

```json
[
  {
    "conversation_index": 0,
    "title": "API 대화 기록 불러오기",
    "messages": [
      { "index": 0, "author": "user", "text": "..." },
      { "index": 1, "author": "ChatGPT", "text": "..." }
    ]
  }
]
```

## API 레퍼런스

- `convert_file_to_json(html_path: str | Path, out_path: str | Path) -> None`
  - 파일에서 읽어 변환 후 JSON 파일로 저장.
- `parse_file(html_path: str | Path) -> list[dict]`
  - 파일에서 읽어 파싱 결과를 파이썬 객체로 반환.
- `parse_html_to_conversations(html_str: str) -> list[dict]`
  - HTML 문자열을 바로 파싱해 반환.

## 동작 노트

- 줄바꿈은 보존됩니다(`\r\n`/`\r` → `\n` 정규화).
- 한글 등 유니코드는 그대로 저장됩니다(`ensure_ascii=False`).
- `author` 또는 `text`가 비어도 레이아웃이 유지되며, 두 값이 모두 비어 있으면 메시지는 생략됩니다.
- 입력 파일이 없으면 CLI는 에러 메시지를 출력하고 종료하며, 라이브러리 사용 시엔 `FileNotFoundError`가 발생할 수 있습니다.
