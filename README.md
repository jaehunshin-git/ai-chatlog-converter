# personal-ai-agent

대화형 HTML을 JSON(scheme.json 포맷)으로 변환하는 파서/CLI를 포함한 예제 프로젝트입니다.

## 주요 기능
- HTML 대화 로그를 파싱하여 제목/작성자/본문을 추출
- JSON 파일로 저장 또는 라이브러리로 직접 사용
- 콘솔 스크립트: `ai-chatlog-converter` (구: `chatlog-convert`)

## 빠른 시작
PyPI 배포 전, 아래 방법으로 쉽게 사용할 수 있습니다.

### Git에서 직접 설치
```bash
# 권장: 패키지 이름을 명시한 PEP 508 형식
pip install "ai-chatlog-converter @ git+https://github.com/jaehunshin-git/ai-chatlog-converter.git@main"

# 만약 일부 환경에서 메타데이터가 UNKNOWN으로 감지되어 실패한다면, #egg 플래그를 사용하세요.
# (pip가 패키지 이름을 올바르게 인식하도록 힌트를 제공합니다)
pip install "git+https://github.com/jaehunshin-git/ai-chatlog-converter.git@main#egg=ai-chatlog-converter"
# 설치 후
ai-chatlog-converter --help
```

자세한 설치/실행 및 CLI/라이브러리 사용법은 `docs/chatlog_converter.md`를 참고하세요.

## 라이브러리 사용법
```python
from chatlog_converter import parse_file, convert_file_to_json

conversations = parse_file("input.html")
convert_file_to_json("input.html", "out.json")
```

## 의존성
- Python >= 3.12
- selectolax >= 0.3.34, < 0.4

## 개발 노트
- 패키징: PEP 517(pyproject.toml), setuptools 빌드 백엔드
- 엔트리포인트: `ai-chatlog-converter` (별칭 `chatlog-convert` 유지)
- 락/동기화: `uv.lock`, `uv sync`
