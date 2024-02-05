# GitLab Pages 사용법

1. 마지막 rules의 branch 이름을 "gl-pages"로 변경해 사용
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
    
3. `public/` 폴더에 웹사이트 넣기
4. GitLab 프로젝트에서 `Deploy -> Pages -> Use unique domain` 체크 확인후 그 밑에 페이지 URL 확인
5. `Settings -> General -> Visibility (expand) -> Pages -> Everyone` 으로 설정해 URL을 가진 모두가 볼 수 있게 함
6. 프로젝트에서 `Settings -> Access Tokens -> Add new token` 에서 expiration 1년 뒤로 설정, `write repository` scope, Maintainer role 설정 후 토큰 생성
    - Maintainer가 아닐 경우, 기본 branch는 protected branch로 설정되어 push하지 못할 수 있음. 아니면 developer로 설정 후 protected branch 해지하기.
