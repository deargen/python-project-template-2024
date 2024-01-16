# python-project-template-2023

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Actions status](https://github.com/kiyoon/python-project-template-2023/workflows/Style%20checking/badge.svg)](https://github.com/kiyoon/python-project-template-2023/actions)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Actions status](https://github.com/kiyoon/python-project-template-2023/workflows/Linting/badge.svg)](https://github.com/kiyoon/python-project-template-2023/actions)

[![Actions status](https://github.com/kiyoon/python-project-template-2023/workflows/Tests/badge.svg)](https://github.com/kiyoon/python-project-template-2023/actions)

[![Actions status](https://github.com/kiyoon/python-project-template-2023/workflows/Deploy%20docs/badge.svg)](https://github.com/kiyoon/python-project-template-2023/actions)

새 파이썬 프로젝트 시작할 때 사용하실 템플릿입니다.

**주요 기능**

1. Github Actions로 black (formatter), isort (formatter), ruff (linter), pytest (unit test) 통과 여부 확인
2. pytest 커맨드로 유닛 테스트 사용 가능
3. MkDocs 이용해 자동 document 생성  
  a. GitLab Pages 이용 (GitHub Pages는 Private repo일 경우 유료인 문제가 있음)

## 돌려 보기

1. `pip install -e .`으로 dependencies 및 mlproject 패키지 설치
2. `python tools/color_logging_main.py` 실행해보기. 로깅 내용은 `train.log` 파일에도 기록됨 (저장 위치는 알아서 변경해 쓰기)
3. `pip install -e .[dev]` (다른방법: `pip install -r requirements_dev.txt` 으로 pytest 등 개발자용 패키지도 설치가능
4. `pytest` 커맨드로 테스트 실행해보기.
6. `import mlproject; print(mlproject.__version__)` 해보면 `0.1.0+4.g75bbed7.dirty` 이런식으로 나옴.  
  a. 0.1.0 버전 이후 4개의 커밋이란 뜻. 그리고 커밋되지 않은 수정사항이 있는 상태이면 dirty버전임.

## 파일 설명

1. `.github` 폴더: 깃헙 액션 및 Issues 템플릿을 정의합니다.
2. `src/mlproject` 폴더: `import mlproject` 해서 사용할 수 있는 함수나 클래스 등을 정의합니다.  
  a. 모델, 데이터셋 등
3. `tools/` 폴더: import 하지 않고 바로 실행 가능한 파일들. (예: train.py)
4. `tests/` 폴더: `pytest` 실행시 실행되는 함수들
5. `pyproject.toml`: 파이썬 프로젝트 일반 정보. `pip install -e .`으로 설치할 때 설치되는 dependencies는 물론, ruff등 외부 툴의 설정도 포함합니다.
6. `requirements.txt`: 혹시 모를 dependency 오류를 방지하기 위해 현재 사용중인 static version 작성. `pyproject.toml`과 얼추 비슷해야함.
7. `requirements_dev.txt`: 프로그램 사용자가 아닌 개발자에게 필요한 dependencies. `pyproject.toml`과 얼추 비슷해야함.

## Github 사용법

예시로 issues와 pull requests가 있음. 어떻게 쓰는건지 둘러보기.

1. main이 아닌 branch를 만들어 개발
2. 해당 branch를 push하고, pull request를 올림
3. 어떤 issue를 fix하는지 쓰기 (예: Fixes #1) -> accept되면 자동으로 issue 닫힘
4. pull request는 다른 팀원이 간략히 코드 리뷰하고 squash 혹은 rebase하면 됨. merge는 웬만하면 피하기.

더 엄격하게 하고 싶으면, 깃헙 프로젝트 세팅에서 main branch protection 및 merge 못하게 할 수 있음.

### 새 버전 Release
어느 정도 stable한 버전이다 싶으면 release에서 새 버전 생성 가능. 내용은 비우고 tag로 버전 이름만 적으면 됨.

`.github/workflows.deploy.yml`에 있는 대로, 새로운 버전 태그가 생기면 자동 release 및 `CHANGELOG.md` 생성이 됨.

## 템플릿 사용하기

1. `src/mlproject` 폴더 이름 원하는 걸로 바꾸기 (`import mlproject` 할 때 이름)
2. `pyproject.toml`에 바꿔야하는 부분 주석 되어있음. 바꿔 쓰기
3. `requirements.txt`에는 fixed version을 적고, `pyproject.toml`의 패키지들은 dynamic version으로 하기
4. `README.md`에 있는 badge들 URL (python-project-template-2023 -> 새 주소) 바꾸어 주어야 제대로 테스트 결과가 뜸.
5. `.github` 폴더, `setup.py`는 그대로 복사해 두면 됨
6. 테스트를 작성하지 않은 경우, `tests/` 폴더 안의 파일 전부 삭제하면 GitHub Actions에서 테스트 통과됨.
