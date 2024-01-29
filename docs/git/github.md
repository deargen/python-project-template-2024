# Github 사용법

## Pull request 하기

1. main이 아닌 branch를 만들어 개발
2. 해당 branch를 push하고, pull request를 올림
3. 어떤 issue를 fix하는지 쓰기 (예: Fixes #1) -> accept되면 자동으로 issue 닫힘
4. pull request는 다른 팀원이 간략히 코드 리뷰하고 squash 혹은 rebase하면 됨. merge는 웬만하면 피하기.
    - 웬만하면 PR은 **squash**해서 PR ID `예: (#2)`가 커밋 메시지에 들어가게 함.
5. accept된 PR은 조금 지나면 branch 삭제.
6. 추가로 작업은 다시 main branch에서 새로 branch 파서 작업

## Project settings

![image](https://github.com/kiyoon/jupynium.nvim/assets/12980409/3e76bd49-67c3-4211-a332-4c365127a9e2)

Settings 페이지에서 다음과 같이 수정:


### Branch protection rule

1. main branch는 다양한 사람들이 이용하는 branch 이므로 force push, deletion을 하면 안됨.

해당 옵션은 branch protection rule을 만들면 default임.

![image](https://github.com/kiyoon/jupynium.nvim/assets/12980409/7315bf29-f8e0-4395-b5a0-49f0231da94a)

2. 이해하기 어려운 merge commit을 피하고 linear history 유지하기

![image](https://github.com/kiyoon/jupynium.nvim/assets/12980409/c2bd4df7-6aa1-42f6-ac16-7f8a879acb22)

이렇게 하면 PR을 merge할 때 merge commit은 disable됨.

![image](https://github.com/kiyoon/jupynium.nvim/assets/12980409/9c5c1577-a879-4cfd-a783-7c3febb68475)

웬만하면 PR은 squash하기.


### Environments

mkdocs 자동 빌드를 후 GitLab으로 호스팅하기 위해서 환경변수 설정이 필요함.  

1. Settings -> Environments 에서 mkdocs라는 이름의 환경 만들기

    ![image](https://github.com/kiyoon/jupynium.nvim/assets/12980409/b997c3b1-4b5a-49cb-a02d-b1e043f9d517)

2. Environment secrets에 `GL_TOKEN`이라는 이름으로 GitLab token값 넣어두기.

    ```md
    💡 Token같은 민감한 데이터는 CI 코드에 넣지 말고 environment secrets을 사용합니다.

    CI 파일에서 `environment: mkdocs` 추가 후 `${{ secrets.GL_TOKEN }}`과 같이 접근합니다.
    ```

3. Environment variables에 `GL_PROJECT` 이름으로 GitLab project 주소 넣어두기. (예: deargen-ai/python-project-template-docs)

### GitHub Actions Permissions

GitHub Actions이 프로젝트에 commit을 직접 할 수 있게 합니다.

- 프로젝트 Settings → Actions → General → Workflow Permissions → Read and write → Save

