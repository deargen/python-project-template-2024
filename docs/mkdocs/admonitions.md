# Note 창 띄우기 (a.k.a. Admonition, callouts, alerts ...)

주의 깊게 봐야 할 설명은 Admonition 기능을 사용합니다.  
마크다운 파일에 아래와 같이 작성합니다.

```md
> [!NOTE]
> 설명을 적습니다.

> [!TIP]
> 팁을 적습니다.

> [!WARNING]
> 경고를 적습니다.
```

출력은 아래와 같습니다.

> [!NOTE]
> 설명을 적습니다.

> [!TIP]
> 팁을 적습니다.

> [!WARNING]
> 경고를 적습니다.

## Implementation Details

기존 mkdocs admonition 기능은 다음과 같은 문법입니다.

```
!!! note
    This is a note
```

하지만 GitHub에서는 다음과 같은 blockquote 문법을 사용합니다.

```
> [!NOTE]
> This is a note
```

[mkdocs-callouts](https://github.com/sondregronas/mkdocs-callouts) 플러그인을 사용하면 mkdocs에서도 GitHub과 동일한 문법을 사용할 수 있습니다. (템플릿에 이미 설치되어 있습니다.)

동일한 문법을 사용하면 mkdocs 뿐 아니라 GitHub에서 docs를 미리보기 할 때도 동일한 결과를 얻을 수 있습니다.  
하지만 중복된 type으로는 NOTE, TIP, WARNING 밖에 없고 추가적인 mkdocs type (danger 등)은 웬만하면 사용하지 않는 것이 좋습니다.

### References

- 기존 mkdocs 문법: <https://squidfunk.github.io/mkdocs-material/reference/admonitions/>
- GitHub 문법: <https://github.com/orgs/community/discussions/16925>
