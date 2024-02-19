# 페이지에 소스코드 설명 추가하기

## 설명하고 싶은 모듈/함수/클래스가 있다면 다음과 같이 마크다운 파일에 적으면 됩니다.

```md
::: mlproject.two_numbers.TwoNumbers
    options:
        show_root_heading: true
```

출력은 아래와 같습니다.

::: mlproject.two_numbers.TwoNumbers
    options:
        show_root_heading: true


---
## Submodule까지 전부 포함하고 싶으시면 다음과 같이 작성합니다.

```md
::: mlproject
    options:
        show_root_heading: true
        show_submodules: true
```

출력은 아래와 같습니다.

::: mlproject
    options:
        show_submodules: true


---
## 소스코드만 출력하고 싶으시면 다음과 같이 작성합니다.

```md
::: mlproject.two_numbers.TwoNumbers
    options:
        show_docstring_description: false
        show_docstring_examples: false
        members: false
        show_bases: false
        show_source: true
```

출력은 아래와 같습니다.

::: mlproject.two_numbers.TwoNumbers
    options:
        show_docstring_description: false
        show_docstring_examples: false
        members: false
        show_bases: false
        show_source: true


더 자세한 설명은 [mkdocstrings](https://mkdocstrings.github.io/usage/)를 참고하세요.

---

## 목차에서 Heading level을 바꾸고 싶다면 마크다운처럼 #을 쓰시면 됩니다.
```md
### ::: mlproject.two_numbers.TwoNumbers
    options:
        show_docstring_description: false
        show_docstring_examples: false
        members: false
        show_bases: false
        show_source: true
```

출력은 생략.

---

## 문제 사항 해결

다음과 같은 에러가 날 경우, 파이썬 모듈을 찾지 못하는 것입니다.

```
🕙 18:14:24 ❯ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
ERROR   -  mkdocstrings: ppmi.pymol_visulize.pymol_plugin could not be found
ERROR   -  Error reading page 'reference/ppmi/pymol_visulize/pymol_plugin/index.md':
ERROR   -  Could not collect 'ppmi.pymol_visulize.pymol_plugin'
```

**Solution**: 각 폴더에 `__init__.py` 파일을 만드세요. `scripts/gen_init_py.py` 파일을 실행하면 됩니다.
