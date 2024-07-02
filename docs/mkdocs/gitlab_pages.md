# GitLab Pages

mkdocs로 작성된 문서는 GitLab Pages로 호스팅합니다.

GitLab을 이용하는 이유는 다음과 같습니다.

1. GitHub Pages는 private repo로 하려면 Enterprise plan 필요
2. GitLab Pages는 read / write 권한 및 문서 버전관리가 용이

GitHub repo의 main branch로 push 한 경우, GitHub CI에서 GitLab으로 push합니다. 그러면 GitLab CI가 돌며 page 호스팅을 완료합니다.

## mkdocs용 GitLab repo 세팅

1. deargen-ai 계정으로 로그인해서 repo 만들기 (예: deargen-ai/ppmi-docs)
    - 🚨 deargen group에 만들면 안됨! group 프로젝트는 access token 생성이 유료 계정만 가능함.
2. `gl-pages` branch에 해당 파일 `.gitlab-ci.yml` 으로 커밋
    - 출처: https://gitlab.com/pages/plain-html
    
    ```yaml
    image: busybox
    
    pages:
      stage: deploy
      script:
        - echo "The site will be deployed to $CI_PAGES_URL"
      artifacts:
        paths:
          - public
      rules:
        - if: $CI_COMMIT_BRANCH == "gl-pages"
    ```

    이제 `public/` 폴더에 웹사이트 넣으면 페이지가 호스팅 됨.  
    본 template은 GitHub Actions가 자동으로 GitLab으로 push하여 document webpage가 생성됨.

3. GitLab 프로젝트에서 `Deploy -> Pages -> Use unique domain` 체크 해제해야 URL이 깔끔하게 나옴.
4. 기밀 문서가 아닌 경우, `Settings -> General -> Visibility (expand) -> Pages -> Everyone` 으로 설정하면 전체 공개.
5. 프로젝트에서 `Settings -> Access Tokens -> Add new token` 에서 expiration 1년 뒤로 설정, `write repository` scope, Maintainer role 설정 후 토큰 생성
    - Maintainer가 아닐 경우, 기본 branch는 protected branch로 설정되어 push하지 못할 수 있음. 아니면 developer로 설정 후 protected branch 해지하기.
6. 프로젝트에서 `Manage -> Members -> Invite a group -> deargen`을 Guest로 추가하면 디어젠 모든 분들에게 읽기 권한이 주어짐.


## GitHub repo 세팅

1. GitHub repo로 가서 `Setting -> Secrets and variables -> Actions` 에서 `New repository secret` 추가
    - Name: `GITLAB_TOKEN`
    - Secret: 위에서 생성한 GitLab access token
2. `Setting -> Secrets and variables -> Actions` 에서 Variables 탭으로 간 뒤 `GITLAB_PROJECT`를 추가
    - Name: `GITLAB_PROJECT`
    - Value: GitLab docs repo 이름 (예: deargen-ai/ppmi-docs)
    - 주의: push할 repo의 이름이고 document URL이 아님.
