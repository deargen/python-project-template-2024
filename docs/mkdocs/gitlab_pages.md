# GitLab Pages 사용법

1. `gl-pages` branch에 해당 파일 `.gitlab-ci.yml` 으로 커밋
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

2. GitLab 프로젝트에서 `Deploy -> Pages -> Use unique domain` 체크 해제해야 URL이 깔끔하게 나옴.
3. 기밀 문서가 아닌 경우, `Settings -> General -> Visibility (expand) -> Pages -> Everyone` 으로 설정하면 전체 공개.
4. 프로젝트에서 `Settings -> Access Tokens -> Add new token` 에서 expiration 1년 뒤로 설정, `write repository` scope, Maintainer role 설정 후 토큰 생성
    - Maintainer가 아닐 경우, 기본 branch는 protected branch로 설정되어 push하지 못할 수 있음. 아니면 developer로 설정 후 protected branch 해지하기.
