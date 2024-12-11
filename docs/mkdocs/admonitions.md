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

> [!CAUTION]
> 주의사항을 적습니다.

> [!IMPORTANT]
> 중요한 정보를 적습니다.
```

출력은 아래와 같습니다.

> [!NOTE]
> 설명을 적습니다.

> [!TIP]
> 팁을 적습니다.

> [!WARNING]
> 경고를 적습니다.

> [!CAUTION]
> 주의사항을 적습니다.

> [!IMPORTANT]
> 중요한 정보를 적습니다.

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

하지만, mkdocs에서는 깃헙과 달리 caution과 important 타입이 없기 때문에 해당 디자인은 css로 추가 정의해주어야 합니다 (템플릿에 이미 정의되어 있습니다). 설정법은 아래 reference 참고. 

### References

- 기존 mkdocs 문법: <https://squidfunk.github.io/mkdocs-material/reference/admonitions/>
- GitHub 문법: <https://github.com/orgs/community/discussions/16925>
- 비슷한 플러그인: [mkdocs-github-admonitions-plugin](https://github.com/PGijsbers/admonitions)
- mkdocs-callouts 설정법: <https://github.com/sondregronas/mkdocs-callouts/issues/22#issuecomment-2535429645>
