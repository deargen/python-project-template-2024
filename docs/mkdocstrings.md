# 페이지에 소스코드 설명 추가하기

## 설명하고 싶은 모듈/함수/클래스가 있다면 다음과 같이 마크다운 파일에 적으면 됩니다.

```md
::: mlproject.utils.TwoNumbers
    options:
        show_root_heading: true
```

출력은 아래와 같습니다.

::: mlproject.utils.TwoNumbers
    options:
        show_root_heading: true



## 만약 submodule까지 전부 포함하고 싶으시면 다음과 같이 작성합니다.

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


## 소스코드만 출력하고 싶으시면 다음과 같이 작성합니다.

```md
::: mlproject.utils.TwoNumbers
    options:
        members: false
```

출력은 아래와 같습니다.

::: mlproject.utils.TwoNumbers
    options:
        members: false


더 자세한 설명은 [mkdocstrings](https://mkdocstrings.github.io/usage/)를 참고하세요.



# 문제 사항 해결

다음과 같은 에러가 날 경우, 파이썬 모듈을 찾지 못하는 것입니다.

```
🕙 18:14:24 ❯ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
ERROR   -  mkdocstrings: ppmi.pymol_visulize.pymol_plugin could not be found
ERROR   -  Error reading page 'reference/ppmi/pymol_visulize/pymol_plugin/index.md':
ERROR   -  Could not collect 'ppmi.pymol_visulize.pymol_plugin'
```

**Solution**: 각 폴더에 `__init__.py` 파일을 만드세요.
