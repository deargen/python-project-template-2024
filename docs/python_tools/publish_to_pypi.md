# Publish a Python package to PyPI

`uv`를 사용하면 간단합니다. (build, twine 설치 필요 X).

PYPI_API_TOKEN도 쓰지 마세요. 보안상 좋지 않습니다. 대신, trusted publisher에 Github Action yml파일 경로를 등록하면 됩니다.
프로젝트가 존재하지 않는 경우 (업로드 하기 전) pending publisher로 등록하면 됩니다.

<https://docs.pypi.org/trusted-publishers/adding-a-publisher/>


```bash
uv build --sdist
uv publish
```
