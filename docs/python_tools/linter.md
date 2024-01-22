# Linter

- **Linter**: 코드 스타일 등 프로젝트에서 정한 룰을 지켰는지 체크하며 간단한 potential bug도 잡아줍니다.
- Formatter와 차이점: 코드 자체 로직이나 함수 등 수정을 권유합니다. 맹신하지 말고 가이드라 생각하고 쓰세요.
- LSP와 차이점:
    1. 속도: LSP는 프로젝트 전체를 분석해 함수 definition 위치 등도 파악하지만 linter는 한 파일만 체크합니다.
    2. Linter는 에러가 주로 스타일 관련이지만 LSP와 겹치는 에러도 있긴 합니다 (예: 사용되지 않은 variable, import 구문).

## Python linter

- flake8: PEP8 스타일 가이드를 지켜주는 파이썬 대표 linter. 확장 플러그인도 많습니다.
- **ruff:** flake8 및 인기 플러그인을 전부 rust로 구현해 속도가 굉장히 빨라진 python linter. 저희 프로젝트에서는 ruff를 사용합니다.
    - 쉬운 설치: `pip install ruff` 후 플러그인을 따로 설치하지 않아도 됩니다.
    - formatter 포함: black과 isort와 유사한 구현도 존재합니다.
        - 다만 beta 버전이라 결과가 버전마다 자주 바뀌며, edge case 에러가 많이 있는것 같아 아직은 black, isort 사용합니다.
        - VSCode에서 ruff organizeImports를 꼭 비활성화 해 주세요.

### Linting 비활성화

Linting 결과를 무시하고 싶은 경우:

1. Line 비활성화: 라인 끝에 `# noqa: D401` 과 같은 주석을 남겨주면 해당 코드(D401)가 비활성화됩니다.
    - `# noqa` 까지만 적으면 모든 코드를 비활성화합니다.
2. File 비활성화: 수정하는 파일 맨 위에 `# flake8: noqa: D401 D402`와 같은 주석을 남기면 파일 전체에서 비활성화합니다.
3. Project 단위 비활성화: `pyproject.toml`에서 `[tools.ruff.lint]` 항목에 `ignore`를 추가합니다.

`pyproject.toml` 예시:

```toml
[tool.ruff]
# Black will enforce line length to be 88, except for docstrings and comments.
# We set it to 120 so we have more space for docstrings and comments.
line-length = 120

[tool.ruff.lint]
# OPTIONALLY ADD MORE LATER
select = [
  # flake8
  "E",
  "F",
  "W",
  "B",    # Bugbear
  "D",    # Docstring
  "D401", # Augment the convention by requiring an imperative mood for all docstrings.
  "N",    # Naming
  "C4",   # flake8-comprehensions
  "UP",   # pyupgrade
  "SIM",  # simplify
  "RUF",  # ruff-specific
  "RET",  # return
  "PTH",  # path
  "T10",  # debug statements
  "T20",  # print statements
]

ignore = [
  "E402", # Module level import not at top of file
  # Relax the convention by _not_ requiring documentation for every function parameter.
  "D417",
]

[tool.ruff.lint.pydocstyle]
convention = "google"
```
