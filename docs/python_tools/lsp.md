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

- Pylance 에러 예시

```python
def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

# Call the function with correct arguments
num = add_numbers(2, 3)

# Call the function with INCORRECT arguments
add1 = 'abc'
result = add_numbers(add1, num)     # 🚨 TYPE ERROR!

# pylance 에러를 무시하기 위해서는 강제로 type을 지정해주면 됩니다.
add1: int = 'abc'                # 🚨 이 라인에서 에러가 한번 나긴 함.
# 하지만, 다음 줄 부터는 add1을 int라 생각하고 pylance가 코드를 파싱함.
result = add_numbers(add1, num)  # ✅ NO TYPE ERROR!
print(result)    # 'abc5'
# result는 int라고 생각함. 이를 억지로 해결하려면 
```

위 처럼 억지로 type을 맞춰서 실행하면, 결국 result는 int라고 생각해 pylance가 프로젝트를 parsing합니다.  
해결법:

1. 억지로 해결:

```python
add1 = 'abc'
result: str = add_numbers(add1, num)
# 그 다음부터 result는 str이라고 생각됨.
```

2. 함수 definition을 변경:
```python
def add_numbers_or_string(var1: int | str, var2: int | str) -> int | str:
    if isinstance(var2, str):
        var1 = str(var1)
    return var1 + var2
```
