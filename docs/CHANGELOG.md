# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [v0.5.0] - 2025-05-07

### Key Changes

- Adapt `changelog-action` and `parse-changelog-action`
    - The changelog will not be commited automatically. Instead, it will create a PR.
    - Merging the PR will create a release.

### :boom: BREAKING CHANGES
- due to [`722b226`](https://github.com/deargen/python-project-template-2024/commit/722b226e740fa91b22c83a5cdbe0262902c62ae2) - deploy creates a PR, and merging it will create a release *(commit by [@kiyoon](https://github.com/kiyoon))*:

  deploy creates a PR, and merging it will create a release


### :sparkles: New Features
- [`9b9a822`](https://github.com/deargen/python-project-template-2024/commit/9b9a8225a98faa2b2846b5a92fc3d5e4fac33d17) - **ci**: basedpyright type checking *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`e96c60f`](https://github.com/deargen/python-project-template-2024/commit/e96c60fabae144d592e87cd4523e45873d9ba6af) - yaml, yml editorconfig *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`3659b36`](https://github.com/deargen/python-project-template-2024/commit/3659b3680ea5b517342a514f10c3d5aa95cb6c15) - editorconfig vscode *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`722b226`](https://github.com/deargen/python-project-template-2024/commit/722b226e740fa91b22c83a5cdbe0262902c62ae2) - deploy creates a PR, and merging it will create a release *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`476d317`](https://github.com/deargen/python-project-template-2024/commit/476d3179c4cc1f4828ac66b40cdd5097965aa3b8) - vscode settings *(commit by [@kiyoon](https://github.com/kiyoon))*

### :wrench: Chores
- [`e5bd44a`](https://github.com/deargen/python-project-template-2024/commit/e5bd44ab28062e2bb35aff679bbda6a51027f22f) - taplo format pyproject.toml *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.4.1] - 2025-02-26
### :sparkles: New Features
- [`e79995e`](https://github.com/deargen/python-project-template-2024/commit/e79995ef846370f05b2a821646ed7f91cf6d08e8) - more project urls *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`3ee3c22`](https://github.com/deargen/python-project-template-2024/commit/3ee3c22864515156c7fd9b1d4d04c19ed99b69e6) - mkdocstrings make indented *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`3f9fef3`](https://github.com/deargen/python-project-template-2024/commit/3f9fef3c0ab8a4f72b3196d73bcecb0e7a2a6372) - ruff select all rules except ignored rules *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`ebc31f1`](https://github.com/deargen/python-project-template-2024/commit/ebc31f16ae0ac6640ffa6d2ad4bc21e075776107) - fix ruff rules *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`a4e93df`](https://github.com/deargen/python-project-template-2024/commit/a4e93df8aa59595a5a53d6d427d4b1263b9043fe) - ruff ignore todo comments *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`a84c483`](https://github.com/deargen/python-project-template-2024/commit/a84c4835a0905a83708ec55155ede32ab17671b2) - nbval Jupyter Notebook regression testing *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`12b98ec`](https://github.com/deargen/python-project-template-2024/commit/12b98ec9e9673306f44b07ba64df05fd839e172b) - ignore ruff ARG *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`62c86e5`](https://github.com/deargen/python-project-template-2024/commit/62c86e57e4baee6baad11cc2c6585de1f8bfcaa6) - ruff ignore TC in cli *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`0fe5c9a`](https://github.com/deargen/python-project-template-2024/commit/0fe5c9abdcef3da457e275fa0921cdc7734fd8cc) - remove PERF ruff lint *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`147e072`](https://github.com/deargen/python-project-template-2024/commit/147e07257675cb26ae0c2864f6f291abd3608067) - optionally support windows *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`d78ae4f`](https://github.com/deargen/python-project-template-2024/commit/d78ae4ffc80ad84ee2c39959a4dd2f6fd083899c) - typer -> cyclopts *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`2fda191`](https://github.com/deargen/python-project-template-2024/commit/2fda1917e56fe7e86a8fbd7cbb3a21f9badc7919) - vscode basedpyright *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`9b5dea2`](https://github.com/deargen/python-project-template-2024/commit/9b5dea2304a850d3d43f89c3b6275d6fa1b2c5c9) - no ruff T201 (print statement) in ipynb *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`2e154ef`](https://github.com/deargen/python-project-template-2024/commit/2e154ef8c633aa95cf27f371958aac870fd2524a) - build include directories *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`d6ee73b`](https://github.com/deargen/python-project-template-2024/commit/d6ee73b6912b357c716097bbf16bfe1889db3e9a) - **mkdocs**: github flavored alert not rendered when used with snippets *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`d4c1f63`](https://github.com/deargen/python-project-template-2024/commit/d4c1f638353832f97ffc81d1c6ea2ccac9f4e9a3) - wrong year in LICENSE *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`aeb670f`](https://github.com/deargen/python-project-template-2024/commit/aeb670fab1864e4c3a003076969f1ac6a007f794) - nbval ignore kernel in notebook. Use current env *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.4.0] - 2024-12-26
### :boom: BREAKING CHANGES
- due to [`5cb3c66`](https://github.com/deargen/python-project-template-2024/commit/5cb3c6663f494b3c99dfd23b5394fa2da7f49cef) - hatchling, version-pioneer *(commit by [@kiyoon](https://github.com/kiyoon))*:

  hatchling, version-pioneer


### :sparkles: New Features
- [`e44cf89`](https://github.com/deargen/python-project-template-2024/commit/e44cf89340221a3439d04eadaa05c71bdb3c4d4d) - do not fix ruff version *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`e965403`](https://github.com/deargen/python-project-template-2024/commit/e9654034a0db9082fe753af67fa4ab64017e5496) - ignore D205 1 blank line lint *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`2c00c0e`](https://github.com/deargen/python-project-template-2024/commit/2c00c0ed4e46a5459bc70f47739a0c50a789d3c3) - typer help text from docstring *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`5cb3c66`](https://github.com/deargen/python-project-template-2024/commit/5cb3c6663f494b3c99dfd23b5394fa2da7f49cef) - hatchling, version-pioneer *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`1f8ca7b`](https://github.com/deargen/python-project-template-2024/commit/1f8ca7b7a6e96ba2a48841905c07e08a540a5a3b) - version style with master and dev branch distance *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`a855d64`](https://github.com/deargen/python-project-template-2024/commit/a855d640912f728b8946eddba41ed5b2a992f394) - pkg_is_editable *(commit by [@kiyoon](https://github.com/kiyoon))*

### :recycle: Refactors
- [`f1e4220`](https://github.com/deargen/python-project-template-2024/commit/f1e422003e35c699cce58536e1fddb82897b5871) - editable install detect *(commit by [@kiyoon](https://github.com/kiyoon))*

### :wrench: Chores
- [`76d4f58`](https://github.com/deargen/python-project-template-2024/commit/76d4f58eb9864d457aa6fc4a37f13ca92a85c475) - ignore logger.exception lint *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`54a01de`](https://github.com/deargen/python-project-template-2024/commit/54a01de9d37fd198c83bb010e41e1d93f0692540) - pip compile *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.3.3] - 2024-12-17
### :sparkles: New Features
- [`8a87e9a`](https://github.com/deargen/python-project-template-2024/commit/8a87e9a085a9f580f2396e671fd57b5d6a0828df) - **mkdocs**: use github flavoured callouts *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`40fd8c5`](https://github.com/deargen/python-project-template-2024/commit/40fd8c5a2ea5489c9f0d7f9973d64e700e1adae4) - **mkdocs**: github admonitions *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`94fc67e`](https://github.com/deargen/python-project-template-2024/commit/94fc67e8803a7ce1ad09581f3794ea5d989bd54c) - **mkdocs**: math equations *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`c6c9616`](https://github.com/deargen/python-project-template-2024/commit/c6c961676df333dc0a7b831ecdf1284ae0ae6be6) - **mkdocs**: github style *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`35b30ed`](https://github.com/deargen/python-project-template-2024/commit/35b30ed2c3e6ccd0499267f028c522119eaaec44) - **ruff**: remove magic-value-comparison (PLR2004) rule *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`7232d17`](https://github.com/deargen/python-project-template-2024/commit/7232d17ceb0c254b93be99f055fceafaaac225ca) - move pip-compile configuration to `pyproject.toml` *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`23a08c1`](https://github.com/deargen/python-project-template-2024/commit/23a08c1428182b03dc9b3230c48ec710aef6a005) - remove dependabot *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`11c5f50`](https://github.com/deargen/python-project-template-2024/commit/11c5f50a6640b2671d3ecdffcb4a0121fa3995cf) - use lint-essential (central managed rulesets) *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`ae7cb50`](https://github.com/deargen/python-project-template-2024/commit/ae7cb503342d551e2503dc0a90be656946342743) - INP only in src/ *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`2c374f1`](https://github.com/deargen/python-project-template-2024/commit/2c374f1441da07dda815cfcf454e47f452e7e122) - log path logging *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`a94b965`](https://github.com/deargen/python-project-template-2024/commit/a94b9656ebac12f3e9fde21e23d16e7a98a614ed) - setuptools pypi publish bug *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`2127fd3`](https://github.com/deargen/python-project-template-2024/commit/2127fd373d14ed5ded497fc18ac1c1b667f93a7d) - INP001 directories *(commit by [@kiyoon](https://github.com/kiyoon))*

### :recycle: Refactors
- [`d47ce9e`](https://github.com/deargen/python-project-template-2024/commit/d47ce9ec2286d4118f80786d55fc728fba320afb) - move update_data_dirs() up *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.3.2] - 2024-11-27
### :sparkles: New Features
- [`44e1aa5`](https://github.com/deargen/python-project-template-2024/commit/44e1aa52f1e4b78aab2680d51b180d1a6f99eff2) - essential lint as test *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`5ccd478`](https://github.com/deargen/python-project-template-2024/commit/5ccd4789c728deff012ef13fa66f104cb3d201bd) - pyproject toml *(commit by [@kiyoon](https://github.com/kiyoon))*

### :recycle: Refactors
- [`792dba3`](https://github.com/deargen/python-project-template-2024/commit/792dba398738090c0678359cbb588da8813616a9) - rename some variables (app_name -> APP_NAME etc.) *(commit by [@kiyoon](https://github.com/kiyoon))*

### :white_check_mark: Tests
- [`7e3eed0`](https://github.com/deargen/python-project-template-2024/commit/7e3eed00c3fcd36555edfc406874d9559acdb619) - log_cli *(commit by [@kiyoon](https://github.com/kiyoon))*

### :wrench: Chores
- [`6d46488`](https://github.com/deargen/python-project-template-2024/commit/6d46488d099a51050a7ea84b5bac49581b83ff15) - type *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`f18dda3`](https://github.com/deargen/python-project-template-2024/commit/f18dda3acfa3d277d293f983d9f59eb372b929a6) - english docs *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.3.1] - 2024-11-12
### :boom: BREAKING CHANGES
- due to [`cf178a5`](https://github.com/deargen/python-project-template-2024/commit/cf178a531806fe99a76e1e0ae5fdd9d1715e841c) - ml_project.utils.log.setup_logging -> ml_project.setup_logging *(commit by [@kiyoon](https://github.com/kiyoon))*:

  ml_project.utils.log.setup_logging -> ml_project.setup_logging


### :recycle: Refactors
- [`cf178a5`](https://github.com/deargen/python-project-template-2024/commit/cf178a531806fe99a76e1e0ae5fdd9d1715e841c) - ml_project.utils.log.setup_logging -> ml_project.setup_logging *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.3.0] - 2024-11-11

### 🔆  Highlights
기존 템플릿은 `pip install -e .` 처럼 development mode로 설치하는 것을 기본 전제로 했다. 하지만,

**기존 방법의 단점:**

- 이렇게 하면 무조건 repository clone을 해야 사용할 수 있으므로 간단히 설치해 CLI를 사용하기 어려워진다.

**변경 방법의 장점: 설치가 훨씬 수월해진다.**
- `pip install .` (-e 없이) 해도 사용 가능. (PROJECT_DIR만 사용 못함)
- `pipx install .`, `uv tool install .`처럼 API없이 CLI만 사용하도록 설치도 가능.

#### Breaking Changes (주의 사항)
- PROJECT_DIR type이 `Path` -> `Path | None`으로 변경. Non-development mode install (pip install -e 안했을때) None으로 설정.
    - 웬만하면 사용 자제하고 개발/테스트할 때만 사용 권장.
- `setup_logging()` default로 file logging 안하도록 변경. `setup_logging(log_dir=LOG_DIR)` 사용.

#### New Features
- `ml-project config` CLI로 template.env를 가장 적합한 디렉토리에 복사함.


### :boom: BREAKING CHANGES
- due to [`ed5d8ed`](https://github.com/deargen/python-project-template-2024/commit/ed5d8edf870c75d8044e9d3000d99f079d4619b7) - drop windows (not in default) *(commit by [@kiyoon](https://github.com/kiyoon))*:

  drop windows (not in default)

- due to [`b2fa2e9`](https://github.com/deargen/python-project-template-2024/commit/b2fa2e917cded278670bfedfd50a7655c2003c59) - prevent circular import *(commit by [@kiyoon](https://github.com/kiyoon))*:

  prevent circular import

- due to [`6b0e335`](https://github.com/deargen/python-project-template-2024/commit/6b0e33510649dd21b363843b0f66d921279583dd) - non-development installation support *(PR [#28](https://github.com/deargen/python-project-template-2024/pull/28) by [@kiyoon](https://github.com/kiyoon))*:

  non-development installation support (#28)


### :sparkles: New Features
- [`088ac67`](https://github.com/deargen/python-project-template-2024/commit/088ac671deda79021c65dad85fc3ca31a3a62f46) - update requirements_docs.in to support python 3.12 *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`01ede09`](https://github.com/deargen/python-project-template-2024/commit/01ede0949b732393bf19a37e4d4385e9c199ca56) - vscode default settings *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`9772d0e`](https://github.com/deargen/python-project-template-2024/commit/9772d0ef31487cd9f9fea400e0ec001ce95f7799) - **ruff**: ignore unused imports in __init__.py *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`ed5d8ed`](https://github.com/deargen/python-project-template-2024/commit/ed5d8edf870c75d8044e9d3000d99f079d4619b7) - **pip-compile**: drop windows (not in default) *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`3ced2e3`](https://github.com/deargen/python-project-template-2024/commit/3ced2e3ec5336b1d7b087414f6f55de2f56bf732) - biotest *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`d216290`](https://github.com/deargen/python-project-template-2024/commit/d21629045d56f409057dc87c0ebc93d8883e403f) - ban lightning *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`d14c903`](https://github.com/deargen/python-project-template-2024/commit/d14c90310b2d195f989cc06793aeca34d2b5c5e2) - add banned api *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`051e2e6`](https://github.com/deargen/python-project-template-2024/commit/051e2e645d8022fa685518191b42df5aa829ff91) - make pylinter less strict *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`4a24cc5`](https://github.com/deargen/python-project-template-2024/commit/4a24cc5bfaaae4544e600b563d352178898047a4) - ruff ban os.system *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`3120164`](https://github.com/deargen/python-project-template-2024/commit/31201648b00569ba261662605ac8af344a76ec62) - **ruff**: ban easydict *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`6b0e335`](https://github.com/deargen/python-project-template-2024/commit/6b0e33510649dd21b363843b0f66d921279583dd) - non-development installation support *(PR [#28](https://github.com/deargen/python-project-template-2024/pull/28) by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`53fc9f5`](https://github.com/deargen/python-project-template-2024/commit/53fc9f554b9c18a65a1faf8e9402ca389c3fcca8) - tests directory doesn't need namespace *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`5b2ee15`](https://github.com/deargen/python-project-template-2024/commit/5b2ee15ca89373a279dc25759f259731af15de7e) - disable some ruff rules for CLI *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`99972df`](https://github.com/deargen/python-project-template-2024/commit/99972df1f954592f0c802dde2b2fce808f96971c) - ruff and health check logic *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`b2fa2e9`](https://github.com/deargen/python-project-template-2024/commit/b2fa2e917cded278670bfedfd50a7655c2003c59) - prevent circular import *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`6c3e3dc`](https://github.com/deargen/python-project-template-2024/commit/6c3e3dcb482b747ad4a0e3c75ff62fa41278a9d8) - **config**: improve abstraction, doctest *(commit by [@kiyoon](https://github.com/kiyoon))*

### :recycle: Refactors
- [`fb23283`](https://github.com/deargen/python-project-template-2024/commit/fb23283dd2b379c97b8ef88a3861573e62801c0f) - remove clearml dependency and example *(commit by [@kiyoon](https://github.com/kiyoon))*

### :wrench: Chores
- [`ac88a3e`](https://github.com/deargen/python-project-template-2024/commit/ac88a3e6feb4944669bfd0cc9229b73a79e4b650) - update first party *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.2.5] - 2024-10-14
### :boom: BREAKING CHANGES
- due to [`0ee9ddb`](https://github.com/deargen/python-project-template-2024/commit/0ee9ddb5093e671ec077a5fc00ae5f68ec744ce6) - easier gitlab page setup guide (but defaults to master branch *(commit by [@kiyoon](https://github.com/kiyoon))*:

  easier gitlab page setup guide (but defaults to master branch


### :sparkles: New Features
- [`0ee9ddb`](https://github.com/deargen/python-project-template-2024/commit/0ee9ddb5093e671ec077a5fc00ae5f68ec744ce6) - easier gitlab page setup guide (but defaults to master branch *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`872bbf9`](https://github.com/deargen/python-project-template-2024/commit/872bbf9023fea5701980b8daef4767fbd97664df) - **replace-name**: mac compatible sed *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`3f0aae4`](https://github.com/deargen/python-project-template-2024/commit/3f0aae42ece6eaedaa661ba202a1ee3586945eaf) - **ci**: check mkdocs *(PR [#27](https://github.com/deargen/python-project-template-2024/pull/27) by [@kiyoon](https://github.com/kiyoon))*
- [`e3a4041`](https://github.com/deargen/python-project-template-2024/commit/e3a40419987e9b3b7b4398c3c70dfe2efc25775c) - **replace_project_name.sh**: sed issue with mac *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.2.4] - 2024-10-10
### :sparkles: New Features
- [`b6360ab`](https://github.com/deargen/python-project-template-2024/commit/b6360ab906197ca9fe59c5478b3528b474d9b8a7) - **ci**: add exclude-types input to deploy.yml, fix(ci): check-docs.yml *(PR [#26](https://github.com/deargen/python-project-template-2024/pull/26) by [@kiyoon](https://github.com/kiyoon))*


## [v0.2.3] - 2024-10-05
### :sparkles: New Features
- [`2261a27`](https://github.com/deargen/python-project-template-2024/commit/2261a27b084e7f06947d6f5d8454fbccc89b4803) - micromamba cache better key *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`bebe843`](https://github.com/deargen/python-project-template-2024/commit/bebe843bd6fc714142ff1c92d6c7ebcc67bdac7f) - **config**: undefined variable *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`becff68`](https://github.com/deargen/python-project-template-2024/commit/becff68b9080c65b27f85e98a0a786c3e3bddf75) - relax pylint max statements *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`580b4ee`](https://github.com/deargen/python-project-template-2024/commit/580b4eee572bbc1a30a9bd9be03a8a205c65e6f6) - **ci**: ubuntu-24.04 *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`54f0cae`](https://github.com/deargen/python-project-template-2024/commit/54f0cae043b77fd95c7eb06f1035dcfb70a2a9b1) - **ci**: deploy dry run *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.2.2] - 2024-09-26
### :sparkles: New Features
- [`d0f1d71`](https://github.com/deargen/python-project-template-2024/commit/d0f1d7167626b9f723cff19da251af322abd1806) - replace string script to use template instantly *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`5d07c12`](https://github.com/deargen/python-project-template-2024/commit/5d07c12e76ca8615288c77638fb3b524eb76c38a) - log console theme *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`e4d2b12`](https://github.com/deargen/python-project-template-2024/commit/e4d2b124d95052828d50179396a32b40fad3f347) - success level color *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`6837b01`](https://github.com/deargen/python-project-template-2024/commit/6837b014076dcbaaf570f4430d647c07e4b572e5) - **ruff**: more lint rules *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`63db4d0`](https://github.com/deargen/python-project-template-2024/commit/63db4d0f44b14fe895e7b53c8dbf9e9ea0a973f9) - better pylint tolerance *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`13cc21d`](https://github.com/deargen/python-project-template-2024/commit/13cc21d28ae3de5cb5d0dc20d0da938d2f4c61ef) - **ruff**: remove ARG lint *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`60ae13a`](https://github.com/deargen/python-project-template-2024/commit/60ae13a21c12266ee77ea95eeb619ad873e0a6c1) - **ci**: micromamba *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`008df63`](https://github.com/deargen/python-project-template-2024/commit/008df630c357578b8c651507405e47841e44cc0a) - change module name with script *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`5e03af9`](https://github.com/deargen/python-project-template-2024/commit/5e03af98111d2e884f690cc449a8f4018060ca88) - rename module actually *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.2.1] - 2024-09-08
### :boom: BREAKING CHANGES
- due to [`3674e0a`](https://github.com/deargen/python-project-template-2024/commit/3674e0a52b3d37f0a065fdc3c9d6f051eb5910c6) - remove slack *(PR [#25](https://github.com/deargen/python-project-template-2024/pull/25) by [@kiyoon](https://github.com/kiyoon))*:

  remove slack (#25)


### :sparkles: New Features
- [`3f623d8`](https://github.com/deargen/python-project-template-2024/commit/3f623d86cdff079a7727ad5f4289122d568cbdd2) - mkdocs sort source order and ignore some modules in API reference *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`d19eaa1`](https://github.com/deargen/python-project-template-2024/commit/d19eaa122edf7aed9faa0bb8fded999da0b5b0d5) - typer cli *(PR [#24](https://github.com/deargen/python-project-template-2024/pull/24) by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`2890b02`](https://github.com/deargen/python-project-template-2024/commit/2890b02ea698b298fea354616b48760a6e83563d) - enable some pyright diagnostics *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`7cc5642`](https://github.com/deargen/python-project-template-2024/commit/7cc56420aaa9cce11424c381b06305b89141ce14) - change unknown linux to manylinux *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`5d098dc`](https://github.com/deargen/python-project-template-2024/commit/5d098dca7d95dfcaff290f6e979a52336a114516) - support more platform than Linux for basedpyright *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`2bb1cf3`](https://github.com/deargen/python-project-template-2024/commit/2bb1cf3cd841a6a81503b431de72c6d2f737fba0) - stub file in mkdocstrings *(commit by [@kiyoon](https://github.com/kiyoon))*

### :recycle: Refactors
- [`3674e0a`](https://github.com/deargen/python-project-template-2024/commit/3674e0a52b3d37f0a065fdc3c9d6f051eb5910c6) - remove slack *(PR [#25](https://github.com/deargen/python-project-template-2024/pull/25) by [@kiyoon](https://github.com/kiyoon))*


## [v0.2.0] - 2024-07-02
### :sparkles: New Features
- [`6892dcc`](https://github.com/deargen/python-project-template-2024/commit/6892dcc2763fd96d9d0b86d691132ab0c02ca0cd) - reusable workflows *(PR [#23](https://github.com/deargen/python-project-template-2024/pull/23) by [@kiyoon](https://github.com/kiyoon))*


## [v0.1.5] - 2024-06-28
### :sparkles: New Features
- [`929fb46`](https://github.com/deargen/python-project-template-2024/commit/929fb464bd66f910fa59eaceec6e0d4ded84faef) - health check, install binaries, font etc. *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`fab2e06`](https://github.com/deargen/python-project-template-2024/commit/fab2e06f8b5601aa6b8c37cf30e0a3b4bfddf20a) - vscode extensions recommendations *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`3687e2f`](https://github.com/deargen/python-project-template-2024/commit/3687e2f7982a4e8d2b1e6b19c66e55d255733d24) - mac separate dependencies *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`7d22258`](https://github.com/deargen/python-project-template-2024/commit/7d22258e44be06fd9890d5fa0409185740ef70c2) - mac dependencies *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`0390e7a`](https://github.com/deargen/python-project-template-2024/commit/0390e7ae975414fda4e01097d2c67fece62eab8b) - gh action annotation for ruff *(PR [#21](https://github.com/deargen/python-project-template-2024/pull/21) by [@kiyoon](https://github.com/kiyoon))*
- [`8a20166`](https://github.com/deargen/python-project-template-2024/commit/8a20166f22efb02f221d6a89ed2fbec8119c5e62) - check docs compiling *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`dd09beb`](https://github.com/deargen/python-project-template-2024/commit/dd09beb28ef02e8fc0084127a4ab0d5c58ca7f55) - dry-run changelog generation *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`09672e0`](https://github.com/deargen/python-project-template-2024/commit/09672e03fa0114ea600069377bf22cd70a3c924a) - get_python_version.py without toml dependency, compile reqs with *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`c3fc757`](https://github.com/deargen/python-project-template-2024/commit/c3fc7570ffc16cf55aa3696f323257a6034b3886) - deploy dry run completely separate job *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`22f16d5`](https://github.com/deargen/python-project-template-2024/commit/22f16d574be015cdd568487866e44b3d0573aec8) - **slack**: send_only *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`4bd8ae8`](https://github.com/deargen/python-project-template-2024/commit/4bd8ae894d327ee832e8a0825828509427e6fec5) - slack token default being wrong token *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`8a63607`](https://github.com/deargen/python-project-template-2024/commit/8a63607dad7902248c5643c6251cfcb213bccf2a) - dry-run deploy leaving version tag *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`f9adbf7`](https://github.com/deargen/python-project-template-2024/commit/f9adbf71768066b28721822ca73b7b5c03c3e45e) - maybe fix echo evaluating backticks *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`be3b895`](https://github.com/deargen/python-project-template-2024/commit/be3b895f24220658d2d1ba4a08131f11edde1e18) - maybe fix wrong echo *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`cd6f2ee`](https://github.com/deargen/python-project-template-2024/commit/cd6f2ee55699fd70849d528ec022b0f8a5ffd0f4) - ci deploy always dry-run *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`d4d9766`](https://github.com/deargen/python-project-template-2024/commit/d4d9766337f786134c72ec2397dc0244ab80f447) - get python version *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`7bee54b`](https://github.com/deargen/python-project-template-2024/commit/7bee54b3af0af91836ddd515a681887f72c3580d) - use min python version instead of max *(PR [#22](https://github.com/deargen/python-project-template-2024/pull/22) by [@kiyoon](https://github.com/kiyoon))*

### :wrench: Chores
- [`6ba5a0a`](https://github.com/deargen/python-project-template-2024/commit/6ba5a0ab16eb6d98e19feac3b4f5741c104a2686) - ignore ruff SIM108 *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.1.4] - 2024-03-08
### :sparkles: New Features
- [`fa319d1`](https://github.com/deargen/python-project-template-2024/commit/fa319d1efca76f72b08a0a0013da810f426942a8) - dependabot *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`d13437a`](https://github.com/deargen/python-project-template-2024/commit/d13437a7ae32f6924d77482093e914a752718a77) - doctest, test cache *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`5c64a64`](https://github.com/deargen/python-project-template-2024/commit/5c64a644036682c193da3379640893def147929d) - diagram with mermaid *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`87a5e82`](https://github.com/deargen/python-project-template-2024/commit/87a5e820b9d1afa15ea5c8fd2a3ad0e8d01c0dcc) - config system with env vars *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`828d38b`](https://github.com/deargen/python-project-template-2024/commit/828d38bafa33243221c77105e9a3eca843f74bbd) - use uv pip compile *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`aa79009`](https://github.com/deargen/python-project-template-2024/commit/aa79009b4b0445ecf02d1f2446c973f39fe56885) - slack and health *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`11430d5`](https://github.com/deargen/python-project-template-2024/commit/11430d5f70f2e6afadd700c7f56226a737d4bfaa) - send exception to slack (txt, html, pdf) *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`40fcb05`](https://github.com/deargen/python-project-template-2024/commit/40fcb05a1cc4de783c1ec05a8326075b34a209e4) - dynamic dependencies (no more declaring inside pyproject.toml) *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`c65c2aa`](https://github.com/deargen/python-project-template-2024/commit/c65c2aab2685e0f90e904219ebee01570b439c14) - requirements *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`964e190`](https://github.com/deargen/python-project-template-2024/commit/964e1908a2066188c61750ef4e85423bdab8da40) - docs *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`4b16c37`](https://github.com/deargen/python-project-template-2024/commit/4b16c37ff1811a2319a2757e78fc6b14edfeb42a) - docs *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`270c1b3`](https://github.com/deargen/python-project-template-2024/commit/270c1b3adc305ef4ca1bb27495dd85cba30cd656) - doctest *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`1f4adfe`](https://github.com/deargen/python-project-template-2024/commit/1f4adfee1d9603546357f4840a0efd31a60a6d75) - ppmi -> mlproject *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`8750e67`](https://github.com/deargen/python-project-template-2024/commit/8750e67d73301a594c81fcba8cb5fdf93a4d0178) - docs *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`25c6266`](https://github.com/deargen/python-project-template-2024/commit/25c62667c71db2951d953b1bd70bf6d4a9b78e47) - ci *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`32a7947`](https://github.com/deargen/python-project-template-2024/commit/32a7947095380c0a0cdb58b473f812ee1614e438) - failing doctest *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`eeb48a0`](https://github.com/deargen/python-project-template-2024/commit/eeb48a0cd9257051efaaa3e7c565b787e189fd0e) - requirements_dev *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`15c58d5`](https://github.com/deargen/python-project-template-2024/commit/15c58d522dba0b233ab5270e94ccb0d854d54ef1) - compile_requirements *(commit by [@kiyoon](https://github.com/kiyoon))*

### :zap: Performance Improvements
- [`35a8ec9`](https://github.com/deargen/python-project-template-2024/commit/35a8ec98eb46ed7c5f163182aa7ff90eeb2339f8) - cache doc pip dependencies *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`dff52a1`](https://github.com/deargen/python-project-template-2024/commit/dff52a19e5cf374632dc4b1fcdf00b28177f6348) - improve docs action *(commit by [@kiyoon](https://github.com/kiyoon))*

### :recycle: Refactors
- [`c269ff8`](https://github.com/deargen/python-project-template-2024/commit/c269ff865813ecdba743de02ed03e0853ff097e8) - remove hard-coded versions from CI *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`9f2a693`](https://github.com/deargen/python-project-template-2024/commit/9f2a6936ac1b58fcc18301f6e25992c03e7a7b23) - ruff version from requirements *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`7d983e7`](https://github.com/deargen/python-project-template-2024/commit/7d983e7d468a390200932835686f9ca3356fe138) - rich print exporting, not only traceback *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.1.3] - 2024-01-28
### :sparkles: New Features
- [`26e3420`](https://github.com/deargen/python-project-template-2024/commit/26e3420d7a7fa0855106056f52f3742e0f8c8981) - **mkdocs**: add __init__.py generator script *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`dac4beb`](https://github.com/deargen/python-project-template-2024/commit/dac4beb0856e9f5156f2d3840021270ae4c60dc5) - logging, more example of docstring *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`afd9514`](https://github.com/deargen/python-project-template-2024/commit/afd95146b7f6f5def19c21a587b57983593b9729) - format on action *(commit by [@kiyoon](https://github.com/kiyoon))*

### :bug: Bug Fixes
- [`b877fc8`](https://github.com/deargen/python-project-template-2024/commit/b877fc82d755e3b449b8bb99221d968c8f19099a) - ci *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`156859a`](https://github.com/deargen/python-project-template-2024/commit/156859acaf77c1e3477efdeeb481652ba3c3bffd) - some ppmi stuff *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`8c18b80`](https://github.com/deargen/python-project-template-2024/commit/8c18b804fbaa8c4e270c1dca13d12e5622f26691) - ci *(commit by [@kiyoon](https://github.com/kiyoon))*

### :wrench: Chores
- [`7b4dcf8`](https://github.com/deargen/python-project-template-2024/commit/7b4dcf8f3d954e2a818a1d0c20f510c75035421a) - change url *(commit by [@kiyoon](https://github.com/kiyoon))*

### :flying_saucer: Other Changes
- [`dd2cb1d`](https://github.com/deargen/python-project-template-2024/commit/dd2cb1d68adfe10c1073ea812e5f5b427a326d30) - Merge branch 'master' of ssh://github.com/deargen/python-project-template-2024 *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`21ac2b3`](https://github.com/deargen/python-project-template-2024/commit/21ac2b3aa8fb0d5f7b234eb1ced89f383e7215c4) - Merge branch 'master' of ssh://github.com/deargen/python-project-template-2024 *(commit by [@kiyoon](https://github.com/kiyoon))*
- [`7afc6d4`](https://github.com/deargen/python-project-template-2024/commit/7afc6d4e0d6fef2703f00921f006bf47582ea32b) - Merge branch 'master' of ssh://github.com/deargen/python-project-template-2024 *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.1.2] - 2024-01-16
### :wrench: Chores
- [`e4445cf`](https://github.com/deargen/python-project-template-2024/commit/e4445cf9962154a4e8f4df2bbe04b80584dce769) - test new changelog path *(commit by [@kiyoon](https://github.com/kiyoon))*

### :flying_saucer: Other Changes
- [`e3cb529`](https://github.com/deargen/python-project-template-2024/commit/e3cb529dfbccbacc9a1bc4e6d32a368a9e7bd209) - Merge branch 'master' of ssh://github.com/deargen/python-project-template-2024 *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.1.1] - 2024-01-16
### :wrench: Chores
- [`e375a3b`](https://github.com/deargen/python-project-template-2024/commit/e375a3b0c96c8fc49aa86948f63226a73b11f0de) - move CHANGELOG.md into docs/ *(commit by [@kiyoon](https://github.com/kiyoon))*


## [v0.1.0] - 2024-01-16
### :wrench: Chores
- [`2e302a0`](https://github.com/deargen/python-project-template-2024/commit/2e302a0cb155aa7b11a6d76f99bfff5abb504890) - change URL *(commit by [@kiyoon](https://github.com/kiyoon))*


[v0.1.0]: https://github.com/deargen/python-project-template-2024/compare/v0.0.0...v0.1.0
[v0.1.1]: https://github.com/deargen/python-project-template-2024/compare/v0.1.0...v0.1.1
[v0.1.2]: https://github.com/deargen/python-project-template-2024/compare/v0.1.1...v0.1.2
[v0.1.3]: https://github.com/deargen/python-project-template-2024/compare/v0.1.2...v0.1.3
[v0.1.4]: https://github.com/deargen/python-project-template-2024/compare/v0.1.3...v0.1.4
[v0.1.5]: https://github.com/deargen/python-project-template-2024/compare/v0.1.4...v0.1.5
[v0.2.0]: https://github.com/deargen/python-project-template-2024/compare/v0.1.6...v0.2.0
[v0.2.1]: https://github.com/deargen/python-project-template-2024/compare/v0.2.0...v0.2.1
[v0.2.2]: https://github.com/deargen/python-project-template-2024/compare/v0.2.1...v0.2.2
[v0.2.3]: https://github.com/deargen/python-project-template-2024/compare/v0.2.2...v0.2.3
[v0.2.4]: https://github.com/deargen/python-project-template-2024/compare/v0.2.3...v0.2.4
[v0.2.5]: https://github.com/deargen/python-project-template-2024/compare/v0.2.4...v0.2.5
[v0.3.0]: https://github.com/deargen/python-project-template-2024/compare/v0.2.5...v0.3.0
[v0.3.1]: https://github.com/deargen/python-project-template-2024/compare/v0.3.0...v0.3.1
[v0.3.2]: https://github.com/deargen/python-project-template-2024/compare/v0.3.1...v0.3.2
[v0.3.3]: https://github.com/deargen/python-project-template-2024/compare/v0.3.2...v0.3.3
[v0.4.0]: https://github.com/deargen/python-project-template-2024/compare/v0.3.3...v0.4.0
[v0.4.1]: https://github.com/deargen/python-project-template-2024/compare/v0.4.0...v0.4.1
[v0.5.0]: https://github.com/deargen/python-project-template-2024/compare/v0.4.1...v0.5.0
