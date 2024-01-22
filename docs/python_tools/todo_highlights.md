# TODO highlights

- 주석에 있는 `# TODO: ` 등을 하이라이팅해주는 플러그인입니다.
- 다른 collaborator가 꼭 알아야 할 중요한 정보는 쉽게 알아 볼 수 있게 키워드를 통일시켜 하이라이팅해야 합니다.

## VSCode에서 설치

- vscode extension에서 [TODO Highlight v2](https://marketplace.visualstudio.com/items?itemName=jgclark.vscode-todo-highlight) 설치
- setting.json에 아래 내용 추가

```json
"todohighlight.isEnable": true,
"todohighlight.keywords": [
    "FIX:",
    "BUG:",
    "ISSUE:",
    "DEBUG:",
    "REVIEW:",
    "NOTE:",
    "INFO:",
    "TODO:",
    "CHECK:",
    "PERF:",
    "WARN:",
    "WARNING:",
    "TEST:",
],
```
