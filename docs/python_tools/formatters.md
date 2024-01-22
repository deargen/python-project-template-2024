# Formatter

- **formatter:** 코드 자체는 바꾸지 않고, 코드 모양을 바꾸어주는 툴.
- 포매터 적용으로 인해 코드 로직이 바뀔 확률은 굉장히 적으므로 그냥 IDE에서 format on save 적용시키면 됨.

## Python formatters

- [Black](https://github.com/psf/black): 파이썬 대표 formatter
  - line length: 88
  - string은 double quotation (")
- [isort](https://github.com/PyCQA/isort): import 구문 정렬
  - 파이썬 내장, third party (pip install), first party (우리 프로젝트) 순서
  - 알파벳 순서


## VSCode settings

vscode extension에서 **[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter), [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort), [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)** 설치

```json
// settings.json

"[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true, // 저장할 때마다 formatting
    "editor.codeActionsOnSave": {
        "source.organizeImports": true // 저장할 때마다 import sorting
    },
},
"isort.args": ["--profile", "black"], // black과 호환성을 고려하겠다
"isort.path": ["isort"], // isort extension의 isort가 아니라 환경에 설치된 isort 사용
"ruff.organizeImports": false, // ruff가 import sorting 을 하지 못하게 함
```
