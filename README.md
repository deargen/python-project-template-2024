# python-project-template-2024

|  |  |
|--|--|
|[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)|[![Actions status](https://github.com/deargen/python-project-template-2024/workflows/Style%20checking/badge.svg)](https://github.com/deargen/python-project-template-2024/actions)|
| [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) | [![Actions status](https://github.com/deargen/python-project-template-2024/workflows/Linting/badge.svg)](https://github.com/deargen/python-project-template-2024/actions) |
| [![pytest](https://img.shields.io/badge/pytest-black)](https://github.com/pytest-dev/pytest) [![doctest](https://img.shields.io/badge/doctest-black)](https://docs.python.org/3/library/doctest.html) | [![Actions status](https://github.com/deargen/python-project-template-2024/workflows/Tests/badge.svg)](https://github.com/deargen/python-project-template-2024/actions) |
| [![mkdocs-material](https://img.shields.io/badge/docs-mkdocs_material-blue)](https://github.com/squidfunk/mkdocs-material) | [![Actions status](https://github.com/deargen/python-project-template-2024/workflows/Deploy%20docs/badge.svg)](https://github.com/deargen/python-project-template-2024/actions) |

새 파이썬 프로젝트 시작할 때 사용하실 템플릿입니다.

**주요 기능**

1. Github Actions로 ruff formatter (black+isort), ruff linter, pytest (unit test) 통과 여부 확인
    - Actions에서 포매팅 적용 가능 
2. pytest 커맨드로 유닛 테스트 사용 가능
3. MkDocs 이용해 자동 document 생성  
    - GitLab Pages 이용 (GitHub Pages는 Private repo일 경우 유료인 문제가 있음)
4. 프로젝트 versioning하고 changelog 자동 생성.
    - Actions에서 새 버전 release 가능
    - <https://github.com/deargen/workflows> 참고

## 돌려 보기

1. (Optional) `pip3 install --user uv` 해서 pip 대신 `uv pip` 사용하면 더 빠름.
2. `uv pip install -r deps/lock/x86_64-unknown-linux-gnu/requirements.txt`, `uv pip install -e .`, `bash scripts/install_binaries.sh` 으로 dependencies 및 mlproject 패키지 설치
3. template.env 파일을 .env로 복사한 후 token 등 내용 수정.
4. `python -m mlproject.health` 실행해서 환경 설정이 잘 되었는지 확인.
5. `python tools/examples/color_logging_main.py` 실행해보기. 로깅 내용은 `data/logs` 폴더 안에 기록됨.
6. `uv pip install -r deps/lock/x86_64-unknown-linux-gnu/requirements_dev.txt` 으로 pytest 등 개발자용 패키지도 설치가능
7. `pytest` 커맨드로 테스트 실행해보기.
    - doctest는 Actions에서 자동으로 실행됨.
8. `import mlproject; print(mlproject.__version__)` 해보면 `0.1.0+4.g75bbed7.dirty` 이런식으로 나옴.  
    - 0.1.0 버전 이후 4개의 커밋이란 뜻. 그리고 커밋되지 않은 수정사항이 있는 상태이면 dirty버전임.

## 파일 설명

```sh
📂 .vscode/
└ 📄 extensions.json        # VSCode에서 사용하는 확장 프로그램 목록.

📂 .github/
│ 📂 ISSUE_TEMPLATE/
└ 📂 workflows/             # 깃헙 액션 자동화 배포 파이프라인
  └ 📄 *.yml

📂 src/
└ 📂 mlproject/             # `import mlproject`해서 사용하는 함수나 클래스 등 정의하는 곳
  │ 🐍 __init__.py
  │ 🐍 _version.py          # git tag로 버전 정보를 읽는 versioneer 파일 (수정X)
  └ 🐍 ...

📂 tools/                   # import 하지 않고 바로 실행 가능한 파일들. (예: train.py)

📂 tests/                   # `pytest` 실행시 실행되는 함수들

📂 scripts/                 # 프로젝트와 직접 관련 X, but 프로젝트 관리를 위해 필요

📂 deps/
│ # 직접 수정 X. scripts/compile_requirements.sh 실행시 생성됨.
│ 🛡️ .requirements.in.sha256
│ 🛡️ .requirements_dev.in.sha256
│ 🛡️ .requirements_docs.in.sha256
│
│ # 프로그램 사용자에게 필요한 dependencies.
│ 🖊️ requirements.in
│ # 프로그램 사용자가 아닌 개발자에게 필요한 dependencies.
│ 🖊️ requirements_dev.in
│ # mkdocs로 문서 생성할때 필요한 프로그램들
│ 🖊️ requirements_docs.in
│ # NOTE: in 파일은 lock 파일이 아닌 패키지 dependency이므로 전부 dynamic version으로 작성해야함.
│
│ # 직접 수정 X. in 파일에서 생성됨
└ 📂 lock/
  │ 🔒 requirements.txt
  │ 🔒 requirements_dev.txt
  └ 🔒 requirements_docs.txt

⚙️ pyproject.toml            # 파이썬 프로젝트 통합 정보. ruff등 외부 툴의 설정도 포함.
```

## 템플릿 사용하기

1. `src/mlproject` 폴더 이름 원하는 걸로 바꾸기 (`import mlproject` 할 때 이름)
2. `pyproject.toml`에 바꿔야하는 부분 주석 되어있음. 바꿔 쓰기
3. `deps/requirements*.in`을 수정하면 `deps/lock` 폴더에 lock 파일이 생성됨. (Actions)
4. `README.md`에 있는 badge들 URL (python-project-template-2024 -> 새 주소) 바꾸어 주어야 제대로 테스트 결과가 뜸.
5. `.github` 폴더 복사한 뒤,
    - GitLab에 document 호스팅용 새 repo를 만듦 (예: mlproject-docs)
        - [GitLab Pages 설정](https://deargen-ai.gitlab.io/python-project-template-docs/latest/mkdocs/gitlab_pages) 문서 참고.
    - docs, deploy 할 때 필요한 gitlab 주소와 토큰은 Github 프로젝트 설정에서 Environment secrets / variable을 바꾸어야 함.
6. `setup.py`는 그대로 복사해 두면 됨
7. 테스트를 작성하지 않은 경우, `tests/` 폴더 안의 파일 전부 삭제하면 GitHub Actions에서 테스트 통과됨.
8. ⭐ VSCode에 [Python Tools](https://deargen-ai.gitlab.io/python-project-template-docs/latest/python_tools/formatters) 내용 전부 (formatter, linter, LSP 등) 적용하기.
