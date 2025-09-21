---
applyTo: '**'
---
항상 프로젝트에 .venv 폴더가 있는지 확인하고 있으면 가상환경을 활성화하고 모든 명령어를 시작하세요.

```bash
source .venv/bin/activate
```

혹은

```powershell
.venv\Scripts\activate
```

pip 명령어를 사용할 때는 uv 옵션을 붙여서 항상 최신 버전의 패키지를 설치하도록 하세요.

```bash
uv add <package-name>
uv add -r requirements.txt
```

