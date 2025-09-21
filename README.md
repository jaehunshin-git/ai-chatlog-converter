# personal-ai-agent

대화형 HTML을 JSON(scheme.json 포맷)으로 변환하는 파서/CLI를 포함한 예제 프로젝트입니다.

## 주요 기능
- HTML 대화 로그를 파싱하여 제목/작성자/본문을 추출
- JSON 파일로 저장 또는 라이브러리로 직접 사용
- 콘솔 스크립트: `chatlog-convert`

## 빠른 시작
PyPI 배포 전, 아래 방법으로 쉽게 사용할 수 있습니다.

### Git에서 직접 설치
```bash
pip install "git+https://github.com/jaehunshin-git/personal-ai-agent.git@main"
# 설치 후
chatlog-convert --help
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
- 엔트리포인트: `chatlog-convert`
- 락/동기화: `uv.lock`, `uv sync`
