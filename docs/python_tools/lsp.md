# LSP (Language Server Protocol)

- LSP: 프로젝트 전체를 체크해 IDE에서 go to definition, signature (함수 미리보기) 기능 등을 제공합니다.
    - 그 이외의 linter와 비슷한 기능도 일부 구현되기도 합니다. (언어마다 다름)
- IDE에 내장된 경우가 많습니다. (NeoVim, VSCode 내장 기능)

## Python LSP (Pylance, Pyright)

VSCode에서는 pylance, 다른 IDE에서는 오픈소스 버전인 pyright을 사용합니다.

- LSP 기능 이외 Static type checking 기능이 있습니다. C++ 처럼 type을 명확히 지켜줬는지 체크합니다.  
    - 모든 변수, 함수의 type을 적을 필요는 없고, 간단한 경우는 알아서 추측합니다.
    - Inlay hints 기능을 켜서 LSP에서 추측하는 타입이 뭔지 보면서, 잘못된 부분은 명시하면서 코딩해야 좋습니다.
    - **VSCode에 type checking 및 inlay hint 적용**
        - Pylance 플러그인 설치 확인. 기본으로 설치된 경우가 많음. 
        - 너무 복잡해지면 안 좋으니 일단 functionReturnTypes, variableTypes 만 사용
        - setting.json에 아래 내용 추가
            ```json
            "python.analysis.inlayHints.functionReturnTypes": true,
            "python.analysis.inlayHints.variableTypes": true,
 			"python.analysis.typeCheckingMode": "basic",
            ```


