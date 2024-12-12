# Publish a Python package to PyPI

`uv`를 사용하면 간단합니다. (build, twine 설치 필요 X).

```bash
uv build --sdist
uv publish
```

## Trusted publisher

PYPI_API_TOKEN 쓰지 마세요. 보안상 좋지 않습니다. 대신, trusted publisher에 Github Action yml파일 경로를 등록하면 됩니다.
프로젝트가 존재하지 않는 경우 (업로드 하기 전) pending publisher로 등록하면 됩니다.

<https://docs.pypi.org/trusted-publishers/adding-a-publisher/>

```yml hl_lines="6-8 15-18" title=".github/workflows/deploy.yml"
jobs:
  publish-to-pypi:
    if: ${{ github.event.inputs.dry-run == 'false' }}
    needs: commit-changelog-and-release
    runs-on: ubuntu-24.04
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.inputs.version-tag }}
      - name: Install uv
        uses: astral-sh/setup-uv@v4
      - name: Build and upload to PyPI
        run: |
          uv build --sdist
          uv publish
```

dry-run input과 needs는 옵션입니다. 필요한 경우 사용하세요.
