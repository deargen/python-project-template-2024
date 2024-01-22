# Linter

- **Linter**: 코드 스타일 등 프로젝트에서 정한 룰을 지켰는지 체크하며 간단한 potential bug도 잡아줍니다.
- Formatter와 차이점: 코드 자체 로직이나 함수 등 수정을 권유합니다.
- LSP와 차이점: LSP는 프로젝트 전체를 분석해 함수 definition 위치 등도 파악하지만 linter는 빠르게 한 파일만 체크합니다. 에러가 주로 스타일 관련이지만 겹치는 에러도 있긴 합니다.

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
