# Formatter

- **formatter:** 코드 자체는 바꾸지 않고, 코드 모양을 바꾸어주는 툴.  
    - Why?: 협업 환경에서 룰을 정하지 않으면 conflict가 많이 생겨 resolve하기 힘들며 실질적은 변경사항 리뷰하기 힘듦.
- 포매터 적용으로 인해 코드 로직이 바뀔 확률은 굉장히 적으므로 그냥 IDE에서 format on save 적용시키면 됨.

## Python formatters

- [Black](https://github.com/psf/black): 파이썬 대표 formatter
    - line length: 88
        - Why?: 코드가 너무 길면 한 화면에 코드 두개를 띄워 비교하든지, 디버깅을 하느라 UI가 많이 떠 있을 때 읽기 힘듦.
    - string은 double quotation (")
    - 함수 parameters는 한 줄에 하나씩
    - Examples:

**Before Black:**

```python
def calculate(a_large_number, another_large_number, yet_another_large_number, final_large_number):
    sum_of_first_two=a_large_number+another_large_number
    sum_of_last_two= yet_another_large_number+ final_large_number
    overall_sum =sum_of_first_two +sum_of_last_two
    return overall_sum
```

**After Black:**

```python
def calculate(
    a_large_number,
    another_large_number,
    yet_another_large_number,
    final_large_number,
):
    sum_of_first_two = a_large_number + another_large_number
    sum_of_last_two = yet_another_large_number + final_large_number
    overall_sum = sum_of_first_two + sum_of_last_two
    return overall_sum
```

- [isort](https://github.com/PyCQA/isort): import 구문 정렬
    - 파이썬 내장, third party (pip install), first party (우리 프로젝트) 순서
    - 알파벳 순서
    - 같은 모듈에서 import 하는 elements 전부 합쳐줌
    - Examples:

**Before isort:**

```python
from my_lib import Object
import os
from my_other_lib import run
import sys
import mlproject
from third_lib import Widget
```

**After isort:**

```python
import os
import sys

from my_lib import Object
from my_other_lib import run
from third_lib import Widget

import mlproject
```

## VSCode settings

1. CLI commands 설치:  
```bash
conda deactivate
pip install black isort
```

2. vscode extension에서 **[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter), [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)** 설치

3. VSCode settings.json 수정

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
```

💡 isort의 버전이 5.13 이상이어야 합니다!! (`conda deactivate` 한 후 `isort --version`으로 확인)
